# 数据仪表盘风

**适用场景:**
- 数据分析报告
- 业绩展示
- KPI 汇报
- 实时数据展示
- 商业智能BI
- 运营数据看板

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "数据仪表盘风",
  "best_for": "数据密集型汇报、运营分析、KPI 复盘和业务洞察展示",
  "visual_direction": "bright modern SaaS analytics dashboard, clean BI interface, lightweight data cards, precise charts, professional and non-oppressive",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "white #FFFFFF, very light blue-gray #F5F8FC, or mist gray #F8FAFC",
    "composition": "dashboard grid with title area, KPI cards, chart panels, and status list",
    "density": "medium-high information density with enough card spacing and clear grouping"
  },
  "color_palette": {
    "primary": "data blue #2563EB or #1976D2",
    "secondary": "cyan #06B6D4 and soft purple #8B5CF6",
    "status": "green #10B981, orange #F59E0B, red #EF4444 used sparingly",
    "text": "deep navy #0F172A and neutral gray #64748B",
    "rule": "avoid dark control-room backgrounds, heavy neon, and oppressive black panels"
  },
  "typography": {
    "title": "bold clean sans-serif, dashboard header style",
    "numbers": "large tabular numerals for KPI values",
    "labels": "small but readable sans-serif chart labels",
    "text_quality": "Chinese labels and KPI names must be exact and legible"
  },
  "layout_patterns": [
    "top KPI strip with 3-4 cards and trend arrows",
    "main area split into workflow cards and a line chart",
    "lower area with donut chart, bar chart, and recent activity table",
    "large central insight card surrounded by supporting metrics"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. Choose and adapt the composition according to each slide's semantic role; avoid repeating the same blueprint on adjacent slides unless it is a deliberate repeated sequence.",
  "layout_blueprints": [
    {
      "name": "SaaS BI overview",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["dashboard title and subtitle"]},
        {"position": "top-right", "count": 4, "labels": ["KPI card 1", "KPI card 2", "KPI card 3", "KPI card 4"]},
        {"position": "middle-left", "count": 3, "labels": ["process card 1", "process card 2", "process card 3"]},
        {"position": "middle-right", "count": 1, "labels": ["line chart panel"]},
        {"position": "bottom", "count": 3, "labels": ["donut chart", "bar chart", "recent records table"]}
      ]
    },
    {
      "name": "single insight dashboard",
      "sections": [
        {"position": "center", "count": 1, "labels": ["large insight card"]},
        {"position": "surrounding", "count": 4, "labels": ["supporting metric", "trend sparkline", "status list", "risk indicator"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "white cards, soft shadows, pale borders, line charts, bar charts, progress rings, KPI cards, status dots, trend arrows, mini sparklines",
    "avoid": "dark monitoring wall, dense cyberpunk glow, unreadable tiny table text, random numbers without structure"
  },
  "rendering_constraints": [
    "The slide should look like a polished SaaS analytics product screenshot adapted for presentation.",
    "Charts should be visually plausible and organized, even when illustrative.",
    "No watermark, no unrelated logo, no slide number unless explicitly requested."
  ]
}
```
