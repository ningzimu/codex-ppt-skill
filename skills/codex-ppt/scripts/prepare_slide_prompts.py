#!/usr/bin/env python3
"""Prepare per-slide image generation jobs for codex-ppt.

This script is deterministic. It does not call an image model. It turns a
structured deck spec into one self-contained JSON job file per slide.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any, Dict, Iterable, List, Optional

from slide_run_state import (
    DEFAULT_MAX_CONCURRENT_SLIDES,
    now_iso,
    rel_to_deck,
    save_jobs,
    set_run_status,
)


def _die(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        _die(f"Spec file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _die(f"Invalid JSON in {path}: {exc}")
    if not isinstance(data, dict):
        _die("Deck spec must be a JSON object.")
    return data


def _as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _string_list(value: Any) -> List[str]:
    return [str(item).strip() for item in _as_list(value) if str(item).strip()]


_MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def _parse_markdown_image(value: str) -> Optional[Dict[str, str]]:
    match = _MARKDOWN_IMAGE_RE.search(value)
    if not match:
        return None
    alt_text = match.group(1).strip()
    path = match.group(2).strip()
    description = value[: match.start()].strip(" \t\n\r:-;")
    role_parts = [part for part in [description, alt_text] if part]
    return {
        "path": path,
        "role": " — ".join(role_parts) if role_parts else "reference image",
    }


def _resolve_image_path(path: str, *, base_dir: Path) -> str:
    path = path.strip()
    if not path:
        return path
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", path):
        return path
    candidate = Path(path)
    if candidate.is_absolute():
        return str(candidate)
    return str((base_dir / candidate).resolve())


def _normalize_input_image(entry: Any, *, slide_number: int, image_index: int, base_dir: Path) -> Dict[str, Any]:
    if isinstance(entry, dict):
        image = dict(entry)
        raw_path = image.get("path") or image.get("attachment") or image.get("markdown")
        if isinstance(raw_path, str):
            parsed = _parse_markdown_image(raw_path)
            if parsed:
                image["path"] = parsed["path"]
                image.setdefault("role", parsed["role"])
        if isinstance(image.get("path"), str):
            image["path"] = _resolve_image_path(image["path"], base_dir=base_dir)
        return image
    if isinstance(entry, str):
        parsed = _parse_markdown_image(entry)
        if not parsed:
            _die(
                f"Slide {slide_number}: required_images entry {image_index} must be an "
                "object or a Markdown image reference like ![alt](path)."
            )
        lowered = entry.lower()
        fidelity = ""
        if "strict input asset" in lowered:
            fidelity = "strict input asset; preserve the supplied image content"
        return {
            "path": _resolve_image_path(parsed["path"], base_dir=base_dir),
            "role": parsed["role"],
            "fidelity": fidelity,
        }
    _die(f"Slide {slide_number}: required_images entry {image_index} has unsupported type.")


def _slide_images(slide: Dict[str, Any], *, slide_number: int, base_dir: Path) -> List[Dict[str, Any]]:
    images: List[Dict[str, Any]] = []
    for index, image in enumerate(_as_list(slide.get("required_images") or slide.get("input_images")), start=1):
        images.append(_normalize_input_image(image, slide_number=slide_number, image_index=index, base_dir=base_dir))
    return images


def _sample_generation_method(spec: Dict[str, Any], *, base_dir: Path) -> Optional[Dict[str, Any]]:
    method = spec.get("sample_generation_method") or spec.get("image_generation_method")
    if method is None:
        return None
    if not isinstance(method, dict):
        _die("sample_generation_method must be an object when present.")
    method = dict(method)
    for key in ("approved_sample_path", "sample_slide_path", "sample_output_path"):
        if isinstance(method.get(key), str):
            method[key] = _resolve_image_path(method[key], base_dir=base_dir)
    return method


def _method_backend_label(method: Optional[Dict[str, Any]]) -> Optional[str]:
    if not method:
        return None
    for key in ("backend_used", "selected_backend", "backend", "tool_name"):
        value = method.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _format_block(title: str, value: Any) -> str:
    if value is None or value == "" or value == [] or value == {}:
        return ""
    if isinstance(value, (dict, list)):
        body = json.dumps(value, ensure_ascii=False, indent=2)
    else:
        body = str(value).strip()
    return f"## {title}\n{body}\n"


def _format_input_images(images: Iterable[Dict[str, Any]]) -> str:
    lines: List[str] = []
    for idx, image in enumerate(images, start=1):
        path = str(image.get("path") or image.get("attachment") or "").strip()
        role = str(image.get("role") or "reference image").strip()
        fidelity = str(image.get("fidelity") or image.get("constraints") or "").strip()
        if not path:
            _die(f"Input image {idx} is missing path or attachment.")
        if fidelity:
            lines.append(f"- Image {idx}: {path} — {role}; {fidelity}")
        else:
            lines.append(f"- Image {idx}: {path} — {role}")
    return "\n".join(lines)


def _slide_number(slide: Dict[str, Any], fallback: int) -> int:
    raw = slide.get("number", fallback)
    try:
        number = int(raw)
    except (TypeError, ValueError):
        _die(f"Invalid slide number: {raw}")
    if number <= 0:
        _die(f"Slide number must be positive: {number}")
    return number


def _build_prompt(
    *,
    deck: Dict[str, Any],
    slide: Dict[str, Any],
    number: int,
    global_style_reference: Optional[Dict[str, Any]],
    base_dir: Path,
) -> str:
    title = str(slide.get("title") or f"Slide {number}").strip()
    style = deck.get("style", {})
    images: List[Dict[str, Any]] = []
    if global_style_reference:
        images.append(global_style_reference)
    images.extend(_slide_images(slide, slide_number=number, base_dir=base_dir))
    required_background = {
        key: value
        for key, value in {
            "deck_context": deck.get("deck_context"),
            "slide_local_context": slide.get("local_context"),
        }.items()
        if value not in (None, "", [], {})
    }

    prompt_parts = [
        "# Codex PPT Slide Image Prompt\n",
        _format_block("Canvas", {
            "type": "16:9 full-slide PowerPoint image",
            "language": deck.get("language", "Chinese"),
            "slide_number": number,
            "render_slide_number": False,
        }),
        _format_block("Deck Goal", deck.get("goal")),
        _format_block("Required Background", required_background),
        _format_block("Global Style", style),
    ]

    if images:
        prompt_parts.append("## Input Images\n")
        prompt_parts.append(_format_input_images(images))
        prompt_parts.append("\n")

    prompt_parts.extend(
        [
            _format_block("Slide", {
                "number": number,
                "title": title,
                "role": slide.get("role"),
                "intent": slide.get("intent"),
            }),
            _format_block("Text", {
                "title": title,
                "key_points": _string_list(slide.get("key_points")),
                "speaker_focus": slide.get("speaker_focus"),
            }),
            _format_block("Layout", slide.get("layout")),
            _format_block("Visual Elements", slide.get("visual_elements")),
            _format_block("Source Image Rules", slide.get("source_image_rules")),
            _format_block("Constraints", _string_list(slide.get("constraints"))),
        ]
    )

    if global_style_reference:
        prompt_parts.append(
            "## Style Reference Rule\n"
            "Use Image 1 as the approved sample-slide style reference. Match its palette, "
            "typography mood, density, texture, and overall visual identity. Do not copy "
            "its exact layout unless this slide's layout explicitly asks for it.\n"
        )

    if images:
        prompt_parts.append(
            "## Input Image Handling Rules\n"
            "For any input image marked as a strict input asset, include it visibly and "
            "preserve its content. Do not redraw, replace, relabel, or invent a similar "
            "figure. Scale and crop only as needed for composition while keeping the "
            "important labels, arrows, data, and relationships recognizable.\n"
        )

    prompt_parts.append(
        "## Universal Constraints\n"
        "- The final image itself must contain the title and key points.\n"
        "- Render Chinese text exactly and legibly; avoid garbled characters.\n"
        "- Keep the confirmed deck style consistent while varying layout by slide role.\n"
        "- No watermark, unrelated logo, or extra slide number.\n"
    )
    return "\n".join(part for part in prompt_parts if part)


def _job_images(
    slide: Dict[str, Any],
    *,
    number: int,
    global_style_reference: Optional[Dict[str, Any]],
    base_dir: Path,
) -> List[Dict[str, Any]]:
    images: List[Dict[str, Any]] = []
    if global_style_reference:
        images.append(global_style_reference)
    images.extend(_slide_images(slide, slide_number=number, base_dir=base_dir))
    return images


def _write_template(path: Path) -> None:
    template = {
        "deck_name": "example-deck",
        "language": "Chinese",
        "goal": "Explain the core idea of the source article.",
        "deck_context": {
            "source_summary": "Short source-wide summary that workers may need when a slide refers to the broader article.",
            "core_claim": "The central thesis that should stay consistent across the deck.",
            "canonical_terms": ["Term one", "Term two", "Term three"],
        },
        "selected_image_backend": "built-in image tool",
        "max_concurrent_slides": 6,
        "sample_generation_method": {
            "backend_used": "built-in image tool",
            "tool_name": "image_gen",
            "mode": "generate",
            "prompt_source": "the approved sample slide job prompt",
            "size": "16:9 landscape, 2560x1440 target",
            "quality": "medium",
            "approved_sample_path": "/absolute/path/to/approved-sample-slide.png",
            "input_context_preparation": "view_image local required images before built-in generation",
            "handoff_rule": "Subagents must use this same backend/tool/mode; return a blocker if unavailable.",
        },
        "style": {
            "name": "手绘技术解释风",
            "visual_direction": "clean hand-drawn technical explainer",
            "color_palette": "white background, black marker lines, pale yellow highlights",
            "typography": "large readable Chinese headings, compact handwritten annotations",
        },
        "approved_style_reference": {
            "path": "/absolute/path/to/approved-sample-slide.png",
            "role": "approved sample slide style reference",
            "fidelity": "match style only; do not copy layout or content",
        },
        "slides": [
            {
                "number": 1,
                "title": "Cover",
                "role": "cover",
                "intent": "Open the talk",
                "key_points": ["Point one", "Point two"],
                "local_context": {
                    "required_background": "Facts, lists, definitions, comparisons, or prior-slide references this slide needs to be self-contained.",
                },
                "layout": {"composition": "large title with one supporting visual"},
                "visual_elements": {"main_visual": "topic-specific hand-drawn metaphor"},
                "constraints": ["Keep text sparse"],
                "sample_approved": True,
            },
            {
                "number": 2,
                "title": "Evidence",
                "role": "data evidence",
                "intent": "Explain a supplied result figure",
                "key_points": ["Preserve the original figure", "Add two callouts"],
                "required_images": [
                    {
                        "path": "/absolute/path/to/result_01.png",
                        "role": "strict input asset and main evidence figure",
                        "fidelity": "preserve data, axes, labels, legends, colors, and values",
                    },
                    "strict input asset and comparison chart\n\n![Result chart](assets/figures/result_02.png)",
                ],
                "layout": {"composition": "source figure left, explanation cards right"},
            },
        ],
    }
    path.write_text(json.dumps(template, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", help="Deck spec JSON file.")
    parser.add_argument("--out-dir", help="Deck project directory.")
    parser.add_argument("--write-template", help="Write an example deck spec JSON and exit.")
    parser.add_argument(
        "--selected-backend",
        help="Confirmed image backend label, such as `built-in image tool` or `scripts/image_gen.py`.",
    )
    parser.add_argument(
        "--max-concurrent-slides",
        type=int,
        default=None,
        help=f"Maximum slide subagents to dispatch at once. Defaults to {DEFAULT_MAX_CONCURRENT_SLIDES}.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing prompt files.")
    args = parser.parse_args()

    if args.write_template:
        _write_template(Path(args.write_template))
        return 0

    if not args.spec or not args.out_dir:
        _die("Use --spec and --out-dir, or --write-template.")

    spec_path = Path(args.spec)
    spec = _read_json(spec_path)
    spec_dir = spec_path.resolve().parent
    slides = spec.get("slides")
    if not isinstance(slides, list) or not slides:
        _die("Deck spec must include a non-empty slides array.")

    numbered_slides: List[tuple[int, Dict[str, Any], int]] = []
    seen_slide_numbers: Dict[int, int] = {}
    for fallback, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            _die(f"Slide entry {fallback} must be an object.")
        number = _slide_number(slide, fallback)
        if number in seen_slide_numbers:
            _die(
                f"Duplicate slide number {number}: slide entries "
                f"{seen_slide_numbers[number]} and {fallback} would both write slide_{number:02d}.json."
            )
        seen_slide_numbers[number] = fallback
        numbered_slides.append((fallback, slide, number))

    out_dir = Path(args.out_dir)
    prompts_dir = out_dir / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "origin_image").mkdir(parents=True, exist_ok=True)

    global_style_reference = spec.get("approved_style_reference")
    if global_style_reference is not None and not isinstance(global_style_reference, dict):
        _die("approved_style_reference must be an object when present.")
    if global_style_reference and isinstance(global_style_reference.get("path"), str):
        global_style_reference = dict(global_style_reference)
        global_style_reference["path"] = _resolve_image_path(global_style_reference["path"], base_dir=spec_dir)

    sample_generation_method = _sample_generation_method(spec, base_dir=spec_dir)
    max_concurrent_slides = args.max_concurrent_slides
    if max_concurrent_slides is None:
        max_concurrent_slides = int(spec.get("max_concurrent_slides", DEFAULT_MAX_CONCURRENT_SLIDES))
    if max_concurrent_slides < 1:
        _die("max_concurrent_slides must be >= 1.")
    selected_backend = (
        args.selected_backend
        or spec.get("selected_image_backend")
        or spec.get("image_backend")
        or _method_backend_label(sample_generation_method)
    )
    slide_job_entries: List[Dict[str, Any]] = []

    for fallback, slide, number in numbered_slides:
        use_style_reference = bool(slide.get("use_approved_style_reference", True))
        slide_style_reference = global_style_reference if use_style_reference else None
        prompt = _build_prompt(
            deck=spec,
            slide=slide,
            number=number,
            global_style_reference=slide_style_reference,
            base_dir=spec_dir,
        )
        images = _job_images(slide, number=number, global_style_reference=slide_style_reference, base_dir=spec_dir)
        job = {
            "slide": number,
            "title": slide.get("title", f"Slide {number}"),
            "prompt": prompt,
            "out": f"slide_{number:02d}.png",
            "input_images": images,
            "requires_context_images": bool(images),
            "expected_backend": selected_backend,
            "sample_generation_method": sample_generation_method,
            "generation_contract": {
                "must_use_selected_image_backend": True,
                "must_match_sample_generation_method": bool(sample_generation_method),
                "forbidden_final_image_methods": [
                    "local drawing/rendering scripts",
                    "Pillow-generated slides",
                    "SVG/HTML/CSS/canvas screenshots",
                    "python-pptx/PptxGenJS/native PPT layout screenshots",
                    "manually composited text/image overlays",
                ],
                "must_return": ["backend_used", "selected_source", "qa_note"],
            },
        }
        prompt_path = prompts_dir / f"slide_{number:02d}.json"
        if prompt_path.exists() and not args.force:
            _die(f"Slide job file already exists: {prompt_path} (use --force)")
        prompt_path.write_text(json.dumps(job, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        slide_id = f"slide_{number:02d}"
        final_image = out_dir / "origin_image" / f"{slide_id}.png"
        sample_approved = bool(slide.get("sample_approved") or slide.get("approved_sample"))
        status = "accepted" if sample_approved and final_image.exists() else "pending"
        slide_job_entries.append(
            {
                "slide_id": slide_id,
                "number": number,
                "title": slide.get("title", f"Slide {number}"),
                "job": rel_to_deck(out_dir, prompt_path),
                "out": rel_to_deck(out_dir, final_image),
                "input_images": images,
                "requires_context_images": bool(images),
                "status": status,
                "dispatch": None,
                "result": {
                    "final_image": rel_to_deck(out_dir, final_image),
                    "accepted_sample": True,
                }
                if status == "accepted"
                else None,
                "blocker": None,
            }
        )

    slide_jobs = {
        "run_status": "jobs_prepared",
        "deck_name": spec.get("deck_name"),
        "selected_backend": selected_backend,
        "sample_generation_method": sample_generation_method,
        "max_concurrent_slides": max_concurrent_slides,
        "slides": slide_job_entries,
        "updated_at": now_iso(),
    }
    save_jobs(out_dir, slide_jobs)
    set_run_status(out_dir, "jobs_prepared", "prepared slide prompt jobs")

    print(f"Wrote {len(slides)} slide job file(s) to {prompts_dir}")
    print(f"Wrote slide job state to {out_dir / 'slide_jobs.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
