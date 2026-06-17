# Codex OAuth Image Provider Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Codex OAuth image provider that writes generated slide images through the existing local CLI path without requiring `OPENAI_API_KEY`.

**Architecture:** Extend the existing `ImageProvider` abstraction with a `CodexOAuthImageProvider` that returns base64 payloads from the Codex Responses endpoint. Keep output writing centralized in `image_gen.py`, remove public mask support, and route backend selection through `factory.py`.

**Tech Stack:** Python stdlib `urllib.request`, existing `pytest` tests, existing `image_gen.py` CLI, existing Markdown docs.

---

### Task 1: Provider Interface And Existing Providers

**Files:**
- Modify: `skills/codex-ppt/scripts/image_providers/base.py`
- Modify: `skills/codex-ppt/scripts/image_providers/openai_compatible.py`
- Modify: `skills/codex-ppt/scripts/image_providers/atlascloud.py`
- Modify: `tests/test_image_providers.py`

- [ ] **Step 1: Update tests for mask removal**

Replace the OpenAI-compatible edit test so it calls `provider.edit(payload, [image_path])` and asserts image bytes only. Remove mask file setup and mask assertions.

- [ ] **Step 2: Run the focused provider test**

Run: `python3 -m pytest tests/test_image_providers.py::test_openai_compatible_provider_preserves_edit_file_payload_shape -q`

Expected: FAIL because the current interface still requires `mask_path`.

- [ ] **Step 3: Remove `mask_path` from provider interface**

Change `ImageProvider.edit()` to accept only `payload` and `image_paths`.

- [ ] **Step 4: Update existing providers**

Update OpenAI-compatible and AtlasCloud providers to match the new `edit(payload, image_paths)` signature. Remove OpenAI mask file forwarding and AtlasCloud's mask-specific error branch.

- [ ] **Step 5: Run provider tests**

Run: `python3 -m pytest tests/test_image_providers.py -q`

Expected: PASS after test updates and provider signature changes.

### Task 2: Codex OAuth Provider

**Files:**
- Create: `skills/codex-ppt/scripts/image_providers/codex_oauth.py`
- Modify: `skills/codex-ppt/scripts/image_providers/__init__.py`
- Modify: `tests/test_image_providers.py`

- [ ] **Step 1: Add failing tests**

Add tests for:

- reading `CODEX_AUTH_FILE`
- generating a Responses body with `image_generation`
- parsing `response.output_item.done`
- parsing `response.completed`
- edit image conversion to data URLs
- passing `output_compression` and `moderation`

- [ ] **Step 2: Run Codex OAuth tests**

Run: `python3 -m pytest tests/test_image_providers.py -q`

Expected: FAIL because `image_providers.codex_oauth` does not exist.

- [ ] **Step 3: Implement provider**

Create `CodexOAuthImageProvider` with:

- auth file/token helpers
- `available()`
- `generate(payload)`
- `edit(payload, image_paths)`
- `generate_batch(payload, attempts, job_label)`
- SSE parser and payload extractor
- data URL conversion for input images

- [ ] **Step 4: Run provider tests**

Run: `python3 -m pytest tests/test_image_providers.py -q`

Expected: PASS.

### Task 3: Backend Selection And CLI Runtime

**Files:**
- Modify: `skills/codex-ppt/scripts/image_providers/factory.py`
- Modify: `skills/codex-ppt/scripts/image_gen.py`
- Modify: `tests/test_image_gen_runtime.py`
- Modify: `tests/test_image_providers.py`

- [ ] **Step 1: Add failing backend selection tests**

Add tests that assert:

- `auto` selects Codex OAuth when auth is available.
- explicit `atlascloud` and `openai-compatible` still work.
- explicit `codex-oauth` without auth raises a clear error.
- dry-run preview includes `backend`.
- missing `OPENAI_API_KEY` does not fail when Codex OAuth is selected.

- [ ] **Step 2: Run focused tests**

Run: `python3 -m pytest tests/test_image_gen_runtime.py tests/test_image_providers.py -q`

Expected: FAIL because selector and CLI flags are missing.

- [ ] **Step 3: Implement backend selector**

Add `backend` argument support in `factory.create_image_provider()` and `--backend` / `CODEX_PPT_IMAGE_BACKEND` support in `image_gen.py`.

- [ ] **Step 4: Remove early API-key gate**

Replace the current unconditional `_ensure_api_key(args.dry_run)` call with backend-aware validation after provider selection. Codex OAuth must not require `OPENAI_API_KEY`.

- [ ] **Step 5: Remove CLI mask argument**

Remove `edit_parser.add_argument("--mask")`, mask validation, and mask preview output.

- [ ] **Step 6: Run runtime tests**

Run: `python3 -m pytest tests/test_image_gen_runtime.py tests/test_image_providers.py -q`

Expected: PASS.

### Task 4: Runtime Doctor And Documentation

**Files:**
- Modify: `skills/codex-ppt/scripts/codex_ppt_runtime.py`
- Modify: `tests/test_codex_ppt_runtime.py`
- Modify: `skills/codex-ppt/docs/backend-selection.md`
- Modify: `skills/codex-ppt/docs/cli-api-fallback.md`
- Modify: `skills/codex-ppt/docs/image-model-configuration.md`
- Modify: `skills/codex-ppt/docs/project-assembly-and-reporting.md`
- Modify: `skills/codex-ppt/docs/user-supplied-assets.md`
- Modify: `README.md`
- Modify: `README_en.md`
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Add or update doctor tests**

If doctor reports backend status, add a test for Codex OAuth availability. Keep AtlasCloud `/models` skip behavior intact.

- [ ] **Step 2: Update docs**

Make `scripts/image_gen.py --backend auto` the preferred Codex path, document Codex OAuth auth reuse, remove mask references, and keep README Chinese/English content aligned.

- [ ] **Step 3: Update changelog**

Add an English `## Unreleased` fix entry without PR number. Add the PR reference later after opening the PR.

- [ ] **Step 4: Run doc-related tests**

Run: `python3 -m pytest tests/test_codex_ppt_runtime.py -q`

Expected: PASS.

### Task 5: Verification And Commit

**Files:**
- All changed files from previous tasks.

- [ ] **Step 1: Run focused suite**

Run: `python3 -m pytest tests/test_image_gen_runtime.py tests/test_image_providers.py tests/test_codex_ppt_runtime.py -q`

Expected: PASS.

- [ ] **Step 2: Run CLI help checks**

Run:

```bash
python3 skills/codex-ppt/scripts/image_gen.py generate --help
python3 skills/codex-ppt/scripts/image_gen.py edit --help
```

Expected: both commands exit 0, show `--backend`, and `edit --help` does not show `--mask`.

- [ ] **Step 3: Run Codex OAuth dry-run**

Run a dry-run with `--backend auto` and no output generation.

Expected: JSON preview includes `backend: codex-oauth` when local Codex auth is present.

- [ ] **Step 4: Review diff**

Run: `git diff --stat` and inspect touched files.

Expected: changes are scoped to provider, CLI, docs, tests, README, changelog, and Superpowers docs.

- [ ] **Step 5: Commit**

Commit implementation changes with an English Conventional Commit message.
