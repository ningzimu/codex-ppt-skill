# 手绘技术解释风

**适用场景:**
- 中文技术文章配图
- 技术概念解释
- 课程课件
- 知识卡片
- 产品机制说明
- AI / 软件工程主题分享
- 需要降低理解门槛的复杂概念

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "手绘技术解释风",
  "best_for": "中文技术文章、课程课件、复杂概念解释、知识卡片和软件工程/AI 主题的低压力说明图",
  "visual_direction": "clean Chinese handdrawn technical explainer, near-white paper background, thin sketch lines, light pencil hatching, small precise central diagram, restrained pastel markers, lots of whitespace, calm educational tone",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "near-white paper #FCFBF7, not yellow, no full-page border",
    "composition": "small central explanatory diagram with sparse labels, surrounding whitespace, short title and minimal visible text",
    "density": "low to moderate; one core idea per slide; avoid dense whiteboard clutter"
  },
  "color_palette": {
    "line": "soft graphite #2F3437 or dark gray ink, thin and slightly irregular",
    "accent": "pale blue #BFD7F1, sage green #CFE2D1, light peach #F4C7B8, pale lavender #D8C7EF",
    "background": "near-white, clean, not kraft, not cream-heavy",
    "rule": "pastel marks are used for emphasis only; keep the page calm and airy"
  },
  "typography": {
    "title": "restrained handwritten Chinese title, medium-large but not poster-sized",
    "body": "short handwritten Chinese labels, few words per label, easy to inspect",
    "emphasis": "light underline, small bracket, soft marker highlight, or tiny note tag",
    "text_quality": "Chinese text must be exact, sparse, and readable; avoid long paragraphs"
  },
  "layout_patterns": [
    "central concept diagram with 3-4 short surrounding labels",
    "before-after explanation with two small sketch panels",
    "flow diagram with 3 steps and minimal arrows",
    "mental model page with one metaphor object and short annotations",
    "matrix or decision guide with sparse handwritten notes",
    "summary page with one small character or object and three takeaway labels"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; keep visual DNA stable while varying archetypes such as metaphor, process, comparison, matrix, and summary. Avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "small central concept map",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["short handwritten title"]},
        {"position": "center", "count": 1, "labels": ["small precise concept diagram"]},
        {"position": "around center", "count": 4, "labels": ["label 1", "label 2", "label 3", "label 4"]},
        {"position": "bottom-right", "count": 1, "labels": ["one-sentence takeaway"]}
      ]
    },
    {
      "name": "technical before-after",
      "sections": [
        {"position": "top", "count": 1, "labels": ["short page title"]},
        {"position": "left", "count": 1, "labels": ["before sketch panel"]},
        {"position": "right", "count": 1, "labels": ["after sketch panel"]},
        {"position": "between panels", "count": 1, "labels": ["thin handdrawn arrow"]},
        {"position": "bottom", "count": 3, "labels": ["why it matters", "tradeoff", "next step"]}
      ]
    },
    {
      "name": "one idea teaching card",
      "sections": [
        {"position": "center-left", "count": 1, "labels": ["metaphor object or tiny engineer/reader character"]},
        {"position": "center-right", "count": 3, "labels": ["core idea", "common mistake", "useful rule"]},
        {"position": "background", "count": 1, "labels": ["very light pencil hatching and pastel highlight"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "thin handdrawn arrows, small diagrams, pencil hatching, pastel marker blocks, bracket notes, simple software/AI icons, tiny engineer or reader character at most once",
    "avoid": "messy whiteboard frame, marker tray, large cartoon characters, dense handwriting, yellowed paper, decorative stickers, poster-scale title, full-page border, digital UI cards"
  },
  "rendering_constraints": [
    "The slide should feel like a calm handdrawn technical article illustration, not a brainstorming whiteboard.",
    "Keep the central drawing small and precise with generous empty space.",
    "Use minimal Chinese text and make every visible word correct.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
