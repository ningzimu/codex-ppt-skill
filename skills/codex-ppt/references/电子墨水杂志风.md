# 电子墨水杂志风

**适用场景:**
- 线下分享
- 行业内部讲话
- AI / 科技产品发布
- Demo day
- 个人观点型演讲
- 非虚构叙事
- 需要强节奏感的主题演讲

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "电子墨水杂志风",
  "best_for": "线下演讲、观点分享、AI/科技发布、非虚构叙事和需要强个人表达的横向演示",
  "visual_direction": "electronic ink editorial presentation, premium magazine layout, serif headline, sans-serif body, monospace metadata, restrained WebGL-like ink flow background only as subtle texture, strong hero/non-hero rhythm",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "off-white #F7F4EA, ink black #111111, deep indigo #1E2A78, forest ink #163B2F, kraft paper #D8C3A5, or dune sand #D9C29E depending on theme",
    "composition": "editorial grid with strong margins, magazine-like hierarchy, hero pages alternating with quieter content pages",
    "density": "moderate to low information density, designed for stage readability and narrative pacing"
  },
  "color_palette": {
    "base": "paper-like light background or deep ink background",
    "primary": "ink black, off-white, or deep indigo",
    "accent": "one restrained accent such as vermilion, electric blue, forest green, or sand gold",
    "metadata": "muted gray or low-contrast monochrome",
    "rule": "use a curated theme palette; avoid random custom colors and decorative gradients"
  },
  "typography": {
    "title": "large editorial serif Chinese headline or elegant high-contrast display type",
    "body": "clean sans-serif, short paragraphs or compact bullets",
    "metadata": "small monospace labels for chapter, date, source, index, or tags",
    "text_quality": "Chinese text must be exact, readable, and typeset like a magazine spread"
  },
  "layout_patterns": [
    "hero cover with oversized serif headline and subtle ink-flow background",
    "chapter divider with one provocative sentence and metadata strip",
    "data poster with one huge number, footnote, and tiny supporting labels",
    "left text right image with image treated as editorial photography or abstract ink plate",
    "big quote page with pull quote, source line, and large whitespace",
    "before-after comparison with two editorial columns"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; alternate hero and non-hero pages to create rhythm, and avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "hero editorial opener",
      "sections": [
        {"position": "left or center", "count": 1, "labels": ["oversized serif headline"]},
        {"position": "top or side edge", "count": 3, "labels": ["chapter label", "date/source", "short metadata"]},
        {"position": "background", "count": 1, "labels": ["subtle ink-flow or paper texture"]},
        {"position": "bottom", "count": 1, "labels": ["one-line thesis"]}
      ]
    },
    {
      "name": "magazine argument spread",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["slide title"]},
        {"position": "left column", "count": 2, "labels": ["argument block", "evidence block"]},
        {"position": "right half", "count": 1, "labels": ["editorial image, diagram, or abstract visual plate"]},
        {"position": "bottom", "count": 1, "labels": ["monospace metadata strip"]}
      ]
    },
    {
      "name": "data broadsheet",
      "sections": [
        {"position": "center-left", "count": 1, "labels": ["huge number or keyword"]},
        {"position": "right column", "count": 3, "labels": ["supporting fact 1", "supporting fact 2", "supporting fact 3"]},
        {"position": "bottom-left", "count": 1, "labels": ["source / caveat / time range"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "editorial rules, thin dividers, paper grain, subtle ink-flow texture, cropped photography zones, metadata strips, chapter marks, pull quotes, huge numerals",
    "avoid": "template-like cards, shiny corporate gradients, cute illustrations, dense tables, dashboard overload, generic stock-photo collage"
  },
  "rendering_constraints": [
    "The slide should feel like an electronic magazine page adapted for a stage presentation.",
    "Use large readable typography and strong whitespace.",
    "Do not turn every page into a hero cover; alternate page intensity across the deck.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
