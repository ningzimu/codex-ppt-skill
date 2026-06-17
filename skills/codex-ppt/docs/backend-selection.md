# Backend Selection

Read this before selecting the image backend or generating the first sample slide.

This skill supports two local image-generation routes:

1. Local image CLI, using `scripts/image_gen.py --backend auto`. In Codex this normally selects Codex OAuth and reuses the local Codex login.
2. Third-party/API provider adapters through the same CLI, such as AtlasCloud or OpenAI-compatible providers.

The UI built-in image tool, such as Codex `image_gen` or OpenClaw `image_generate`, is no longer the default route for Codex because it may not expose a stable local output path to the skill workflow.

## Decision Rules

- Prefer `scripts/image_gen.py --backend auto` for Codex PPT slide images. It writes directly to the requested `--out` path and keeps the same contract for sample slides, final slides, edits, and batch generation.
- In Codex, `--backend auto` uses Codex OAuth first when `~/.codex/auth.json` or `CODEX_AUTH_FILE` is available. This reuses the user's Codex/GPT subscription login and does not require `OPENAI_API_KEY`.
- If Codex OAuth is unavailable, `--backend auto` falls through to AtlasCloud when `OPENAI_BASE_URL` points to AtlasCloud, otherwise to the OpenAI-compatible provider.
- Use `--backend atlascloud` or `--backend openai-compatible` only when the user explicitly wants that provider or Codex OAuth is unavailable.
- Use the UI built-in image tool only when the user explicitly asks for it or the local CLI route is unavailable. If using the UI tool, ensure the final slide image is still saved and recorded at the expected project-local path.
- Before generating the first image, tell the user which local backend will be used and which auth/config it will rely on. Do not ask for separate backend confirmation.
- The local image CLI loads `~/.codex-ppt-skill/.env` automatically. Run the CLI normally; do not manually parse `.env` or ask for configuration before an error.
- Ask for `OPENAI_API_KEY` configuration only after the selected backend is AtlasCloud or OpenAI-compatible and that provider reports missing config, after authentication/base URL/model errors, or when the user explicitly wants to change API settings.

Read `cli-api-fallback.md` before generating images with `scripts/image_gen.py`. For API key, base URL, model, backend, and `.env` configuration, read `image-model-configuration.md` only after the selected provider reports missing or invalid configuration, or when the user explicitly wants to change those settings.

## Sample Generation Announcement

Codex OAuth local backend:

```text
我将使用本地图片 CLI 生成样张：`scripts/image_gen.py --backend auto`。当前会走 Codex OAuth，复用本机 Codex/GPT 会员认证，并把图片直接写到项目的 `origin_image/` 路径。
```

Third-party provider:

```text
我将使用本地图片 CLI 的第三方/API provider 生成样张，读取 `~/.codex-ppt-skill/.env` 中的 `OPENAI_BASE_URL` / `CODEX_PPT_IMAGE_MODEL` 配置。
```

If the user questions the backend, resolve that before generating the sample slide. Otherwise continue directly to sample generation and ask for approval after showing the sample.
