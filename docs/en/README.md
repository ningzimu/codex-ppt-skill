# Codex PPT Skill Documentation

Codex PPT is a presentation-generation skill built for Codex. It also works with agents that support `SKILL.md`, including Claude Code, OpenClaw, and Hermes Agent. It turns articles, reports, papers, course notes, or rough ideas into image-based presentations: first planning the outline and visual style, then generating each complete slide as an image, and finally assembling the images into a `.pptx` file.

## How to Read This Documentation

If you just want to get started quickly, begin with the [Quick Start](/en/quickstart.md).

If you need to install the skill, configure models, or connect it to different agents, see [Installation and Configuration](/en/installation.md).

If you want to understand the complete generation process, confirmation checkpoints, and quality control, see the [Standard Workflow](/en/workflow.md).

If you are already using the skill and have encountered a problem, see the [FAQ](/en/faq.md).

## Pages

- [Quick Start](/en/quickstart.md): The shortest path for first-time users, example commands, and output files.
- [Design Philosophy](/en/design.md): Why the skill uses image-based presentations, staged confirmation, and a two-skill design.
- [Installation and Configuration](/en/installation.md): Installation and update methods for Codex, OpenClaw, Claude Code, and Hermes Agent, plus API/CLI fallback configuration.
- [Standard Workflow](/en/workflow.md): The complete process, from confirming the outline, style, backend, and sample slide to generating and assembling the full deck.
- [Styles and Personal Style Library](/en/styles.md): Previews of the 12 built-in styles, reproducing a style from reference materials, and saving styles you like to your personal style library for long-term reuse.
- [FAQ](/en/faq.md): Common questions about editability, API keys, sample slides, inserting source materials, and revising individual slides.
- [Example Prompts](/en/prompts.md): Reusable prompts for turning articles into presentations, thesis defenses, executive reports, specified styles, and single-slide revisions.

## Key Features

- Image-based presentation generation: Each slide is a complete 16:9 slide image, ideal for scenarios that require strong visual expression and a consistent style.
- Staged confirmation workflow: Confirm the outline, visual style, image-generation method, and sample slide before generating the full deck to reduce rework.
- 12 built-in styles: Options include clean professional, scientific defense, hand-drawn technical explanation, McKinsey-style, party and government red, and teaching courseware. See [Styles and Personal Style Library](/en/styles.md).
- Style matching from reference materials: The skill can review a user-provided presentation, PDF, or screenshots, understand the visual style of each page, and generate a similar style.
- Personal style library: Styles you like can be saved to `~/.codex-ppt-skill/references/`, outside the skill installation directory. They remain available after skill updates and can be reused by name in future projects.
- Place specified source materials on designated slides: You can assign original paper figures, experiment results, architecture diagrams, or screenshots to specific slides.
- Multiple agent environments: In addition to Codex, the skill works with agents that support `SKILL.md`, including Claude Code, OpenClaw, and Hermes Agent.
- Automatic PowerPoint assembly: The skill generates `outline.md`, individual slide images, and `speech.md`, then assembles everything into a `.pptx` file.
- Third-party API support for text models and the `gpt-image-2` image-generation model.
- Companion speaker notes: Speaker notes are generated and inserted into the PowerPoint notes pages by default.
- Targeted post-generation edits for specific slides that need improvement. See the [FAQ](/en/faq.md).

## Use Cases

- Turning technical articles into presentation decks
- Turning papers, research reports, or survey materials into presentations
- Turning course notes into teaching slides
- Product introductions, business reports, and project summaries
- Thesis defenses, project applications, midterm reviews, and final acceptance presentations
- Image-based presentations that require a consistent visual language

## Important Notes

Codex PPT generates image-based presentations. They offer strong visual consistency, but the text, charts, and shapes on a slide cannot be edited individually as they can in a traditional PowerPoint file.

If you need to convert the result into an editable presentation, you can use [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) after generation.

You cannot use this skill without access to the `gpt-image-2` image-generation model. See [Installation and Configuration](/en/installation.md).

## Related Links

- GitHub repository: https://github.com/ningzimu/codex-ppt-skill
- ClawHub page: https://clawhub.ai/ningzimu/codex-ppt
- Use case showcase: https://github.com/ningzimu/codex-ppt-skill/issues/34
- Editable presentation conversion skill: https://github.com/ningzimu/image-to-editable-ppt-skill
