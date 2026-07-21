# HTML deck QA

Run both deterministic validation and browser inspection. Passing the script does not prove that a slide is visually correct.

## Deterministic validation

Run:

```bash
python3 scripts/validate_deck.py /absolute/path/deck.html \
  --expect-slides <count> --strict
```

Resolve every error. Resolve warnings unless the user explicitly approved the exception.

## Browser inspection

Open the HTML directly or serve its directory with:

```bash
python3 -m http.server 8000 --directory /absolute/path/to/deck-directory
```

Inspect every slide at these viewport sizes:

- 1600×900: design coordinate baseline.
- 1366×768: common laptop presentation viewport.
- 390×844: confirm the scaled stage remains reachable on mobile.

Transient browser screenshots may be used for inspection, but do not save or deliver raster slide files.

Check:

- no title, label, axis, source, or required image is clipped;
- no text block overlaps another element;
- body text is presentation-readable and line breaks are intentional;
- the primary message is obvious within three seconds;
- adjacent slides do not repeat the same composition mechanically;
- palette, typography, stroke language, and spacing remain coherent;
- required facts, names, numbers, citations, and assets are exact;
- decorative SVG does not capture pointer events or pollute accessibility output;
- keyboard navigation works for arrows, Page Up/Down, Space, Home, and End;
- fullscreen and notes toggles work;
- the URL hash opens the requested slide;
- reduced-motion mode remains usable;
- browser console shows no uncaught errors or failed asset requests;
- print preview places one 16:9 slide per page without controls.

## Revision threshold

Regenerate the composition, rather than applying tiny patches, when a slide has more than one of these problems:

- content only fits by using text below 24 px;
- the reading order is ambiguous;
- the reference style is recognizable only by color;
- more than six equal-weight modules compete for attention;
- the dominant diagram does not communicate a relationship;
- the slide resembles a web dashboard when the chosen direction is editorial, illustrative, academic, or consulting.

