# Slide Generation And Subagents

Read this before full-deck image generation, preparing slide jobs, dispatching subagents, recording results, or handling blockers.

## Final Slide Image Generation

Generate one image per slide with the selected image backend. Every final `slide_XX.png` must be produced by the built-in image tool or by `scripts/image_gen.py`; programmatic rendering or hybrid text overlay is not acceptable for slide image creation.

After the outline, visual style, image backend, and sample slide have all been approved, create final downstream artifacts if they do not already exist:

- `deck_spec.json`
- `prompts/slide_XX.json`
- `speech.md`

Do not create these final downstream artifacts before outline approval. If the user explicitly asks for pre-approval planning files, use `.draft.` filenames and synchronize them after approval.

`deck_spec.json` must include `sample_generation_method` copied from the approved sample before `prepare_slide_prompts.py` is run. The helper copies that method into each `prompts/slide_XX.json` and into `slide_jobs.json`, so workers can see the exact backend, tool, mode, image context preparation, and output constraints used for the approved sample.

Before full production, create structured per-slide image jobs. Prefer the bundled deterministic helper:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/prepare_slide_prompts.py \
  --spec {base_dir}/{deck_name}/deck_spec.json \
  --out-dir {base_dir}/{deck_name} \
  --selected-backend "<confirmed backend label>" \
  --force
```

The helper writes:

```text
{base_dir}/{deck_name}/
├── prompts/
│   ├── slide_01.json
│   ├── slide_02.json
│   └── ...
├── slide_jobs.json
└── slide_run_state.json
```

Each `prompts/slide_XX.json` is a self-contained slide job. It includes the slide number, title, output filename, input image list, whether context images are required, and the full prompt text. Use these JSON job files for built-in image generation, CLI/API fallback coordination, and subagent handoff. Do not create a separate job manifest unless the user explicitly asks for one.

The parent agent is responsible for packaging context before dispatch. A slide subagent only sees its assigned single-slide job, the images explicitly passed to it, and the handoff text. Do not assume the subagent knows the source article, full outline, previous slides, later slides, or any concept held only in the parent agent's conversation context.

For any slide that depends on cross-slide or source-wide meaning, write the necessary background directly into `deck_spec.json` before preparing prompts:

- Use deck-level `deck_context` for canonical concepts that multiple slides may need, such as the source summary, core claim, term list, taxonomy, characters, definitions, chronology, or required naming.
- Use slide-level `local_context` for page-specific facts that must be visible to that one worker, such as "summarize these six traits", "compare these two methods", "continue this three-step framework", or "use this exact quote".
- Expand references like "the six traits", "the above framework", "the previous conclusion", or "these examples" into explicit lists or definitions inside `deck_context` or `local_context`. Avoid leaving them as implicit pointers.

The goal is not to make subagents validate missing context. The goal is for the parent agent to hand each worker a complete enough task packet so the worker can simply execute the assigned page.

`slide_jobs.json` is the dispatch state file. It records each slide's prompt job, final output path, status, selected backend, sample generation method, subagent dispatch metadata, result provenance, and blocker state. Do not hand-edit slide statuses; use the bundled status scripts.

`deck_spec.json` may express `required_images` either as structured objects or as Markdown image reference strings. The helper extracts the image path from strings such as `strict input asset\n\n![Result 01](assets/figures/result_01.png)` and carries the surrounding text / alt text into the image role.

Use a structured visual brief for each slide. Image generation works best when the prompt separates canvas, style, layout, text, visual elements, and constraints instead of relying only on a long style paragraph.

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
  "deck_context": {
    "source_summary": "{brief source-wide summary}",
    "core_claim": "{the deck's central thesis}",
    "canonical_terms": ["{term 1}", "{term 2}", "{term 3}"]
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
  "local_context": {
    "required_background": "{facts, lists, definitions, comparisons, or prior-slide references this slide needs to be self-contained}"
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

If preparing prompts manually instead of using `prepare_slide_prompts.py`, still save each full slide job under `{base_dir}/{deck_name}/prompts/slide_XX.json` before generation. The saved job must include `prompt`, `out`, and `input_images`, including any deck-level approved sample slide style reference and all slide-level source images with explicit role labels.

## Parallel Slide Generation With Subagents

After the user approves the sample slide and full-deck generation is authorized, slide subagents are mandatory whenever the current runtime can spawn them. Use one subagent per remaining slide image job. Do not generate the remaining deck sequentially merely for convenience. If subagents cannot be spawned, stop at the dispatch step and report a blocker instead of producing a lower-quality sequential deck.

Use the slide state scripts as the dispatch contract: the main agent spawns workers, then records dispatch and result state. A slide is not considered dispatched or complete until the relevant script records it.

Parent agent responsibilities:

- Own `outline.md`, `deck_spec.json`, `prompts/`, `origin_image/`, QA, `speech.md`, and final PPT assembly.
- Run `prepare_slide_prompts.py` or otherwise write full per-slide JSON jobs and `slide_jobs.json` before delegation.
- Run `slide_job_status.py` to see dispatch slots and pending slide ids before each batch.
- Ensure the approved sample slide is included in every non-sample job as a style-only input image when available.
- Ensure every dispatched slide job is self-contained. If a slide summarizes, compares, continues, or refers to deck-wide concepts, put the required concepts into `deck_context` or the slide's `local_context` before running `prepare_slide_prompts.py`.
- Ensure `sample_generation_method` is present in `deck_spec.json`, every `prompts/slide_XX.json`, and `slide_jobs.json`; it must describe the exact backend/tool/mode used to generate the approved sample.
- If the approved sample slide already exists and should not be regenerated, mark that slide in `deck_spec.json` with `sample_approved: true` or `approved_sample: true` before running `prepare_slide_prompts.py`; the helper records it as `accepted` when the final image file exists.
- In built-in `image_gen` mode, ensure every slide-level required local source image has already been inspected with `view_image` before any delegated job that depends on it.
- In CLI/API fallback mode, ensure each JSON job lists the required source images and that the selected CLI path can use them; if the CLI path cannot attach input images for a slide, do not delegate that slide as a text-only replacement for the asset.
- Spawn subagents with exactly one slide job each, up to `dispatch_slots_available`.
- Immediately after each successful spawn, run `record_slide_dispatch.py` with the real agent id and prompt path.
- After each worker returns, visually check its selected output, then run `record_slide_result.py` to copy the selected generated image into `origin_image/slide_XX.png` and record backend provenance.
- If a worker cannot use the selected image backend or cannot access required input images, run `record_slide_blocker.py` and report the blocker.

Subagent responsibilities:

- Read exactly the assigned `prompts/slide_XX.json`.
- Use the selected image backend only; do not switch between built-in image generation and CLI/API fallback.
- Follow the `sample_generation_method` from the assigned job. Use the same tool family, generation/edit mode, image context preparation, and model/config details that produced the approved sample.
- Generate the final slide candidate by calling the selected image generation backend. Do not create final slide images with local drawing, HTML/SVG/canvas screenshots, Pillow, python-pptx/PptxGenJS layouts, or manually composited text/image overlays.
- Treat the approved sample slide as style reference only.
- Treat any required source images as strict input assets and preserve their content according to the prompt.
- Inspect the generated candidate for text quality, style consistency, required-image inclusion, and layout issues before returning it.
- Return only the selected original generated image path, the backend used, and a one-sentence QA note.

Subagents must not edit `outline.md`, `deck_spec.json`, other slide job files, `origin_image/`, `speech.md`, or the final `.pptx`. The parent agent alone records selected outputs and performs final assembly.

Do not continue sequentially after the sample if subagents are part of the confirmed full-generation workflow and cannot be used. Stop and report the blocker, unless the user explicitly changes the requirement.

Dispatch loop:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/slide_job_status.py \
  {base_dir}/{deck_name}

~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/record_slide_dispatch.py \
  {base_dir}/{deck_name} \
  --slide slide_02 \
  --agent-id <agent id> \
  --agent-nickname "<nickname if available>" \
  --prompt-file prompts/slide_02.json
```

