# 清爽专业风

**适用场景:**
- 毕业答辩
- 工作总结
- 工作 review
- 技术分享
- 项目复盘
- 晋升述职
- 阶段性成果汇报

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "清爽专业风",
  "best_for": "毕业答辩、工作总结、工作 review、技术分享、项目复盘和晋升述职等需要清晰表达过程、成果、问题和下一步的场景",
  "visual_direction": "clean modern professional deck, calm technical presentation, structured evidence-driven layout, readable pragmatic visual system, light background with crisp hierarchy",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "warm white #FFFFFF, light gray #F8FAFC, or very pale blue #F6F9FF",
    "composition": "title zone, structured content zone, evidence/diagram zone, and concise takeaway zone",
    "density": "medium information density, enough room for technical details without visual clutter"
  },
  "color_palette": {
    "primary": "professional blue #2563EB or slate blue #334155",
    "secondary": "calm teal #0F766E or muted cyan #0891B2",
    "accent": "soft amber #F59E0B for highlights and risk/attention notes",
    "neutral": "slate gray #475569, light border #E2E8F0, pale card background #F8FAFC",
    "rule": "use restrained professional colors; avoid playful neon, luxury gold, or heavy dark backgrounds"
  },
  "typography": {
    "title": "clear bold sans-serif, report-like and authoritative",
    "body": "clean sans-serif, strong hierarchy, left-aligned for readability",
    "labels": "small but readable labels for timeline, evidence, metrics, and code/process diagrams",
    "text_quality": "Chinese text must be exact, readable, and suitable for formal reporting"
  },
  "layout_patterns": [
    "problem-process-result-next steps",
    "timeline plus milestone cards",
    "technical architecture diagram with key takeaways",
    "summary dashboard with achievements, issues, learnings, and plan",
    "defense slide with research question, method, evidence, and conclusion"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "work review summary",
      "sections": [
        {"position": "top", "count": 1, "labels": ["slide title and context subtitle"]},
        {"position": "left column", "count": 3, "labels": ["目标", "完成情况", "关键结果"]},
        {"position": "right column", "count": 2, "labels": ["问题与风险", "下一步计划"]},
        {"position": "bottom", "count": 1, "labels": ["one-sentence takeaway"]}
      ]
    },
    {
      "name": "technical sharing flow",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["topic title and motivation"]},
        {"position": "center", "count": 1, "labels": ["architecture / workflow / method diagram"]},
        {"position": "right", "count": 3, "labels": ["核心机制", "实践经验", "注意事项"]},
        {"position": "bottom", "count": 3, "labels": ["before", "after", "impact"]}
      ]
    },
    {
      "name": "graduation defense evidence slide",
      "sections": [
        {"position": "top", "count": 1, "labels": ["研究问题 / 答辩主题"]},
        {"position": "left", "count": 1, "labels": ["方法路线图"]},
        {"position": "center", "count": 2, "labels": ["实验/项目证据", "关键数据"]},
        {"position": "right", "count": 1, "labels": ["结论与贡献"]},
        {"position": "bottom", "count": 1, "labels": ["限制与后续工作"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "timeline, checklist, progress bars, architecture blocks, process arrows, evidence cards, metric badges, issue/risk callouts, code-like panels, simple icons",
    "avoid": "overly decorative poster layout, random stock photos, cute stickers, dense unreadable tables, exaggerated marketing style"
  },
  "rendering_constraints": [
    "The slide should look suitable for a real workplace review, thesis defense, or technical sharing session.",
    "Prioritize clarity, evidence, and logical flow over decoration.",
    "All diagrams and labels should feel purposeful and related to the slide content.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
