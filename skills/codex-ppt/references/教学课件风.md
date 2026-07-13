# 教学课件风

**适用场景:**
- 高校课程、专题讲座与课堂教学
- 技术培训、知识科普与专业能力建设
- 概念讲解、体系梳理、案例分析与研究进展介绍
- 需要同时呈现文字、图解、图片和数据的教学型演示

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "教学课件风",
  "best_for": "高校课程、专题讲座、技术培训、知识科普、概念讲解、体系梳理、案例分析和研究进展介绍",
  "visual_direction": "clear and credible academic courseware with structured knowledge communication, evidence-supported explanation, discipline-appropriate visuals, and a professional classroom tone shaped by the lesson rather than a fixed technical template",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "white or very light cool gray with restrained pale-blue structural accents",
    "composition": "structured teaching slide with a clear title hierarchy and a content-driven combination of text, images, diagrams, charts, formulas, source material, annotations, or comparisons selected according to the lesson objective",
    "density": "balanced teaching density: substantial enough to support explanation, but never sparse, paragraph-heavy, or crowded; use strong grouping, alignment, and readable whitespace"
  },
  "color_palette": {
    "primary": "deep academic navy #0B2E6D and clear blue #1769AA",
    "secondary": "light blue #EAF3FB and cool gray #F3F6F9",
    "accent": "choose a small set of restrained auxiliary colors according to the subject matter, source material, and semantic categories",
    "neutral": "ink black #1F2937, body gray #4B5563, border gray #D7E0EA",
    "rule": "use the blue system to establish the teaching structure; select auxiliary colors only when the content needs semantic distinction, then apply them consistently rather than decoratively"
  },
  "typography": {
    "title": "large bold Chinese sans-serif resembling Microsoft YaHei or Source Han Sans, usually dark navy, concise and immediately readable",
    "body": "compact but readable Chinese sans-serif with clear indentation and short explanatory phrases",
    "labels": "bold short labels with strong contrast, used when hierarchy or semantic categories need clarification rather than as mandatory card decoration",
    "text_quality": "all Chinese text, Latin terms, formulas, units, and data labels must be exact, readable, and non-garbled"
  },
  "title_system": {
    "consistency_rule": "Keep title typeface, weight, color logic, alignment, and spacing consistent across slides of the same page type.",
    "cover": "May combine a large course title with one or more subject-relevant visuals and concise presenter or course information; choose the visual structure according to the discipline and topic.",
    "section_divider": "May use a concise section title with stronger whitespace and a restrained academic cue.",
    "content_slide": "Keep the page topic immediately recognizable, but let title alignment, supporting accents, and surrounding composition adapt to the teaching content.",
    "closing": "Use a concise acknowledgement or closing statement together with a subject-relevant visual or summary echo; keep the page informative and visually complete rather than leaving a nearly empty text-only slide.",
    "flexibility": "Treat the title system as a consistency guide rather than a fixed template. Do not force every slide into the same header, rule, alignment, or decorative treatment."
  },
  "layout_patterns": [
    "course cover combining a clear title hierarchy with subject-relevant visual material and concise course information",
    "concept explanation using the most suitable combination of diagrams, images, definitions, formulas, source excerpts, or annotated examples",
    "sequence, process, development, or causal explanation with a clear viewing order",
    "comparison or relationship page whose structure follows the concepts being contrasted or connected",
    "case, text, artwork, experiment, event, or application analysis supported by relevant evidence and explanation",
    "overview or synthesis page organizing examples, themes, findings, or knowledge relationships",
    "knowledge summary using a concise framework, conclusion, or takeaway",
    "closing or acknowledgement page combining a short closing statement with a restrained subject-relevant visual"
  ],
  "layout_usage_rule": "Choose the layout that best supports the teaching objective and viewing sequence. Every slide should combine meaningful visual explanation with readable text; use one strong visual or several complementary photographs, diagrams, charts, maps, formulas, documents, artworks, screenshots, or annotated examples according to the discipline and content. Keep the visual language coherent without forcing every page into cards, equal columns, or one repeated composition.",
  "layout_blueprints": [
    {
      "name": "概念 / 知识讲解",
      "sections": [
        {"position": "title area", "count": 1, "labels": ["lesson question or core concept"]},
        {"position": "primary teaching field", "count": 1, "labels": ["the most suitable visual and explanatory structure for the concept"]},
        {"position": "supporting field", "count": 1, "labels": ["definitions, examples, evidence, annotations, or implications as needed"]}
      ]
    },
    {
      "name": "过程 / 关系讲解",
      "sections": [
        {"position": "title area", "count": 1, "labels": ["process, development, comparison, or relationship topic"]},
        {"position": "primary relationship field", "count": 1, "labels": ["sequence, cause, contrast, hierarchy, interaction, or transformation"]},
        {"position": "supporting field", "count": 1, "labels": ["conditions, examples, evidence, annotations, or summary as needed"]}
      ]
    },
    {
      "name": "案例 / 材料 / 证据",
      "sections": [
        {"position": "context field", "count": 1, "labels": ["case, text, event, artwork, experiment, or application context"]},
        {"position": "evidence field", "count": 1, "labels": ["relevant visual material, source excerpt, data, observations, or comparison"]},
        {"position": "teaching conclusion field", "count": 1, "labels": ["interpretation, lesson learned, or takeaway"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "discipline-relevant photographs, artworks, archival documents, source excerpts, maps, formulas, tables, charts, diagrams, screenshots, multi-image evidence groups, annotated images, timelines, relationship structures, restrained icons, and subtle academic background texture; cards and grids may be used when they genuinely clarify the material but are not the default",
    "avoid": "text-only pages, purely decorative illustration, repetitive card grids, default three-column layouts, generic AI-looking imagery, unsupported futuristic or technical styling, random 3D icons, playful stickers, excessive gradients, heavy shadows, glossy elements, inconsistent icon styles, dense ungrouped text, unrelated stock imagery, and ornamental layouts that weaken the teaching sequence"
  },
  "image_treatment": {
    "photos": "use relevant and credible course or case images as evidence, crop them consistently, and pair them with concise explanatory labels; one page may use a single main image or several complementary images when they explain different aspects of the topic",
    "screenshots": "place inside clean frames and preserve important interface details, annotations, and labels",
    "charts": "use the palette semantically, retain accurate axes and values, and emphasize the comparison or trend being taught",
    "illustrations": "choose diagrams, maps, explanatory drawings, documentary collage, symbolic graphics, or other illustration treatments appropriate to the discipline and lesson; avoid decorative scenes that do not teach anything",
    "discipline_materials": "treat formulas, artworks, historical documents, literary excerpts, medical images, scientific figures, and other subject-specific materials as valid visual evidence when relevant and accurately represented"
  },
  "rendering_constraints": [
    "The slide must look like professional academic courseware, not a marketing pitch deck.",
    "Prioritize teaching sequence, conceptual clarity, and readable evidence over visual decoration.",
    "Every slide must contain both meaningful visual content and readable text; visuals should explain, demonstrate, compare, or provide evidence rather than merely decorate.",
    "Visual content may include photographs, diagrams, charts, maps, formulas, artworks, documents, source excerpts, screenshots, or other discipline-appropriate material; it does not always mean a decorative illustration.",
    "Avoid both underfilled slides and long blocks of prose. Convert dense explanations into diagrams, image groups, structured labels, or concise teaching points.",
    "Keep related information visibly grouped and maintain a clear viewing order.",
    "Avoid tiny text; split or simplify content when it cannot remain readable at presentation distance.",
    "Use semantic accent colors consistently across the deck.",
    "Do not force every slide into repeated cards, equal columns, a fixed module count, or an identical information grid.",
    "Avoid an obvious AI-generated look: no fabricated text inside images, implausible photo details, generic glowing technology effects, random decorative objects, or repetitive template-like compositions.",
    "Do not invent university, school, laboratory, company, or course logos; use only user-provided identity assets.",
    "Do not inherit topics, examples, imagery, terminology, or organizations from a style reference unless they are required by the source content.",
    "No watermark and no unrelated logo."
  ]
}
```
