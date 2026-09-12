"""Offline regression checks for GPT Image model requests."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/codex-ppt/scripts"))
import image_gen
import codex_ppt_runtime


class ImageModelTests(unittest.TestCase):
    def test_new_models_accept_quality_and_custom_size(self):
        for model in (
            "gpt-image-2.5-flare",
            "gpt-image-2.5-sunburst",
            "openai/gpt-image-2.5-flare-2026-09-08",
            "openai/gpt-image-2.5-sunburst/edit",
        ):
            for quality in ("xhigh", "max"):
                with self.subTest(model=model, quality=quality):
                    image_gen._validate_generate_payload({
                        "model": model, "quality": quality,
                        "size": "2560x1440", "background": "transparent",
                    })

    def test_legacy_models_reject_new_quality(self):
        for model in ("gpt-image-2", "openai/gpt-image-2/edit", "gpt-image-1.5"):
            for quality in ("xhigh", "max"):
                with self.subTest(model=model, quality=quality), self.assertRaises(SystemExit):
                    image_gen._validate_quality(quality, model)

    def test_unknown_model_does_not_inherit_new_quality(self):
        for model in ("gpt-image-2.5", "gpt-image-2.5-flare-invalid", "gpt-image-20"):
            with self.subTest(model=model), self.assertRaises(SystemExit):
                image_gen._validate_quality("max", model)

    def test_legacy_transparency_and_fidelity_rules(self):
        for model in ("gpt-image-2", "openai/gpt-image-2-2026-04-21/edit"):
            with self.subTest(model=model), self.assertRaises(SystemExit):
                image_gen._validate_model_specific_options(model=model, background="transparent")
            with self.subTest(model=model), self.assertRaises(SystemExit):
                image_gen._validate_model_specific_options(model=model, background=None, input_fidelity="high")
        image_gen._validate_model_specific_options(model="gpt-image-1.5", background="transparent")

    def test_size_constraints_remain_enforced(self):
        for model in ("gpt-image-2.5-flare", "gpt-image-2.5-sunburst", "gpt-image-2"):
            image_gen._validate_size("3840x2160", model)
            for size in ("4096x2160", "1025x1024", "3840x3840", "3840x1024", "256x256"):
                with self.subTest(model=model, size=size), self.assertRaises(SystemExit):
                    image_gen._validate_size(size, model)

    def run_cli(self, *args):
        output = io.StringIO()
        with (
            patch.object(sys, "argv", ["image_gen.py", *args]),
            patch.object(image_gen, "_load_runtime_env"),
            patch.dict("os.environ", {"OPENAI_BASE_URL": "https://api.openai.com/v1"}, clear=True),
            contextlib.redirect_stdout(output),
        ):
            self.assertEqual(image_gen.main(), 0)
        return json.loads(output.getvalue())

    def test_cli_defaults_preserve_size_and_quality(self):
        result = self.run_cli("generate", "--prompt", "slide", "--dry-run")
        self.assertEqual(result["model"], "gpt-image-2.5-flare")
        self.assertEqual(result["model"], codex_ppt_runtime.DEFAULT_MODEL)
        self.assertEqual(result["size"], "2560x1440")
        self.assertEqual(result["quality"], "medium")

    def test_generate_and_edit_transparent_requests(self):
        with tempfile.TemporaryDirectory() as temp:
            image = Path(temp) / "reference.png"
            image.write_bytes(b"reference")
            for command in (("generate",), ("edit", "--image", str(image))):
                for fmt in ("png", "webp"):
                    with self.subTest(command=command[0], fmt=fmt):
                        result = self.run_cli(
                            *command, "--prompt", "slide",
                            "--model", "gpt-image-2.5-sunburst",
                            "--quality", "max", "--background", "transparent",
                            "--output-format", fmt,
                            "--out", str(Path(temp) / f"out.{fmt}"), "--dry-run",
                        )
                        self.assertEqual(result["model"], "gpt-image-2.5-sunburst")
                        self.assertEqual(result["quality"], "max")
                        self.assertEqual(result["background"], "transparent")
                        self.assertEqual(result["output_format"], fmt)

    def test_transparent_jpeg_is_rejected(self):
        with self.assertRaises(SystemExit):
            self.run_cli("generate", "--prompt", "slide", "--background", "transparent", "--output-format", "jpeg", "--dry-run")

    def test_batch_overrides_validate_effective_model(self):
        with tempfile.TemporaryDirectory() as temp:
            jobs = Path(temp) / "jobs.jsonl"
            job = {
                "prompt": "slide", "model": "gpt-image-2.5-sunburst",
                "quality": "xhigh", "background": "transparent", "output_format": "webp",
            }
            jobs.write_text(json.dumps(job) + "\n")
            args = ("generate-batch", "--input", str(jobs), "--out-dir", temp, "--dry-run")
            result = self.run_cli(*args)
            self.assertEqual(result["model"], job["model"])
            self.assertEqual(result["quality"], "xhigh")
            self.assertEqual(result["output_format"], "webp")
            job["model"] = "gpt-image-2"
            jobs.write_text(json.dumps(job) + "\n")
            with self.assertRaises(SystemExit):
                self.run_cli(*args)


if __name__ == "__main__":
    unittest.main()
