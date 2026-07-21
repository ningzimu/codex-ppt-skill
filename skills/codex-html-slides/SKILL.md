---
name: codex-html-slides
description: Create polished, self-contained HTML presentations from articles, reports, papers, notes, outlines, PDFs, Word documents, or reference decks. Use when Codex needs to build, restyle, or revise a browser-playable 16:9 slide deck whose pages remain editable as HTML/CSS/inline SVG, especially when the user wants image-quality visual styling without generating full-slide PNG, JPEG, WebP, PPTX, or PDF outputs.
---

# Codex HTML Slides

## Output contract

Create one browser-playable `.html` file by default. Build every slide from editable DOM, CSS, and inline SVG on a fixed 1600×900 canvas that scales to the viewport.

Do not:

- call an image-generation backend;
- generate or save full-slide PNG, JPEG, WebP, GIF, PDF, or PPTX files;
- use a screenshot, canvas export, or rasterized reference page as a slide background;
- hide a bitmap of a completed slide inside HTML;
- add CDN, web-font, framework, or network dependencies unless the user explicitly accepts a non-self-contained deck.

User-supplied figures, photos, logos, and screenshots may appear as content assets when required. Preserve them faithfully, fit the layout around them, and embed them as data URIs when the final file must remain self-contained. Never treat one supplied image as the entire slide.

## Required references

- Read `references/visual-system.md` before deriving a style or authoring the sample slide.
- Read `references/style-recipes.md` when using a built-in direction or translating an image-style deck into CSS/SVG.
- Read `references/qa.md` before final validation and delivery.

## Workflow

1. Understand the source.
   - Identify topic, audience, purpose, language, desired slide count, presentation setting, and mandatory content.
   - Inspect supplied files and distinguish style references from content assets.

2. Confirm the outline.
   - Draft slide titles, roles, core message, evidence, and intended visual mechanism.
   - Vary roles across cover, section divider, thesis, comparison, process, framework, data, evidence, and closing slides.
   - Ask the user to approve the outline before producing a non-trivial deck.

3. Confirm the visual system.
   - If the user supplies a reference image, PDF, PPT, or PPTX, analyze its geometry, palette, typography, shape language, depth, texture, image treatment, and information density. Recreate the system; never reuse a full rendered page as a background.
   - Otherwise offer two or three concrete directions from `references/style-recipes.md`, recommend one, and confirm it.
   - Define CSS tokens for palette, type scale, spacing, radii, borders, shadows, and motion before styling individual slides.

4. Initialize the deck.
   - Run:

     ```bash
     python3 scripts/create_deck.py /absolute/path/deck.html \
       --title "Deck title" --lang zh-CN --theme clean-professional
     ```

   - Keep the template runtime and replace the sample content rather than rebuilding navigation from scratch.

5. Build and approve one sample slide.
   - Implement exactly one representative slide using final DOM/CSS/SVG techniques.
   - Preview it at 1600×900 and at the user's likely display size.
   - Confirm hierarchy, density, visual fidelity, and text accuracy before expanding the deck.

6. Build the complete deck.
   - Add one `<section class="slide" data-slide>` per page.
   - Keep the visual identity consistent while giving each slide a content-driven composition.
   - Use inline SVG for diagrams, illustrations, texture, masks, charts, and hand-drawn effects. Keep text as real HTML or SVG text when practical.
   - Embed speaker notes in `<aside class="speaker-notes">` when notes are requested.

7. Verify interaction and layout.
   - Preserve keyboard, touch, fullscreen, hash navigation, notes, progress, reduced-motion, and print behavior from the template.
   - Run the bundled validator, then inspect every slide in a browser as required by `references/qa.md`.

8. Deliver.
   - Report the absolute HTML path, slide count, selected visual direction, self-contained status, validation result, and any intentionally external assets.

## Slide authoring standard

Use this structure for every page:

```html
<section class="slide" id="slide-2" data-slide aria-labelledby="slide-2-title">
  <div class="slide-content layout-comparison">
    <p class="eyebrow">SECTION / 02</p>
    <h2 id="slide-2-title">A conclusion-led title</h2>
    <!-- semantic HTML and inline SVG -->
  </div>
  <aside class="speaker-notes">Optional presenter-only notes.</aside>
</section>
```

Follow these rules:

- Keep slide coordinates deterministic. Compose inside 1600×900; let the runtime scale the stage.
- Use a clear reading order and one dominant visual idea per slide.
- Keep titles concise and body copy presentation-sized. Split content instead of shrinking it.
- Prefer purposeful grids, editorial composition, diagrams, and scale contrast over repetitive rounded cards.
- Make diagrams explain relationships. Connectors, labels, arrows, legends, and emphasis must encode meaning.
- Use exact user text, names, numbers, citations, and official marks. Do not invent evidence or logos.
- Keep decorative elements `aria-hidden="true"`; label meaningful diagrams and controls.
- Use theme variables and reusable classes instead of scattered one-off colors.

## Image-quality styling without slide images

Translate image aesthetics into native layers:

- Composition: asymmetric grids, cropping, overlap, focal axes, strong negative space, and deliberate edge tension.
- Typography: extreme but controlled scale contrast, editorial line breaks, optical alignment, and a consistent title system.
- Depth: restrained shadows, translucent planes, borders, blur, and foreground/background separation.
- Texture: CSS gradients, repeating patterns, blend modes, and inline SVG filters rather than raster grain files.
- Illustration: inline SVG paths, symbols, patterns, clipping, markers, and controlled irregularity.
- Data: semantic HTML tables or SVG charts with direct labels and a visible conclusion.
- Motion: short state transitions that support hierarchy; never depend on animation to reveal essential content.

The result should feel art-directed like a high-quality rendered slide, but remain inspectable and editable as HTML.

## Revision rules

Revise the source DOM, CSS variables, layout classes, or inline SVG. Never repair a page by screenshotting it and replacing the slide with an `<img>` element. Re-run validation and browser QA after any structural or style revision.

## Validation

Run:

```bash
python3 scripts/validate_deck.py /absolute/path/deck.html \
  --expect-slides 10 --strict
```

Acceptance requires:

- a valid self-contained HTML document;
- the expected number of uniquely identified 16:9 slides;
- no full-slide raster references or `origin_image` pipeline;
- no external scripts, stylesheets, fonts, frames, or media unless explicitly approved;
- functional navigation and readable content at the required viewport sizes;
- no clipping, accidental overflow, console errors, or hidden essential content;
- consistent visual identity with varied, content-driven layouts.

