from __future__ import annotations

import base64
import json
import mimetypes
import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from urllib import error, request
from urllib.request import urlopen as default_urlopen

from .base import ImageProvider


DEFAULT_CODEX_AUTH_FILE = "~/.codex/auth.json"
DEFAULT_CODEX_RESPONSES_BASE_URL = "https://chatgpt.com/backend-api/codex"
DEFAULT_CODEX_RESPONSES_MODEL = "gpt-5.5"
MAX_CODEX_RESPONSE_BYTES = 64 * 1024 * 1024
MAX_CODEX_BASE64_CHARS = 64 * 1024 * 1024
USER_AGENT = "codex-ppt-skill/0.1 (+https://github.com/ningzimu/codex-ppt-skill)"

UrlOpen = Callable[..., Any]


class CodexOAuthImageProvider(ImageProvider):
    def __init__(
        self,
        *,
        auth_file: Optional[Path] = None,
        responses_base_url: Optional[str] = None,
        responses_model: Optional[str] = None,
        urlopen: UrlOpen = default_urlopen,
        timeout: int = 180,
    ) -> None:
        self.auth_file = auth_file or codex_auth_file()
        self.responses_base_url = (
            responses_base_url
            or os.getenv("CODEX_RESPONSES_BASE_URL")
            or DEFAULT_CODEX_RESPONSES_BASE_URL
        ).rstrip("/")
        self.responses_model = (
            responses_model or os.getenv("CODEX_RESPONSES_MODEL") or DEFAULT_CODEX_RESPONSES_MODEL
        )
        self._urlopen = urlopen
        self.timeout = timeout

    @classmethod
    def available(cls, auth_file: Optional[Path] = None) -> bool:
        return load_codex_access_token(auth_file or codex_auth_file()) is not None

    def _generate(self, payload: Dict[str, Any]) -> List[str]:
        return self._run(payload, [])

    def _edit(self, payload: Dict[str, Any], image_paths: List[Path]) -> List[str]:
        return self._run(payload, image_paths)

    def _run(self, payload: Dict[str, Any], image_paths: List[Path]) -> List[str]:
        count = int(payload.get("n", 1))
        outputs: List[str] = []
        body = self._body(payload, image_paths)
        for _ in range(count):
            text = self._post_sse(body)
            outputs.extend(extract_codex_image_payloads(text))
        return outputs

    def _body(self, payload: Dict[str, Any], image_paths: List[Path]) -> Dict[str, Any]:
        prompt = str(payload["prompt"])
        tool: Dict[str, Any] = {
            "type": "image_generation",
            "model": payload["model"],
        }
        for key in (
            "size",
            "quality",
            "output_format",
            "background",
            "output_compression",
            "moderation",
        ):
            value = payload.get(key)
            if value is not None:
                tool[key] = value

        content: List[Dict[str, Any]] = [{"type": "input_text", "text": prompt}]
        for path in image_paths:
            content.append(
                {
                    "type": "input_image",
                    "image_url": image_to_data_url(path),
                    "detail": "auto",
                }
            )

        return {
            "model": self.responses_model,
            "input": [{"role": "user", "content": content}],
            "instructions": "You are an image generation assistant.",
            "tools": [tool],
            "tool_choice": {"type": "image_generation"},
            "stream": True,
            "store": False,
        }

    def _post_sse(self, body: Dict[str, Any]) -> str:
        token = load_codex_access_token(self.auth_file)
        if not token:
            raise RuntimeError(f"Codex OAuth auth is missing. Expected {self.auth_file}.")
        req = request.Request(
            f"{self.responses_base_url}/responses",
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            method="POST",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "text/event-stream",
                "Content-Type": "application/json",
                "User-Agent": USER_AGENT,
            },
        )
        try:
            with self._urlopen(req, timeout=self.timeout) as resp:
                chunks: List[bytes] = []
                total = 0
                while True:
                    chunk = resp.read(1024 * 64)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > MAX_CODEX_RESPONSE_BYTES:
                        raise RuntimeError("Codex image response exceeded size limit.")
                    chunks.append(chunk)
                return b"".join(chunks).decode("utf-8", errors="replace")
        except error.HTTPError as exc:
            detail = exc.read(4096).decode("utf-8", errors="replace")
            raise RuntimeError(f"Codex Responses request failed (HTTP {exc.code}): {detail}") from exc
        except error.URLError as exc:
            raise RuntimeError(f"Codex Responses request failed: {exc.reason}") from exc


def codex_auth_file() -> Path:
    return Path(os.getenv("CODEX_AUTH_FILE", DEFAULT_CODEX_AUTH_FILE)).expanduser()


def load_codex_access_token(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    tokens = data.get("tokens")
    if not isinstance(tokens, dict):
        return None
    token = tokens.get("access_token")
    if isinstance(token, str) and token.strip():
        return token.strip()
    return None


def image_to_data_url(path: Path) -> str:
    mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def parse_codex_sse_events(body: str) -> List[Dict[str, Any]]:
    events: List[Dict[str, Any]] = []
    for line in body.splitlines():
        if not line.startswith("data: "):
            continue
        payload = line[6:].strip()
        if not payload or payload == "[DONE]":
            continue
        try:
            event = json.loads(payload)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            events.append(event)
    return events


def extract_codex_image_payloads(body: str) -> List[str]:
    events = parse_codex_sse_events(body)
    for event in events:
        if event.get("type") in {"response.failed", "error"}:
            error_obj = event.get("error")
            if isinstance(error_obj, dict):
                message = error_obj.get("message") or error_obj.get("code")
            else:
                message = event.get("message")
            raise RuntimeError(str(message or "Codex image generation failed."))

    payloads: List[str] = []
    for event in events:
        item = event.get("item")
        if (
            event.get("type") == "response.output_item.done"
            and isinstance(item, dict)
            and item.get("type") == "image_generation_call"
            and isinstance(item.get("result"), str)
        ):
            result = item["result"]
            if len(result) > MAX_CODEX_BASE64_CHARS:
                raise RuntimeError("Codex image payload exceeded size limit.")
            payloads.append(result)

    if payloads:
        return payloads

    for event in events:
        if event.get("type") != "response.completed":
            continue
        response_obj = event.get("response")
        output = response_obj.get("output") if isinstance(response_obj, dict) else None
        if not isinstance(output, list):
            continue
        for item in output:
            if (
                isinstance(item, dict)
                and item.get("type") == "image_generation_call"
                and isinstance(item.get("result"), str)
            ):
                result = item["result"]
                if len(result) > MAX_CODEX_BASE64_CHARS:
                    raise RuntimeError("Codex image payload exceeded size limit.")
                payloads.append(result)

    if not payloads:
        raise RuntimeError("No image payload found in Codex response.")
    return payloads
