# 党政红风格

**适用场景:**
- 党政机关工作汇报、专题学习与会议材料
- 政策宣讲、党建活动、年度总结与重点工作部署
- 国企、事业单位和公共服务机构的正式汇报

**GPT-Image-2 风格 Brief:**
```json
{
  "type": "16:9 full-slide PowerPoint image",
  "style_name": "党政红风格",
  "best_for": "党政机关、国企和事业单位的工作汇报、政策宣讲、党建学习、年度总结与重点工作部署",
  "visual_direction": "solemn, authoritative, and optimistic Chinese public-sector presentation with a recognizable Chinese-red identity, restrained gold accents, strong Chinese typography, and a visual expression shaped by the subject rather than a fixed ceremonial layout",
  "canvas": {
    "aspect_ratio": "16:9",
    "background": "choose red, warm ivory, a restrained gradient, a relevant photograph, or a subtle abstract treatment according to the page role and subject; any landscape, architecture, ribbon, skyline, or cultural motif is optional and must serve the content rather than become a default background",
    "composition": "formal and balanced with a prominent title hierarchy and disciplined alignment; allow centered, asymmetric, image-led, modular, or spacious compositions when they better express the content",
    "density": "medium information density with controlled whitespace, clear reading order, and enough supporting text or evidence to make each page useful"
  },
  "color_palette": {
    "primary": "Chinese red #C41E3A for main titles, structural emphasis, and key labels",
    "secondary": "deep red #9E1530 for contrast and warm ivory #FFF9F2 for the main canvas",
    "accent": "restrained matte gold #D6A84B and warm amber #E9A11B for icons, connectors, and small title ornaments",
    "neutral": "ink black #262626, dark gray #4A4A4A, pale warm gray #F3EEE7",
    "rule": "use Chinese red to establish authority and gold as a restrained accent. Balance red, warm ivory, and neutral space according to page role; avoid glitter, glossy gradients, and festive red-and-gold decoration"
  },
  "typography": {
    "title": "large bold Microsoft YaHei or Source Han Sans style Chinese sans-serif, visually strong, dignified, and immediately noticeable",
    "body": "Microsoft YaHei or Source Han Sans style Chinese sans-serif, concise, highly readable, and aligned to a strict grid",
    "labels": "bold white or dark-red text on restrained red or pale-gold blocks",
    "text_quality": "all Chinese text must be exact, fully legible, non-garbled, and suitable for formal government reporting"
  },
  "title_system": {
    "consistency_rule": "Keep the title hierarchy, typeface, weight, color logic, and spacing consistent across slides of the same page type.",
    "cover": "Use a prominent, dignified title treatment that may be centered, offset, or integrated with a relevant visual according to the composition.",
    "section_divider": "Use a concise title and a clear transition in scale, color, whitespace, or imagery without requiring a fixed navigation bar or ornament.",
    "content_slide": "Keep the page topic immediately recognizable, but align the title with the composition and information structure; centered and left-aligned treatments are both valid.",
    "flexibility": "Treat the title system as a hierarchy and consistency rule, not a fixed arrangement. Do not require a navigation strip, centered title, gold separator, numbering style, or identical decoration on every slide."
  },
  "layout_patterns": [
    "cover or opener with a dominant title and a subject-relevant photographic, illustrative, architectural, landscape, or abstract visual",
    "section divider with a concise statement and a clear transition created through scale, whitespace, color, or imagery",
    "content explanation organized around the most important relationship, argument, process, comparison, or evidence",
    "work deployment or policy interpretation page whose modules, sequence, and emphasis follow the source content",
    "achievement or data page combining key figures, charts, images, and evidence-based captions as needed",
    "summary or closing page that reinforces the central message with a strong but restrained visual conclusion"
  ],
  "layout_usage_rule": "Keep the red-led identity, typography, and formal tone consistent while varying title placement, background treatment, imagery, information structure, and whitespace by page purpose. Do not force every slide into the same grid, module count, title position, or decorative motif; use lighter backgrounds when they improve readability.",
  "layout_blueprints": [
    {
      "name": "封面 / 开场",
      "sections": [
        {"position": "primary visual field", "count": 1, "labels": ["prominent title and concise supporting information"]},
        {"position": "supporting field", "count": 1, "labels": ["optional subject-relevant photograph, illustration, architecture, landscape, or abstract visual"]}
      ]
    },
    {
      "name": "信息阐释 / 工作部署",
      "sections": [
        {"position": "title zone", "count": 1, "labels": ["clear page topic or guiding statement"]},
        {"position": "main content field", "count": 1, "labels": ["the dominant argument, relationship, process, comparison, or evidence structure"]},
        {"position": "supporting field", "count": 1, "labels": ["supporting text, data, images, or callouts selected according to the source"]}
      ]
    },
    {
      "name": "成果 / 总结",
      "sections": [
        {"position": "primary message field", "count": 1, "labels": ["central conclusion, achievement, or call to action"]},
        {"position": "evidence field", "count": 1, "labels": ["figures, chart, comparison, documentary image, or concise supporting points as appropriate"]}
      ]
    }
  ],
  "visual_elements": {
    "allowed": "content-relevant photography, illustrations, landscapes, architecture, skylines, public-service scenes, people, abstract ribbons or color fields, restrained red-and-gold accents, formal information modules, simple icons, clean charts, and subtle cultural motifs; none of these elements is mandatory",
    "avoid": "repeating the same landmark or ornament without content justification, invented or inaccurate official marks, excessive ceremonial decoration, thick shadows, glossy 3D text, glitter, festival or wedding motifs, cartoon styling, unrelated stock imagery, and decorative elements that compete with the message"
  },
  "image_treatment": {
    "photos": "use relevant and credible documentary, landscape, architectural, public-service, or institutional imagery; it may be full-bleed, cropped, framed, or integrated with a restrained red treatment, but avoid heavy filters that obscure the subject",
    "screenshots": "place inside clean warm-white frames with short source labels and no ornamental clutter",
    "charts": "use red as the primary series, gold for one key highlight, and neutral gray for comparison; keep labels direct and readable",
    "illustrations": "choose a flat, graphic, painterly, or restrained symbolic treatment according to the subject; do not impose a fixed landmark, ribbon, skyline, or landscape motif",
    "official_symbols": "use a party emblem, national emblem, flag, seal, or other official symbol only when the content genuinely requires it and an accurate, authorized source asset is available; never invent, approximate, or redesign official symbols"
  },
  "rendering_constraints": [
    "The slide must look like a formal Chinese government or public-sector report, not a festival poster or commercial advertisement.",
    "Use large, dignified Chinese sans-serif typography resembling Microsoft YaHei or Source Han Sans.",
    "Follow a consistent title system across slides of the same page type, while allowing cover, section-divider, and content-slide variants.",
    "Let the page role and source content determine title placement, background, imagery, module count, and composition.",
    "Do not force a navigation strip, centered title, gold separator, landscape, Great Wall, skyline, ribbon, or other specific motif onto every slide.",
    "Use Chinese red #C41E3A as the main red and gold as a restrained supporting accent.",
    "Keep gold restrained and matte; do not use glossy metallic or embossed 3D text.",
    "Use exact readable Chinese text and a clear top-to-bottom or left-to-right hierarchy.",
    "Do not invent, approximate, or redesign official marks, government logos, party emblems, national emblems, seals, flags, or institutional names.",
    "No watermark and no unrelated logo."
  ]
}
```
