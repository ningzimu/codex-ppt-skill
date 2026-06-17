from __future__ import annotations

from abc import ABC, abstractmethod
import asyncio
from pathlib import Path
import re
import sys
import time
from typing import Any, Awaitable, Callable, Dict, List, Optional


DEFAULT_RETRY_ATTEMPTS = 5
RETRYABLE_HTTP_CODES = {408, 409, 425, 429, 500, 502, 503, 504}


class ImageProvider(ABC):
    """Common API shape used by image_gen.py command handlers."""

    retry_attempts = DEFAULT_RETRY_ATTEMPTS

    def generate(self, payload: Dict[str, Any]) -> List[str]:
        """Generate images and return base64-encoded image payloads."""
        return self._with_retries(
            lambda: self._generate(payload),
            attempts=self.retry_attempts,
            job_label="image generation",
        )

    def edit(
        self,
        payload: Dict[str, Any],
        image_paths: List[Path],
    ) -> List[str]:
        """Edit input images and return base64-encoded image payloads."""
        return self._with_retries(
            lambda: self._edit(payload, image_paths),
            attempts=self.retry_attempts,
            job_label="image edit",
        )

    @abstractmethod
    def _generate(self, payload: Dict[str, Any]) -> List[str]:
        """Generate images once without cross-provider retries."""

    @abstractmethod
    def _edit(
        self,
        payload: Dict[str, Any],
        image_paths: List[Path],
    ) -> List[str]:
        """Edit input images once without cross-provider retries."""

    async def generate_batch(
        self,
        payload: Dict[str, Any],
        *,
        attempts: int,
        job_label: str,
    ) -> List[str]:
        """Generate one batch job with common retry behavior."""
        return await self._with_async_retries(
            lambda: asyncio.to_thread(self._generate, payload),
            attempts=attempts,
            job_label=job_label,
        )

    def _with_retries(
        self,
        func: Callable[[], List[str]],
        *,
        attempts: int,
        job_label: str,
    ) -> List[str]:
        last_exc: Optional[Exception] = None
        attempts = max(1, attempts)
        for attempt in range(1, attempts + 1):
            try:
                return func()
            except Exception as exc:
                last_exc = exc
                if not _is_transient_error(exc) or attempt == attempts:
                    raise
                sleep_s = _retry_delay_seconds(attempt)
                _print_retry(job_label, attempt, attempts, exc, sleep_s)
                self._retry_sleep(sleep_s)
        raise last_exc or RuntimeError("unknown error")

    async def _with_async_retries(
        self,
        func: Callable[[], Awaitable[List[str]]],
        *,
        attempts: int,
        job_label: str,
    ) -> List[str]:
        last_exc: Optional[Exception] = None
        attempts = max(1, attempts)
        for attempt in range(1, attempts + 1):
            try:
                return await func()
            except Exception as exc:
                last_exc = exc
                if not _is_transient_error(exc) or attempt == attempts:
                    raise
                sleep_s = _retry_delay_seconds(attempt)
                _print_retry(job_label, attempt, attempts, exc, sleep_s)
                await asyncio.sleep(sleep_s)
        raise last_exc or RuntimeError("unknown error")

    def _retry_sleep(self, seconds: float) -> None:
        time.sleep(seconds)


def _retry_delay_seconds(attempt: int) -> float:
    return min(60.0, 2.0**attempt)


def _print_retry(
    job_label: str,
    attempt: int,
    attempts: int,
    exc: Exception,
    sleep_s: float,
) -> None:
    print(
        f"{job_label} attempt {attempt}/{attempts} failed ({exc.__class__.__name__}); retrying in {sleep_s:.1f}s",
        file=sys.stderr,
    )


def _is_transient_error(exc: Exception) -> bool:
    code = _status_code(exc)
    if code is not None:
        return code in RETRYABLE_HTTP_CODES or code >= 500

    name = exc.__class__.__name__.lower()
    if "timeout" in name or "tempor" in name or "ratelimit" in name or "rate_limit" in name:
        return True

    msg = str(exc).lower()
    transient_markers = (
        "429",
        "rate limit",
        "too many requests",
        "timeout",
        "timed out",
        "temporarily",
        "connection reset",
        "connection aborted",
        "remote end closed",
        "network is unreachable",
        "bad gateway",
        "service unavailable",
        "gateway timeout",
        "ssl",
        "eof",
    )
    if any(marker in msg for marker in transient_markers):
        return True
    return re.search(r"http\s+(5[0-9]{2}|429)", msg) is not None


def _status_code(exc: Exception) -> Optional[int]:
    for attr in ("status_code", "status", "code"):
        value = getattr(exc, attr, None)
        if isinstance(value, int):
            return value
    return None
