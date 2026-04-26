---
name: codex-ppt
description: Generate image-based PowerPoint decks from articles, reports, papers, notes, or outlines. Use this skill when the user asks Codex to create a visually unified PPT/PPTX deck where each slide is a full-slide generated image, then assemble those images into a PowerPoint file.
---

# Codex PPT

## Overview

This skill creates image-based PPT decks. Each slide is a complete 16:9 image generated with Codex's built-in `gpt-image-2` capability. The image contains the slide title, key points, and visual composition. The generated images are then assembled into a `.pptx` file with `scripts/assemble_ppt.py`.

Use Codex's built-in `gpt-image-2` image generation and image editing capabilities for every slide image.

## Use When

Use this skill when the user asks to:

- Turn an article, report, paper, document, course note, or rough outline into a PPT.
- Create a visually consistent presentation deck.
- Generate slides as full-page images.
- Produce supporting `outline.md` and `speech.md` files.
- Assemble generated slide images into a `.pptx`.

Do not use this skill for ordinary editable PowerPoint layouts where each textbox, chart, or shape must remain separately editable. This workflow prioritizes visual quality and consistency over editability.

## Workflow

### 1. Understand Source Content

Read the user-provided content fully enough to identify:

- Main topic and intended audience
- Presentation goal
- Required or implied page count
- Required style or brand constraints
- Any sections that must be included or excluded

If the user did not specify a page count, choose a practical count based on content length. Typical decks are 8-12 slides.

### 2. Plan The Deck Outline

Create a concise outline before generating images. For each slide, define:

- Slide number
- Slide title
- 3-5 key points
- Optional visual idea
- Layout role and intent, such as cover, agenda, section divider, concept explanation, process, comparison, timeline, data evidence, architecture, case study, summary, or Q&A

Show the outline to the user for confirmation before generating slide images, unless the user explicitly asked you to skip confirmation.

Recommended structure:

```text
Slide 1: Cover
Slide 2: Context / problem
Slide 3-7: Main argument or sections
Slide 8: Summary / recommendation / closing
```

### 3. Confirm A Unified Visual Style

Before generating slide images, discuss the visual style with the user. Prefer a multiple-choice question: offer 2-3 concrete style directions and mark one as your recommendation.

Each style option should briefly specify:

- Color palette
- Layout system
- Typography direction
- Illustration or image treatment
- Decorative elements
- Density and whitespace rules

After the user chooses a style, create one final style direction and keep the visual identity consistent across all slide prompts. Keep color palette, typography, texture, icon/illustration language, and overall mood stable. Do not reuse the same layout on every page.

The `references/` directory contains optional style references. Use them as inspiration, not as rigid templates. Adapt the style to the topic and audience.

Important: a deck should have one coherent visual identity, not one repeated composition. Treat each reference as a style system: stable palette, typography, icon language, texture, and visual mood; variable page layout chosen from the slide's content role. `layout_blueprints` are candidate starting points only. Do not apply the same blueprint to every slide.

Available references:

- `references/清爽专业风.md`
- `references/创意杂志风.md`
- `references/电子墨水杂志风.md`
- `references/数据仪表盘风.md`
- `references/复古扁平插画风.md`
- `references/手绘技术解释风.md`
- `references/手绘白板风.md`
- `references/温暖手工风.md`

Example style confirmation:

```text
我建议用 A，因为它最适合这份内容的受众和表达目标。

A. 清爽专业风（推荐）：浅色背景、蓝绿强调色、结构清晰，适合汇报、答辩和技术分享。
B. 创意杂志风：大标题、强图片、留白更大胆，适合分享和传播。
C. 数据仪表盘风：指标卡、图表感布局，适合数据密集型报告。

你选哪个？也可以指定要调整的配色、布局或插画方向。
```

### 4. Generate One Sample Slide For Approval

After the outline and style are confirmed, generate exactly one sample slide image with `gpt-image-2` before full production.

Sample slide requirements:

