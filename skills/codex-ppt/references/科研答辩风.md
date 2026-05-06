# 科研答辩风

**适用场景:**
- 科研项目申报答辩
- 基金申请与重点专项汇报
- 中期检查与结题验收
- 论文开题、预答辩和毕业答辩
- 课题分解、技术路线、研究基础、风险分析和预期成果展示
- 高校、科研院所、实验室和产学研项目的正式汇报

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "科研答辩风",
  "best_for": "科研项目申报、基金答辩、课题中期检查、结题验收、论文答辩和实验室阶段性成果汇报等正式学术场景",
  "visual_direction": "formal Chinese academic research defense deck, authoritative but adaptable project presentation, evidence-driven layout, structured scientific diagrams, concise conclusions, and disciplined visual hierarchy",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "clean white #FFFFFF with subtle light gray #F5F7FA content background",
    "composition": "structured academic slide with title area, evidence area, explanatory diagrams, tables, callouts, or conclusion area chosen according to slide content",
    "density": "medium-high to high information density, suitable for serious academic defense, while keeping clear reading order and alignment"
  },
  "color_palette": {
    "primary": "deep academic blue #003F8F or #004A9F",
    "secondary": "research blue #0B5CAD and pale blue #EAF2FF",
    "accent": "formal red #B5121B or #C00000 used sparingly for key conclusions, risks, breakthroughs, and emphasized phrases",
    "neutral": "black #111111, dark gray #333333, light border gray #D8DEE8, pale table fill #F3F6FA",
    "optional": "muted gold #F3DFA2 only for cover or major title emphasis",
    "rule": "prefer blue for structure and red for critical arguments, but adapt emphasis to the topic and source material; avoid colorful decorative palettes, heavy gradients, playful icons, and casual illustration styles"
  },
  "typography": {
    "title": "bold Chinese sans-serif, large, formal, report-like, left aligned",
    "section_labels": "white bold Chinese text on deep blue blocks or arrow labels",
    "body": "dense but readable Chinese sans-serif, mostly black, key phrases in red bold",
    "tables": "compact academic table typography with clear header rows and restrained category emphasis",
    "text_quality": "Chinese text must be exact, readable, non-garbled, and suitable for formal research defense"
  },
  "page_system": {
    "header": "usually use a clear title area with optional section number and optional project/institution mark; cover pages and divider pages may use a different composition",
    "divider": "optional thin horizontal rule, blue segment, or subtle academic separator when it helps hierarchy",
    "body": "structured content area with light borders, module labels, evidence cards, diagrams, or tables as needed",
    "footer": "optional one-sentence takeaway strip or conclusion line when the slide needs a strong final claim",
    "logo_rule": "use only user-provided logos or a neutral text placeholder such as 项目标识; do not invent real institution logos or unrelated brand names"
  },
  "layout_patterns": [
    "research background with literature timeline, policy/report evidence, and problem statement",
    "research status with left-side evidence collage and right-side challenge comparison",
    "topic decomposition with multi-column task chain and right-side vertical research path",
    "research content page with three evidence cards and supporting mechanism images",
    "core objective page with arrow label, large target sentence, technical route, and mechanism diagram",
    "platform support page with equipment photos, prior achievements, certificates, and bullet evidence",
    "risk analysis four-quadrant grid with risk type, risk judgment, mitigation evidence, and bottom conclusion",
    "expected outcomes table with category, measurable indicators, and assessment method"
  ],
  "layout_usage_rule": "Use these patterns as flexible starting points, not mandatory templates. Keep the deck's academic tone, disciplined hierarchy, restrained palette, and evidence-first logic, while adapting the body layout to each slide's role and source material.",
  "layout_blueprints": [
    {
      "name": "研究背景 / 研究现状",
      "sections": [
        {"position": "top", "count": 1, "labels": ["one-sentence problem or status statement with optional emphasized phrases"]},
        {"position": "left large area", "count": 1, "labels": ["literature timeline / technical evolution / evidence collage"]},
        {"position": "right column", "count": 1, "labels": ["report evidence / industry challenge / application pain point"]},
        {"position": "bottom", "count": 1, "labels": ["optional takeaway conclusion"]}
      ]
    },
    {
      "name": "课题分解 / 技术路线",
      "sections": [
        {"position": "top", "count": 1, "labels": ["project objective sentence"]},
        {"position": "middle", "count": 3, "labels": ["课题一", "课题二", "课题三"]},
        {"position": "left side", "count": 2, "labels": ["应用基础研究", "关键任务核心内容"]},
        {"position": "right side", "count": 4, "labels": ["性能研究", "应用验证", "深入探索", "关系研究"]},
        {"position": "bottom", "count": 1, "labels": ["chain-summary sentence"]}
      ]
    },
    {
      "name": "核心目标 / 研究目标",
      "sections": [
        {"position": "top-left", "count": 1, "labels": ["blue arrow label: 核心目标 or 研究目标"]},
        {"position": "top-right", "count": 1, "labels": ["target sentence with key phrases"]},
        {"position": "middle", "count": 2, "labels": ["content detail box 1", "content detail box 2"]},
        {"position": "bottom", "count": 3, "labels": ["method diagram", "mechanism image", "application validation image"]},
        {"position": "bottom-center", "count": 1, "labels": ["technical route statement"]}
      ]
    },
    {
      "name": "研究内容 / 证据展示",
      "sections": [
        {"position": "top", "count": 1, "labels": ["research content sentence with key variables"]},
        {"position": "middle", "count": 3, "labels": ["研究内容一", "研究内容二", "研究内容三"]},
        {"position": "inside each card", "count": 3, "labels": ["blue title bar", "scientific figure or chart", "short evidence caption"]},
        {"position": "bottom", "count": 1, "labels": ["integrated conclusion or mechanism statement"]}
      ]
    },
    {
      "name": "风险分析",
      "sections": [
        {"position": "top", "count": 1, "labels": ["risk control thesis statement"]},
        {"position": "middle grid", "count": 4, "labels": ["技术风险", "安全风险", "性能风险", "管理风险"]},
        {"position": "bottom", "count": 1, "labels": ["supporting scientific images and final conclusion"]}
      ]
    },
    {
      "name": "预期成果 / 考核指标",
      "sections": [
        {"position": "top", "count": 3, "labels": ["高价值", "全覆盖", "可量化"]},
        {"position": "middle", "count": 1, "labels": ["large table: 类别 / 具体指标 / 考核方式"]},
        {"position": "left table column", "count": 4, "labels": ["理论创新与知识产权", "技术突破与材料开发", "人才培养与学术影响", "长远发展潜力"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "academic tables, blue arrow labels, restrained red emphasis text, flow arrows, technical route diagrams, paper figure collages, mechanism diagrams, laboratory or equipment photos, certificates, report thumbnails, structured grids, light shadows",
    "avoid": "minimalist empty pages, marketing hero layouts, cartoon illustrations, decorative gradients, random icons, playful stickers, excessive whitespace, vague stock photos, fruits, animals, people cutouts, unrelated decorative objects"
  },
  "writing_style": {
    "sentence_patterns": [
      "系统研究……并揭示……机制",
      "构建……体系，实现……精准调控",
      "围绕……形成完整闭环研究链条",
      "通过……验证……性能",
      "可有效规避或化解……风险",
      "所有成果均设置具体、可测量指标"
    ],
    "emphasis_rule": "Use red bold text selectively for the scientific problem, key breakthrough, risk judgment, measurable outcome, or page-level conclusion; do not over-highlight every sentence."
  },
  "rendering_constraints": [
    "The slide must look like a serious Chinese academic research defense deck, not a commercial pitch deck.",
    "Keep a recognizable academic presentation system across slides, but do not force every page into the same header or grid.",
    "Every page should have a clear top-to-bottom or left-to-right reading order.",
    "Use high-density scientific content, but keep text blocks aligned and readable.",
    "Use blue structural labels and red conclusion phrases when useful, without making the page mechanically blue-red.",
    "Do not include fruit, people, animals, random objects, fictional brand marks, or unrelated decorative icons.",
    "No watermark, no unrelated logo, no fake real institution logo, no extra slide number unless requested."
  ]
}
```
