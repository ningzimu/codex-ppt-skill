# Installation and Configuration

## One-Sentence Installation

The recommended approach is to send the following sentence directly to Codex and let it install the skill for you:

```text
Please install this codex-ppt skill for me: https://github.com/ningzimu/codex-ppt-skill
```

## Manual Installation for Codex

Run the following command to install the `codex-ppt` skill in Codex's global skills directory:

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent codex \
  --global
```

Restart Codex after installation so the new skill takes effect.

You can also download `codex-ppt-skill-v*.zip` from [GitHub Releases](https://github.com/ningzimu/codex-ppt-skill/releases), extract it, place the included `codex-ppt` folder at `~/.codex/skills/codex-ppt`, and restart Codex.

If you are developing this repository locally, you can symlink the skill directory into the Codex skills directory for real-time testing:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/codex-ppt-skill/skills/codex-ppt ~/.codex/skills/codex-ppt
```

## OpenClaw Installation

```bash
openclaw skills install codex-ppt
```

If you use OpenClaw's skill allowlist, add `codex-ppt` to the allowlist.

## Claude Code / Hermes Agent

Claude Code:

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent claude-code \
  --global
```

Hermes Agent:

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent hermes-agent \
  --global
```

Common destination directories are `~/.claude/skills/codex-ppt` for Claude Code and `~/.hermes/skills/codex-ppt` for Hermes Agent. During local development, you can likewise use a symlink instead of copying the directory.

## Updating the Skill

The recommended approach is to send the following sentence directly to your agent and let it update the skill for you:

```text
Please update the codex-ppt skill to the latest version. The repository is: https://github.com/ningzimu/codex-ppt-skill
```

For a manual update, rerun the installation command above for the relevant agent. This overwrites the installed skill with the latest version. Alternatively, download the latest `codex-ppt-skill-v*.zip` from [GitHub Releases](https://github.com/ningzimu/codex-ppt-skill/releases), extract it, and replace the existing `codex-ppt` directory. Restart the agent after the update.

Updates are safe: runtime configuration such as API keys is stored in `~/.codex-ppt-skill/.env`, while your personal style library is stored in `~/.codex-ppt-skill/references/`. Both are outside the skill installation directory, so updating or reinstalling the skill will not remove them. See the [Releases page](https://github.com/ningzimu/codex-ppt-skill/releases) or the repository's `CHANGELOG.md` for the changes in each version.

## Image-Generation Model Configuration

You cannot use this skill without access to the `gpt-image-2` model. The skill depends heavily on the `gpt-image-2` image-generation model.

## How Do I Know Whether I Have Access to `gpt-image-2`?

- If you subscribe to ChatGPT Plus or Pro, you have access to the `gpt-image-2` model by default. Codex includes a built-in image-generation tool.
- If you access Codex through a third-party relay API, ask it to generate an image containing complex Chinese text, such as a poem written in running script. Check whether the image is generated successfully and whether the Chinese characters contain errors. If everything works, no further configuration is required.
- If neither option works, you will need to purchase access to a relay API that provides the `gpt-image-2` model.

You usually do not need to configure the image-generation model manually. While you use Codex PPT, the AI automatically detects the image-generation backend. If none is available, it will ask you to configure an image-generation backend API and guide you through the setup.

## Notes on Third-Party APIs

This skill includes a script compatible with OpenAI's official image-generation interface. If you use a third-party `gpt-image-2` relay API, try providing:

- The relay service's base URL
  - If the relay service gives an endpoint such as `https://xxx/v1/images/generations`, set the base URL to `https://xxx/v1`.
  - If the relay service already gives `https://xxx/v1`, do not append another layer, which would produce `.../v1/v1`.
  - For official OpenAI, `OPENAI_BASE_URL` can be omitted; the default is the official `https://api.openai.com/v1`.
- The relay service's API key
- The exact `gpt-image-2` model name used by the relay service

After providing this information to the AI, ask it to generate an image. If it still does not work, the relay service may use a custom image-generation scheme that is not fully compatible with the OpenAI image API. Send the relay service's official image-generation documentation to the AI so it can learn the interface and adapt the image-generation script.
