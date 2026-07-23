# Codex PPT Skill 문서

Codex PPT는 Codex용 PPT 생성 skill이며, Claude Code, OpenClaw, Hermes Agent 등 `SKILL.md`를 지원하는 agent에서도 사용할 수 있습니다. 글, 보고서, 논문, 수업 노트 또는 거친 아이디어를 이미지형 프레젠테이션으로 변환합니다. 먼저 개요와 시각 스타일을 설계하고, 각 슬라이드의 완성 이미지를 차례로 생성한 뒤, 마지막으로 `.pptx` 파일로 조립합니다.

## 문서 읽는 순서

빠르게 시작하려면 먼저 [빠른 시작](/ko/quickstart.md)을 읽으세요.

설치, 모델 설정 또는 여러 agent 연동 방법이 필요하다면 [설치 및 설정](/ko/installation.md)을 읽으세요.

전체 생성 과정, 확인 단계와 품질 관리를 이해하려면 [표준 워크플로](/ko/workflow.md)를 읽으세요.

사용 중 문제가 생겼다면 [자주 묻는 질문](/ko/faq.md)을 확인하세요.

## 하위 문서

- [빠른 시작](/ko/quickstart.md): 처음 사용할 때의 가장 짧은 절차, 예시 명령과 결과물 안내.
- [설계 철학](/ko/design.md): 이미지형 PPT, 단계별 확인, 두 skill의 역할 분담을 채택한 이유.
- [설치 및 설정](/ko/installation.md): Codex, OpenClaw, Claude Code, Hermes Agent의 설치 및 업데이트 방법과 API/CLI fallback 설정.
- [표준 워크플로](/ko/workflow.md): 개요 확인, 스타일 확인, 백엔드 확인, 샘플 슬라이드 확인부터 전체 생성과 조립까지의 완전한 과정.
- [스타일 및 개인 스타일 라이브러리](/ko/styles.md): 12가지 내장 스타일 미리보기, 참고 자료의 스타일 재현, 마음에 드는 스타일을 개인 스타일 라이브러리에 저장해 장기적으로 재사용하는 방법.
- [자주 묻는 질문](/ko/faq.md): 편집 가능 여부, API key, 샘플 슬라이드, 이미지 삽입, 개별 슬라이드 수정 등 자주 묻는 문제.
- [예시 프롬프트](/ko/prompts.md): 글을 PPT로 변환, 논문 발표, 경영진 보고, 스타일 지정, 개별 슬라이드 수정 등에 바로 재사용할 수 있는 프롬프트.

## 주요 기능

- 이미지형 PPT 생성: 각 페이지가 완성된 16:9 슬라이드 이미지로 만들어져, 강한 시각적 표현과 일관된 스타일이 필요한 상황에 적합합니다.
- 단계별 확인 절차: 개요, 시각 스타일, 이미지 생성 방식과 샘플 슬라이드를 먼저 확인한 뒤 전체 PPT를 생성해 재작업을 줄입니다.
- 12가지 내장 스타일: 손그림 기술 설명, 연구 발표, 깔끔한 전문 스타일, McKinsey 스타일, 당·정 홍보용 레드 스타일, 교육용 코스웨어 등 다양한 방향을 제공합니다. 자세한 내용은 [스타일 및 개인 스타일 라이브러리](/ko/styles.md)를 참고하세요.
- 참고 자료 기반 스타일 재현: 사용자가 제공한 PPT, PDF 또는 스크린샷을 읽고 각 페이지의 이미지 스타일을 이해한 뒤 유사하게 생성할 수 있습니다.
- 개인 스타일 라이브러리 축적: 마음에 드는 스타일을 `~/.codex-ppt-skill/references/`에 저장할 수 있습니다. skill 설치 디렉터리 외부에 보관되므로 skill을 업데이트해도 사라지지 않으며, 이후 이름으로 바로 재사용할 수 있습니다.
- 지정 이미지 삽입: 논문 원본 이미지, 실험 결과 그래프, 아키텍처 다이어그램 또는 스크린샷을 특정 슬라이드에 사용하도록 지정할 수 있습니다.
- 여러 agent 환경 지원: Codex 외에도 Claude Code, OpenClaw, Hermes Agent 등 `SKILL.md`를 지원하는 agent에서 사용할 수 있습니다.
- PowerPoint 자동 조립: `outline.md`, 각 슬라이드 이미지, `speech.md`를 생성하고 최종적으로 `.pptx` 파일로 조립합니다.
- 서드파티 API를 통한 텍스트 모델 및 `gpt-image-2` 이미지 생성 모델 사용 지원.
- PPT 발표 대본 생성을 지원하며, 기본적으로 PPT 메모 영역에 자동 삽입합니다.
- 생성 후 만족스럽지 않은 특정 슬라이드만 선택적으로 수정할 수 있습니다. 자세한 내용은 [자주 묻는 질문](/ko/faq.md)을 참고하세요.

## 활용 사례

- 기술 문서를 발표용 PPT로 변환
- 논문, 연구 보고서 또는 조사 자료를 프레젠테이션으로 변환
- 수업 노트를 강의 자료로 변환
- 제품 소개, 비즈니스 보고, 프로젝트 회고
- 연구 발표, 프로젝트 신청, 중간 점검, 최종 검수
- 일관된 시각 언어가 필요한 이미지형 프레젠테이션

## 중요 안내

Codex PPT는 이미지형 PPT를 생성합니다. 시각적 일관성은 높지만, 슬라이드 안의 텍스트, 차트와 도형을 기존 PPT처럼 개별적으로 편집할 수는 없습니다.

편집 가능한 PPT로 추가 변환해야 한다면 생성 후 [image-to-editable-ppt-skill](https://github.com/ningzimu/image-to-editable-ppt-skill)을 사용할 수 있습니다.

`gpt-image-2` 이미지 생성 모델을 사용할 권한이 없다면 이 skill을 사용할 수 없습니다. 자세한 내용은 [설치 및 설정](/ko/installation.md)을 참고하세요.

## 관련 링크

- GitHub 저장소: https://github.com/ningzimu/codex-ppt-skill
- ClawHub 페이지: https://clawhub.ai/ningzimu/codex-ppt
- 사용 사례 전시: https://github.com/ningzimu/codex-ppt-skill/issues/34
- 편집 가능한 PPT 변환 skill: https://github.com/ningzimu/image-to-editable-ppt-skill
