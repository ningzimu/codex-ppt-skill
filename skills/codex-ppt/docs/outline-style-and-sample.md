# Outline, Style, And Sample

Read this before writing or updating `outline.md`, offering visual styles, using files from `references/`, or generating/approving the sample slide.

If the user asks to save a finished deck style or a user-supplied image/PDF/PPT/PPTX style for future reuse, read `style-library.md`.

## Plan The Deck Outline

Create a concise `outline.md` draft before generating images. For each slide, define:

- Slide number
- Slide title
- 3-5 key points
- Optional visual idea
- Layout role and intent, such as cover, agenda, section divider, concept explanation, process, comparison, timeline, data evidence, architecture, case study, summary, or Q&A
- Required source images, if any, including the image path or attachment name, its role on the slide, and whether it is a strict input asset or only a style/layout reference

Save the draft to `{base_dir}/{deck_name}/outline.md` once the project directory is known. If the output directory is not known yet, show the outline in chat first and write it to `outline.md` immediately after creating the project directory.

Show the outline to the user for confirmation and wait for approval before moving to visual style selection or image generation, unless the user explicitly asked you to skip confirmation. If any slide lists required source images, explicitly ask the user to verify that each image is assigned to the correct slide and role before generation. If the user requests changes, update `outline.md` and ask for confirmation again.

Stop after writing the outline draft. At this point, report the `outline.md` path, slide count, required source images and their slide mapping, and that no slide images or PPTX have been generated yet. Do not proceed to `deck_spec.json`, `speech.md`, prompt preparation, style selection, backend selection, or sample generation until the user approves the outline.

If the user approved a sample slide, record that approved `slide_XX.png` path as the deck-level style reference. Later slide prompts and subagent handoffs should include it as a style-only reference so each page keeps the same palette, typography mood, density, texture, and visual identity without copying the sample's exact layout.

Recommended structure:

```text
Slide 1: Cover
Slide 2: Context / problem
Slide 3-7: Main argument or sections
Slide 8: Summary / recommendation / closing
```

For slides that use source images, add lines like:

```markdown
Slide 5: Experiment Results
- Key points: ...
- Required images:
  - Main evidence figure; strict input asset; preserve data, axes, labels, legends, colors, and values

    ![Result 01](assets/figures/result_01.png)

  - Supporting model architecture; strict input asset; preserve labels and arrows

    ![Model Architecture](assets/figures/model_architecture.png)
```

Use Markdown image syntax inside the `Required images` list whenever the asset is local and renderable in the outline. This lets the user visually verify the exact asset mapping during outline review. Keep the descriptive text next to each image so `prepare_slide_prompts.py` can convert the same asset into structured prompt input later.

## Confirm A Unified Visual Style

Before generating slide images, discuss the visual style with the user unless the user has already provided a clear style direction or reference material.

If the user has already specified a style, provided a style image, or provided a PDF/PPT/PPTX to use as style reference, do not force a 2-3 option style selection. Extract the usable style rules, briefly restate them, then proceed to backend confirmation and sample generation.

For PDF/PPT/PPTX style references, do not infer the visual system from document structure, outline text, XML, file metadata, or slide object hierarchy alone. First render or export representative pages/slides into real page images, inspect those rendered images, and derive the style from what is actually visible on the pages. If the file has multiple visual sections, inspect enough representative pages to capture the shared style and any section-specific variations.

When extracting style from reference material, separate content reuse from style reuse. Unless the user explicitly asks to reuse the source content, treat the provided image/PDF/PPT/PPTX as a style reference only.

If the user has not provided a clear style, prefer a multiple-choice question: offer 2-3 concrete style directions and mark one as your recommendation. Each style option should briefly specify:

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
- `references/科研答辩风.md`
- `references/复古扁平插画风.md`
- `references/手绘技术解释风.md`
- `references/手绘白板风.md`
- `references/温暖手工风.md`
- `references/麦肯锡风格.md`

When adding a reusable style to the library, also add its `references/{style_name}.md` file to this list.

Example style confirmation:

```text
我建议用 A，因为它最适合这份内容的受众和表达目标。

A. 清爽专业风（推荐）：浅色背景、蓝绿强调色、结构清晰，适合汇报、答辩和技术分享。
B. 创意杂志风：大标题、强图片、留白更大胆，适合分享和传播。
C. 数据仪表盘风：指标卡、图表感布局，适合数据密集型报告。

你选哪个？也可以指定要调整的配色、布局或插画方向，或者上传一张喜欢的 PPT 风格图片让我参考。
```

## Generate One Sample Slide For Approval

After the outline, style, and image backend are confirmed, generate exactly one sample slide image before full production.

Sample slide requirements:

- Use the confirmed style description.
- Prefer a representative content slide over the cover when possible.
- Demonstrate the intended deck rhythm: the sample should show how the chosen style adapts to a real content page, not just a generic fixed template.
- Save it directly as the intended final slide filename, such as `{base_dir}/{deck_name}/origin_image/slide_08.png`. In CLI/API fallback mode, use `scripts/image_gen.py generate --out` for that exact path.
- Show the sample image to the user.
- Ask the user to confirm the visual style, typography, layout density, and Chinese text quality.

Do not generate the full deck until the user approves the sample slide. If the user requests changes, revise the style description and regenerate that same `slide_XX.png` file first. Once approved, keep that file as the final slide for its page. Do not create `sample_slide.png` in `origin_image/`, because the assembly step is designed around final `slide_XX` filenames.

After the sample slide is approved, record the sample generation method in `deck_spec.json` before preparing full-deck jobs. This is the contract the parent passes to subagents so they use the same image-generation path as the sample, not a cheaper local rendering path. Include at least:

- `backend_used`: the confirmed backend label, such as `built-in image tool` or `scripts/image_gen.py`.
- `tool_name`: the actual tool or command used, such as `image_gen`, `image_generate`, or `scripts/image_gen.py`.
- `mode`: `generate` or `edit`.
- `prompt_source`: where the approved sample prompt came from.
- `size`, `quality`, and model/config details when the backend exposes them.
- `approved_sample_path`: the approved `origin_image/slide_XX.png` path.
- `input_context_preparation`: how local source/style images were made available, such as `view_image` for built-in mode.
- `handoff_rule`: subagents must use the same backend/tool/mode and return a blocker if that path is unavailable.