Result recording:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/record_slide_result.py \
  {base_dir}/{deck_name} \
  --slide slide_02 \
  --agent-id <agent id> \
  --backend-used "built-in image tool" \
  --selected-source /absolute/path/to/generated/slide_02.png \
  --qa-note "Text readable; style matches the approved sample."
```

Blocker recording:

```bash
~/.codex-ppt-skill/.venv/bin/python {skill_root}/scripts/record_slide_blocker.py \
  {base_dir}/{deck_name} \
  --slide slide_02 \
  --agent-id <agent id> \
  --reason "selected image backend unavailable in worker"
```

Subagent handoff template lives in `../prompts/slide-worker.md`. Use that template instead of writing a new ad hoc worker prompt.

Save images as:

```text
{base_dir}/{deck_name}/origin_image/slide_01.png
{base_dir}/{deck_name}/origin_image/slide_02.png
...
```

After each image is generated, the parent agent should record it with `record_slide_result.py`, which copies it into `{base_dir}/{deck_name}/origin_image/` and rejects backend provenance that does not match the selected backend or sample generation method. Do not leave final slide images only in a temporary or default generated-images directory, and do not manually mark slide state complete.

In CLI/API fallback mode, read `cli-api-fallback.md` for text-only generation commands, image-input limitations, edit commands, transparency rules, and runtime troubleshooting.

Final slide image naming rules:

- Rename final slide images strictly by slide order: `slide_01.png`, `slide_02.png`, `slide_03.png`, ...
- Use zero-padded two-digit numbers for normal decks.
- The approved sample slide should already have the correct `slide_XX.png` filename and should be reused directly.
- Keep rejected variants, drafts, or reference images out of `origin_image/`. If you need to preserve them, place them in the project root or a separate `drafts/` directory.
- Before assembling, verify every expected `slide_XX.png` exists in `origin_image/`, there are no missing or extra final slide images, and `slide_job_status.py` shows all non-sample slide jobs as `recorded`.

For Chinese decks, explicitly ask the image backend to render Chinese text accurately and avoid garbled characters.
