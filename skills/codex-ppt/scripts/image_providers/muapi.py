from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from .openai_compatible import OpenAICompatibleImageProvider


MUAPI_HOSTNAME = "api.muapi.ai"
MUAPI_DEFAULT_MODEL = "flux-schnell"
MUAPI_ALLOWED_SIZES = frozenset({"1024x1024", "1792x1024", "1024x1792"})


def is_muapi_base_url(base_url: Optional[str]) -> bool:
    if not base_url:
        return False
    try:
        parsed = urlparse(base_url)
    except ValueError:
        return False
    return parsed.scheme.lower() == "https" and (parsed.hostname or "").lower() == MUAPI_HOSTNAME


class MuAPIImageProvider(OpenAICompatibleImageProvider):
    """Adapter for MuAPI's documented OpenAI-compatible image surface."""

    _SUPPORTED_FIELDS = ("model", "prompt", "n", "size")
    _OPTIONAL_DEFAULTS = {"quality": "medium", "output_format": "png"}

    def _prepare_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        unsupported = []
        for key, value in payload.items():
            if key in self._SUPPORTED_FIELDS or value is None:
                continue
            if self._OPTIONAL_DEFAULTS.get(key) == value:
                continue
            unsupported.append(key)
        if unsupported:
            names = ", ".join(sorted(unsupported))
            raise ValueError(
                "MuAPI's OpenAI-compatible image endpoint accepts only model, prompt, n, and size; "
                f"unsupported option(s): {names}."
            )
        return {key: payload[key] for key in self._SUPPORTED_FIELDS if key in payload}

    def edit(
        self,
        payload: Dict[str, Any],
        image_paths: List[Path],
        mask_path: Optional[Path],
    ) -> List[str]:
        raise ValueError(
            "MuAPI's documented OpenAI-compatible image endpoint supports generation only; "
            "image editing is unavailable."
        )
