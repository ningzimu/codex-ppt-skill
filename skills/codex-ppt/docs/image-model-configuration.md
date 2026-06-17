# Image Model Configuration

Use this reference only when the local image CLI reports missing config or the runtime config must be changed.

Do not manually parse `.env`. The local image CLI loads the shared config automatically. Run the image command first, then use this document only if the selected backend reports missing or invalid configuration.

Ask the user to configure or update settings only when:

- The selected AtlasCloud or OpenAI-compatible provider reports missing `OPENAI_API_KEY`.
- The user explicitly wants to change API key, base URL, backend, or model.
- A real API call fails with authentication, permission, base URL, or model-not-found errors.

## When Configuration Is Needed

Configure image API access only for AtlasCloud or OpenAI-compatible image generation.

Typical cases:

- The user explicitly chooses AtlasCloud or another third-party API.
- The skill is being used from Claude Code, OpenClaw, Hermes Agent, or another agent without Codex OAuth auth and without another local image backend.

If Codex is being used through a GPT subscription and `~/.codex/auth.json` or `CODEX_AUTH_FILE` is available, the local CLI can use `--backend auto` / Codex OAuth and should not ask the user to configure `OPENAI_API_KEY`.

## Required And Optional Values

- `OPENAI_API_KEY` is required only for AtlasCloud and OpenAI-compatible providers.
- `OPENAI_BASE_URL` is optional. When it is unset, the CLI uses the official OpenAI API for `openai-compatible`. When it is set, the CLI uses the configured third-party provider base URL.
- `CODEX_PPT_IMAGE_MODEL` is optional. The default is `gpt-image-2`. Use a custom value only when the provider requires one.
- `CODEX_PPT_IMAGE_BACKEND` is optional. The default is `auto`, which prefers Codex OAuth when available.

Configure provided API settings with `scripts/codex_ppt_runtime.py config --api-key`. The config command writes `~/.codex-ppt-skill/.env`.

## Codex OAuth Example

No `OPENAI_API_KEY` is required when local Codex auth is available:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/image_gen.py generate \
  --backend auto \
  --prompt "{sample_prompt}" \
  --out {base_dir}/{deck_name}/origin_image/slide_01.png
```

The Codex OAuth backend reuses local Codex auth and calls the official Codex images endpoints, `/backend-api/codex/images/generations` and `/backend-api/codex/images/edits`.

Use `--backend codex-oauth` only when you want to require this route and fail if Codex auth is missing.

## Official OpenAI Example

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-api-key" \
  --model gpt-image-2
```

## OpenAI-Compatible Provider Example

Use this shape for providers that implement the OpenAI Images API paths used by the local image CLI.

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-provider-api-key" \
  --base-url "https://xxxx.example.com/v1" \
  --model gpt-image-2
```

This produces the same effective runtime config as:

```env
OPENAI_API_KEY=your-provider-api-key
OPENAI_BASE_URL=https://xxxx.example.com/v1
CODEX_PPT_IMAGE_MODEL=gpt-image-2
CODEX_PPT_IMAGE_BACKEND=openai-compatible
```

For OpenAI-compatible providers, `OPENAI_BASE_URL` should normally end at the provider's `/v1` root. Do not set it to `/images/generations`, `/images/edits`, or another terminal endpoint. The local image CLI appends the image-generation or image-edit path through the OpenAI SDK.

Use the provider's model name only when the provider documents a custom name. Otherwise prefer `gpt-image-2`.

## AtlasCloud Example

For AtlasCloud, set `--model` to the base model name. The CLI chooses the matching generation or editing model route internally.

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-atlascloud-api-key" \
  --base-url "https://api.atlascloud.ai/api/v1/model" \
  --model openai/gpt-image-2 \
  --backend atlascloud
```

## Runtime Config

The config is written to:

```text
~/.codex-ppt-skill/.env
```

The file is created with mode `0600`. It is shared by Codex, Claude Code, OpenClaw, Hermes Agent, and other local agents.

Process environment variables override `.env` values. A command-line `--model` overrides `CODEX_PPT_IMAGE_MODEL` for that single command.
