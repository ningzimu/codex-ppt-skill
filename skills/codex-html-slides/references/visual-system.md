# HTML slide visual system

## Contents

1. Coordinate system
2. Reference-style reconstruction
3. Typography
4. Composition and rhythm
5. Native visual techniques
6. Diagrams and data
7. Asset handling
8. Common failure modes

## 1. Coordinate system

Author each slide on a fixed 1600×900 canvas. The runtime scales the entire stage uniformly, so positions, type, and line weights remain stable across screens.

Use an 80–112 px outer safe area. Establish a deck grid before styling:

```css
:root {
  --canvas-w: 1600;
  --canvas-h: 900;
  --safe-x: 96px;
  --safe-y: 72px;
  --grid-gap: 24px;
}

.slide-content {
  position: absolute;
  inset: var(--safe-y) var(--safe-x);
}
```

Decorative geometry may bleed outside the safe area. Keep titles, body text, captions, axes, and required assets inside it.

## 2. Reference-style reconstruction

When a user supplies a style reference, extract a reusable system rather than copying isolated decoration.

Record these observations:

1. Geometry: dominant axes, margins, column ratios, crop behavior, overlap, and focal point.
2. Palette: background, surface, text, muted text, structural line, and one or two accents.
3. Typography: font category, title/body ratio, weight, tracking, line height, casing, and alignment.
4. Shape language: square or rounded, border weight, corner treatment, arrowheads, connectors, and icon style.
5. Depth: flat, outlined, paper-like, translucent, elevated, embossed, or layered.
6. Texture: grain, hatch, dot screen, grid, paper fiber, glow, or none.
7. Density: amount of text, module count, whitespace, and typical diagram complexity.
8. Rhythm: which elements repeat across the deck and which change by slide role.

Convert the observations to named CSS variables. Use a small token set:

```css
[data-theme="custom"] {
  --bg: #f5f2eb;
  --surface: #fffdf8;
  --ink: #20252b;
  --muted: #69717a;
  --accent: #e0523f;
  --line: #20252b;
  --radius: 6px;
  --shadow: 8px 8px 0 rgb(32 37 43 / 12%);
}
```

Match hierarchy, spacing, proportions, and visual grammar before adding small decorative details. These structural attributes contribute more to perceived fidelity than copied ornaments.

## 3. Typography

Use real text instead of outlined or raster text. Prefer system stacks for offline decks:

```css
--font-sans: Inter, ui-sans-serif, "PingFang SC", "Microsoft YaHei", sans-serif;
--font-serif: Georgia, "Songti SC", "STSong", serif;
--font-mono: "SFMono-Regular", Consolas, monospace;
```

If the user provides a licensed font file, embed it with a data-URI `@font-face`. Do not fetch Google Fonts or another CDN in a self-contained deck.

Recommended 1600×900 ranges:

- Cover title: 96–176 px.
- Content title: 48–76 px.
- Key metric: 88–160 px.
- Body: 26–36 px.
- Caption or metadata: 18–24 px.

Use deliberate line breaks and balanced line lengths. Avoid more than 8–10 lines in one text block. Split the slide when content only fits below 24 px.

## 4. Composition and rhythm

Give each slide one dominant visual mechanism. Candidate mechanisms include:

- hero typography plus a geometric or SVG counterweight;
- one large diagram with edge annotations;
- a 60/40 evidence-and-conclusion split;
- a comparison axis, matrix, timeline, funnel, system map, or layered architecture;
- one large number with a cause/effect trail;
- an editorial collage made from native shapes and supplied content assets.

Vary composition by semantic role. Do not repeat the same three-card grid on adjacent pages. Maintain identity through palette, type, line style, and spacing rather than a rigid master layout.

## 5. Native visual techniques

Use CSS gradients to create atmosphere:

```css
.slide {
  background:
    radial-gradient(circle at 78% 24%, rgb(99 102 241 / 18%), transparent 26%),
    linear-gradient(145deg, #fafcff, #eef2ff 58%, #f8fafc);
}
```

Use repeating gradients for paper ruling, grids, halftone, and hatching. Use `clip-path` for wedges and crops. Use pseudo-elements for crop marks, tape, underlines, ribbons, and oversized numerals.

Use inline SVG for:

- curved connectors and arrow markers;
- hand-drawn paths with `filter` turbulence/displacement;
- technical grids and architectural linework;
- charts, maps, node networks, and exploded diagrams;
- masks, clipping paths, patterns, and duotone filters.

Keep SVG `viewBox` coordinates stable. Mark purely decorative SVG as `aria-hidden="true"`. Give meaningful SVG a `<title>` and a descriptive `aria-label`.

Use `mix-blend-mode`, `backdrop-filter`, and blur sparingly. Always provide sufficient contrast when effects are unsupported.

## 6. Diagrams and data

Start with the relationship, not the container. Ask what the viewer must understand: sequence, comparison, hierarchy, feedback, ownership, magnitude, or dependency.

Build charts and diagrams with direct labels. Use one accent to identify the conclusion. Avoid legends that force repeated eye travel. Include units, time periods, baselines, and sources when present in the material.

For dense tables, emphasize rows or columns structurally rather than adding more colors. Use tabular numerals and align decimal places.

## 7. Asset handling

Supplied images may be used as content evidence. Preserve labels and essential regions. Crop only when the user permits it.

For a self-contained deck:

- embed raster assets as base64 data URIs;
- inline SVG assets after sanitizing unsafe scripts and external links;
- include meaningful `alt` text;
- keep image dimensions explicit to prevent layout shifts.

Do not embed a full reference slide or generated screenshot as a background. The page must remain a composition of editable native elements.

## 8. Common failure modes

- Web-dashboard look: too many uniform cards, pills, and icon tiles.
- Template repetition: identical title bars and three-column modules on every slide.
- Decoration without concept: arbitrary gradients, blobs, and lines that do not reinforce meaning.
- Weak hierarchy: title, body, data, and annotations have similar visual weight.
- Tiny-text rescue: content is forced below presentation-readable sizes.
- Fake richness: many shadows and effects replace composition and information design.
- Raster shortcut: a finished slide image is placed behind token HTML.
- Reference mismatch: colors are copied, but geometry, density, typography, and shape language are not.

