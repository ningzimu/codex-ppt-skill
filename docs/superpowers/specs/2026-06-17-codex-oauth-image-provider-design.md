# Codex OAuth Image Provider Design

Date: 2026-06-17

## Problem

`codex-ppt` needs every generated slide image to end up at a deterministic local path such as `origin_image/slide_01.png`. The current Codex built-in image tool is no longer a stable fit for that contract because its visible result is not exposed as a local file path to the skill workflow.

The latest `main` branch already has an image provider abstraction:

- `ImageProvider.generate(payload) -> list[str]`
- `ImageProvider.edit(payload, image_paths) -> list[str]`
- `ImageProvider.generate_batch(payload, attempts, job_label) -> list[str]`

Providers return base64 payloads, and `image_gen.py` owns output path creation, overwrite checks, decoding, writing, and optional downscaling. The fix should reuse that abstraction instead of adapting to the UI built-in tool's changing return shape.

## Goals

- Add a high-priority Codex OAuth image provider that reuses the local Codex login from `~/.codex/auth.json` or `CODEX_AUTH_FILE`.
- Keep output path handling identical across Codex OAuth, AtlasCloud, and OpenAI-compatible providers.
- Make Codex subscription users able to generate and edit slide images without configuring `OPENAI_API_KEY`.
- Preserve AtlasCloud and OpenAI-compatible providers behind explicit selection and automatic fallback when Codex OAuth is unavailable.
- Remove `mask` support from the public image CLI so all providers expose the same edit contract.
- Update workflow docs so agents prefer the local CLI with Codex OAuth over the UI built-in image tool.

## Non-Goals

- Do not depend on the Codex UI built-in `image_gen` response format.
- Do not add a new output directory convention.
- Do not add new slide generation modes outside the existing `generate`, `edit`, and `generate-batch` commands.
- Do not preserve provider-specific `mask` behavior.
- Do not add AtlasCloud behavior beyond preserving the existing provider.

## Provider Contract

The image provider contract remains base64-first:

```text
provider.generate(payload) -> base64 images
provider.edit(payload, image_paths) -> base64 images
provider.generate_batch(payload, attempts, job_label) -> base64 images
image_gen.py -> writes --out / --out-dir and optional downscaled copies
```

`ImageProvider.edit()` should drop the `mask_path` parameter. OpenAI-compatible and AtlasCloud providers should accept only the same image inputs as Codex OAuth: prompt plus one or more input image paths.

## Codex OAuth Provider

Add `skills/codex-ppt/scripts/image_providers/codex_oauth.py`.

Authentication:

- Default auth file: `~/.codex/auth.json`
- Override: `CODEX_AUTH_FILE`
- Token field: `tokens.access_token`

Endpoint and models:

- Default base URL: `https://chatgpt.com/backend-api/codex`
- Request path: `/responses`
- Base URL override: `CODEX_RESPONSES_BASE_URL`
- Responses model override: `CODEX_RESPONSES_MODEL`
- Image model: existing `payload["model"]`, usually `gpt-image-2`

Request shape:

- Send a Responses request with `stream: true` and `store: false`.
- User content contains one `input_text` item for the prompt.
- `edit` appends each local input image as an `input_image` data URL.
- Tool is `{"type": "image_generation", ...}`.
- `tool_choice` is `{"type": "image_generation"}`.

Supported tool fields:

- `model`
- `size`
- `quality`
- `output_format`
- `background`
- `output_compression`
- `moderation`

`n` is handled by the provider by issuing one request per requested output, matching the reference implementation pattern from `image-to-editable-ppt`.

SSE parsing:

- Parse `data: ...` server-sent events.
- Fail on `response.failed` or `error`.
- Prefer `response.output_item.done` items where `item.type == "image_generation_call"` and `item.result` is a string.
- Also support completed responses where `response.output` contains `image_generation_call` items.
- Return the extracted base64 payloads only; never write files inside the provider.

## Mask Removal

Real Codex OAuth testing on 2026-06-17 showed:

- Passing `mask` inside the `image_generation` tool returns `HTTP 400` with `Unknown parameter: 'tools[0].mask'`.
- Passing `output_compression` is accepted and returns an image.
- Passing `moderation` is accepted and returns an image.

To keep provider behavior uniform, remove mask support from every backend instead of falling back to a provider-specific API path.

Required changes:

- Remove `--mask` from `image_gen.py edit`.
- Remove mask file validation from `image_gen.py`.
- Remove `mask_path` from `ImageProvider.edit()`.
- Remove OpenAI-compatible mask file forwarding.
- Remove AtlasCloud's mask-specific error path.
- Remove documentation that says edit supports masks.
- Update tests that currently expect mask forwarding.

## Backend Selection

Add a backend selector:

