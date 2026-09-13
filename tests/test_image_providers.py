"""Offline regression checks for image-provider adapters."""

import asyncio
import base64
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/codex-ppt/scripts"))
from image_providers.factory import create_image_provider
from image_providers.muapi import MuAPIImageProvider


class _FakeResponse:
    def __init__(self, body: bytes):
        self.headers = {"Content-Length": str(len(body))}
        self._body = body
        self._read = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self, size=-1):
        if self._read:
            return b""
        self._read = True
        return self._body


class ImageProviderTests(unittest.TestCase):
    def test_factory_selects_muapi_adapter_for_official_https_host(self):
        provider = create_image_provider(
            api_key="test-key",
            base_url="https://api.muapi.ai/v1",
        )
        self.assertIsInstance(provider, MuAPIImageProvider)

    def test_muapi_maps_url_result_without_forwarding_api_key(self):
        image_bytes = b"fake-image-bytes"
        api_requests = []
        image_requests = []

        class Images:
            def generate(self, **payload):
                api_requests.append(payload)
                return SimpleNamespace(data=[SimpleNamespace(url="https://cdn.example.test/image.png")])

        def urlopen(request, timeout):
            image_requests.append((request, timeout))
            return _FakeResponse(image_bytes)

        provider = MuAPIImageProvider(
            api_key="do-not-forward",
            base_url="https://api.muapi.ai/v1",
            client_factory=lambda: SimpleNamespace(images=Images()),
            urlopen=urlopen,
        )

        images = provider.generate({
            "model": "flux-schnell",
            "prompt": "a slide",
            "n": 1,
            "size": "1024x1024",
            "quality": "medium",
            "output_format": "png",
        })

        self.assertEqual(api_requests, [{
            "model": "flux-schnell",
            "prompt": "a slide",
            "n": 1,
            "size": "1024x1024",
        }])
        self.assertEqual(base64.b64decode(images[0]), image_bytes)
        request, timeout = image_requests[0]
        self.assertEqual(timeout, 60)
        self.assertIsNone(request.get_header("Authorization"))
        self.assertEqual(request.get_method(), "GET")

    def test_muapi_batch_uses_same_payload_and_url_decoding(self):
        image_bytes = b"batch-image"
        api_requests = []

        class AsyncImages:
            async def generate(self, **payload):
                api_requests.append(payload)
                return SimpleNamespace(data=[SimpleNamespace(url="https://cdn.example.test/batch.png")])

        provider = MuAPIImageProvider(
            api_key="test-key",
            base_url="https://api.muapi.ai/v1",
            async_client_factory=lambda: SimpleNamespace(images=AsyncImages()),
            urlopen=lambda request, timeout: _FakeResponse(image_bytes),
        )

        images = asyncio.run(provider.generate_batch(
            {
                "model": "flux-schnell",
                "prompt": "a batch slide",
                "n": 1,
                "size": "1792x1024",
                "quality": "medium",
                "output_format": "png",
            },
            attempts=1,
            job_label="[test]",
        ))

        self.assertEqual(api_requests[0], {
            "model": "flux-schnell",
            "prompt": "a batch slide",
            "n": 1,
            "size": "1792x1024",
        })
        self.assertEqual(base64.b64decode(images[0]), image_bytes)

    def test_muapi_rejects_unsupported_provider_options(self):
        provider = MuAPIImageProvider(api_key="test-key", base_url="https://api.muapi.ai/v1")
        with self.assertRaisesRegex(ValueError, r"unsupported option\(s\): quality"):
            provider._prepare_payload({
                "model": "flux-schnell",
                "prompt": "a slide",
                "n": 1,
                "size": "1024x1024",
                "quality": "high",
            })

    def test_url_results_must_use_https(self):
        provider = MuAPIImageProvider(api_key="test-key", base_url="https://api.muapi.ai/v1")
        with self.assertRaisesRegex(ValueError, "must use HTTPS"):
            provider._image_item_to_base64(SimpleNamespace(url="http://cdn.example.test/image.png"))


if __name__ == "__main__":
    unittest.main()
