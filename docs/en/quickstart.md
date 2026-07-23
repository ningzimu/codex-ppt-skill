# Quick Start

## Who This Is For

This page is for first-time Codex PPT users. All you need is an article, report, outline, paper, or set of course notes. Then ask your agent to use the `codex-ppt` skill to generate a presentation.

## Shortest Way to Get Started

First install the skill by following [Installation and Configuration](/en/installation.md). Then use the skill directly in Codex to create your presentation.

```text
Please use the codex-ppt skill to turn /path/to/article.md into a Chinese presentation of about 10 slides.
```

If you already know the intended style and use case, be more specific:

```text
Please use the codex-ppt skill to turn this technical article into a 12-slide Chinese presentation. Use a clean, professional style suitable for an internal technical talk. Slide 5 must use the architecture diagram I provided, and slide 8 must preserve the experiment results figure.
```

## Recommendations for Your First Use

- Ask the agent to generate `outline.md` first, then confirm the slide count, titles, and key points for each slide.
- Do not skip sample-slide confirmation. Review one slide before generating the full deck.
- If one slide is unsatisfactory, revise only that slide instead of regenerating the entire deck.
- If you have a reference presentation, screenshot, or PDF, ask the agent to analyze its style before generating the new presentation.

## Generated Outputs

You will usually receive:

- `outline.md`: Presentation outline
- `origin_image/slide_XX.png`: Final image for each slide
- `speech.md`: Speaker notes for each slide
- `{presentation-name}.pptx`: Final PowerPoint file
