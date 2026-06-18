# Slide Worker Prompt

Use this template when dispatching a slide subagent after the sample slide is approved and the workflow reaches full-deck generation.

```text
Generate slide <N> for this codex-ppt deck.

Deck dir: <absolute deck dir>
Slide job file: <absolute deck dir>/prompts/slide_<NN>.json
Output target owned by parent: <absolute deck dir>/origin_image/slide_<NN>.png
Selected image backend: <scripts/image_gen.py --backend auto (codex-oauth) OR scripts/image_gen.py --backend atlascloud/openai-compatible>
Sample generation method copied from the approved sample:
- backend_used: <exact backend label recorded by parent>
- tool_name: <scripts/image_gen.py>
- mode: <generate OR edit>
- model/config: <model, size, quality, backend>
- prompt_source: <approved sample prompt source>
- input_context_preparation: <how local images were made visible or attached>
- approved_sample_path: <absolute path to approved origin_image/slide_XX.png>
- handoff_rule: use this same backend/tool/config; use generate for new slides unless this job has strict input_images or is a repair
Style reference images to inspect before generation:
- <absolute path> - approved sample slide style reference; match style only, do not copy layout
Strict input images already prepared by the parent:
- <absolute path> - strict input asset; preserve labels/data/arrows/content

Read the JSON job file, then follow its `prompt` field exactly. Use the selected image backend and the recorded sample generation method only.
You must produce the final slide candidate by calling the selected image generation backend:
- Before calling the backend, visually inspect every local image listed in `style_reference_images` and `input_images`.
- Local CLI mode for normal new slides: use `scripts/image_gen.py generate --prompt-file <job prompt file> --out <deck dir>/drafts/slide_<NN>_candidate.png`; the CLI reads the JSON job file's `prompt` field exactly.
- Local CLI mode for slides with strict `input_images`: use `scripts/image_gen.py edit --image <asset> ... --prompt-file <job prompt file> --out <deck dir>/drafts/slide_<NN>_candidate.png`; the CLI reads the JSON job file's `prompt` field exactly.
- Local CLI mode for repairing an existing generated slide: use `scripts/image_gen.py edit --image <existing slide> --prompt ... --out <deck dir>/drafts/slide_<NN>_revised.png`.
- Do not pass approved sample/style reference images as `--image` inputs unless the JSON job also lists them under `input_images`.
- UI built-in mode is allowed only if the parent explicitly selected it and described how to save the result to the target path.

Forbidden for final slide image creation:
- local drawing or rendering scripts
- Pillow-generated slides
- SVG, HTML/CSS, or canvas screenshots
- python-pptx/PptxGenJS/native PPT layout screenshots
- manually composited text, card, chart, or image overlays

If you cannot use the selected image backend, stop and return `blocker=<reason>` instead of creating a lower-quality replacement.
If you cannot follow the recorded sample generation method, stop and return `blocker=<reason>` instead of switching tools.
Do not edit slide job files, origin_image, speech.md, or assemble the PPT.

Before returning, visually check:
- Chinese text is readable and not garbled
- style matches the approved sample slide
- required source images are visibly included and not replaced by a similar redraw
- no overlapping or truncated important content

Return only:
backend_used=<exact selected backend label>
selected_source=<absolute deck dir>/drafts/slide_<NN>_candidate.png
qa_note=<one sentence>
```
