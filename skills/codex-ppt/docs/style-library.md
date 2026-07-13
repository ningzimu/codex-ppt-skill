# Style Library

Read this when the user asks to save a finished deck style, a sample-slide style, or a user-supplied image/PDF/PPT/PPTX style into the reusable style library.

The goal is to save a reusable visual system, not the current deck's private content.

User custom styles are saved to `${CODEX_PPT_HOME:-~/.codex-ppt-skill}/references/`, outside the skill install directory, so they survive skill updates and reinstalls. Never write user custom styles into the skill's own `references/` directory; that directory is reserved for built-in styles shipped with the skill.

## When To Use

Use this workflow when the user says things like:

- Save this style.
- Add this PPT style to the style library.
- Let future decks use this style.
- Turn this image/PDF/PPT/PPTX style into a built-in reference.
- Save the style from the finished deck.

If the user only wants to use a style once, extract a temporary style description for the current deck instead of writing a new style file.

## Inspect The Visual Source

Use the actual visible pages as the source of truth.

- For a finished codex-ppt deck, inspect the final `origin_image/slide_XX.png` files or exported slide page images.
- For a sample slide, inspect the approved sample image.
- For user-provided image references, inspect the image itself.
- For PDF/PPT/PPTX references, first render or export representative pages/slides into real page images, then inspect those images. Do not infer the style from file structure, text, XML, metadata, or object hierarchy alone.

Inspect enough pages to capture the style system. Prefer at least one cover or opener, one ordinary content slide, one diagram/process/data slide when available, and one closing or summary slide. If the deck has obvious section-specific variants, record those variants inside the style file.

## Extract The Style System

Extract reusable visual rules:

- `style_name`: short reusable name.
- `best_for`: suitable scenarios and audiences.
- `visual_direction`: one concise description of the style identity.
- `canvas`: aspect ratio, background, composition, density, whitespace.
- `color_palette`: primary, secondary, accent, neutral colors, plus usage rules.
- `typography`: title, body, labels, hierarchy, alignment, text quality rules.
- `layout_patterns`: recurring page types and composition patterns.
- `layout_usage_rule`: how to vary layouts while keeping the same identity.
- `layout_blueprints`: 2-4 reusable composition blueprints, described semantically rather than copied from one slide.
- `visual_elements`: allowed and avoided icons, diagrams, cards, textures, decorations, photos, charts.
- `image_treatment`: how photos, screenshots, charts, or illustrations are handled.
- `rendering_constraints`: rules the image model should follow.

Do not save private or one-off content as style:

- Do not save the user's original article text, business data, personal information, customer names, private project names, paper results, exact quotes, or slide copy.
- Do not save source images or screenshots as required dependencies of the style file.
- Do not preserve identifiable logos or brand names unless the user explicitly asks for a reusable brand style.
- Do not make the style depend on external files; the style file must be self-contained.

## Name The Style

Name the file:

```text
${CODEX_PPT_HOME:-~/.codex-ppt-skill}/references/{style_name}.md
```

Create the directory first if it does not exist.

Naming rules:

- Prefer a short Chinese style name, usually 2-8 Chinese characters or a concise Chinese phrase.
- Name the reusable visual style, not the project, client, paper, or event.
- Avoid personal names, company names, customer names, paper titles, or temporary task names.
- Avoid vague names like `我的风格1`, `好看风`, or `新风格`.
- Good examples: `深色数据科技风`, `极简发布会风`, `柔和学术插画风`, `高密度咨询风`.

If the target filename already exists in the user style directory, ask whether to overwrite, merge, or choose a new name. If the filename matches a built-in style in the skill's `references/`, tell the user the custom file will take priority over the built-in style with the same name, and confirm that is intended before saving.

## Write The Style File

Match the structure of the built-in files in the skill's `references/`:

    # {style_name}

    **适用场景:**
    - ...
    - ...

    **GPT-Image-2 风格 Brief:**
    ```json
    {
      "type": "16:9 full-slide PowerPoint image",
      "style_name": "{style_name}",
      "best_for": "...",
      "visual_direction": "...",
      "canvas": {
        "aspect_ratio": "16:9",
        "background": "...",
        "composition": "...",
        "density": "..."
      },
      "color_palette": {
        "primary": "...",
        "secondary": "...",
        "accent": "...",
        "neutral": "...",
        "rule": "..."
      },
      "typography": {
        "title": "...",
        "body": "...",
        "labels": "...",
        "text_quality": "..."
      },
      "layout_patterns": [
        "...",
        "..."
      ],
      "layout_usage_rule": "...",
      "layout_blueprints": [
        {
          "name": "...",
          "sections": [
            {"position": "...", "count": 1, "labels": ["..."]}
          ]
        }
      ],
      "visual_elements": {
        "allowed": "...",
        "avoid": "..."
      },
      "image_treatment": {
        "photos": "...",
        "screenshots": "...",
        "charts": "...",
        "illustrations": "..."
      },
      "rendering_constraints": [
        "...",
        "..."
      ]
    }
    ```

The JSON should be directly reusable as a slide generation style brief. Keep it descriptive enough for future agents, but avoid embedding task-specific content.

## Discovery

No registration step is needed. Future style confirmation steps scan `${CODEX_PPT_HOME:-~/.codex-ppt-skill}/references/` and merge its files with the built-in style list, so the saved file is discoverable automatically. Do not edit `docs/outline-style-and-sample.md` or any other file inside the skill for a user custom style.

## Final Response

Report:

- The new style name.
- The saved file path under `${CODEX_PPT_HOME:-~/.codex-ppt-skill}/references/`.
- That the style is stored outside the skill install, so it survives skill updates and reinstalls.
- A one-sentence note on how to request it later, for example: "以后可以说：用「深色数据科技风」生成这份 PPT。"
