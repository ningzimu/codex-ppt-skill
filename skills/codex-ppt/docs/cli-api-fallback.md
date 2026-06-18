# Local Image CLI

Use this reference after the local image CLI has been selected for sample generation. The main `SKILL.md` owns the backend decision rules; this document owns commands, runtime setup, image-input limits, editing, transparency, and troubleshooting.

Let `{skill_root}` mean the directory containing `SKILL.md`.

## Runtime Setup

Local image CLI commands use the shared runtime environment. Before running `scripts/assemble_ppt.py` or image commands, make sure the shared runtime exists. If `~/.codex-ppt-skill/.venv/bin/python` is missing, or if importing script dependencies fails, create or refresh the environment:

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py bootstrap
```

This is an internal setup step for the skill. Do not ask the user to run it unless dependency installation fails and user approval or troubleshooting is required.

The local image CLI loads `~/.codex-ppt-skill/.env` automatically for image backend configuration. Do not manually parse `.env`. For API key, base URL, model, backend, and config troubleshooting, read `image-model-configuration.md` only after the selected provider reports missing or invalid configuration, when the user explicitly wants to change those settings, or when a real API call reports authentication, permission, base URL, or model availability failure.

## Generate One Slide

Sample-generation command:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py generate \
  --backend auto \
  --model gpt-image-2 \
  --prompt "{sample_prompt}" \
  --size 2048x1152 \
  --quality medium \
  --out {base_dir}/{deck_name}/origin_image/slide_01.png
```

For sample generation, pass the prompt directly with `--prompt`. Do not create `style.md`, draft prompt files, formal `prompts/slide_XX.json` job files, or `slide_jobs.json` before the sample is approved. If the sample prompt is too long for a shell argument, pipe it with `--prompt-file -` instead of writing a prompt file.

The local image CLI accepts model names containing `gpt-image-`, such as `gpt-image-2` or `openai/gpt-image-2`.

When generating from saved `prompts/slide_XX.json` files, use the job's `prompt` field only when the job does not require input images:

```bash
python3 -c 'import json, pathlib; print(json.loads(pathlib.Path("{base_dir}/{deck_name}/prompts/slide_01.json").read_text())["prompt"])' | \
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py generate \
  --backend auto \
  --prompt-file - \
  --size 2048x1152 \
  --quality medium \
  --out {base_dir}/{deck_name}/origin_image/slide_01.png
```

Before using this text-only `generate` path, inspect the assigned `prompts/slide_XX.json`. If `style_reference_images` is non-empty, visually inspect those images first, then continue with `generate`; do not pass style references as `--image` inputs. If `input_images` is non-empty or `requires_context_images` is true, use `scripts/image_gen.py edit --image ...` with every required source image, or stop and ask the user whether to switch backend. Do not generate a text-only replacement for a strict input asset.

## Capabilities And Sizes

The local image CLI supports:

- `generate`: create one or more images from a prompt.
- `edit`: edit one or more existing images.

The provider abstraction retries transient network and provider failures up to five attempts before surfacing an error.

When Codex OAuth is selected, the CLI reuses local Codex auth and calls the official Codex images endpoints.

The local image CLI defaults to 2K 16:9 landscape output, `2048x1152`, because it is an official popular GPT Image 2 landscape size and keeps slide text clearer while staying below the pixel limit. For 4K landscape slides, use `--size 3840x2160 --quality high` only when the user asks for 4K, text-heavy slides need sharper output, or the default result is blurry. For portrait assets, use `--size 2160x3840` only if the user requests portrait output.

## Editing Slides

If a slide is mostly correct but has an issue, use the selected backend's edit capability when available:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py edit \
  --backend auto \
  --image {slide_path} \
  --prompt {edit_prompt} \
  --out {new_slide_path}
```

Replace the final slide only after validating the edited output.

## Transparent Backgrounds

Transparent-background requests:

- Built-in mode should use a flat chroma-key background and local removal when appropriate.
- The local image CLI should also prefer chroma-key generation plus `scripts/remove_chroma_key.py` for simple opaque subjects.
- `gpt-image-2` does not support `--background transparent`. If the user needs true model-native transparency, ask before switching to `--model gpt-image-1.5 --background transparent`.

## Assembly And Doctor

`assemble_ppt.py` supports `16:9` and `4:3`. Use `16:9` unless the user requests otherwise.

Run the doctor when troubleshooting local image backend access:

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py doctor --check-api
```
