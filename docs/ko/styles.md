# 스타일 및 개인 스타일 라이브러리

Codex PPT의 시각 스타일은 두 곳에서 가져옵니다. skill과 함께 배포되는 **내장 스타일**과, 로컬 컴퓨터에 저장되어 skill을 업데이트해도 사라지지 않는 **개인 스타일 라이브러리**입니다.

## 내장 스타일

skill에는 12가지 참고 스타일이 내장되어 있어 프롬프트를 잘 작성하지 못해도 바로 시작할 수 있습니다. PPT를 만들 때 다음 예시처럼 스타일 이름을 직접 말하면 됩니다.

```text
codex-ppt skill을 사용해서 이 자료를 10페이지 PPT로 만들고, 내장된 「손그림 기술 설명 스타일」을 사용해 주세요.
```

| 깔끔한 전문 스타일 | 창의적 매거진 스타일 |
| --- | --- |
| ![깔끔한 전문 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/clean-professional.png) | ![창의적 매거진 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/creative-magazine.png) |
| 전자 잉크 매거진 스타일 | 데이터 대시보드 스타일 |
| ![전자 잉크 매거진 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/e-ink-magazine.png) | ![데이터 대시보드 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/data-dashboard.png) |
| 복고풍 플랫 일러스트 스타일 | 손그림 기술 설명 스타일 |
| ![복고풍 플랫 일러스트 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/retro-flat-illustration.png) | ![손그림 기술 설명 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-technical.png) |
| 손그림 화이트보드 스타일 | 따뜻한 핸드메이드 스타일 |
| ![손그림 화이트보드 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/handdrawn-whiteboard.png) | ![따뜻한 핸드메이드 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/warm-handmade.png) |
| 연구 발표 스타일 | McKinsey 스타일 |
| ![연구 발표 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/scientific-defense.png) | ![McKinsey 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/mckinsey-style.png) |
| 당·정 홍보용 레드 스타일 | 교육용 코스웨어 스타일 |
| ![당·정 홍보용 레드 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/party-government-red.png) | ![교육용 코스웨어 스타일](https://raw.githubusercontent.com/ningzimu/codex-ppt-skill/main/assets/style-previews/teaching-courseware.png) |

스타일은 색상, 글꼴의 분위기, 레이아웃 밀도와 일러스트 언어로 이루어진 하나의 시각 시스템이지, 고정된 템플릿이 아닙니다. 같은 스타일에서도 각 페이지의 레이아웃은 콘텐츠 역할에 따라 달라지므로 모든 페이지가 똑같아 보이지 않습니다.

## 참고 자료의 스타일 재현

내장 스타일로 요구 사항을 충족할 수 없다면 마음에 드는 스타일 참고 자료를 제공할 수 있습니다. 스크린샷 한 장이나 여러 장, 또는 전체 PPT/PDF도 가능합니다. 먼저 agent가 참고 자료의 색상, 레이아웃, 글꼴과 시각 요소를 분석한 뒤 해당 스타일로 새 PPT를 생성하도록 하는 것을 권장합니다.

```text
codex-ppt skill을 사용해 PPT를 생성해 주세요. 시각 스타일은 제가 업로드한 PDF를 참고하세요. 제공한 자료의 각 페이지 이미지를 자세히 읽고 스타일을 충분히 이해한 뒤, 그 스타일을 재현해 생성해 주세요.
```

주의: 기본적으로 스타일만 재현하고 내용은 재사용하지 않습니다. 명시적으로 요청하지 않는 한 참고 자료의 텍스트와 데이터는 새 PPT에 옮겨지지 않습니다.

## 개인 스타일 라이브러리

생성된 PPT의 스타일이 마음에 든다면 조정한 사용자 지정 스타일이든 참고 자료에서 재현한 스타일이든 agent에게 저장하도록 요청해 나중에 바로 재사용할 수 있습니다.

```text
이 PPT의 시각 스타일이 마음에 듭니다. 개인 스타일 라이브러리에 저장해 주세요.
```

저장 방식의 주요 특징은 다음과 같습니다.

- **저장 위치**: 개인 스타일 라이브러리는 `~/.codex-ppt-skill/references/`에 있습니다(`CODEX_PPT_HOME` 환경 변수로 위치 변경 가능). skill 설치 디렉터리 **외부**에 있으므로 skill을 업데이트하거나 다시 설치해도 개인 스타일을 덮어쓰거나 잃지 않습니다.
- **자동 검색**: 저장 후 별도로 등록할 필요가 없습니다. 다음에 PPT 스타일을 선택할 때 agent가 개인 스타일 라이브러리를 자동으로 검색해 내장 스타일과 함께 표시합니다.
- **같은 이름 우선 적용**: 개인 스타일이 내장 스타일과 같은 이름이면 개인 스타일이 우선합니다. 이 기능을 이용해 내장 스타일을 사용자화할 수도 있습니다. 같은 이름으로 조정된 버전을 저장하면 기본 효과를 덮어씁니다.
- **재사용 방법**: 이후에는 스타일 이름을 직접 말하면 됩니다. 예: “『다크 데이터 테크 스타일』로 이 PPT를 생성해 주세요.”

생성이 끝난 뒤 이 deck이 사용자 지정 또는 조정된 스타일을 사용했다면 agent도 최종 보고에서 스타일을 저장할 수 있다고 안내합니다. 수정하지 않은 내장 스타일은 다시 저장할 필요가 없습니다.

## 관련 문서

- [예시 프롬프트](/ko/prompts.md): 내장 스타일 지정, 참고 스타일 재현, 스타일 저장을 위한 전체 프롬프트.
- [자주 묻는 질문](/ko/faq.md): 스타일이 달라지거나 페이지가 마음에 들지 않을 때의 처리 방법.