- CLI flag: `--backend auto|codex-oauth|atlascloud|openai-compatible`
- Environment value: `CODEX_PPT_IMAGE_BACKEND`
- Default: `auto`

Selection behavior:

- `auto`:
  - Use `codex-oauth` when a Codex access token is available.
  - Otherwise route AtlasCloud base URLs to `AtlasCloudImageProvider`.
  - Otherwise use `OpenAICompatibleImageProvider`.
- `codex-oauth`:
  - Require a readable Codex access token.
  - Do not require `OPENAI_API_KEY`.
- `atlascloud`:
  - Use `AtlasCloudImageProvider`.
  - Require `OPENAI_API_KEY`.
- `openai-compatible`:
  - Use `OpenAICompatibleImageProvider`.
  - Require `OPENAI_API_KEY`.

`image_gen.py` should stop calling `_ensure_api_key()` before command execution. API key validation should happen only after backend selection proves that an API-key provider is being used.

Dry-run output should include:

- `backend`
- `endpoint`
- `outputs`
- `outputs_downscaled`
- provider-specific preview fields such as `auth_file`, `responses_model`, or mapped AtlasCloud model names.

## Command Behavior

`generate`:

- Build the existing payload.
- Select provider.
- Print provider-specific status.
- Decode returned base64 through the existing shared writer.

`edit`:

- Build the existing payload.
- Validate input image paths.
- Select provider.
- Pass prompt payload and image paths only.
- Decode returned base64 through the existing shared writer.

`generate-batch`:

- Use the same selected provider for every job in the batch.
- For Codex OAuth, implement `generate_batch()` with conservative retry behavior around synchronous `generate()`, using `asyncio.to_thread`.
- Keep existing output path and downscale behavior unchanged.

## Documentation Updates

Update these docs:

- `skills/codex-ppt/docs/backend-selection.md`
- `skills/codex-ppt/docs/cli-api-fallback.md`
- `skills/codex-ppt/docs/image-model-configuration.md`
- `skills/codex-ppt/docs/project-assembly-and-reporting.md`
- `skills/codex-ppt/docs/user-supplied-assets.md` if it still distinguishes built-in vs CLI paths in a way that would route users back to UI image generation.

New workflow guidance:

- Prefer `scripts/image_gen.py` with `--backend auto`.
- In Codex, `auto` should normally select Codex OAuth and write directly to the requested local path.
- Use the UI built-in image tool only if the user explicitly asks for it or the local CLI path is unavailable.
- Ask for `OPENAI_API_KEY` only when the selected provider is AtlasCloud or OpenAI-compatible.

Update `README.md` and `README_en.md` in sync:

- Mention Codex OAuth/member login as the default local CLI path for Codex users.
- Mention third-party providers remain available through explicit backend selection and existing API config.

Update `CHANGELOG.md` under `## Unreleased` with an English entry. Add the PR reference in a follow-up commit after the PR number is known.

## Tests

Add or update tests for:

- Factory auto-selects Codex OAuth when auth is available.
- Factory honors explicit `atlascloud` and `openai-compatible`.
- Factory errors clearly when explicit `codex-oauth` has no auth token.
- Codex OAuth provider reads the token from `~/.codex/auth.json` or `CODEX_AUTH_FILE`.
- Codex OAuth generate posts the expected Responses body and returns base64 from SSE.
- Codex OAuth edit converts local input images to data URLs.
- Codex OAuth parses both `response.output_item.done` and `response.completed` image payload shapes.
- `output_compression` and `moderation` are included in the Codex OAuth tool body.
- `mask` is no longer accepted by the CLI parser or provider interface.
- `image_gen.py --dry-run` shows the selected backend.
- Missing `OPENAI_API_KEY` does not fail when Codex OAuth is selected.
- Missing `OPENAI_API_KEY` still fails when AtlasCloud or OpenAI-compatible is selected for a real call.

Recommended verification command:

```bash
python3 -m pytest tests/test_image_gen_runtime.py tests/test_image_providers.py tests/test_codex_ppt_runtime.py -q
```

If a live smoke test is appropriate after unit tests pass, run one small Codex OAuth dry-run and one low-quality real generation into a temporary path, without printing secrets or image base64.

## Acceptance Criteria

- Codex users with `~/.codex/auth.json` can run `scripts/image_gen.py generate --out <path>` without `OPENAI_API_KEY`.
- Generated and edited images are written only by the shared writer in `image_gen.py`.
- `--mask` is gone from public CLI help and docs.
- `--output-compression` and `--moderation` remain supported and pass through Codex OAuth.
- Existing AtlasCloud and OpenAI-compatible tests continue to pass after their interfaces are updated.
- Backend selection docs no longer recommend the unstable UI built-in image tool as the default Codex path.
