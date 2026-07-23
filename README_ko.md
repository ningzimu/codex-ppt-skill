# Codex PPT Skill

[简体中文](README.md) · [English](README_en.md) · **한국어**

[![Docs](https://img.shields.io/badge/docs-Guide-111827)](https://ningzimu.github.io/codex-ppt-skill/#/ko/) [![ClawHub](https://img.shields.io/badge/ClawHub-codex--ppt-cd3b35)](https://clawhub.ai/ningzimu/codex-ppt) [![ClawMama](https://img.shields.io/badge/ClawMama-codex--ppt-2CA5E0)](https://app.clawmama.run/skills/5lak48/hermes?utm_source=github&utm_medium=issue&utm_campaign=skill_outreach_ningzimu_codex_ppt_skill) [![GitHub stars](https://img.shields.io/github/stars/ningzimu/codex-ppt-skill?style=flat&logo=github&label=stars)](https://github.com/ningzimu/codex-ppt-skill/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ningzimu/codex-ppt-skill?style=flat&logo=github&label=forks)](https://github.com/ningzimu/codex-ppt-skill/forks)

PowerPoint 덱을 생성하는 Codex용 skill입니다. Codex 외에도 Claude Code, OpenClaw, Hermes Agent 등 `SKILL.md`를 지원하는 다른 에이전트에서도 사용할 수 있으며, 이런 비(非)Codex 환경에서는 보통 `gpt-image-2`, 서드파티 이미지 API, 또는 OpenAI 호환 이미지 생성 엔드포인트 설정이 필요합니다. 이 skill은 글, 리포트, 논문, 강의 노트 등의 원본 자료를 "한 페이지 통이미지" 형식의 프레젠테이션으로 변환합니다. 먼저 개요와 시각 스타일을 기획하고, 각 슬라이드를 전면 이미지로 생성한 뒤, 마지막에 로컬 스크립트로 이미지들을 `.pptx` 파일로 조립합니다.

## 스폰서

<table>
<tr>
<td width="180"><img src="assets/atlas-cloud-logo.png" alt="Atlas Cloud" width="160"></td>
<td>본 프로젝트를 후원해 주신 <a href="https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=codex-ppt-skill">Atlas Cloud</a>에 감사드립니다. AtlasCloud는 이미지 생성, 비디오 생성, LLM 등을 하나의 API로 제공하는 멀티모달 AI 추론 플랫폼입니다. 본 skill은 기존의 API key, base URL, 모델명 설정을 그대로 사용해 AtlasCloud의 GPT Image 2 생성·편집 엔드포인트를 호출할 수 있으며, 사용량 기반 과금과 즉시 사용 가능한 설정을 제공합니다. 전체 모델 목록은 <a href="https://www.atlascloud.ai/zh/models">Atlas Cloud 모델 페이지</a>를 참고하세요.</td>
</tr>
</table>

## 참고 사항

> [!TIP]
> 이 skill은 글, 리포트, 개요, 아이디어로부터 이미지 기반 PPT 덱을 생성합니다. 강한 시각적 표현에 적합하지만, 슬라이드 요소를 직접 편집할 수는 없습니다. 편집 가능한 PPT가 필요하다면 생성된 덱을 [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)로 변환해 보세요.
>
> `codex-ppt`와 `image-to-editable-ppt`에 대한 자세한 소개는 [skill_duo_intro.pdf](assets/skill_duo_intro.pdf)를 참고하세요. 이 덱은 `codex-ppt` skill로 다음 프롬프트를 사용해 생성했습니다: "请分别阅读 Codex PPT和 Image to Editable PPT 这两个技能的内容，然后用 Codex PPT 帮我做一个PPT吧，20页，每个技能的介绍10页。"
>
> 이 PPT skill의 설계와 튜닝에 대한 실전 노트는 중국어 아티클 [2000 个 GitHub Star 换来的经验：好的 AI Skill 是调出来的，不是写出来的](https://mp.weixin.qq.com/s/LaxWBX-nogHPpSxlk-Vs8Q)에서 볼 수 있습니다.

> [!NOTE]
> 다른 사용자들이 이 skill로 만든 더 많은 PPT 예시를 보려면 상단 고정 쇼케이스 이슈 [欢迎分享 codex-ppt 使用案例和 PPT 效果](https://github.com/ningzimu/codex-ppt-skill/issues/34)를 방문하세요.

이 skill은 견고한 PPT 생성 워크플로를 제공하는 것을 목표로 합니다. 폭넓게 두루 쓰이도록 하다 보니 워크플로가 일상적으로 필요한 것보다 다소 복잡하며, 그 복잡함이 때로 불안정성이나 불필요한 선택지를 만들 수 있습니다. 예를 들어 Codex 내장 이미지 생성과 API/CLI fallback 생성을 모두 지원하고, 서브에이전트 유무 두 경우 모두를 지원합니다. 대부분의 사용자는 결국 이 중 한 가지 경로만 사용하게 됩니다.

자주 쓰는 경로가 잘 돌아가게 되면, AI 어시스턴트에게 이 skill을 수정해 자신의 선호(선호하는 이미지 백엔드, 서브에이전트 사용 여부, 출력 디렉터리 규칙, 시각 스타일, 슬라이드 페이싱 등)를 고정해 달라고 요청하는 것을 고려해 보세요. 그러면 매번 같은 선택을 반복할 필요가 없습니다.

덱을 만들다 마음에 드는 레이아웃이나 시각 스타일을 발견하면 — 이 skill로 만든 것이든 다른 곳에서 찾은 것이든 — AI에게 개인 스타일 라이브러리(`~/.codex-ppt-skill/references/`)에 저장해 달라고 요청해 점차 자신만의 컬렉션을 쌓을 수 있습니다. 개인 스타일 라이브러리는 skill 설치 디렉터리 밖에 있으므로, skill을 업데이트하거나 재설치해도 사라지지 않습니다. Skill은 매우 개인적인 워크플로이므로, 자신의 습관에 맞게 튜닝해 실제 업무에 더 유용하게 만드세요.

skill 설계와 사용에 대한 기본 소개는 [good-skill-design.pptx](assets/good-skill-design.pptx)를 참고하세요. 이 덱 역시 이 skill로 만들었으며, 손그림 기술 설명 스타일을 사용했고, Claude의 skill 설계 모범 사례 아티클 [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)를 기반으로 합니다.

## 특징

- 여러 에이전트에서 동작: Codex, Claude Code, OpenClaw, Hermes Agent 등 `SKILL.md` 기반 환경을 지원합니다. 내장 이미지 생성·편집 도구를 우선 사용할 수 있는 Codex가 가장 권장되는 환경입니다.
- 서드파티 이미지 공급자 연동: OpenAI 호환 엔드포인트, AtlasCloud, `base URL`, 커스텀 모델명 설정을 지원하므로, API/CLI fallback에서 `gpt-image-2`나 호환 이미지 모델을 사용할 수 있습니다.
- 안정적인 단계형 워크플로: 전체 덱 생성 전에 개요, 슬라이드 수, 시각 스타일, 이미지 백엔드, 샘플 슬라이드를 확인하여 완성 PPT 생성 시의 이탈과 재작업을 줄입니다.
- 원샷이 아닌 가이드형: 계속 진행하기 전에 `outline.md`, 슬라이드별 핵심 포인트, 스타일 방향, 샘플 슬라이드 품질을 확인하도록 요청합니다.
- 낮은 준비 부담: 글, 리포트, 논문, 강의 노트, Markdown 파일, 개요, PDF, Word 문서 등을 모두 시작 자료로 사용할 수 있습니다.
- 내장 PPT 스타일 레퍼런스 12종: 클린 프로페셔널, 학술 발표(디펜스), 당정(党政) 레드, 강의 교안, 전자잉크 매거진, 손그림 기술 설명, 대시보드, 맥킨지 스타일 등을 포함합니다. 프롬프트를 직접 쓰고 싶지 않다면 손그림 기술 설명 스타일이 좋은 출발점입니다.
- 커스텀 스타일 복제 지원: 마음에 드는 이미지, PDF, PPT/PPTX를 제공하면 에이전트가 그 색상, 레이아웃, 타이포그래피, 시각 시스템을 분석한 뒤 해당 스타일로 새 덱을 생성할 수 있습니다.
- 재사용 가능한 개인 스타일 라이브러리 구축: 덱 스타일이 마음에 들면 에이전트에게 `~/.codex-ppt-skill/references/`에 저장하도록 요청해 이후 덱에서 바로 재사용할 수 있습니다. 이 라이브러리는 skill 설치 밖에 있어 업데이트에도 유지되며, 같은 이름의 개인 스타일은 내장 스타일보다 우선합니다.
- 병렬 서브에이전트 생성 지원: 샘플 슬라이드가 승인되면 하나의 서브에이전트가 슬라이드 하나를 담당하고, 가독성·스타일 일관성·내용 완결성을 자체 점검한 뒤 수정할 이슈를 보고할 수 있습니다.
- 필수 이미지 삽입 지원: 논문 그림, 실험 차트, 스크린샷, 아키텍처 다이어그램 등을 특정 슬라이드에 지정하면, 생성된 페이지가 그 주위로 레이아웃과 테마를 맞춥니다.
- 발표 노트 생성: `speech.md`를 만들고 PPTX 조립 시 각 슬라이드에 노트를 기록해, 발표하거나 수정하기 쉽게 합니다.

## 출력 예시

아래는 기술 공유 덱의 예시입니다. 각 페이지는 `gpt-image-2`로 생성한 완전한 16:9 슬라이드 이미지이며, 로컬 스크립트로 PPTX 파일로 조립됩니다.

![생성된 PPT 예시](assets/slides_example.png)

아래는 논문 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)를 기반으로 한 학술 발표 예시입니다. 모델 아키텍처, 어텐션 모듈, 어텐션 시각화 등 논문의 원본 그림을 입력 자산으로 특정 슬라이드에 지정한 뒤, 그 그림들을 중심으로 일관된 덱을 생성하는 방법을 보여줍니다(Issue #14 참고).

![논문 그림 삽입 예시](assets/paper-figures-example.png)

## 스타일 예시

아래 미리보기 이미지들은 사용자가 제작 전에 시각 방향을 고를 수 있도록 `gpt-image-2`로 생성한 것입니다.

| 클린 프로페셔널 | 크리에이티브 매거진 |
| --- | --- |
| ![클린 프로페셔널](assets/style-previews/clean-professional.png) | ![크리에이티브 매거진](assets/style-previews/creative-magazine.png) |
| 전자잉크 매거진 | 데이터 대시보드 |
| ![전자잉크 매거진](assets/style-previews/e-ink-magazine.png) | ![데이터 대시보드](assets/style-previews/data-dashboard.png) |
| 레트로 플랫 일러스트 | 손그림 기술 설명 |
| ![레트로 플랫 일러스트](assets/style-previews/retro-flat-illustration.png) | ![손그림 기술 설명](assets/style-previews/handdrawn-technical.png) |
| 손그림 화이트보드 | 따뜻한 수제 느낌 |
| ![손그림 화이트보드](assets/style-previews/handdrawn-whiteboard.png) | ![따뜻한 수제 느낌](assets/style-previews/warm-handmade.png) |
| 학술 발표(디펜스) | 맥킨지 스타일 |
| ![학술 발표(디펜스)](assets/style-previews/scientific-defense.png) | ![맥킨지 스타일](assets/style-previews/mckinsey-style.png) |
| 당정 레드 | 강의 교안 |
| ![당정 레드](assets/style-previews/party-government-red.png) | ![강의 교안](assets/style-previews/teaching-courseware.png) |

## 출력 구조

각 PPT는 독립된 프로젝트 디렉터리에 생성됩니다:

```text
{base_dir}/{deck_name}/     # 이 덱을 위한 독립 프로젝트 디렉터리
├── origin_image/           # 최종 슬라이드 이미지만 저장
│   ├── slide_01.png        # 1번 슬라이드 이미지
│   ├── slide_02.png        # 2번 슬라이드 이미지
│   └── ...                 # 이후 슬라이드 이미지, 슬라이드 순서대로 명명
├── outline.md              # 확정된 개요, 슬라이드 수, 제목, 핵심 포인트
├── speech.md               # PPT에 기록되는 발표 노트
└── {deck_name}.pptx        # 최종 조립된 PowerPoint 파일
```

`origin_image/`로 각 슬라이드에 사용된 최종 이미지를 검토할 수 있습니다. 파일은 `slide_01.png`, `slide_02.png` 식으로 순서대로 명명되어, 덱을 시각적으로 미리 보거나 특정 슬라이드 하나만 수정 요청하기 쉽습니다.

`speech.md`는 동반되는 발표 대본입니다. `.pptx`를 조립할 때 그 내용이 각 슬라이드의 발표 노트에 기록되므로, PowerPoint에서 발표하는 동안 바로 보거나, 편집하거나, 사용할 수 있습니다.

## 활용 사례

- 기술 아티클을 공유용 덱으로 변환.
- 논문이나 리포트를 프레젠테이션으로 변환.
- 강의 노트를 교육용 슬라이드로 변환.
- 연구 제안, 중간 점검, 최종 과제 검수, 학위 논문 발표용 덱 제작.
- 비즈니스 리포트, 제품 소개, 연구 요약 제작.
- 강한 시각적 일관성이 필요한 이미지 기반 프레젠테이션 제작.

## 설치

### 한 문장 설치

권장: 아래 문장을 에이전트에게 보내 skill을 대신 설치하게 하세요:

```text
이 codex-ppt skill을 설치해 줘: https://github.com/ningzimu/codex-ppt-skill
```

### Codex 수동 설치

Codex에 수동으로 설치하려면 `skills` CLI로 이 skill을 Codex의 전역 skills 디렉터리에 추가하세요:

```bash
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent codex \
  --global
```

설치 후 새 skill이 인식되도록 Codex를 재시작하세요.

또는 GitHub Releases에서 `codex-ppt-skill-v*.zip`을 다운로드해 압축을 풀고, 그 안의 `codex-ppt` 디렉터리를 `~/.codex/skills/codex-ppt`에 두고 Codex를 재시작해도 됩니다.

이 저장소를 로컬에서 개발 중이라면, 대신 skill 디렉터리를 Codex skills 디렉터리로 심볼릭 링크해 변경 사항이 즉시 반영되게 할 수 있습니다:

```bash
mkdir -p ~/.codex/skills
ln -s /path/to/codex-ppt-skill/skills/codex-ppt ~/.codex/skills/codex-ppt
```

### OpenClaw

ClawHub에서 설치:

```bash
openclaw skills install codex-ppt
```

ClawHub 페이지: [clawhub.ai/ningzimu/codex-ppt](https://clawhub.ai/ningzimu/codex-ppt)

OpenClaw skill 허용 목록을 사용한다면 `codex-ppt`를 허용 skill에 추가하세요.

### Claude Code 및 Hermes Agent

이 에이전트들은 `SKILL.md` skill을 읽을 수 있습니다. `skills` CLI로도 설치할 수 있습니다:

```bash
# Claude Code
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent claude-code \
  --global

# Hermes Agent
npx -y skills@latest add ningzimu/codex-ppt-skill \
  --skill codex-ppt \
  --agent hermes-agent \
  --global
```

일반적인 대상 디렉터리는 Claude Code는 `~/.claude/skills/codex-ppt`, Hermes Agent는 `~/.hermes/skills/codex-ppt`입니다.

이 저장소를 로컬에서 개발 중이라면 복사 대신 심볼릭 링크를 사용해 변경 사항이 즉시 반영되게 할 수 있습니다.

### 업데이트

위의 해당 설치 명령을 다시 실행해 설치된 skill을 최신 버전으로 덮어쓰거나, 에이전트에게 업데이트를 요청하기만 하면 됩니다:

```text
codex-ppt skill을 최신 버전으로 업데이트해 줘. 저장소는: https://github.com/ningzimu/codex-ppt-skill
```

업데이트 후 에이전트를 재시작하세요. API key 설정(`~/.codex-ppt-skill/.env`)과 개인 스타일 라이브러리(`~/.codex-ppt-skill/references/`)는 skill 설치 디렉터리 밖에 있으므로, 업데이트나 재설치로 사라지지 않습니다.

## 이미지 모델 설정

> [!TIP]
> Codex PPT를 그냥 평소처럼 사용해 덱을 만들면 됩니다. 대부분의 경우 이미지 모델을 손으로 설정할 필요가 없습니다. 워크플로가 이미지 백엔드를 고르라고 할 때 AI가 현재 환경을 확인하고 필요한 정보를 안내합니다.
>
> - Codex의 내장 이미지 생성을 사용한다면 보통 별도 API key가 필요 없습니다.
> - 서드파티 공급자나 OpenAI 호환 프록시가 필요하다고 확인했다면, API key, base URL, 모델명을 설정하기 전에 AI에게 [이미지 모델 설정 가이드](skills/codex-ppt/docs/image-model-configuration.md)를 읽어 달라고 요청하세요.

특정 해상도, 더 높은 품질, 슬라이드 하나 수정을 요청하는 것만으로는 서드파티 API 설정이 자동으로 시작되지 않습니다. GPT 구독으로 Codex를 사용하고 Codex의 내장 이미지 생성 도구를 쓸 수 있다면, 대개 내장 이미지 도구를 계속 사용할 수 있고 API key를 준비할 필요가 없습니다.

## 사용법

Codex, Claude Code, OpenClaw, Hermes Agent에게 `codex-ppt` skill을 명시적으로 지정해 요청하세요. 예:

```text
codex-ppt skill을 사용해 /path/to/article.md를 약 10장짜리 PPT로 만들어 줘.
```

skill은 다음 워크플로를 따릅니다:

1. 원본 내용을 읽고 덱 개요를 기획합니다.
2. `outline.md`를 생성하고 슬라이드 수, 슬라이드 제목, 핵심 포인트를 확인받습니다.
3. 2~3개의 시각 스타일 옵션을 제시하고 하나를 추천해 사용자 확인을 받습니다.
4. 첫 이미지 생성 전에 이미지 생성 백엔드를 밝히고 확인받습니다.
5. 확정된 이미지 백엔드로 샘플 슬라이드 하나를 생성해 스타일, 레이아웃 리듬, 텍스트 품질을 승인받습니다.
6. PPT 프로젝트 디렉터리를 만듭니다.
7. 같은 이미지 백엔드로 모든 슬라이드 이미지를 하나씩 생성합니다.
8. 텍스트 가독성, 스타일 일관성, 내용 완결성을 점검합니다.
9. `speech.md`를 생성합니다.
10. `assemble_ppt.py`로 `.pptx`를 조립합니다.
11. 선택 사항: 생성된 PPT 스타일이 정말 마음에 들면 스타일 라이브러리에 저장합니다. 이미 내장 스타일을 사용했다면 다시 저장할 필요는 없습니다.

## 사용 팁

- Codex 구독자는 기본적으로 내장 이미지 생성 도구를 사용합니다. 이 도구의 출력 해상도는 비교적 낮고, 현재 수동 해상도 설정을 제공하지 않습니다. 더 높은 해상도의 이미지가 필요하면 `gpt-image-2` API를 통한 생성(API key, base URL, 모델명으로 설정하는 API/CLI fallback 경로)으로 전환하세요. API/CLI fallback 경로에서 스크립트 기본 해상도는 2K 16:9 가로이며, 특히 텍스트가 많은 페이지에서 슬라이드 이미지가 여전히 흐릿하면 AI에게 4K로 전환해 달라고 요청하세요.
- 특정 슬라이드의 내용, 레이아웃, 색상, 문구가 마음에 들지 않으면, 전체 덱을 다시 생성하는 대신 현재 에이전트에게 그 슬라이드를 상세히 다듬어 달라고 요청하세요.

![슬라이드 단건 수정 예시: PPT를 열고 주석을 클릭해 수정할 영역을 표시](assets/single-slide-revision-example.png)

- 마음에 드는 PPT 스타일 레퍼런스(스크린샷 하나, 여러 장, 또는 전체 PPT/PDF)를 제공할 수도 있습니다. 현재 에이전트에게 먼저 색상, 레이아웃, 타이포그래피, 시각 요소를 분석한 뒤 해당 스타일로 새 덱을 생성해 달라고 요청하세요. 결과가 좋으면 그 스타일을 개인 스타일 라이브러리 `~/.codex-ppt-skill/references/`에 저장하도록 요청해 이후에 재사용할 수 있으며, skill을 업데이트해도 사라지지 않습니다.
- 논문 그림, 실험 차트, 스크린샷, 아키텍처 다이어그램을 포함해야 한다면, 개요에서 각 이미지의 대상 슬라이드와 역할을 지정하세요.

## QA

- 문서: [codex-ppt FAQ 및 사용 노트](https://ningzimu.github.io/codex-ppt-skill/#/faq)

## 커뮤니티

QR 코드를 스캔해 Skill 커뮤니티 그룹에 참여하고, 사용 경험을 공유하고, 이슈를 제보하고, 업데이트 소식을 받아보세요.

<img src="assets/codex-ppt-community-qr.png" alt="Codex PPT Skill 커뮤니티 QR 코드" width="220">

Telegram: [CodexPPT](https://t.me/CodexPPT)

## 관련 프로젝트

- [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill): 슬라이드 스크린샷, PDF 페이지, 이미지 기반 PPTX 파일을 편집 가능한 PowerPoint 덱으로 재구성합니다. `codex-ppt`가 이미지 기반 슬라이드를 생성한 뒤에 유용합니다.
- [codex-gpt-image](https://github.com/ningzimu/codex-gpt-image): Codex OAuth / 멤버 로그인 기반의 `gpt-image-2` 이미지 생성 skill입니다.
- [handdrawn-tech-illustrations](https://github.com/ningzimu/handdrawn-tech-illustrations): 중국어 기술 콘텐츠를 위한 손그림 일러스트 skill입니다. 기술 아티클, 제품 노트, 스크린샷, 개요, 대략적인 아이디어를 아티클 삽화, 개념 설명 그래픽, WeChat 커버 이미지, Rednote 커버로 변환하며, 친근하고 가벼운 카툰풍에 중국어 가독성이 좋고 적당한 정보 밀도를 갖습니다.
- [awesome-ai-ppt](https://github.com/ningzimu/awesome-ai-ppt): 오픈소스 AI PPT 프로젝트를 HTML-first, image-first, PPTX-native, 변환, 자동화 인프라 등의 워크플로별로 정리한 큐레이션 목록입니다. 에이전트나 개발자가 PPT 덱을 만들고, 편집하고, 변환하고, 검사하는 데 도움이 되는 GitHub 프로젝트에 초점을 둡니다.
- [claude-code-lens](https://github.com/ningzimu/claude-code-lens): Claude Code의 API 트래픽, 로그, 프롬프트, 도구 호출을 위한 로컬 관찰(observability) 도구로, 에이전트가 실제로 무엇을 하는지 이해하는 데 유용합니다.

## 라이선스

MIT

## 감사의 말

[LinuxDO](https://linux.do) 커뮤니티의 지원에 감사드립니다.