- Use the confirmed style description.
- Prefer a representative content slide over the cover when possible.
- Demonstrate the intended deck rhythm: the sample should show how the chosen style adapts to a real content page, not just a generic fixed template.
- Save it directly as the intended final slide filename, such as `{base_dir}/{deck_name}/origin_image/slide_08.png`.
- Show the sample image to the user.
- Ask the user to confirm the visual style, typography, layout density, and Chinese text quality.

Do not generate the full deck until the user approves the sample slide. If the user requests changes, revise the style description and regenerate that same `slide_XX.png` file first. Once approved, keep that file as the final slide for its page. Do not create `sample_slide.png` in `origin_image/`, because the assembly step is designed around final `slide_XX` filenames.

### 5. Create The Project Directory

Use this output structure:

```text
{base_dir}/{deck_name}/
├── origin_image/
│   ├── slide_01.png
│   ├── slide_02.png
│   └── ...
├── outline.md
├── speech.md
└── {deck_name}.pptx
```

If the user did not specify a destination, use the current working directory or the directory that contains the source file.

You may initialize the directory structure with:

```bash
~/.codex/skills/codex-ppt/.venv/bin/python ~/.codex/skills/codex-ppt/scripts/assemble_ppt.py {base_dir} {deck_name}.pptx --init
```

### 6. Generate All Slide Images

Generate one image per slide with Codex's built-in `gpt-image-2` image generation capability. Every final `slide_XX.png` must be produced by `gpt-image-2`; programmatic rendering or hybrid text overlay is not acceptable for slide image creation.

Use a structured visual brief for each slide. GPT-Image-2 works best when the prompt separates canvas, style, layout, text, visual elements, and constraints instead of relying only on a long style paragraph.

Keep the deck visually coherent but vary slide layouts according to page semantics. Treat style references and `layout_blueprints` as candidate patterns, not fixed templates. Across a normal deck, deliberately mix suitable page types such as:

- cover / section divider
- context or problem framing
- process or timeline
- comparison or tradeoff
- data / evidence / KPI
- architecture or workflow diagram
- summary / conclusion / next steps

Avoid generating every slide as the same three-card layout. For each slide, choose a layout that fits its content and explain that choice in the `layout.intent` field.

```json
{
  "type": "16:9 full-slide PowerPoint image",
  "language": "Chinese",
  "canvas": {
    "aspect_ratio": "16:9",
    "use_full_canvas": true,
    "slide_number": "do not render a slide number"
  },
  "style": {
    "name": "{confirmed style name}",
    "visual_direction": "{same final style description for every slide}",
    "color_palette": "{main colors and accent colors}",
    "typography": "{font personality, hierarchy, weight, text alignment}",
    "texture_and_finish": "{flat, paper, dashboard, editorial, whiteboard, etc.}",
    "deck_consistency": "same palette, typography, icon language, texture, and mood across all slides"
  },
  "layout": {
    "role": "{cover, agenda, section divider, concept, process, comparison, timeline, data evidence, architecture, case study, summary, Q&A, etc.}",
    "intent": "{why this page uses this layout: cover, comparison, timeline, data evidence, workflow, summary, etc.}",
    "composition": "{specific layout for this slide}",
    "content_zones": "{title zone, body zone, visual zone, footer or callout zones}",
    "variation_rule": "same style identity as the deck, but vary composition by slide role; do not repeat the same blueprint on adjacent slides unless the content is part of a deliberate repeated sequence",
    "relationship_to_previous_slide": "{new layout, continuation layout, mirrored layout, or deliberate repeated sequence}",
    "spacing": "clear hierarchy, coherent alignment, no overlapping elements"
  },
  "text": {
    "title": "{slide title}",
    "key_points": ["{point 1}", "{point 2}", "{point 3}"],
    "text_quality": "render all Chinese text exactly, clearly, and without garbled characters"
  },
  "visual_elements": {
    "main_visual": "{icons, diagram, chart, illustration, dashboard cards, collage, or other content-specific visual idea}",
    "supporting_elements": "{arrows, cards, callouts, decorative elements, labels}"
  },
  "constraints": [
    "The final image itself must contain the title and key points.",
    "All text must be readable and correctly spelled.",
    "Keep the confirmed style consistent with the rest of the deck.",
    "No watermark, no unrelated logo, no extra slide number."
  ]
}
```

