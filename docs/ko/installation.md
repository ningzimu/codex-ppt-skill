# 설치 및 설정

## 한 문장으로 설치하기

아래 문장을 Codex에 직접 보내 설치를 맡기는 것을 권장합니다.

```text
이 codex-ppt skill을 설치해 주세요. 링크: https://github.com/ningzimu/codex-ppt-skill
```

## Codex 수동 설치

명령줄에서 다음 명령을 실행해 `codex-ppt` skill을 Codex의 전역 skills 디렉터리에 설치합니다.

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent codex \
  --global
```

설치 후 Codex를 재시작하면 새 skill이 적용됩니다.

[GitHub Releases](https://github.com/ningzimu/codex-ppt-skill/releases)에서 `codex-ppt-skill-v*.zip`을 다운로드해 압축을 푼 뒤, 그 안의 `codex-ppt` 폴더를 `~/.codex/skills/codex-ppt`에 넣고 Codex를 재시작하는 방법도 있습니다.

이 저장소를 로컬에서 개발하는 경우, 실시간으로 수정 사항을 테스트할 수 있도록 skill 디렉터리를 Codex skills 디렉터리에 심볼릭 링크로 연결할 수 있습니다.

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/codex-ppt-skill/skills/codex-ppt ~/.codex/skills/codex-ppt
```

## OpenClaw 설치

```bash
openclaw skills install codex-ppt
```

OpenClaw의 skill allowlist를 사용하는 경우 허용 목록에 `codex-ppt`를 추가해야 합니다.

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

일반적인 대상 디렉터리는 Claude Code의 경우 `~/.claude/skills/codex-ppt`, Hermes Agent의 경우 `~/.hermes/skills/codex-ppt`입니다. 로컬 개발 시에는 복사 대신 심볼릭 링크를 사용할 수도 있습니다.

## skill 업데이트

아래 문장을 사용 중인 agent에게 직접 보내 업데이트를 맡기는 것을 권장합니다.

```text
codex-ppt skill을 최신 버전으로 업데이트해 주세요. 저장소: https://github.com/ningzimu/codex-ppt-skill
```

수동으로 업데이트할 때는 위에서 해당 agent에 맞는 설치 명령을 다시 실행하면 설치된 skill이 최신 버전으로 덮어써집니다. 또는 [GitHub Releases](https://github.com/ningzimu/codex-ppt-skill/releases)에서 최신 `codex-ppt-skill-v*.zip`을 다운로드해 압축을 풀고 기존 `codex-ppt` 디렉터리를 교체할 수 있습니다. 업데이트 후 agent를 재시작하면 적용됩니다.

업데이트는 안전합니다. API key 등의 런타임 설정은 `~/.codex-ppt-skill/.env`에, 개인 스타일 라이브러리는 `~/.codex-ppt-skill/references/`에 저장되며 모두 skill 설치 디렉터리 외부에 있습니다. 따라서 skill을 업데이트하거나 다시 설치해도 사라지지 않습니다. 각 버전의 변경 사항은 [Releases 페이지](https://github.com/ningzimu/codex-ppt-skill/releases) 또는 저장소의 `CHANGELOG.md`에서 확인할 수 있습니다.

## 이미지 생성 모델 설정

현재 환경에서 사용할 수 있는 내장 도구 또는 호환 이미지 API가 필요합니다. 특정 모델에 의존하지 않습니다.

API/CLI fallback의 기본 모델은 `gpt-image-2.5-flare`이며, `--model gpt-image-2.5-sunburst`로 전환할 수 있습니다. 두 모델은 `xhigh` / `max` 품질과 투명 PNG/WebP를 지원합니다. 기본값은 2K 16:9와 `medium`을 유지합니다. 이전 모델의 매개변수 제한은 유지되며, 서드파티 서비스가 지원하는 모델과 매개변수를 확인해야 합니다.

AI는 내장 도구를 호출할 수 있는지 먼저 확인한 뒤 샘플을 생성하여 텍스트와 시각 품질을 검증합니다. 실제 모델과 매개변수는 환경에 따라 다르며, ChatGPT 구독이나 이미지 생성 성공만으로 2.5 사용을 입증할 수 없습니다. API/CLI fallback을 선택한 후 오류에 따라 API key, base URL, 서비스가 지원하는 모델명을 설정합니다.

## 서드파티 API 유의 사항

이 skill에는 OpenAI 공식 이미지 생성 방식을 지원하는 스크립트가 포함되어 있습니다. 서드파티 `gpt-image-2.5-flare` 프록시 API를 사용하는 경우 다음 정보를 제공해 보세요.

- 프록시 서비스의 base URL
  - 프록시 서비스에서 제공한 예시가 `https://xxx/v1/images/generations`라면 base URL에는 `https://xxx/v1`을 입력합니다.
  - 프록시 서비스에서 이미 `https://xxx/v1`을 제공했다면 한 단계를 더 추가하지 마세요. 그렇지 않으면 `.../v1/v1`이 됩니다.
  - OpenAI 공식 서비스를 사용하는 경우 `OPENAI_BASE_URL`을 입력하지 않아도 됩니다. 기본값은 공식 주소인 `https://api.openai.com/v1`입니다.
- 프록시 서비스의 API key
- 프록시 서비스의 구체적인 `gpt-image-2.5-flare` 모델명

위 정보를 AI에 제공한 뒤 이미지 생성을 시도하세요. 실행되지 않는다면 사용하는 프록시 서비스에 OpenAI 이미지 생성 인터페이스와 완전히 호환되지 않는 자체 이미지 생성 방식이 있을 수 있습니다. 프록시 서비스의 공식 이미지 생성 문서를 AI에 전달해 스크립트를 학습하고 조정하도록 하세요.
