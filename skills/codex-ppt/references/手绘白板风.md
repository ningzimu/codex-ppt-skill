# 手绘白板风

**适用场景:**
- 教学讲解
- 培训课程
- 头脑风暴
- 概念说明
- 技术分享
- 内部研讨

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "手绘白板风",
  "best_for": "概念解释、技术分享、培训课程和需要亲和力的思路拆解",
  "visual_direction": "realistic whiteboard explanation slide, marker handwriting, sketched diagrams, friendly teaching atmosphere, authentic whiteboard details",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "warm off-white whiteboard surface #FAFAF5 with subtle marker smudges",
    "composition": "freeform but organized whiteboard layout with title, three concept blocks, arrows, and small doodle illustrations",
    "density": "moderate, readable, brainstorming feel without chaos"
  },
  "color_palette": {
    "primary": "black marker for main text",
    "accent": "red #E74C3C, blue #3498DB, orange #F39C12 marker annotations",
    "support": "green #27AE60, purple #9B59B6, yellow sticky note #FFF9C4",
    "rule": "colors should look like real marker ink, not digital neon"
  },
  "typography": {
    "title": "large neat handwritten Chinese marker style",
    "body": "clear handwritten marker text, slightly irregular but readable",
    "emphasis": "circle, underline, boxed words, sticky-note comments",
    "text_quality": "Chinese handwriting must remain accurate and legible"
  },
  "layout_patterns": [
    "three hand-drawn boxes connected by arrows",
    "central concept bubble with surrounding notes",
    "simple process diagram with sketches and annotations",
    "left explanation list plus right hand-drawn diagram"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "whiteboard process diagram",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["handwritten title"]},
        {"position": "center", "count": 3, "labels": ["step 1 box", "step 2 box", "step 3 box"]},
        {"position": "between boxes", "count": 2, "labels": ["hand-drawn arrow", "hand-drawn arrow"]},
        {"position": "right edge", "count": 1, "labels": ["sticky-note takeaway"]}
      ]
    },
    {
      "name": "concept map",
      "sections": [
        {"position": "center", "count": 1, "labels": ["main concept bubble"]},
        {"position": "around center", "count": 4, "labels": ["supporting idea", "risk note", "example sketch", "action item"]},
        {"position": "bottom", "count": 1, "labels": ["underlined summary"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "whiteboard frame, marker tray, colored markers, arrows, boxes, clouds, sticky notes, doodle icons, underlines, circled keywords",
    "avoid": "messy illegible handwriting, childish clutter, photoreal people, digital UI cards"
  },
  "rendering_constraints": [
    "The slide should look like a real whiteboard captured cleanly for a presentation.",
    "Keep all Chinese text readable despite handwritten style.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
