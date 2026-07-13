# 风格与个人风格库

Codex PPT 的视觉风格来自两个地方：随 skill 发布的**内置风格**，以及存放在你本机、更新 skill 也不会丢失的**个人风格库**。

## 内置风格

skill 内置 12 种风格参考，不会写提示词也可以直接从这里开始。制作 PPT 时直接说风格名即可，例如：

```text
请使用 codex-ppt skill，把这份材料做成 10 页 PPT，使用内置的「手绘技术解释风」。
```

| 清爽专业风 | 创意杂志风 |
| --- | --- |
| ![清爽专业风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/clean-professional.png) | ![创意杂志风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/creative-magazine.png) |
| 电子墨水杂志风 | 数据仪表盘风 |
| ![电子墨水杂志风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/e-ink-magazine.png) | ![数据仪表盘风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/data-dashboard.png) |
| 复古扁平插画风 | 手绘技术解释风 |
| ![复古扁平插画风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/retro-flat-illustration.png) | ![手绘技术解释风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-technical.png) |
| 手绘白板风 | 温暖手工风 |
| ![手绘白板风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-whiteboard.png) | ![温暖手工风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/warm-handmade.png) |
| 科研答辩风 | 麦肯锡风格 |
| ![科研答辩风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/scientific-defense.png) | ![麦肯锡风格](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/mckinsey-style.png) |
| 党政红风格 | 教学课件风 |
| ![党政红风格](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/party-government-red.png) | ![教学课件风](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/teaching-courseware.png) |

风格是一套视觉系统（配色、字体气质、版式密度、插画语言），不是固定模板；同一套风格下，每页版式会根据内容角色变化，不会每页长得一样。

## 仿照参考材料的风格

如果内置风格不满足需求，可以提供自己喜欢的风格参考：一张截图、多张截图，或完整 PPT/PDF。建议先让 agent 分析参考材料的配色、版式、字体和视觉元素，再按这个风格生成新 PPT：

```text
请使用 codex-ppt skill 生成 PPT。视觉风格参考我上传的这份 PDF。请详细阅读我提供材料中的每一页图片，确保了解其风格，然后仿照其风格进行生成。
```

注意：默认只仿风格、不复用内容。除非你明确要求，参考材料里的文字和数据不会被搬进新 PPT。

## 个人风格库

如果生成的 PPT 风格你很满意，无论是调出来的自定义风格，还是从参考材料复刻的风格，都可以让 agent 保存下来，以后直接复用：

```text
这套 PPT 的视觉风格我很喜欢，请保存到个人风格库。
```

保存机制的几个要点：

- **存放位置**：个人风格库位于 `~/.codex-ppt-skill/references/`（可通过 `CODEX_PPT_HOME` 环境变量改变位置），在 skill 安装目录**之外**。更新或重新安装 skill 时，个人风格不会被覆盖或丢失。
- **自动发现**：保存后无需任何登记。之后制作 PPT 选择风格时，agent 会自动扫描个人风格库，把你的风格和内置风格一起列出来。
- **同名优先**：如果个人风格和某个内置风格同名，以你的个人风格为准。你也可以利用这一点定制内置风格：保存一个同名的调整版即可覆盖默认效果。
- **复用方式**：以后直接说风格名即可，例如「用『深色数据科技风』生成这份 PPT」。

生成完成后，如果这套 deck 用的是自定义或调整过的风格，agent 也会在最终报告里主动提示你可以保存。使用未修改的内置风格时无需重复保存。

## 相关页面

- [示例提示词](prompts.md)：指定内置风格、仿照参考风格、保存风格的完整提示词。
- [常见问题](faq.md)：风格跑偏、页面不满意时的处理方式。
