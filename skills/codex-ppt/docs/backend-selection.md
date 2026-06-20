# Backend Selection

Read this before confirming the image backend or generating the first sample slide.

This skill supports two image backends:

1. Built-in image tool, preferred when available. Example tool names: Codex `image_gen`; OpenClaw `image_generate`.
2. Local API/CLI fallback, using `scripts/image_gen.py`.

## Decision Rules

- Before recommending CLI/API fallback, actively check whether the built-in image generation tool is callable in the current environment. Do not infer availability only from the agent name or subscription context.
- Prefer the built-in image tool when available. In Codex, this usually means the built-in `image_gen` tool. In OpenClaw, this may be `image_generate`. Resolution, quality, aspect ratio, slide-edit requests, or the user saying "use `gpt-image-2`" do not require CLI/API fallback.
- In Codex, treat the built-in image tool as the preferred `gpt-image-2` path when it is available. If the user has a GPT subscription / Codex environment and asks for `gpt-image-2`, do not switch to `scripts/image_gen.py` only to satisfy the model name.
- Use CLI/API fallback only when the built-in tool is unavailable, the built-in tool failed for a required capability, the user explicitly asks for API/CLI or a third-party image API/provider adapter, or the requested capability is unavailable in the built-in tool.
- Do not recommend CLI/API fallback merely because it provides direct `--out` file paths, easier local file management, local config reuse, batch generation convenience, or simpler automation.
- Before generating the first image, tell the user which tool availability you checked, which backend you plan to use, why fallback is or is not needed, and ask for confirmation. Do not treat being in a specific agent environment as proof that the built-in image tool is available.
- CLI/API fallback loads `~/.codex-ppt-skill/.env` automatically. Run the CLI normally; do not manually parse `.env` or ask for configuration before an error.
- Ask for `OPENAI_API_KEY` configuration only after you have intentionally selected CLI/API fallback and that fallback reports missing config, after authentication/base URL/model errors, or when the user explicitly wants to change API settings. Do not mention missing `OPENAI_API_KEY` while the Codex built-in image tool is available. Configure provided values with `scripts/codex_ppt_runtime.py config --api-key`.

If CLI/API fallback is selected, read `cli-api-fallback.md` before generating images. For API key, base URL, model, and `.env` configuration, read `image-model-configuration.md` only after the fallback CLI reports missing or invalid configuration, or when the user explicitly wants to change those settings.

## Confirmation Text

Built-in backend:

```text
我检查到当前环境可调用内置图片生成工具（Codex 通常是 image_gen，OpenClaw 通常是 image_generate），因此准备优先用内置工具生成样张，不切到本地 API/CLI fallback。可以开始生成 1 页样张吗？
```

CLI/API fallback:

```text
我检查后没有可用的内置图片生成工具，或内置工具缺少本页必需能力，因此准备使用本地 API/CLI fallback 生成样张，读取 ~/.codex-ppt-skill/.env 中的 OPENAI_BASE_URL / CODEX_PPT_IMAGE_MODEL 配置。可以开始生成 1 页样张吗？
```

Wait for confirmation before generating the sample slide. If the user questions the backend, resolve that before continuing.
