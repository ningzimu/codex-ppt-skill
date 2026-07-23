# FAQ

## Q: Is the Generated Presentation Editable?

No. Codex PPT generates image-based presentations in which every slide is a complete slide image. The visual result is more consistent, but the text, charts, and shapes on a slide cannot be edited individually as they can in a traditional PowerPoint file. After generation, if you need to adjust the content or visuals, the recommended approach is to continue in the same conversation and ask the AI to revise the specific slide.

Unless necessary, do not convert the presentation into an editable format unless you have sufficient Codex credits.

If you need an editable presentation, try [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill) after generation. However, `image-to-editable-ppt-skill` is currently experimental. It currently supports only ChatGPT Plus / Pro subscribers using Codex and does not support other agents. If its results are unstable, wait for future update announcements.

Note: The image-to-editable skill currently consumes a large number of tokens. It is not friendly to Plus users, while Pro users can use it more freely.

## Q: Does It Support Other Agents?

Yes. Codex PPT is a `SKILL.md`-based skill. In addition to Codex, it works with agents that support `SKILL.md`, including Claude Code, OpenClaw, and Hermes Agent.

This skill is developed and tested primarily with Codex, so Codex offers the best compatibility and is recommended.

Different agents have different image-generation capabilities and tool interfaces. Outside Codex, you will usually need to configure `gpt-image-2` or a third-party OpenAI-compatible image-generation API. See [Installation and Configuration](/en/installation.md), and let the AI guide you through setup based on your current environment.

## Q: How Do I Update the Skill to the Latest Version?

Rerun the installation command to overwrite the installed skill with the latest version, or ask your agent to update it for you, then restart the agent. API key configuration and your personal style library are stored outside the skill installation directory and are preserved during updates. See [Installation and Configuration](/en/installation.md) for the commands.

## Q: Why Does the First Sample Slide Look Good While Later Slides Look Worse or Use a Different Style?

This usually means the sample slide's style was not passed consistently to later slides, or the prompts, backend, or sub-agent execution method changed during generation.

Under normal conditions, once a sample slide is approved, later slides should inherit the same visual language, including the color palette, typographic character, layout density, illustration approach, and image-generation backend. If later slides clearly drift, ask the AI to check whether every slide received the sample as a style reference, whether the same image-generation method was recorded and reused, whether a sub-agent switched to another generation method without permission, and whether individual slide prompts are too broad.

Do not regenerate the entire deck. First select one or two slides with obvious drift and ask the AI to regenerate them using the approved sample as a reference. Explicitly require it to "preserve the sample slide's visual style, use the same image-generation backend, and maintain the same layout density."

## Q: What Should I Do If the Generated Presentation Looks Bad?

First confirm that your `gpt-image-2` model can generate images correctly. If the model is unavailable, returns abnormal quality, or a third-party API or relay service does not correctly support `gpt-image-2`, the output quality will be significantly worse.

After confirming that the model works, ask the AI to address specific issues such as inconsistent styling, text that is too small, overcrowded layouts, unattractive colors, or illustrations that do not match the topic. It is best to regenerate one sample slide first and continue with the full deck only after you are satisfied.

## Q: What Should I Do If the Generated Slide Images Are Blurry?

Codex subscribers use the built-in image-generation tool by default. Its generated images have a relatively low resolution, which currently cannot be specified manually. For higher-resolution images, use the `gpt-image-2` API instead—the API/CLI fallback—and configure the API key, base URL, and model name. See [Installation and Configuration](/en/installation.md).

With the API/CLI fallback, the script defaults to 2K resolution in a 16:9 landscape format. If the image is still blurry, especially on slides with substantial text, ask the AI to generate it at 4K resolution.

## Q: Why Confirm the Outline First?

Because most presentation rework comes from structural problems. Confirming the slide count, titles, order, and key points first prevents you from discovering that the content direction is wrong only after every image has been generated.

## Q: Why Generate a Sample Slide First?

The sample slide establishes the visual baseline for the complete presentation. After it is approved, later slides can inherit the same color palette, typographic character, density, and visual language.

## Q: Do I Need to Configure an API Key in Codex?

If Codex's built-in image-generation tool is available, you usually do not need to configure an API key. You need to configure `OPENAI_API_KEY`, an optional `OPENAI_BASE_URL`, and a model name only when you choose the API/CLI fallback.

## Q: Can I Insert Original Paper Figures or Architecture Diagrams?

Yes. During the outline stage, specify the slide number and purpose for each image, and state whether it is strict source material or a style reference. For paper figures, experiment result charts, screenshots, and architecture diagrams, preserve the original information, labels, axes, values, and arrow relationships wherever possible.

## Q: What Should I Do If One Slide Looks Bad?

Revise only that slide first. Tell the agent the specific issue—for example, the text is too small, the hierarchy is unclear, the color palette is unsuitable, the visual is overcrowded, or a concept is represented inaccurately.

## Q: Can I Save My Own Styles?

Yes. Give the agent presentation screenshots, a PDF, or a complete presentation that you like and ask it to analyze the style. Once you are satisfied with the generated result, ask the agent to save the style to your personal style library at `~/.codex-ppt-skill/references/`. The library is stored outside the skill installation directory, so it is preserved when the skill is updated or reinstalled. If a personal style shares a name with a built-in style, the personal style takes precedence. See [Styles and Personal Style Library](/en/styles.md).
