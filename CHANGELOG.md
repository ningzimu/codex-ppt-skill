# Changelog

Release notes are generated from this file. Keep changelog entries in English.

## Unreleased

### Improvements

- Make the Party-and-Government Red style more adaptable by replacing fixed layout and motif prescriptions with content-driven visual guidance. (#82)
- Make the Teaching Courseware style more adaptable across disciplines by removing example-specific subject matter, fixed module counts, and repetitive card-grid assumptions. (#82)

## 0.5.4

### Features

- Add a reusable Party-and-Government Red style reference and preview for formal public-sector presentations. (#79)
- Add a reusable Teaching Courseware style reference and preview for academic and technical learning presentations. (#79)

## 0.5.3

### Improvements

- Simplify generated speaker notes to include only the spoken talk track for each slide. (#76)

### Documentation

- Add a GitHub Pages documentation site for codex-ppt usage notes. (#76)

## 0.5.2

### Fixes

- Revert the codex-ppt skill contents to the v0.5.0 release state. (#67)

## 0.5.1

### Improvements

- Update the codex-ppt workflow defaults for 2K 16:9 image output, direct sample prompts, mandatory subagent dispatch/refill behavior, and edit-based single-slide revisions. (#64)

### Fixes

- Add Codex OAuth image generation through local Codex auth using the official images endpoints, with provider-level retries for transient failures. (#64)

## 0.5.0

### Features

- Add an AtlasCloud image provider adapter for GPT Image 2 generation and editing. (#60)

### Documentation

- Document OpenAI-compatible and AtlasCloud image provider configuration examples. (#60)

## 0.4.4

### Fixes

- Sort slide images by numeric index when assembling decks. (#52)

### Documentation

- Add README one-sentence install guidance and related project links. (#49)
- Refresh README user guidance for PPT generation workflows, image backend setup, style reuse, and slide revision tips. (#48)

## 0.4.3

### Features

- Add a reusable McKinsey style reference and README preview for conclusion-first consulting decks. (#45)

### Improvements

- Refresh the hand-drawn technical style preview with a clearer Codex PPT explainer illustration. (#45)


## 0.4.2

### Documentation

- Expand speaker notes guidance so `speech.md` uses content-specific delivery styles, natural presenter-facing talk tracks, and separate emphasis and pacing cues. (#43)

## 0.4.1

### Fixes

- Use a cross-platform file lock for slide generation state files so Windows can run state recording scripts. (#41)

## 0.4.0

### Improvements

- Add deck-level and slide-level context fields to slide prompt jobs so subagents receive self-contained task packets. (#39)
- Add a reusable style-library workflow for saving approved deck styles into `references/` for future decks. (#39)

### Fixes

- Prevent concurrent slide state writes from overwriting dispatch, result, or blocker records. (#39)

### Documentation

- Move detailed codex-ppt workflow guidance into supporting docs and keep the main skill file within SkillHub limits. (#39)
- Clarify how to use user-specified styles and image/PDF/PPT/PPTX style references without forcing an extra style-selection step. (#39)
- Require PDF/PPT/PPTX style references to be inspected as rendered page images before deriving a visual style. (#39)

## 0.3.2

### Documentation

- Add an update and installation reference to the codex-ppt skill instructions. (#36)
- Add a README callout linking to the pinned community showcase issue. (#35)
- Add the generated skill duo introduction PDF to the README tips.

## 0.3.1

### Fixes

- Fix full-deck generation so the parent actively dispatches slide subagents, and subagents must use the selected image generation tool instead of local rendering fallbacks. (#31)

### Documentation

- Clarify that PPT style references can be screenshots or full PPT/PDF files, and that reusable styles can be saved into this skill's `references/` directory. (#24)
- Add a README note about personalizing the codex-ppt workflow and include the good skill design deck. (#22)
- Add a README tip pointing users to image-to-editable-ppt-skill when they need editable PPT reconstruction. (#29)

### Improvements

- Display GitHub Release skill zip assets with their versioned filenames. (#21)
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
