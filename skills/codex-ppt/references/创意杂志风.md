# 创意杂志风

**适用场景:**
- 创意提案
- 品牌展示
- 设计作品集
- 文化活动
- 时尚发布
- 艺术展览
- 创意工作室介绍

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "创意杂志风",
  "best_for": "需要强视觉记忆点、品牌个性或传播感的分享型演示",
  "visual_direction": "high-end editorial magazine spread, bold asymmetry, art-directed composition, graphic tension, premium creative layout",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "white, black, or deep charcoal with intentional negative space",
    "composition": "asymmetric editorial layout with a large headline, image/collage zone, and 2-3 supporting text blocks",
    "density": "strong contrast between dense editorial blocks and open whitespace"
  },
  "color_palette": {
    "base": "black, white, and gray",
    "accent": "one vivid accent such as neon pink #FF006E, lemon yellow #FFED00, or electric cyan #00F5FF",
    "support": "optional lavender, coral, or muted fashion tones",
    "rule": "use one dominant accent color consistently; do not make the palette chaotic"
  },
  "typography": {
    "title": "oversized bold display sans-serif or editorial serif, can occupy 25-45% of the slide",
    "body": "small clean sans-serif blocks with strong alignment",
    "emphasis": "keywords may use accent color, rotated labels, vertical text, or extreme scale contrast",
    "text_quality": "Chinese headline and key points must be exact and readable"
  },
  "layout_patterns": [
    "oversized headline on one side with collage or abstract image block on the other",
    "diagonal color block cutting across the slide",
    "magazine cover style with title, subtitle, and three feature teasers",
    "editorial grid with one large image crop and small annotation labels"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "editorial hero spread",
      "sections": [
        {"position": "left 45%", "count": 1, "labels": ["oversized headline"]},
        {"position": "right 55%", "count": 1, "labels": ["collage or abstract image zone"]},
        {"position": "bottom-left", "count": 3, "labels": ["feature teaser 1", "feature teaser 2", "feature teaser 3"]}
      ]
    },
    {
      "name": "cover story grid",
      "sections": [
        {"position": "top", "count": 1, "labels": ["large cover title"]},
        {"position": "center", "count": 2, "labels": ["main visual block", "accent typography block"]},
        {"position": "right edge", "count": 3, "labels": ["short editorial callouts"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "bold geometric blocks, cropped photography zones, halftone texture, thin rules, torn-paper collage edges, accent stickers, abstract shapes",
    "avoid": "generic corporate icons, overly symmetrical layout, low-contrast text, too many accent colors"
  },
  "rendering_constraints": [
    "The slide should feel designed, not templated.",
    "Maintain legibility despite bold composition.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
