# Styles and Personal Style Library

Codex PPT draws its visual styles from two sources: the **built-in styles** shipped with the skill and your **personal style library**, which is stored locally and remains intact when the skill is updated.

## Built-in Styles

The skill includes 12 built-in style references, so you can get started without knowing how to write prompts. When creating a presentation, simply name the style you want. For example:

```text
Please use the codex-ppt skill to turn this material into a 10-slide presentation using the built-in "Hand-Drawn Technical Explanation" style.
```

| Clean Professional | Creative Magazine |
| --- | --- |
| ![Clean Professional](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/clean-professional.png) | ![Creative Magazine](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/creative-magazine.png) |
| E-Ink Magazine | Data Dashboard |
| ![E-Ink Magazine](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/e-ink-magazine.png) | ![Data Dashboard](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/data-dashboard.png) |
| Retro Flat Illustration | Hand-Drawn Technical Explanation |
| ![Retro Flat Illustration](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/retro-flat-illustration.png) | ![Hand-Drawn Technical Explanation](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-technical.png) |
| Hand-Drawn Whiteboard | Warm Handmade |
| ![Hand-Drawn Whiteboard](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-whiteboard.png) | ![Warm Handmade](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/warm-handmade.png) |
| Scientific Defense | McKinsey-Style |
| ![Scientific Defense](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/scientific-defense.png) | ![McKinsey-Style](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/mckinsey-style.png) |
| Party and Government Red | Teaching Courseware |
| ![Party and Government Red](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/party-government-red.png) | ![Teaching Courseware](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/teaching-courseware.png) |

A style is a visual system—including color palette, typographic character, layout density, and illustration language—not a fixed template. Within one style, each slide's layout changes according to its content role, so the slides do not all look identical.

## Reproducing the Style of Reference Materials

If the built-in styles do not meet your needs, provide a style reference you like: one screenshot, several screenshots, or a complete presentation or PDF. Ask the agent to analyze the colors, layout, typography, and visual elements before generating a new presentation in the same style:

```text
Please use the codex-ppt skill to generate a presentation. Use the PDF I uploaded as the visual style reference. Review every page image in detail to understand its style, then generate the presentation in a similar style.
```

Note: By default, only the style is reproduced, not the content. Unless you explicitly request it, text and data from the reference material will not be copied into the new presentation.

## Personal Style Library

If you are satisfied with a generated presentation's style—whether it is a custom style you developed or a style reproduced from reference material—you can ask the agent to save it for direct reuse:

```text
I really like the visual style of this presentation. Please save it to my personal style library.
```

Key points about how saving works:

- **Storage location**: Your personal style library is located at `~/.codex-ppt-skill/references/` and can be moved using the `CODEX_PPT_HOME` environment variable. It is stored **outside** the skill installation directory, so updating or reinstalling the skill will not overwrite or remove your personal styles.
- **Automatic discovery**: No registration is required after saving. The next time you choose a presentation style, the agent automatically scans your personal style library and lists your styles alongside the built-in styles.
- **Personal styles take precedence**: If a personal style has the same name as a built-in style, your personal style is used. You can use this behavior to customize a built-in style by saving an adjusted version under the same name.
- **Reuse by name**: In the future, simply name the style—for example, "Generate this presentation using the 'Dark Data Technology' style."

After generation, if a deck uses a custom or adjusted style, the agent will also mention in its final report that you can save it. There is no need to save an unmodified built-in style again.

## Related Pages

- [Example Prompts](/en/prompts.md): Complete prompts for choosing a built-in style, matching a reference style, and saving a style.
- [FAQ](/en/faq.md): What to do when the style drifts or a slide is unsatisfactory.
