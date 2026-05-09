# Changelog

Release notes are generated from this file. Keep changelog entries in English.

## Unreleased

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
