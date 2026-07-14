# Codex PPT Skill 说明文档

Codex PPT 是一个面向 Codex 的 PPT 生成 skill，也可在 Claude Code、OpenClaw、Hermes Agent 等支持 `SKILL.md` 的 agent 中使用。它把文章、报告、论文、课程笔记或粗略想法转换成图片式演示文稿：先规划大纲和视觉风格，再逐页生成完整幻灯片图片，最后组装成 `.pptx` 文件。

## 这套文档怎么读

如果你只是想快速上手，先看[快速开始](quickstart.md)。

如果你要安装、配置模型或接入不同 agent，再看[安装与配置](installation.md)。

如果你想理解完整生成过程、确认点和质量控制，再看[标准工作流](workflow.md)。

如果你已经在使用，并且遇到了问题，请查阅[常见问题](faq.md)。

## 子页面

- [快速开始](quickstart.md)：第一次使用时的最短路径、示例命令和产物说明。
- [设计理念](design.md)：为什么采用图片式 PPT、阶段确认和双 skill 分工的设计。
- [安装与配置](installation.md)：Codex、OpenClaw、Claude Code、Hermes Agent 的安装与更新方式，以及 API/CLI fallback 配置。
- [标准工作流](workflow.md)：从大纲确认、风格确认、后端确认、样张确认到整套生成和组装的完整流程。
- [风格与个人风格库](styles.md)：12 种内置风格预览、仿照参考材料复刻风格，以及把满意的风格保存到个人风格库长期复用。
- [常见问题](faq.md)：可编辑性、API key、样张、素材插入、单页修改等高频问题。
- [示例提示词](prompts.md)：文章转 PPT、论文答辩、管理层汇报、指定风格、修改单页等可直接复用的提示词。

## 特色功能

- 图片式 PPT 生成：每一页都是完整 16:9 幻灯片图片，适合追求强视觉表达和统一风格的场景。
- 分阶段确认流程：先确认大纲、视觉风格、图片生成方式和样张，再生成整套 PPT，减少返工。
- 内置 12 种风格：包括手绘技术解释风、科研答辩风、清爽专业风、麦肯锡风格、党政红风格、教学课件风等方向，参见[风格与个人风格库](styles.md)。
- 支持参考材料仿风格：可以阅读用户提供的 PPT、PDF 或截图，理解每页图片风格后再仿照生成。
- 可沉淀个人风格库：满意的风格可以保存到 `~/.codex-ppt-skill/references/`，存放在 skill 安装目录之外，更新 skill 不丢失，后续制作直接按名字复用。
- 支持指定素材入页：可以把论文原图、实验结果图、架构图或截图指定到具体页面中使用。
- 支持多 agent 环境：除 Codex 外，也可在 Claude Code、OpenClaw、Hermes Agent 等支持 `SKILL.md` 的 agent 中使用。
- 自动组装 PowerPoint：生成 `outline.md`、每页图片、`speech.md`，并最终组装为 `.pptx` 文件。
- 支持通过第三方 API 使用文本模型和 `gpt-image-2` 生图模型。
- 支持配套生成 PPT 演讲稿，默认会自动插入 PPT 备注页。
- 支持生成后针对特定不满意的页面做定向修改，参见[常见问题](faq.md)。

## 适用场景

- 技术文章转分享 PPT
- 论文、研究报告或调研材料转演示稿
- 课程笔记转课件
- 产品介绍、商业汇报、项目总结
- 科研答辩、项目申报、中期检查、结题验收
- 需要统一视觉语言的图片式演示文稿

## 关键提醒

Codex PPT 生成的是图片式 PPT：视觉一致性强，但页面里的文字、图表和形状不能像传统 PPT 那样逐项编辑。

如果你需要进一步转换成可编辑 PPT，可以在生成后再使用 [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)。

如果你没有 `gpt-image-2` 生图模型的使用权限，则无法使用该 skill，参见[安装与配置](installation.md)。

## 相关链接

- GitHub 仓库：https://github.com/ningzimu/codex-ppt-skill
- ClawHub 页面：https://clawhub.ai/ningzimu/codex-ppt
- 使用案例展示区：https://github.com/ningzimu/codex-ppt-skill/issues/34
- 可编辑 PPT 转换 skill：https://github.com/ningzimu/image-to-editable-ppt-skill
