#!/usr/bin/env python3
"""Fallback CLI for codex-ppt image generation or editing with GPT Image models.

Used when Codex's built-in image tool is unavailable, when the user explicitly
opts into API mode, or when explicit transparent output requires the
`gpt-image-1.5` fallback path.

Defaults to gpt-image-2 and sends prompts exactly as provided.
Reads OPENAI_API_KEY, and optionally OPENAI_BASE_URL for provider adapters or
OpenAI-compatible proxy providers.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
from pathlib import Path
import re
import sys
import time
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse

from image_providers import create_image_provider
from image_providers.atlascloud import AtlasCloudImageProvider, atlascloud_model_for_operation
from image_providers.base import ImageProvider
from image_providers.codex_oauth import (
    DEFAULT_CODEX_BASE_URL,
    CodexOAuthImageProvider,
)
from image_providers.openai_compatible import OpenAICompatibleImageProvider

DEFAULT_MODEL = "gpt-image-2"
DEFAULT_SIZE = "2048x1152"
DEFAULT_QUALITY = "medium"
DEFAULT_OUTPUT_FORMAT = "png"
DEFAULT_CONCURRENCY = 5
DEFAULT_OUTPUT_PATH = "output/imagegen/output.png"
GPT_IMAGE_MODEL_PREFIX = "gpt-image-"

ALLOWED_LEGACY_SIZES = {"1024x1024", "1536x1024", "1024x1536", "auto"}
ALLOWED_QUALITIES = {"low", "medium", "high", "auto"}
ALLOWED_BACKGROUNDS = {"transparent", "opaque", "auto", None}
ALLOWED_INPUT_FIDELITIES = {"low", "high", None}

GPT_IMAGE_2_MODEL = "gpt-image-2"
GPT_IMAGE_2_MIN_PIXELS = 655_360
GPT_IMAGE_2_MAX_PIXELS = 8_294_400
GPT_IMAGE_2_MAX_EDGE = 3840
GPT_IMAGE_2_MAX_RATIO = 3.0

MAX_IMAGE_BYTES = 50 * 1024 * 1024
MAX_BATCH_JOBS = 500
DEFAULT_RUNTIME_HOME = "~/.codex-ppt-skill"
ENV_FIELDS = (
    "OPENAI_API_KEY",
    "OPENAI_BASE_URL",
    "CODEX_PPT_IMAGE_MODEL",
    "CODEX_PPT_IMAGE_BACKEND",
    "CODEX_IMAGES_BASE_URL",
)
VALID_IMAGE_BACKENDS = ("auto", "codex-oauth", "atlascloud", "openai-compatible")


def _die(message: str, code: int = 1) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(code)


def _warn(message: str) -> None:
    print(f"Warning: {message}", file=sys.stderr)


def _runtime_home() -> Path:
    return Path(os.getenv("CODEX_PPT_HOME", DEFAULT_RUNTIME_HOME)).expanduser()


def _runtime_env_path() -> Path:
    return _runtime_home() / ".env"


def _load_runtime_env() -> None:
    path = _runtime_env_path()
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key not in ENV_FIELDS or os.getenv(key):
            continue
        value = value.strip().strip('"').strip("'")
        os.environ[key] = value


def _default_model() -> str:
    return os.getenv("CODEX_PPT_IMAGE_MODEL", DEFAULT_MODEL)


def _default_backend() -> str:
    return os.getenv("CODEX_PPT_IMAGE_BACKEND", "auto")


def _api_base_url() -> Optional[str]:
    return os.getenv("OPENAI_BASE_URL") or None


def _api_target_label(backend: Optional[str] = None) -> str:
    selected = backend or _preview_backend(None)
    if selected == "codex-oauth":
        return "Codex OAuth image backend (using local Codex login)"
    if selected == "atlascloud":
        base_url = _api_base_url()
        return f"AtlasCloud provider adapter (OPENAI_BASE_URL={base_url})"
    base_url = _api_base_url()
    if base_url:
        return f"third-party image API or OpenAI-compatible proxy (OPENAI_BASE_URL={base_url})"
    return "official OpenAI API (OPENAI_BASE_URL unset)"


def _is_atlascloud_base_url(base_url: str) -> bool:
    hostname = urlparse(base_url).hostname or ""
    return "atlascloud.ai" in hostname.lower()


def _preview_backend(backend: Optional[str]) -> str:
    selected = (backend or _default_backend()).strip().lower()
    if selected == "auto":
        if CodexOAuthImageProvider.available():
            return "codex-oauth"
        base_url = _api_base_url()
        if base_url and _is_atlascloud_base_url(base_url):
            return "atlascloud"
        return "openai-compatible"
    return selected


def _preview_endpoint(kind: str, *, backend: Optional[str] = None) -> str:
    selected = _preview_backend(backend)
    if selected == "codex-oauth":
        base_url = (
            os.getenv("CODEX_IMAGES_BASE_URL")
            or DEFAULT_CODEX_BASE_URL
        )
        if kind == "edit":
            return f"{base_url.rstrip('/')}/images/edits"
        return f"{base_url.rstrip('/')}/images/generations"
    base_url = _api_base_url()
    if selected == "atlascloud" or (base_url and _is_atlascloud_base_url(base_url)):
        return "/api/v1/model/generateImage"
    if kind == "edit":
        return "/v1/images/edits"
    return "/v1/images/generations"


def _preview_model(model: str, kind: str, *, backend: Optional[str] = None) -> str:
    selected = _preview_backend(backend)
    base_url = _api_base_url()
    if selected == "atlascloud" or (base_url and _is_atlascloud_base_url(base_url)):
        operation = "edit" if kind == "edit" else "text-to-image"
        return atlascloud_model_for_operation(model, operation)
    return model


def _skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _create_provider(args: argparse.Namespace) -> ImageProvider:
    try:
        return create_image_provider(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=_api_base_url(),
            backend=getattr(args, "backend", None),
        )
    except (RuntimeError, ValueError) as exc:
        _die(str(exc))
    raise AssertionError("unreachable")


def _provider_backend_name(provider: ImageProvider) -> str:
    if isinstance(provider, CodexOAuthImageProvider):
        return "codex-oauth"
    if isinstance(provider, AtlasCloudImageProvider):
        return "atlascloud"
    if isinstance(provider, OpenAICompatibleImageProvider):
        return "openai-compatible"
    return provider.__class__.__name__


def _provider_preview(provider: ImageProvider) -> Dict[str, Any]:
    if isinstance(provider, CodexOAuthImageProvider):
        return {
            "auth_file": str(provider.auth_file),
            "codex_base_url": provider.codex_base_url,
        }
    return {}


def _ensure_provider_config(provider: ImageProvider, dry_run: bool) -> None:
    backend = _provider_backend_name(provider)
    if backend == "codex-oauth":
        print(
            f"Codex OAuth auth is available. API target: {_api_target_label(backend)}.",
            file=sys.stderr,
        )
        return
    if os.getenv("OPENAI_API_KEY"):
        print(f"OPENAI_API_KEY is set. API target: {_api_target_label(backend)}.", file=sys.stderr)
        return
    if dry_run:
        _warn(f"OPENAI_API_KEY is not set; dry-run only. API target: {_api_target_label(backend)}.")
        return
    runtime_script = _skill_root() / "scripts" / "codex_ppt_runtime.py"
    config_doc = _skill_root() / "docs" / "image-model-configuration.md"
    base_url = _api_base_url()
    model = _default_model()
    if base_url:
        command = (
            f'python3 {runtime_script} config --api-key "your-api-key" '
            f'--base-url "{base_url}" --model {model}'
        )
        target_hint = f"Detected third-party OpenAI-compatible API via OPENAI_BASE_URL={base_url}."
    else:
        command = f'python3 {runtime_script} config --api-key "your-api-key" --model {model}'
        target_hint = "Detected official OpenAI API mode because OPENAI_BASE_URL is not set."
    _die(
        "OPENAI_API_KEY is not set for the selected codex-ppt image provider.\n"
        f"{target_hint}\n"
        "Configure the shared runtime once, or use --backend auto with Codex OAuth auth available:\n"
        f"  {command}\n"
        "To use a third-party proxy, set OPENAI_BASE_URL and the provider's model name.\n"
        f"Details: {config_doc}"
    )


def _read_prompt(prompt: Optional[str], prompt_file: Optional[str]) -> str:
    if prompt and prompt_file:
        _die("Use --prompt or --prompt-file, not both.")
    if prompt_file:
        if prompt_file == "-":
            prompt_text = sys.stdin.read().strip()
            if prompt_text:
                return prompt_text
            _die("Prompt from stdin is empty.")
        path = Path(prompt_file)
        if not path.exists():
            _die(f"Prompt file not found: {path}")
        raw = path.read_text(encoding="utf-8").strip()
        if not raw:
            _die(f"Prompt file is empty: {path}")
        if path.suffix.lower() == ".json" or raw.startswith("{"):
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as exc:
                _die(f"Invalid JSON prompt file {path}: {exc}")
            if not isinstance(data, dict):
                _die(f"JSON prompt file must contain an object with a non-empty prompt field: {path}")
            if isinstance(data, dict) and isinstance(data.get("prompt"), str):
                prompt_text = data["prompt"].strip()
                if prompt_text:
                    return prompt_text
                _die(f"Prompt field is empty in JSON prompt file: {path}")
            _die(f"Missing non-empty prompt field in JSON prompt file: {path}")
        return raw
    if prompt:
        prompt_text = prompt.strip()
        if prompt_text:
            return prompt_text
    _die("Missing prompt. Use --prompt or --prompt-file.")
    return ""  # unreachable


def _check_image_paths(paths: Iterable[str]) -> List[Path]:
    resolved: List[Path] = []
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            _die(f"Image file not found: {path}")
        if path.stat().st_size > MAX_IMAGE_BYTES:
            _warn(f"Image exceeds 50MB limit: {path}")
        resolved.append(path)
    return resolved


def _parse_size(size: str) -> Optional[Tuple[int, int]]:
    match = re.fullmatch(r"([1-9][0-9]*)x([1-9][0-9]*)", size)
    if not match:
        return None
    return int(match.group(1)), int(match.group(2))


def _validate_gpt_image_2_size(size: str) -> None:
    if size == "auto":
        return

    parsed = _parse_size(size)
    if parsed is None:
        _die("size must be auto or WIDTHxHEIGHT, for example 1024x1024.")

    width, height = parsed
    max_edge = max(width, height)
    min_edge = min(width, height)
    total_pixels = width * height

    if max_edge > GPT_IMAGE_2_MAX_EDGE:
        _die("gpt-image-2 size maximum edge length must be less than or equal to 3840px.")
    if width % 16 != 0 or height % 16 != 0:
        _die("gpt-image-2 size width and height must be multiples of 16px.")
    if max_edge / min_edge > GPT_IMAGE_2_MAX_RATIO:
        _die("gpt-image-2 size long edge to short edge ratio must not exceed 3:1.")
    if total_pixels < GPT_IMAGE_2_MIN_PIXELS or total_pixels > GPT_IMAGE_2_MAX_PIXELS:
        _die(
            "gpt-image-2 size total pixels must be at least 655,360 and no more than 8,294,400."
        )


def _validate_size(size: str, model: str) -> None:
    if _is_gpt_image_2_model(model):
        _validate_gpt_image_2_size(size)
        return

    if size not in ALLOWED_LEGACY_SIZES:
        _die(
            "size must be one of 1024x1024, 1536x1024, 1024x1536, or auto for this GPT Image model."
        )


def _validate_quality(quality: str) -> None:
    if quality not in ALLOWED_QUALITIES:
        _die("quality must be one of low, medium, high, or auto.")


def _validate_background(background: Optional[str]) -> None:
    if background not in ALLOWED_BACKGROUNDS:
        _die("background must be one of transparent, opaque, or auto.")


def _validate_input_fidelity(input_fidelity: Optional[str]) -> None:
    if input_fidelity not in ALLOWED_INPUT_FIDELITIES:
        _die("input-fidelity must be one of low or high.")


def _validate_model(model: str) -> None:
    if GPT_IMAGE_MODEL_PREFIX not in model:
        _die(
            "model must be a GPT Image model name containing 'gpt-image-' "
            "(for example gpt-image-2, openai/gpt-image-2, gpt-image-1.5, "
            "gpt-image-1, or gpt-image-1-mini)."
        )


def _is_gpt_image_2_model(model: str) -> bool:
    return GPT_IMAGE_2_MODEL in model


def _validate_model_specific_options(
    *,
    model: str,
    background: Optional[str],
    input_fidelity: Optional[str] = None,
) -> None:
    if not _is_gpt_image_2_model(model):
        return
    if background == "transparent":
        _die(
            "transparent backgrounds are not supported in gpt-image-2, the latest model. "
            "Use --model gpt-image-1.5 --background transparent instead."
        )
    if input_fidelity is not None:
        _die(
            "input_fidelity is not supported in gpt-image-2 because image inputs always use high fidelity for this model."
        )


def _validate_generate_payload(payload: Dict[str, Any]) -> None:
    model = str(payload.get("model", DEFAULT_MODEL))
    _validate_model(model)
    n = int(payload.get("n", 1))
    if n < 1 or n > 10:
        _die("n must be between 1 and 10")
    size = str(payload.get("size", DEFAULT_SIZE))
    quality = str(payload.get("quality", DEFAULT_QUALITY))
    background = payload.get("background")
    _validate_size(size, model)
    _validate_quality(quality)
    _validate_background(background)
    _validate_model_specific_options(model=model, background=background)


def _build_output_paths(
    out: str,
    count: int,
    out_dir: Optional[str],
) -> List[Path]:
    ext = "." + DEFAULT_OUTPUT_FORMAT

    if out_dir:
        out_base = Path(out_dir)
        out_base.mkdir(parents=True, exist_ok=True)
        return [out_base / f"image_{i}{ext}" for i in range(1, count + 1)]

    out_path = Path(out)
    if out_path.exists() and out_path.is_dir():
        out_path.mkdir(parents=True, exist_ok=True)
        return [out_path / f"image_{i}{ext}" for i in range(1, count + 1)]

    if out_path.suffix == "":
        out_path = out_path.with_suffix(ext)
    elif out_path.suffix.lstrip(".").lower() != DEFAULT_OUTPUT_FORMAT:
        _warn(
            f"Output extension {out_path.suffix} does not match default png output."
        )

    if count == 1:
        return [out_path]

    return [
        out_path.with_name(f"{out_path.stem}-{i}{out_path.suffix}")
        for i in range(1, count + 1)
    ]


def _print_request(payload: dict) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _decode_and_write(images: List[str], outputs: List[Path], force: bool) -> None:
    for idx, image_b64 in enumerate(images):
        if idx >= len(outputs):
            break
        out_path = outputs[idx]
        if out_path.exists() and not force:
            _die(f"Output already exists: {out_path} (use --force to overwrite)")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(base64.b64decode(image_b64))
        print(f"Wrote {out_path}")


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value[:60] if value else "job"


def _normalize_job(job: Any, idx: int) -> Dict[str, Any]:
    if isinstance(job, str):
        prompt = job.strip()
        if not prompt:
            _die(f"Empty prompt at job {idx}")
        return {"prompt": prompt}
    if isinstance(job, dict):
        if "prompt" not in job or not str(job["prompt"]).strip():
            _die(f"Missing prompt for job {idx}")
        return job
    _die(f"Invalid job at index {idx}: expected string or object.")
    return {}  # unreachable


def _read_jobs_jsonl(path: str) -> List[Dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        _die(f"Input file not found: {p}")
    jobs: List[Dict[str, Any]] = []
    for line_no, raw in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        try:
            item: Any
            if line.startswith("{"):
                item = json.loads(line)
            else:
                item = line
            jobs.append(_normalize_job(item, idx=line_no))
        except json.JSONDecodeError as exc:
            _die(f"Invalid JSON on line {line_no}: {exc}")
    if not jobs:
        _die("No jobs found in input file.")
    if len(jobs) > MAX_BATCH_JOBS:
        _die(f"Too many jobs ({len(jobs)}). Max is {MAX_BATCH_JOBS}.")
    return jobs


def _merge_non_null(dst: Dict[str, Any], src: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict(dst)
    for k, v in src.items():
        if v is not None:
            merged[k] = v
    return merged


def _job_output_paths(
    *,
    out_dir: Path,
    idx: int,
    prompt: str,
    n: int,
    explicit_out: Optional[str],
) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    ext = "." + DEFAULT_OUTPUT_FORMAT

    if explicit_out:
        base = Path(explicit_out)
        if base.suffix == "":
            base = base.with_suffix(ext)
        elif base.suffix.lstrip(".").lower() != DEFAULT_OUTPUT_FORMAT:
            _warn(
                f"Job {idx}: output extension {base.suffix} does not match default png output."
            )
        base = out_dir / base.name
    else:
        slug = _slugify(prompt[:80])
        base = out_dir / f"{idx:03d}-{slug}{ext}"

    if n == 1:
        return [base]
    return [
        base.with_name(f"{base.stem}-{i}{base.suffix}")
        for i in range(1, n + 1)
    ]


async def _run_generate_batch(args: argparse.Namespace) -> int:
    jobs = _read_jobs_jsonl(args.input)
    out_dir = Path(args.out_dir)

    base_payload = {
        "model": args.model,
        "n": args.n,
        "size": args.size,
        "quality": args.quality,
        "background": args.background,
    }

    provider = _create_provider(args)
    backend = _provider_backend_name(provider)
    _ensure_provider_config(provider, args.dry_run)

    if args.dry_run:
        for i, job in enumerate(jobs, start=1):
            prompt = str(job["prompt"]).strip()

            job_payload = dict(base_payload)
            job_payload["prompt"] = prompt
            job_payload = _merge_non_null(job_payload, {k: job.get(k) for k in base_payload.keys()})
            job_payload = {k: v for k, v in job_payload.items() if v is not None}

            _validate_generate_payload(job_payload)

            n = int(job_payload.get("n", 1))
            outputs = _job_output_paths(
                out_dir=out_dir,
                idx=i,
                prompt=prompt,
                n=n,
                explicit_out=job.get("out"),
            )
            _print_request(
                {
                    "backend": backend,
                    "endpoint": _preview_endpoint("generate", backend=backend),
                    "job": i,
                    "outputs": [str(p) for p in outputs],
                    **_provider_preview(provider),
                    **{
                        **job_payload,
                        "model": _preview_model(str(job_payload["model"]), "generate", backend=backend),
                    },
                }
            )
        return 0

    sem = asyncio.Semaphore(args.concurrency)

    any_failed = False

    async def run_job(i: int, job: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        nonlocal any_failed
        prompt = str(job["prompt"]).strip()
        job_label = f"[job {i}/{len(jobs)}]"

        payload = dict(base_payload)
        payload["prompt"] = prompt
        payload = _merge_non_null(payload, {k: job.get(k) for k in base_payload.keys()})
        payload = {k: v for k, v in payload.items() if v is not None}

        n = int(payload.get("n", 1))
        _validate_generate_payload(payload)
        outputs = _job_output_paths(
            out_dir=out_dir,
            idx=i,
            prompt=prompt,
            n=n,
            explicit_out=job.get("out"),
        )
        try:
            async with sem:
                print(f"{job_label} starting", file=sys.stderr)
                started = time.time()
                images = await provider.generate_batch(
                    payload,
                    attempts=args.max_attempts,
                    job_label=job_label,
                )
                elapsed = time.time() - started
                print(f"{job_label} completed in {elapsed:.1f}s", file=sys.stderr)
            _decode_and_write(images, outputs, force=args.force)
            return i, None
        except Exception as exc:
            any_failed = True
            print(f"{job_label} failed: {exc}", file=sys.stderr)
            if args.fail_fast:
                raise
            return i, str(exc)

    tasks = [asyncio.create_task(run_job(i, job)) for i, job in enumerate(jobs, start=1)]

    try:
        await asyncio.gather(*tasks)
    except Exception:
        for t in tasks:
            if not t.done():
                t.cancel()
        raise

    return 1 if any_failed else 0


def _generate_batch(args: argparse.Namespace) -> None:
    exit_code = asyncio.run(_run_generate_batch(args))
    if exit_code:
        raise SystemExit(exit_code)


def _generate(args: argparse.Namespace) -> None:
    prompt = _read_prompt(args.prompt, args.prompt_file)

    payload = {
        "model": args.model,
        "prompt": prompt,
        "n": args.n,
        "size": args.size,
        "quality": args.quality,
        "background": args.background,
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    output_paths = _build_output_paths(args.out, args.n, args.out_dir)

    provider = _create_provider(args)
    backend = _provider_backend_name(provider)
    _ensure_provider_config(provider, args.dry_run)

    if args.dry_run:
        _print_request(
            {
                "backend": backend,
                "endpoint": _preview_endpoint("generate", backend=backend),
                "outputs": [str(p) for p in output_paths],
                **_provider_preview(provider),
                **{
                    **payload,
                    "model": _preview_model(str(payload["model"]), "generate", backend=backend),
                },
            }
        )
        return

    print(
        f"Calling image backend ({backend}) for generation. This can take up to a couple of minutes.",
        file=sys.stderr,
    )
    started = time.time()
    images = provider.generate(payload)
    elapsed = time.time() - started
    print(f"Generation completed in {elapsed:.1f}s.", file=sys.stderr)

    _decode_and_write(images, output_paths, force=args.force)


def _edit(args: argparse.Namespace) -> None:
    prompt = _read_prompt(args.prompt, args.prompt_file)

    image_paths = _check_image_paths(args.image)

    payload = {
        "model": args.model,
        "prompt": prompt,
        "n": args.n,
        "size": args.size,
        "quality": args.quality,
        "background": args.background,
        "input_fidelity": args.input_fidelity,
    }
    payload = {k: v for k, v in payload.items() if v is not None}

    _validate_input_fidelity(args.input_fidelity)
    output_paths = _build_output_paths(args.out, args.n, args.out_dir)

    provider = _create_provider(args)
    backend = _provider_backend_name(provider)
    _ensure_provider_config(provider, args.dry_run)

    if args.dry_run:
        payload_preview = dict(payload)
        payload_preview["image"] = [str(p) for p in image_paths]
        _print_request(
            {
                "backend": backend,
                "endpoint": _preview_endpoint("edit", backend=backend),
                "outputs": [str(p) for p in output_paths],
                **_provider_preview(provider),
                **{
                    **payload_preview,
                    "model": _preview_model(str(payload_preview["model"]), "edit", backend=backend),
                },
            }
        )
        return

    print(
        f"Calling image backend ({backend}) for edit with {len(image_paths)} image(s).",
        file=sys.stderr,
    )
    started = time.time()
    images = provider.edit(payload, image_paths)

    elapsed = time.time() - started
    print(f"Edit completed in {elapsed:.1f}s.", file=sys.stderr)
    _decode_and_write(images, output_paths, force=args.force)


def _add_shared_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--backend", choices=VALID_IMAGE_BACKENDS, default=_default_backend())
    parser.add_argument("--model", default=_default_model())
    parser.add_argument("--prompt", help="Prompt text. Prefer this for sample generation.")
    parser.add_argument("--prompt-file", help="Prompt file path, or '-' for stdin. Prefer this for saved slide jobs.")
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--size", default=DEFAULT_SIZE)
    parser.add_argument("--quality", default=DEFAULT_QUALITY)
    parser.add_argument("--background")
    parser.add_argument("--out", default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--out-dir")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")


def main() -> int:
    _load_runtime_env()
    parser = argparse.ArgumentParser(
        description="Fallback CLI for explicit image generation or editing via GPT Image models"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    gen_parser = subparsers.add_parser("generate", help="Create a new image")
    _add_shared_args(gen_parser)
    gen_parser.set_defaults(func=_generate)

    batch_parser = subparsers.add_parser(
        "generate-batch",
        help="Generate multiple prompts concurrently (JSONL input)",
    )
    _add_shared_args(batch_parser)
    batch_parser.add_argument("--input", required=True, help="Path to JSONL file (one job per line)")
    batch_parser.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY)
    batch_parser.add_argument("--max-attempts", type=int, default=5)
    batch_parser.add_argument("--fail-fast", action="store_true")
    batch_parser.set_defaults(func=_generate_batch)

    edit_parser = subparsers.add_parser("edit", help="Edit an existing image")
    _add_shared_args(edit_parser)
    edit_parser.add_argument("--image", action="append", required=True)
    edit_parser.add_argument("--input-fidelity")
    edit_parser.set_defaults(func=_edit)

    args = parser.parse_args()
    if args.n < 1 or args.n > 10:
        _die("--n must be between 1 and 10")
    if getattr(args, "concurrency", 1) < 1 or getattr(args, "concurrency", 1) > 25:
        _die("--concurrency must be between 1 and 25")
    if getattr(args, "max_attempts", 5) < 1 or getattr(args, "max_attempts", 5) > 10:
        _die("--max-attempts must be between 1 and 10")
    if args.command == "generate-batch" and not args.out_dir:
        _die("generate-batch requires --out-dir")

    _validate_model(args.model)
    _validate_size(args.size, args.model)
    _validate_quality(args.quality)
    _validate_background(args.background)
    _validate_model_specific_options(
        model=args.model,
        background=args.background,
        input_fidelity=getattr(args, "input_fidelity", None),
    )
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
