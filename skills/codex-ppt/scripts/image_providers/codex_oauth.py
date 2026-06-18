from __future__ import annotations

import base64
import json
import mimetypes
import os
import platform
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from urllib import error, request
from urllib.request import urlopen as default_urlopen

from .base import ImageProvider


DEFAULT_CODEX_AUTH_FILE = "~/.codex/auth.json"
DEFAULT_CODEX_BASE_URL = "https://chatgpt.com/backend-api/codex"
MAX_CODEX_RESPONSE_BYTES = 64 * 1024 * 1024
MAX_CODEX_BASE64_CHARS = 64 * 1024 * 1024
CODEX_ORIGINATOR = "codex_cli_rs"
DEFAULT_CODEX_CLI_VERSION = "0.140.0-alpha.19"

UrlOpen = Callable[..., Any]


class CodexOAuthHTTPError(RuntimeError):
    def __init__(self, operation: str, status_code: int, detail: str) -> None:
        self.status_code = status_code
        self.detail = detail
        super().__init__(f"{operation} failed (HTTP {status_code}): {detail}")


class CodexOAuthImageProvider(ImageProvider):
    def __init__(
        self,
        *,
        auth_file: Optional[Path] = None,
        codex_base_url: Optional[str] = None,
        urlopen: UrlOpen = default_urlopen,
        timeout: int = 180,
    ) -> None:
        self.auth_file = auth_file or codex_auth_file()
        self.codex_base_url = (
            codex_base_url
            or os.getenv("CODEX_IMAGES_BASE_URL")
            or DEFAULT_CODEX_BASE_URL
        ).rstrip("/")
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
        return self._run_images_endpoint(payload, image_paths)

    def _run_images_endpoint(self, payload: Dict[str, Any], image_paths: List[Path]) -> List[str]:
        path = "images/edits" if image_paths else "images/generations"
        body = self._images_body(payload, image_paths)
        parsed = self._post_json(path, body)
        return extract_codex_json_image_payloads(parsed)

    def _images_body(self, payload: Dict[str, Any], image_paths: List[Path]) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "prompt": str(payload["prompt"]),
            "model": str(payload["model"]),
        }
        for key in (
            "n",
            "size",
            "quality",
            "background",
        ):
            value = payload.get(key)
            if value is not None:
                body[key] = value

        if "background" not in body:
            body["background"] = "auto"
        if "quality" not in body:
            body["quality"] = "auto"

        if image_paths:
            body["images"] = [{"image_url": image_to_data_url(path)} for path in image_paths]
        return body

    def _post_json(self, path: str, body: Dict[str, Any]) -> Dict[str, Any]:
        req = request.Request(
            f"{self.codex_base_url}/{path}",
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            method="POST",
            headers=self._headers("application/json"),
        )
        try:
            with self._urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read(MAX_CODEX_RESPONSE_BYTES + 1)
                if len(raw) > MAX_CODEX_RESPONSE_BYTES:
                    raise RuntimeError("Codex image response exceeded size limit.")
        except error.HTTPError as exc:
            detail = exc.read(4096).decode("utf-8", errors="replace")
            raise CodexOAuthHTTPError("Codex Images request", exc.code, detail) from exc
        except error.URLError as exc:
            raise RuntimeError(f"Codex Images request failed: {exc.reason}") from exc

        try:
            parsed = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Codex Images request returned invalid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise RuntimeError(f"Unexpected Codex Images response: {parsed}")
        return parsed

    def _headers(self, accept: str) -> Dict[str, str]:
        token, account_id = load_codex_auth(self.auth_file)
        if not token:
            raise RuntimeError(f"Codex OAuth auth is missing. Expected {self.auth_file}.")
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
            "Content-Type": "application/json",
            "User-Agent": codex_user_agent(),
            "originator": CODEX_ORIGINATOR,
        }
        if account_id:
            headers["ChatGPT-Account-ID"] = account_id
        return headers


def codex_auth_file() -> Path:
    return Path(os.getenv("CODEX_AUTH_FILE", DEFAULT_CODEX_AUTH_FILE)).expanduser()


def codex_user_agent() -> str:
    override = os.getenv("CODEX_USER_AGENT")
    if override:
        return override

    system = platform.system()
    if system == "Darwin":
        os_name = "Mac OS"
        os_version = platform.mac_ver()[0] or platform.release()
    else:
        os_name = system or "unknown"
        os_version = platform.release() or "unknown"
    arch = platform.machine() or "unknown"
    terminal = os.getenv("TERM_PROGRAM") or "unknown"
    version = os.getenv("CODEX_CLI_VERSION") or DEFAULT_CODEX_CLI_VERSION
    return f"{CODEX_ORIGINATOR}/{version} ({os_name} {os_version}; {arch}) {terminal}"


def load_codex_auth(path: Path) -> tuple[Optional[str], Optional[str]]:
    if not path.exists():
        return None, None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, None
    tokens = data.get("tokens")
    if not isinstance(tokens, dict):
        return None, None
    token = tokens.get("access_token")
    account_id = tokens.get("account_id")
    normalized_token = token.strip() if isinstance(token, str) and token.strip() else None
    normalized_account_id = (
        account_id.strip() if isinstance(account_id, str) and account_id.strip() else None
    )
    return normalized_token, normalized_account_id


def load_codex_access_token(path: Path) -> Optional[str]:
    token, _ = load_codex_auth(path)
    return token


def extract_codex_json_image_payloads(response: Dict[str, Any]) -> List[str]:
    data = response.get("data")
    if not isinstance(data, list):
        raise RuntimeError(f"Unexpected Codex Images response: {response}")

    payloads: List[str] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        result = item.get("b64_json")
        if not isinstance(result, str):
            continue
        if len(result) > MAX_CODEX_BASE64_CHARS:
            raise RuntimeError("Codex image payload exceeded size limit.")
        payloads.append(result)

    if not payloads:
        raise RuntimeError("No image payload found in Codex Images response.")
    return payloads


def image_to_data_url(path: Path) -> str:
    mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"