Save images as:

```text
{base_dir}/{deck_name}/origin_image/slide_01.png
{base_dir}/{deck_name}/origin_image/slide_02.png
...
```

After each image is generated, copy or move it into `{base_dir}/{deck_name}/origin_image/` immediately. Do not leave final slide images only in Codex's default generated-images directory.

Final slide image naming rules:

- Rename final slide images strictly by slide order: `slide_01.png`, `slide_02.png`, `slide_03.png`, ...
- Use zero-padded two-digit numbers for normal decks.
- The approved sample slide should already have the correct `slide_XX.png` filename and should be reused directly.
- Keep rejected variants, drafts, or reference images out of `origin_image/`. If you need to preserve them, place them in the project root or a separate `drafts/` directory.
- Before assembling, verify every expected `slide_XX.png` exists in `origin_image/` and that there are no missing or extra final slide images.

For Chinese decks, explicitly ask `gpt-image-2` to render Chinese text accurately and avoid garbled characters.

### 7. Quality Check And Repair

Before assembling the PPT, inspect every slide image. Check:

- Text is readable and not garbled.
- Slide content matches the outline.
- Title and key points are not truncated.
- Visual style is consistent across slides.
- No page number appears unless the user requested one.
- Important elements do not overlap.

If a slide has severe text or layout issues, regenerate it with a more constrained prompt. If a slide is mostly correct but has a localized issue, use Codex's built-in `gpt-image-2` image editing capability when available.

### 8. Write Supporting Files

Create `outline.md` with the final deck outline:

```markdown
# {Deck Title}

## Outline

### Slide 1: {Title}
- {Point}
- {Point}

### Slide 2: {Title}
- {Point}
- {Point}
```

Create `speech.md` with speaker notes. Keep it useful and concise: 1-3 short paragraphs per slide is usually enough.

Use headings that the assembly script can map back to slide numbers:

```markdown
## Slide 1: {Title}

{Speaker notes for slide 1}

## Slide 2: {Title}

{Speaker notes for slide 2}
```

### 9. Assemble The PPT

Run:

```bash
~/.codex/skills/codex-ppt/.venv/bin/python ~/.codex/skills/codex-ppt/scripts/assemble_ppt.py {base_dir} {deck_name}.pptx --aspect-ratio 16:9
```

Important:

- `{base_dir}` is the parent directory of `{deck_name}/`.
- `{deck_name}.pptx` must match the project folder name.
- The script reads images from `{base_dir}/{deck_name}/origin_image/`.
- The script only reads final images named like `slide_01.png`, `slide_02.png`, etc.; drafts and sample files are ignored.
- If `{base_dir}/{deck_name}/speech.md` exists and uses `Slide N` headings, the script writes those notes into the corresponding PPT speaker notes.
- The script writes `{base_dir}/{deck_name}/{deck_name}.pptx`.

### 10. Final Report

Report:

- Project directory
- PPT file path
- Slide image directory
- `outline.md` path
- `speech.md` path
- Number of slides
- Confirm that slide images were generated with `gpt-image-2`
- Confirm that speaker notes from `speech.md` were written into the PPT, if applicable
- Any slides that were regenerated or still have known limitations

## Assembly Script Dependency

`scripts/assemble_ppt.py` requires:

```bash
python3 -m venv ~/.codex/skills/codex-ppt/.venv
~/.codex/skills/codex-ppt/.venv/bin/python -m pip install -r ~/.codex/skills/codex-ppt/requirements.txt
```

The script supports `16:9` and `4:3`. Use `16:9` unless the user requests otherwise.

## Prompting Principles

- Keep one global visual style fixed across the deck.
- Vary slide composition by page role; style consistency does not mean repeating the same layout.
- Use `layout_blueprints` as candidate patterns, not mandatory templates.
- Generate one slide per image request.
- Prefer concrete visual direction over generic words like "beautiful" or "professional".
- For dense content, split across more slides instead of crowding one slide.
- Prioritize clarity over decoration.
