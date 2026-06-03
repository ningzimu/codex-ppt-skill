# 麦肯锡风格

**适用场景:**
- 商业咨询型 PPT / PPTX 整套演示
- PPT 封面页、章节页、关键观点页
- 咨询分析页、框架页、方法论页
- 流程图、路线图、矩阵图、价值链、五力模型、2x2 定位图
- 结论页、建议页、执行路线页
- 商业策略、增长、转型、组织、效率、机会、风险等主题
- 需要“文字主导 + 商业隐喻 + 咨询报告质感”的视觉型演示

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "麦肯锡风格",
  "best_for": "商业咨询型 PPT / PPTX 整套演示，包括封面页、章节页、关键观点页、咨询分析页、框架页、方法论页、流程图、路线图、矩阵图、价值链、五力模型、2x2 定位图、结论页、建议页和执行路线页；适合商业策略、增长、转型、组织、效率、机会、风险等需要麦肯锡式理性气质、高端咨询报告视觉、标题信息重构、商业隐喻和清晰商业叙事的场景",
  "visual_direction": "McKinsey / BCG / Bain style rational consulting visual, premium executive report cover, modernist typographic poster, art-directed business metaphor, reconstructed title as architectural structure, precision annotation system, sharp Swiss grid, light blue-gray white palette, clean corporate editorial design, boardroom-ready restraint with real graphic tension",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "white or very pale cool gray field with optional subtle paper grain, light print texture, precise thin grid, quiet margin system, and restrained report-like metadata; avoid turning metadata into a repeated slide template",
    "composition": "first decide the PPT slide role: title/divider/key-message slides use one giant reconstructed core word, one dominant metaphor, strong negative space, and an intentional focal axis, vanishing point, or typographic architecture; analysis/framework/process slides use one core analytical structure and 3-6 ordered modules",
    "density": "title/divider/key-message slides are low-density with strong whitespace and one obvious center; analysis/framework/process slides are medium density, richer but still ordered, scannable, and built around one reading path"
  },
  "color_palette": {
    "primary": "white, off-white, light cool gray, pale blue-gray, ink blue-gray #243447 used as text or hairline emphasis",
    "secondary": "restrained consulting blue-gray, steel blue, mist blue, precise hairline gray",
    "accent": "very small restrained blue, steel blue, or muted gray-blue only for key node, value point, end point, decision point, or important arrow; avoid orange as a default accent",
    "neutral": "near-black #111111 only for small text, slate gray #475569, cool gray #6B7280, light border gray #D8DEE8, very pale background gray #F6F8FA",
    "rule": "colors must feel rational, premium, controlled, and light; avoid large dark navy blocks, orange-led accents, blue-purple neon, cyberpunk glow, fancy gradients, rainbow colors, high-saturation advertising colors, and large warm backgrounds"
  },
  "typography": {
    "title": "modern, clear, restrained, stable consulting-report typography; the main visual title should be custom-reconstructed with thin structural strokes, semi-hollow forms, split strokes, extended strokes, modular cuts, embedded grids, or architectural skeletons; keep it readable and avoid crude bold filled type",
    "body": "short precise Chinese/English labels, no long paragraphs, clear hierarchy, micro-typography for tags, variables, legends, nodes, occasional footers, and conclusions",
    "labels": "use restrained English classification labels such as STRATEGY, MARKET INSIGHT, BUSINESS MODEL, OPERATING MODEL, GROWTH SYSTEM, TRANSFORMATION, INDUSTRY VIEW, METHODOLOGY, RECOMMENDATION, ROADMAP, 2026",
    "text_quality": "main title, subtitle, brand names, people names, terms, English capitalization, and Chinese characters must be accurate; preserve the user's core input term; do not garble Chinese or invent unrelated labels"
  },
  "layout_patterns": [
    "PPT title or divider slide: top information bar with full title, English category tags, year or section number; central giant reconstructed core word; 2-3 edge anchor concepts; optional short takeaway only when it strengthens the page",
    "PPT key-message slide: extract a 2-8 character Chinese core word or 1-4 word English phrase as the main visual, keep the full claim as smaller subtitle text, and use only one dominant metaphor",
    "PPT title/key-message slide: fuse one business metaphor into the typography itself, such as path through strokes, funnel in negative space, matrix grid as character skeleton, data flow emerging from the word, fault line cutting the word, or architecture becoming the word body",
    "PPT title/key-message slide: make the core word feel engineered and art-directed: letter strokes may be cropped, extended, split, semi-transparent, line-drawn, or connected to crosshairs, target marks, measurement lines, nodes, and micro labels",
    "PPT title/key-message slide: create graphic tension through scale contrast, asymmetrical balance, precise alignment, restrained perspective rays, one focal point, and large quiet whitespace; avoid flat centered template composition",
    "PPT title/divider archetype: typographic science/report slide with ultra-thin Chinese character strokes, molecular or data-path particles crossing the word, side annotations, and optional evidence labels",
    "PPT key-message archetype: executive insight slide with a bold but controlled headline, one ribbon/path/spiral/arrow metaphor, vertical outcome scale, small right-side labels, and wide blank field",
    "PPT title/divider archetype: modernist typographic poster slide with oversized English or Chinese letterforms, curved line systems, crop marks, circular labels, and sparse deck metadata",
    "PPT analysis/framework slide: top claim area, central structure such as process, matrix, system, path, funnel, value chain, or layered architecture, side modules for insight, variables, constraints, risks, and opportunities, and an optional recommendation area if the slide needs a takeaway",
    "PPT analysis/process slide: use a clear reading path from left to right, top to bottom, problem to solution, input to output, current state to opportunity, or mechanism to result",
    "PPT framework slide: keep one large analytical mechanism as the hero and use micro annotations, numbered labels, hairline connectors, and restrained side notes instead of icon-heavy cards",
    "PPT analysis archetype: BCG-style matrix, five-forces map, value-chain map, operating-model map, roadmap, or 2x2 decision map with one dominant diagram, disciplined sidebars, small methodology labels, and at most one dark emphasis block",
    "metaphor library: choose exactly one most accurate dominant metaphor from funnel, path, ladder, matrix, coordinate, flywheel, node network, data flow, threshold, window, defense line, fault line, container, compass, or architecture",
    "business metaphor matching: funnel for conversion and filtering; path for strategy and transformation; ladder for maturity and value upgrade; matrix for positioning and priority; coordinate for market map and risk-return; flywheel for growth loops; node network for system collaboration; data flow for automation and efficiency; threshold for gating and risk control; window for timing and opportunity; defense line for governance and compliance; fault line for structural shifts; container for value pools; compass for direction choice; architecture for organization and capability base"
  ],
  "layout_usage_rule": "Use layout_blueprints as candidate starting points only. First identify the PPT slide role: title slide, section divider, key-message slide, analysis/framework slide, process/roadmap slide, matrix/positioning slide, or summary/recommendation slide. For title, divider, and key-message slides, use one giant reconstructed title, one dominant metaphor, low information density, strong whitespace, very few auxiliary words, and a visible graphic idea in the typography itself. For analysis, framework, process, and recommendation slides, use 3-6 main modules, one core structure, one dominant metaphor, concise labels, small legends or numbering, and a clear reading path. Keep a McKinsey-like rational, professional, restrained, premium identity while varying slide layouts across the deck. The slide should feel designed, not merely organized: use optical balance, scale contrast, precise margins, micro labels, and one memorable visual decision. Do not turn a secondary motif, footer, icon, callout strip, or module arrangement into a repeated master layout. Avoid default card grids, generic flowchart templates, and slides that only look organized but have no visual concept.",
  "layout_blueprints": [
    {
      "name": "PPT 封面页 / 章节页: 重构标题 + 单一商业隐喻",
      "sections": [
        {"position": "top", "count": 1, "labels": ["完整标题 / 英文分类标签 / 年份或编号"]},
        {"position": "center", "count": 1, "labels": ["giant reconstructed core word"]},
        {"position": "inside typography", "count": 1, "labels": ["one dominant metaphor fused into typography"]},
        {"position": "left and right edge", "count": 3, "labels": ["起点词", "终点词", "价值词"]},
        {"position": "optional bottom or side", "count": 1, "labels": ["short takeaway only when useful"]}
      ]
    },
    {
      "name": "PPT 关键观点页: 字体结构 + 咨询报告系统",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["small complete title system"]},
        {"position": "top-right", "count": 4, "labels": ["STRATEGY", "INSIGHT", "REPORT COVER", "2026"]},
        {"position": "center 70%", "count": 1, "labels": ["large typographic architecture"]},
        {"position": "background", "count": 1, "labels": ["thin grid, nodes, coordinates, hairline rules"]},
        {"position": "optional edge metadata", "count": 3, "labels": ["CLARITY", "STRUCTURE", "IMPACT or slide-specific tags"]}
      ]
    },
    {
      "name": "PPT 分析页: 核心结构 + 左右辅助模块",
      "sections": [
        {"position": "top", "count": 1, "labels": ["title, subtitle, classification tags"]},
        {"position": "center", "count": 1, "labels": ["core flow / matrix / system / funnel / value chain"]},
        {"position": "left", "count": 2, "labels": ["background insight", "key variable"]},
        {"position": "right", "count": 2, "labels": ["risk or constraint", "opportunity or action"]},
        {"position": "optional bottom or right rail", "count": 1, "labels": ["1-3 concise conclusions when needed"]}
      ]
    },
    {
      "name": "PPT 框架页: 矩阵 / 坐标 / 路线图",
      "sections": [
        {"position": "top", "count": 1, "labels": ["complete analytical title and short subtitle"]},
        {"position": "main area", "count": 1, "labels": ["2x2 matrix / coordinate map / roadmap"]},
        {"position": "inside structure", "count": 4, "labels": ["category", "priority", "risk", "opportunity"]},
        {"position": "side rail", "count": 1, "labels": ["methodology notes and legend"]},
        {"position": "optional bottom or side note", "count": 1, "labels": ["executive implication when needed"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "custom typographic reconstruction, thin rules, precision grid, small nodes, coordinates, occasional target marks, crosshair marks, measurement lines, path lines, subtle vanishing rays, restrained arrows, faint perspective, variable report metadata, small numbering, minimal business diagrams, restrained chart fragments, one dark emphasis area when analytically necessary, paper grain, light print texture, subtle shadows, small legends, micro annotations",
    "avoid": "ordinary big title, no title reconstruction, no visual metaphor, disconnected metaphor and text, unrelated background decoration, generic PPT template, default rounded card grid, repeated decorative motif across all slides, repeated header/footer treatment across all slides, repetitive icon rows, icon-heavy modules, business people icons, handshake icons, cartoon characters, robot avatars, sci-fi blue-purple background, uncontrolled complex infographic, content with no hierarchy, overly thick or ornate typography, unreadable main title, overfilled composition, cheap self-media poster feel"
  },
  "rendering_constraints": [
    "The image must feel like a premium top-tier consulting-company visual work, not an official McKinsey template, not an ordinary PPT page, and not a social-media template.",
    "Text must be part of the structure, not just placed on top of the layout.",
    "The slide must have a visible graphic idea: a typographic structure, focal axis, engineered metaphor, or analytical mechanism that would still be recognizable without decorative labels.",
    "If the source title is long, extract a core visual word or phrase and preserve the complete title as smaller text in the header, side title system, or subtitle.",
    "Choose exactly one dominant metaphor for PPT title, divider, and key-message slides; do not stack multiple unrelated metaphors.",
    "For PPT analysis, framework, process, roadmap, and recommendation slides, all modules must unfold around one dominant metaphor and one core analytical structure.",
    "For PPT title, divider, and key-message slides, allow only 1 giant main visual title, 1 complete small title, 2-4 English tags, 1 dominant metaphor, optional short conclusion, and a few thin lines, nodes, numbering, or grid marks.",
    "For PPT title, divider, and key-message slides, forbid 5 or more modules, 3 or more charts, long explanations, dense icons, multiple conclusion boxes, and full process breakdown.",
    "For PPT analysis, framework, process, roadmap, and recommendation slides, use 3-6 main modules, 1 core large structure, 1-2 auxiliary small structures, key data, labels, numbering, annotations, and optional recommendation or implication area.",
    "For PPT analysis, framework, process, roadmap, and recommendation slides, forbid 8 or more modules, too many colors, too many icons, unlayered text, long paragraphs inside every module, and data/graphics without logical relationship.",
    "Use precise thin lines, small labels, grid, nodes, and a restrained light blue-gray-white palette; avoid large areas of heavy dark blue.",
    "Avoid making every page a neat card layout; use scale, negative space, alignment, and typographic reconstruction to create design value.",
    "Across a deck, keep palette, typography, line language, and report discipline consistent, but vary the dominant structure, secondary motif, and module arrangement according to each slide's role.",
    "Even if most decoration is removed, the core structure and business logic must still stand.",
    "Do not invent a real McKinsey logo, client logo, confidential label, proprietary watermark, unrelated logo, or watermark."
  ]
}
```
