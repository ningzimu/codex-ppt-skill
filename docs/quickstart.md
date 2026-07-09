# 快速开始

## 适合谁

这页给第一次使用 Codex PPT 的人看。你只需要准备一份文章、报告、大纲、论文或课程笔记，然后让 agent 使用 `codex-ppt` skill 生成 PPT。

## 最短使用方式

先安装 skill，参见[安装与配置](installation.md)。然后，在 Codex 里直接使用这个 skill 进行 PPT 制作。

```text
请使用 codex-ppt skill，把 /path/to/article.md 做成 10 页左右的中文 PPT。
```

如果你已经知道风格和用途，可以写得更具体：

```text
请使用 codex-ppt skill，把这篇技术文章做成 12 页中文分享 PPT。风格偏清爽专业，适合内部技术分享；第 5 页必须使用我提供的架构图，第 8 页必须保留实验结果图。
```

## 第一次使用建议

- 先让 agent 生成 `outline.md`，确认页数、标题和每页要点。
- 不要跳过样张确认。先看一页效果，再批量生成整套 PPT。
- 如果某一页不满意，优先只改那一页，不要整套重做。
- 如果有参考 PPT、截图或 PDF，先让 agent 分析风格，再生成新 PPT。

## 生成结果

最终通常会得到：

- `outline.md`：PPT 大纲
- `origin_image/slide_XX.png`：每页正式图片
- `speech.md`：每页演讲备注
- `{PPT名称}.pptx`：最终 PowerPoint 文件
