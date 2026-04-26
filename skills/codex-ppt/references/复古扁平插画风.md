# 复古扁平插画风

**适用场景:**
- 文化创意项目展示
- 品牌故事讲述
- 旅游景点介绍
- 复古产品发布
- 艺术设计作品集
- 创意活动宣传
- 生活方式类演示

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "复古扁平插画风",
  "best_for": "文化创意、品牌故事、生活方式、城市旅游和带叙事感的主题演示",
  "visual_direction": "retro flat vector illustration slide, cream paper texture, monoline black outlines, vintage palette, playful handcrafted design",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "cream/off-white paper #F5F3E8 with subtle grain",
    "composition": "panoramic illustration band plus structured content cards or labels",
    "density": "moderate, decorative but still clear"
  },
  "color_palette": {
    "base": "cream background and dark slate text #34495E",
    "vintage_colors": "coral red #FF6B6B, mint green #95E1D3, mustard yellow #F9CA24, burnt orange #E17055, slate blue #6C7A89",
    "line": "uniform black or deep charcoal outline",
    "rule": "flat fills only, no glossy 3D, no heavy gradients"
  },
  "typography": {
    "title": "bold retro serif or chunky vintage display type",
    "body": "geometric sans-serif, clear and friendly",
    "labels": "small badge labels with outlined shapes",
    "text_quality": "Chinese text must be exact and readable"
  },
  "layout_patterns": [
    "top panoramic flat illustration with bottom content cards",
    "central retro title with three outlined icon cards",
    "2.5D simplified scene with callout labels",
    "vintage poster composition adapted to presentation readability"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "panoramic illustration plus cards",
      "sections": [
        {"position": "top third", "count": 1, "labels": ["panoramic flat vector illustration"]},
        {"position": "middle", "count": 1, "labels": ["large retro title"]},
        {"position": "bottom", "count": 3, "labels": ["outlined content card 1", "outlined content card 2", "outlined content card 3"]}
      ]
    },
    {
      "name": "retro poster diagram",
      "sections": [
        {"position": "center", "count": 1, "labels": ["main simplified scene or object"]},
        {"position": "around center", "count": 4, "labels": ["callout label", "badge", "mini icon", "decorative note"]},
        {"position": "bottom-right", "count": 1, "labels": ["summary plaque"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "flat vector scenes, 2-3px monoline outlines, simplified buildings, plants, clouds, badges, dotted textures, small geometric decorations",
    "avoid": "photorealism, complex shadows, neon palette, overly detailed linework, unreadable decorative type"
  },
  "rendering_constraints": [
    "The slide should feel like a polished retro illustration system, not a random cartoon.",
    "Maintain consistent outline weight across objects.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
