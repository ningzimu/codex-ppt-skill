# Image Model Configuration

Use this reference only when the local API/CLI fallback is needed and the runtime config is missing or must be changed.

Do not manually parse `.env`. The fallback CLI loads the shared config automatically. Run the fallback command first, then use this document only if the CLI reports missing or invalid configuration.

Ask the user to configure or update settings only when:

- The fallback CLI reports missing `OPENAI_API_KEY`.
- The user explicitly wants to change API key, base URL, or model.
- A real API call fails with authentication, permission, base URL, or model-not-found errors.

## When Configuration Is Needed

Configure image API access only for API/CLI fallback image generation.

Typical cases:

- Codex is using a third-party API or OpenAI-compatible proxy for image generation.
- The skill is being used from Claude Code, OpenClaw, Hermes Agent, or another agent without Codex's built-in image tool.

If Codex is being used through a GPT subscription and the built-in image tool is available, do not ask the user to configure `gpt-image-2`.

## Required And Optional Values

- `OPENAI_API_KEY` is required for real API/CLI fallback calls.
- `OPENAI_BASE_URL` is optional. When it is unset, the CLI uses the official OpenAI API. When it is set, the CLI uses the configured third-party provider base URL.
- `CODEX_PPT_IMAGE_MODEL` is optional. The default is `gpt-image-2`. Use a custom value only when the provider requires one.

Configure provided API settings with `scripts/codex_ppt_runtime.py config --api-key`. The config command writes `~/.codex-ppt-skill/.env`.

## Official OpenAI Example

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-api-key" \
  --model gpt-image-2
```

## OpenAI-Compatible Provider Example

Use this shape for providers that implement the OpenAI Images API paths used by the fallback CLI.

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
```

For OpenAI-compatible providers, `OPENAI_BASE_URL` should normally end at the provider's `/v1` root. Do not set it to `/images/generations`, `/images/edits`, or another terminal endpoint. The fallback CLI appends the image-generation or image-edit path through the OpenAI SDK.

Use the provider's model name only when the provider documents a custom name. Otherwise prefer `gpt-image-2`.

## AtlasCloud Example

For AtlasCloud, set `--model` to the base model name. The CLI chooses the matching generation or editing model route internally.

```bash
python3 {skill_root}/scripts/codex_ppt_runtime.py config \
  --api-key "your-atlascloud-api-key" \
  --base-url "https://api.atlascloud.ai/api/v1/model" \
  --model openai/gpt-image-2
```

## Runtime Config

The config is written to:

```text
~/.codex-ppt-skill/.env
```

The file is created with mode `0600`. It is shared by Codex, Claude Code, OpenClaw, Hermes Agent, and other local agents.

Process environment variables override `.env` values. A command-line `--model` overrides `CODEX_PPT_IMAGE_MODEL` for that single command.
