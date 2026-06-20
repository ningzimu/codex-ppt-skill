# CLI/API Fallback

Use this reference only after CLI/API fallback has been selected and confirmed with the user. The main `SKILL.md` owns the backend decision rules; this document owns fallback commands, runtime setup, image-input limits, editing, transparency, and troubleshooting.

Let `{skill_root}` mean the directory containing `SKILL.md`.

## Runtime Setup

CLI/API fallback commands use the shared runtime environment. Before running `scripts/assemble_ppt.py` or fallback image commands, make sure the shared runtime exists. If `~/.codex-ppt-skill/.venv/bin/python` is missing, or if importing script dependencies fails, create or refresh the environment:

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py bootstrap
```

This is an internal setup step for the skill. Do not ask the user to run it unless dependency installation fails and user approval or troubleshooting is required.

The fallback CLI loads `~/.codex-ppt-skill/.env` automatically for `OPENAI_API_KEY`, `OPENAI_BASE_URL`, and `CODEX_PPT_IMAGE_MODEL`. Do not manually parse `.env`. For API key, base URL, model, and config troubleshooting, read `image-model-configuration.md` only after the fallback CLI reports missing or invalid configuration, when the user explicitly wants to change those settings, or when a real API call reports authentication, permission, base URL, or model availability failure.

## Generate One Slide

Basic generation command:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py generate \
  --model gpt-image-2 \
  --prompt-file {prompt_file} \
  --size 2560x1440 \
  --quality medium \
  --out {base_dir}/{deck_name}/origin_image/slide_01.png
```

The fallback CLI accepts model names containing `gpt-image-`, such as `gpt-image-2` or `openai/gpt-image-2`.

When generating from saved `prompts/slide_XX.json` files, use the job's `prompt` field only when the job does not require input images:

```bash
python3 -c 'import json, pathlib; print(json.loads(pathlib.Path("{base_dir}/{deck_name}/prompts/slide_01.json").read_text())["prompt"])' | \
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py generate \
  --prompt-file - \
  --size 2560x1440 \
  --quality medium \
  --out {base_dir}/{deck_name}/origin_image/slide_01.png
```

Before using this text-only `generate` path, inspect the assigned `prompts/slide_XX.json`. If `input_images` is non-empty or `requires_context_images` is true, this command is not sufficient because it does not attach those images. Use a selected backend/path that can pass the required images, such as the built-in image tool with the images visible in context or a CLI/API edit/image-input path that supplies every required source image. If no such path is available, stop and ask the user whether to switch backend. Do not generate a text-only replacement for a strict input asset.

## Capabilities And Sizes

The fallback CLI supports:

- `generate`: create one or more images from a prompt.
- `edit`: edit one or more existing images, optionally with a mask.

The fallback CLI defaults to 2K 16:9 landscape output, `2560x1440`, because it keeps slide text clearer while staying below the `gpt-image-2` pixel limit. For 4K landscape slides, use `--size 3840x2160 --quality high` only when the user asks for 4K, text-heavy slides need sharper output, or the default result is blurry. For portrait assets, use `--size 2160x3840` only if the user requests portrait output.

## Editing Slides

If a slide is mostly correct but has a localized issue, use the selected backend's edit capability when available. In CLI/API fallback mode:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py edit \
  --image {slide_path} \
  --prompt {edit_prompt} \
  --out {new_slide_path}
```

Replace the final slide only after validating the edited output.

## Transparent Backgrounds

Transparent-background requests:

- Built-in mode should use a flat chroma-key background and local removal when appropriate.
- CLI/API fallback should also prefer chroma-key generation plus `scripts/remove_chroma_key.py` for simple opaque subjects.
- `gpt-image-2` does not support `--background transparent`. If the user needs true model-native transparency, ask before switching to `--model gpt-image-1.5 --background transparent --output-format png`.

## Assembly And Doctor

`assemble_ppt.py` supports `16:9` and `4:3`. Use `16:9` unless the user requests otherwise.

Run the API doctor only when troubleshooting fallback API access:

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py doctor --check-api
```
