# Changelog

Release notes are generated from this file. Keep changelog entries in English.

## Unreleased

### Improvements

- Package GitHub Release assets as a skill-only zip for direct manual installation. (#20)

## 0.3.0

### Documentation

- Add an `Attention Is All You Need` example deck with preserved paper figures. (#18)
- Require subagent-based per-slide generation whenever subagents are available. (#18)
- Add mandatory phase gates and stricter image backend selection rules to the codex-ppt skill. (#18)
- Add README examples for assigning original paper figures to specific slides, referencing issue #14. (#18)
- Document Markdown image references inside `Required images`. (#18)
- Clarify how to preserve user-supplied figures and result charts in generated decks, including subagent slide generation with approved sample-slide style references. (#18)
- Document simplified prompt preparation with one self-contained JSON job per slide instead of a separate prompt file and job manifest. (#18)
- Document relative input image path resolution in slide jobs against the `deck_spec.json` directory. (#18)
- Reject duplicate slide numbers when preparing per-slide prompt jobs. (#18)
- Clarify that CLI/API fallback must not text-generate slide jobs that require input images. (#18)

## 0.2.1

### Documentation

- Fix README badge labels and GitHub star/fork badge style. (#16)
- Add GitHub star and fork badges to both READMEs. (#15)
- Recommend `npx skills` installation commands for Codex, Claude Code, and Hermes Agent. (#13)

### Fixes

- Mark local image API fallback config as optional so built-in image tool users do not see unnecessary missing-config warnings. (#12)
- Clarify that Codex built-in image generation remains the preferred `gpt-image-2` path when available, avoiding unnecessary API key prompts. (#11)
- Omit empty changelog subsections from generated release notes. (#10)

## 0.2.0

### Features

- Add ClawHub publishing workflow and skill metadata. (#8)
- Add third-party OpenAI-compatible image API fallback for codex-ppt. (#6)
- Add shared runtime configuration for API key, base URL, and image model reuse. (#6)
- Support Claude Code, OpenClaw, Hermes Agent, and other `SKILL.md`-based agent usage. (#6)

### Improvements

- Default image fallback generation to 2K 16:9 output. (#6)

### Fixes

### Documentation

- Add ClawHub badge and OpenClaw install command to the READMEs. (#8)
- Require explicit image backend confirmation before sample generation. (#6)
- Add agent contribution guidelines for PR, changelog, and release workflows. (#5)

## 0.1.0

### Features

- Add the initial Codex PPT skill and style assets. (#1)

### Documentation

- Add installation and usage documentation. (#2)
