# Design Philosophy

Codex PPT Skill reflects some of my thinking about using AI to create presentations.

The most important thing about AI-generated presentations is not speed, but having a controllable process that produces usable results.

That is why I split the process into several steps:

1. Read the article, paper, report, or Markdown file
2. Generate an outline so the user can confirm the slide count, titles, and focus of each slide
3. Confirm the overall visual style
4. Generate one sample slide to check whether the text, layout, and style are suitable
5. After the sample is approved, generate the complete image-based presentation slide by slide
6. Assemble the slides into a `.pptx` file and add the script to the notes for convenient presentation reference

## Why Generate an Image-Based Presentation First?

Not every scenario requires editability. For technical talks, course notes, book-sharing sessions, paper reviews, or less formal reports, a presentation made from full-slide images is often sufficient and offers better visual consistency.

If presentation generation and editable presentation conversion are tightly coupled from the beginning, the process becomes heavy. While the outline, style, and sample slide are still being revised, adding editable-structure reconstruction makes the workflow slower, more expensive, and harder to control.

That is why I split the process into two skills:

- One generates high-quality image-based presentations
- The other converts an image-only presentation into an editable presentation when needed

I believe it is more reliable to agree on the content and visual direction first, confirm that the generated results are under control, and only then decide whether editable conversion is necessary.

## Improvements Based on Community Feedback

This skill also includes several improvements based on community feedback:

- Supports the image-generation capability included with Codex subscriptions
- Also supports image-generation models through APIs
- Works in agent environments including Codex, Claude Code, and OpenClaw
- Supports parallel generation with sub-agents to speed up multi-slide presentation creation
- Includes guidance for multiple built-in styles, so you can get good results without writing advanced prompts
- Supports using reference images or existing presentations to generate a new presentation in a similar style
- Preserves user-provided source images such as paper figures, experiment result charts, and screenshots wherever possible, reducing the risk of AI redrawing them incorrectly

My goal is not to produce a 20-slide presentation with one click. It is to make AI presentation creation feel more like a real workflow: establish the structure, choose the style, approve a sample, then generate the complete deck and inspect the results.
