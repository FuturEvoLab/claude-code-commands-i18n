# Claude Code 명령어

[English](README.md) · [日本語](README.ja.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-Hant.md) · [한국어](README.ko.md) · [Русский](README.ru.md) · [Español](README.es.md)

![Unofficial](https://img.shields.io/badge/Anthropic-unofficial-lightgrey) [![check](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml/badge.svg)](https://github.com/FuturEvoLab/claude-code-commands-i18n/actions/workflows/check.yml) [![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-blue)](LICENSE-CONTENT) [![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE) ![Commands](https://img.shields.io/badge/commands-115-teal)

> Claude Code의 모든 슬래시 명령을 **영어, 일본어, 중국어 간체, 중국어 번체, 한국어, 러시아어, 스페인어**로 쉽게 설명하는 비공식 참고 자료입니다. 영어 공식 문서를 읽기 어려운 분들을 위해 만들었습니다. 명령마다 짧은 설명과 언제 쓰면 좋은지 보여 주는 현실적인 예시가 있습니다.

## 라이브 미리보기

바로 써 볼 수 있는 정적 페이지입니다. 검색, 언어·테마 전환, 명령어 복사를 할 수 있으며 설치는 필요 없습니다.

### [검색 가능한 웹 버전 →](https://futurevolab.github.io/claude-code-commands-i18n/)

| 기본 테마 | 매트릭스 테마 |
|---|---|
| [![기본 테마](docs/assets/preview-en.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=terminal) | [![매트릭스 테마](docs/assets/preview-matrix.png)](https://futurevolab.github.io/claude-code-commands-i18n/?theme=matrix) |

<p><img src="docs/assets/preview-search.png" alt="search" width="68%"> <img src="docs/assets/preview-mobile.png" alt="mobile" width="28%"></p>

## 문법 읽는 법

- 입력창에 `/`를 입력하면 명령 메뉴가 열립니다. 계속 입력하면 좁혀집니다.
- `[ ]` = 생략 가능, `< >` = 필수, `|` = 그중 하나. 인수는 한국어로 써도 됩니다.
- **스킬** = Claude에게 건네는 묶음 프롬프트. **워크플로** = 여러 에이전트를 백그라운드에서 실행합니다.
- 많은 명령은 버전, 플랜, 플랫폼, 기능 활성화 여부에 따라 다릅니다. 내 화면에 보이는 메뉴가 정답입니다. `/status`로 버전을 확인하세요.

## ★ 여기서 시작

Claude Code를 처음 쓰는 첫 주를 위해 편집자가 고른 명령입니다.

- `/clear` · 새 대화 시작 (이전 대화는 다시 열 수 있음)
- `/compact` · 긴 대화를 요약해 공간 확보
- `/context` · 컨텍스트를 무엇이 채우는지 보기
- `/plan` · 먼저 계획부터, 수정은 승인 후에
- `/resume` · 이전 대화로 돌아가기
- `/rewind` · 되돌리기: 코드와 대화를 이전으로
- `/model` · 모델 바꾸기
- `/init` · 프로젝트의 CLAUDE.md 만들기
- `/code-review` · 커밋 전에 버그 검사, 필요하면 수정까지
- `/loop` · 일정 간격으로 프롬프트 반복
- `/mcp` · 외부 도구 연결 관리
- `/permissions` · Claude가 묻지 않고 할 수 있는 일 정하기
- `/usage` · 비용과 플랜 한도 확인
- `/doctor` · 문제가 생겼을 때 점검 실행
- `/help` · 도움말과 전체 명령 보기
- `/powerup` · 대화형 레슨으로 기능 배우기

## 하고 싶은 일로 명령 찾기

상황을 고르세요. 명령은 시도할 순서대로 나열됩니다.

- **Claude가 뭔가를 망가뜨려서 되돌리고 싶어요** → `/rewind` · `/diff`
- **관계없는 작업을 처음부터 시작하고 싶어요** → `/clear` · `/resume`
- **대화가 길어져서 Claude가 느리거나 자꾸 잊어버려요** → `/context` · `/compact` · `/autocompact`
- **어제 끝내지 못한 작업을 이어서 하고 싶어요** → `/resume` · `/rename` · `/recap`
- **큰 변경 전에 계획부터 보고 싶어요** → `/plan` · `/effort` · `/model`
- **Claude가 항상 한국어로 답하게 하고 싶어요** → `/init` · `/memory`
- **비용과 사용량을 줄이고 싶어요** → `/usage` · `/model` · `/effort` · `/context`
- **커밋이나 배포 전에 점검하고 싶어요** → `/diff` · `/code-review` · `/security-review` · `/verify`
- **여러 작업을 동시에 하거나 백그라운드로 돌리고 싶어요** → `/fork` · `/subtask` · `/background` · `/tasks` · `/batch`
- **작업을 반복하거나 예약해서 실행하고 싶어요** → `/loop` · `/schedule` · `/goal`
- **권한 확인 요청이 너무 많아요** → `/permissions` · `/fewer-permission-prompts`
- **도구를 연결하거나 새 기능을 추가하고 싶어요** → `/mcp` · `/plugin` · `/skills`
- **슬라이드, 디자인, 차트를 만들고 싶어요** → `/slides` · `/design` · `/dataviz` · `/artifacts`
- **컴퓨터를 떠나 휴대폰으로 이어서 하고 싶어요** → `/remote-control` · `/mobile` · `/desktop`
- **Claude Code 자체가 이상하게 동작해요** → `/doctor` · `/status` · `/debug` · `/bug`
- **Claude Code를 제대로 배우고 싶어요** → `/powerup` · `/help` · `/insights`

## 안전 표시

이 표시가 붙은 명령은 특히 주의가 필요합니다.

- **¥ 비용이 들 수 있음**: 유료 사용량을 소비하거나 추가 요금이 발생할 수 있습니다. 먼저 `/usage`와 공식 요금 안내를 확인하세요.
- **↗ 외부로 데이터 전송**: 대화, 코드, 댓글을 다른 서비스(Anthropic, GitHub, 클라우드 세션, 브라우저 안의 사이트)로 보내거나 원격 저장소에 푸시합니다. 무엇이 어디로 가는지 먼저 확인하세요.
- **⚿ 비밀 정보 노출 가능**: 결과물(파일, 클립보드, 보고서)에 대화 내용, 키, 비밀번호, 개인정보가 들어 있을 수 있습니다. 공유하기 전에 검토하고 민감한 부분은 가리거나 지우세요.
- **⇄ 파일을 대량 변경**: 한 번에 많은 파일을 바꾸거나 되돌릴 수 있습니다. 먼저 커밋하거나 백업하고, 실행 후에는 `/diff`로 검토하세요.
- **⚑ 안전 설정 변경**: Claude가 묻지 않고 할 수 있는 일이나 다른 안전 관련 설정을 바꿉니다. 이해하고 신뢰하는 작업만 허용하세요.

## 목차

- [대화와 컨텍스트](#대화와-컨텍스트) (15)
- [모델과 추론](#모델과-추론) (5)
- [프로젝트와 파일](#프로젝트와-파일) (7)
- [리뷰와 검증](#리뷰와-검증) (7)
- [병렬 작업과 백그라운드](#병렬-작업과-백그라운드) (10)
- [자동화와 예약](#자동화와-예약) (4)
- [아티팩트, 슬라이드, 디자인](#아티팩트-슬라이드-디자인) (9)
- [플러그인, 스킬, 연동](#플러그인-스킬-연동) (13)
- [권한과 안전](#권한과-안전) (7)
- [설정과 화면](#설정과-화면) (10)
- [계정과 사용량](#계정과-사용량) (8)
- [클라우드, 원격, 다른 기기](#클라우드-원격-다른-기기) (8)
- [진단과 피드백](#진단과-피드백) (10)
- [기타](#기타) (2)
- [제거됨](#제거됨) (3)

## 대화와 컨텍스트

대화를 새로 시작, 압축, 되감기, 재개하고 컨텍스트 창을 관리합니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/clear`<br>`[name]`<br>★ | clear<br>지우기·초기화 | 컨텍스트가 비어 있는 새 대화를 시작합니다. 프로젝트 메모리는 그대로 남습니다. 이전 대화는 삭제되지 않고 `/resume`으로 다시 열 수 있습니다. 이름을 붙이면 선택 화면에서 이전 대화에 라벨이 붙습니다.<br>별칭: `/reset`, `/new` | 한 기능을 끝내고 관계없는 다음 작업으로 넘어갈 때: `/clear 로그인-기능`. 이전 내용에 방해받지 않고 사용량도 줄어듭니다. |
| `/compact`<br>`[instructions]`<br>★ | compact<br>압축 | 지금까지의 대화를 요약해서 컨텍스트 공간을 확보하고, 같은 대화를 이어갑니다. 지시를 덧붙이면 요약에 무엇을 남길지 정할 수 있습니다. | 긴 작업을 한 뒤: `/compact 데이터베이스 구조와 미해결 버그 목록은 남겨 줘`. |
| `/context`<br>`[all]`<br>★ | context<br>컨텍스트 (Claude가 지금 "기억하고" 있는 내용) | 컨텍스트 사용량을 색깔 격자로 보여 주고, 최적화 제안과 용량 경고도 표시합니다. `all`을 붙이면 항목별 내역을 펼쳐 보여 줍니다. | Claude가 자꾸 잊어버리거나 사용량이 빠르게 늘 때, `/context`로 큰 파일이나 도구 출력이 공간을 채우고 있는지 확인합니다. |
| `/plan`<br>`[description]`<br>★ | plan<br>계획 | 계획 모드로 들어갑니다. Claude가 수정하기 전에 조사하고 계획을 제안합니다. 설명을 붙이면 그 작업을 바로 시작합니다. | 큰 변경 전에: `/plan 인증 버그 수정`. 계획을 검토한 뒤 승인합니다. |
| `/resume`<br>`[session]`<br>★ | resume<br>재개·이어서 하기 | ID나 이름으로 대화를 다시 열거나, 세션 선택 화면을 엽니다. 백그라운드 세션에는 `bg` 표시가 붙습니다.<br>별칭: `/continue` | 어제 작업 도중 노트북을 닫았다면: `/resume`으로 어제 대화를 골라 이어서 합니다. |
| `/rewind`<br>★ · ⇄ 파일을 대량 변경 | rewind<br>되감기 | 대화나 코드(또는 둘 다)를 이전 체크포인트로 되돌리거나, 선택한 메시지부터 요약합니다.<br>별칭: `/checkpoint`, `/undo` | Claude가 여러 파일을 망가뜨렸다면: `/rewind`를 실행하고 수정 전 메시지를 골라 코드와 대화를 함께 되돌립니다. |
| `/autocompact`<br>`[auto\|<tokens>]`<br>v2.1.221 이상 필요 | auto compact<br>자동 압축 | 컨텍스트 창이 얼마나 찼을 때 자동 압축할지 정합니다. 예: `500k`. `auto`는 모델에 맞춘 기본값으로 되돌립니다. 사용자 설정에 저장되고 바로 적용됩니다. | 긴 작업이 잦은 압축으로 끊길 때: `/autocompact 500k`. |
| `/branch`<br>`[name]` | branch<br>분기·브랜치 | 이 지점에서 대화를 분기하고 그쪽으로 전환합니다. 원래 대화는 보존되며 `/resume`으로 돌아갈 수 있습니다. (Git 브랜치가 아니라 대화의 분기입니다.) | 두 가지 방법 중 고민될 때: `/branch B안-시도`. 실패하면 원래 대화로 돌아가 A안을 계속합니다. |
| `/btw`<br>`[question]` | by the way<br>그런데·참고로 | 현재 세션에 대해 곁가지 질문을 하되, 그 내용을 대화에는 추가하지 않습니다. 질문 없이 실행하면 가장 최근의 곁가지 질문을 보여 줍니다. | 작업 중에 오류의 뜻만 알고 싶을 때: `/btw 이 404는 무슨 뜻이야`. 본 작업의 흐름이 흐트러지지 않습니다. |
| `/copy`<br>`[N]` | copy<br>복사 | 마지막 응답을 클립보드에 복사합니다. `/copy 2`는 끝에서 두 번째 응답을 복사합니다. 코드 블록이 있으면 선택 화면에서 블록 하나만 복사할 수 있고, `w`를 누르면 대신 파일로 저장합니다(SSH 접속 중에 편리). | Claude가 써 준 코드 조각이나 명령을 `/copy`로 복사해 필요한 곳에 붙여 넣습니다. |
| `/export`<br>`[filename]`<br>⚿ 비밀 정보 노출 가능 | export<br>내보내기 | 대화를 일반 텍스트로 내보냅니다. 이름을 주면 바로 파일로 저장하고, 아니면 복사/저장 대화상자를 엽니다. | 도움이 된 디버깅 기록을 보관할 때: `/export 디버깅-기록.txt`. |
| `/goal`<br>`[condition\|clear]` | goal<br>목표 | 목표를 설정합니다. 조건이 충족되거나 목표가 해제될 때까지 Claude가 여러 턴에 걸쳐 계속 작업합니다. 인수 없이 실행하면 현재 목표를 보여 주고, `clear`(또는 `stop`, `off` 등)로 목표를 지웁니다. | `/goal 모든 테스트 통과`로 설정하고, 테스트가 모두 통과할 때까지 반복하게 둡니다. |
| `/memory` | memory<br>기억·메모리 | `CLAUDE.md` 메모리 파일을 편집하고, 자동 메모리를 켜고 끄며, 자동 메모리 항목을 보여 줍니다. | 항상 한국어로 답하게 하고 싶다면: `/memory`를 열고 "항상 한국어로 답해 줘" 같은 줄을 추가합니다. |
| `/recap` | recap<br>요약·정리 | 현재 세션을 한 줄로 요약해 줍니다. 원할 때 바로 실행할 수 있습니다. | 회의에서 돌아와 어디까지 했는지 잊었을 때: `/recap`. |
| `/rename`<br>`[name]` | rename<br>이름 바꾸기 | 세션 이름을 바꾸고 프롬프트 바에 표시합니다. 이름 없이 실행하면 대화 내용으로 이름을 만들어 줍니다. | 세션을 여러 개 열어 둘 때: `/rename 백테스트`로 바꿔 두면 `/resume`에서 찾기 쉽습니다. |

## 모델과 추론

모델, 추론 노력 수준, 속도를 바꿉니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/model`<br>`[model]`<br>★ | model<br>모델 | 모델을 바꾸고 새 세션의 기본값으로 저장합니다. 인수 없이 실행하면 선택 화면이 열립니다. 지원되는 모델에서는 좌우 키로 노력 수준을 조절하고, 행에서 `s`를 누르면 이 세션에서만 바꿉니다. | 작은 수정은 빠른 모델로 하고, 버그가 어려워지면 `/model opus`로 바꿉니다. |
| `/advisor`<br>`[model\|off]` | advisor<br>조언자 | 중요한 순간에 두 번째 모델에게 의견을 묻는 advisor 도구를 켜거나 끕니다. `fable`, `opus`, `sonnet` 또는 전체 모델 ID를 받습니다(`fable`은 접근 권한이 필요). 인수 없이 실행하면 선택 화면이 열립니다. | 평소에는 빠른 모델로 작업하고, 중요한 판단에서만 더 강한 모델의 의견을 받을 때: `/advisor opus`. |
| `/effort`<br>`[level\|auto\|status\|ultracode [on\|off]]` | effort<br>노력 수준 (추론의 깊이) | 노력 수준을 정합니다: `low`부터 `xhigh`까지의 단계, `max`, `auto` 중 하나. `status`는 현재 값을 표시합니다. `max`는 이 세션에서만 유효합니다. `ultracode on\|off`로 ultracode를 켜고 끕니다. | 재현이 어려운 버그를 찾을 때: `/effort high`, 오타만 고칠 때: `/effort low`. |
| `/fast`<br>`[on\|off]` | fast<br>빠르게 | 빠른 모드를 켜고 끕니다(같은 모델, 더 빠른 출력). 응답 도중에도 바꿀 수 있으며, 진행 중인 턴은 원래 속도로 끝납니다. 요금은 공식 빠른 모드 문서를 확인하세요. | 시간이 촉박할 때: `/fast on`, 그렇지 않을 때: `/fast off`. |
| `/output-style`<br>`[style]`<br>v2.1.269 이상 필요 | output style<br>출력 스타일 | 출력 스타일 목록을 보여 주거나 하나로 바꿉니다. 예: `/output-style concise`. | 먼저 인수 없이 `/output-style`을 실행해 무엇이 있는지 보고, 하나를 고릅니다(예: 더 간결한 스타일). |

## 프로젝트와 파일

프로젝트 메모리를 설정하고, 폴더를 추가하고, 변경 사항을 검토합니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/init`<br>★ | initialize<br>초기화 | 새 세션마다 읽는 `CLAUDE.md` 안내 파일로 프로젝트를 초기화합니다. Codex나 Gemini CLI 설정을 찾으면 `/import`를 제안합니다. | 새 저장소에서 가장 먼저: `/init`. 그다음 `/memory`로 내용을 다듬습니다. |
| `/add-dir`<br>`<path>` | add directory<br>폴더 추가 | 이동하지 않고 이 세션에서 파일에 접근할 작업 폴더를 추가합니다. 경로 일부를 입력하고 `Tab`을 누르면 자동 완성됩니다. 추가한 폴더의 `.claude/` 설정은 대부분 인식되지 않으며, 네트워크 경로는 대부분 추가할 수 없습니다. | 프런트엔드와 백엔드가 나란히 있을 때: `/add-dir ../backend`. |
| `/cd`<br>`<path>` | change directory<br>폴더 이동 | 대화를 유지한 채 세션을 새 작업 폴더로 옮깁니다. `/add-dir`와 달리 `/cd`는 세션이 있는 위치 자체를 바꿉니다. | 엉뚱한 폴더에서 시작했다면 처음부터 다시 하지 말고: `/cd ~/projects/website`. |
| `/diff` | difference<br>차이·변경 내역 | 작업 트리의 변경 사항을 검토합니다. 지금까지 Claude가 수정한 내용도 포함됩니다. | 커밋하기 전에 `/diff`로 정확히 무엇이 바뀌었는지 확인합니다. |
| `/import`<br>`[codex\|gemini\|cursor] [--dry-run] [--yes]`<br>⇄ 파일을 대량 변경 | import<br>가져오기 | OpenAI Codex, Gemini CLI, Cursor에서 지침 파일, MCP 서버, 명령, 서브에이전트, 스킬을 가져옵니다. `--dry-run`은 미리 보기만 합니다. 일부 클라우드 제공업체에서는 사용할 수 없고, Cursor 가져오기는 v2.1.265 이상이 필요합니다. | Cursor에서 옮겨 올 때: 먼저 `/import cursor --dry-run`으로 확인한 뒤 실제로 가져옵니다. |
| `/insights` | insights<br>인사이트·분석 | 이 컴퓨터의 최근 세션을 HTML 보고서로 만들어 줍니다: 프로젝트, 사용 습관, 자주 막히는 곳, 써 볼 만한 기능. 클라우드 세션에서는 사용할 수 없습니다. | 몇 주 사용한 뒤 `/insights`로 아직 써 보지 않은 기능을 찾아봅니다. |
| `/team-onboarding`<br>⚿ 비밀 정보 노출 가능 | team onboarding<br>팀 온보딩 (새 팀원 맞이하기) | 최근 30일간의 세션, 명령, MCP 사용 내역을 분석해서, 새 팀원이 첫 메시지로 붙여 넣을 수 있는 Markdown 가이드를 작성합니다. | 새 팀원이 합류하면: `/team-onboarding`을 실행하고 가이드를 보내 줍니다. |

## 리뷰와 검증

버그와 취약점을 찾고, 코드를 정리하고, 앱을 실행해 확인합니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/code-review`<br>`[low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]`<br>★ · 스킬 · ¥ 비용이 들 수 있음 · ↗ 외부로 데이터 전송 · ⇄ 파일을 대량 변경 | code review<br>코드 리뷰 | 현재 diff, 또는 PR·브랜치·경로를 대상으로 정확성 버그를 검토합니다. `--fix`는 지적 사항을 적용하고, `--comment`는 GitHub PR이나 GitLab MR에 댓글을 남기며, `ultra`는 클라우드에서 심층 리뷰를 실행합니다.<br>별칭: `/review` | 커밋 전에: `/code-review high --fix`. PR을 검토할 때: `/code-review high 1234`. |
| `/run`<br>스킬 | run<br>실행 | 프로젝트의 앱을 실행하고 조작해서 변경이 동작하는 모습을 확인합니다. | `/run`으로 사이트를 띄우고 새 홈페이지의 스크린샷을 찍게 합니다. |
| `/run-skill-generator`<br>스킬 | skill generator<br>스킬 생성기 | 깨끗한 환경에서 앱을 빌드, 실행, 조작하는 방법을 `/run`과 `/verify`에 알려 주는 프로젝트 전용 스킬을 작성합니다. | 시작 절차가 여러 단계일 때(먼저 데이터베이스 실행 등): 한 번 실행해 두면 이후 `/run`만으로 됩니다. |
| `/security-review` | security review<br>보안 리뷰 | 현재 브랜치와 origin 기본 브랜치의 diff를 분석해 인젝션, 인증 문제, 데이터 노출 같은 취약점을 찾습니다. `origin` 원격 저장소가 필요합니다. | 인증, 결제, 사용자 데이터와 관련된 변경을 배포하기 전에 실행합니다. |
| `/simplify`<br>`[target]`<br>스킬 · ⇄ 파일을 대량 변경 | simplify<br>단순화 | 에이전트 4개가 병렬로 변경된 코드를 재사용, 단순화, 효율, 추상화 수준 관점에서 검토한 뒤 수정을 적용합니다. 정확성 버그는 찾지 않으니, 그런 용도에는 `/code-review`를 사용하세요. | 기능은 동작하는데 코드를 더 깔끔하게 하고 싶을 때: `/simplify`. |
| `/ultrareview`<br>`[PR or branch]`<br>¥ 비용이 들 수 있음 | ultra review<br>울트라 리뷰 (초정밀 리뷰) | 클라우드 샌드박스에서 여러 에이전트가 심층 리뷰를 합니다. 권장 형식은 `/code-review ultra`이고, `/ultrareview`는 별칭입니다. Pro, Max, Ultra에서 무료 3회가 포함되며, 그 뒤에는 사용량 크레딧이 필요합니다. | 중요한 릴리스 전에: `/code-review ultra`. |
| `/verify`<br>스킬 | verify<br>검증 | 테스트나 타입 검사에만 의존하지 않고, 앱을 빌드하고 실행해서 직접 보며 변경이 제대로 동작하는지 확인합니다. 직접 실행했을 때만 동작합니다. | 버튼 동작을 바꿨다면: `/verify`로 실제로 버튼을 눌러 보게 합니다. |

## 병렬 작업과 백그라운드

여러 에이전트를 동시에 실행하거나 작업을 백그라운드로 보냅니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/agents` | agents<br>에이전트 | 서브에이전트를 만들거나 관리하려면 Claude에게 부탁하거나 `.claude/agents/`를 직접 편집하라는 안내를 표시합니다. v2.1.197 이하에서는 대화형 관리 화면을 열었습니다. | 그냥 부탁하면 됩니다: "테스트만 작성하는 서브에이전트를 만들어 줘." |
| `/background`<br>`[prompt]` | background<br>백그라운드 | 세션을 분리해 백그라운드 에이전트로 실행하고 터미널을 비워 줍니다. 그 전에 지시를 하나 더 보낼 수도 있습니다. `claude agents`로 상태를 지켜봅니다.<br>별칭: `/bg` | 30분 걸리는 작업이라면: `/bg 끝나면 결과를 report.md에 써 줘`. |
| `/batch`<br>`<instruction>`<br>스킬 · ⇄ 파일을 대량 변경 | batch<br>일괄 처리 | 큰 변경을 병렬로 진행합니다: 먼저 코드베이스를 조사해 작업을 독립된 단위 5~30개로 나누고 계획을 보여 줍니다. 승인하면 단위마다 백그라운드 서브에이전트가 자체 worktree에서 구현하고 테스트합니다. git 저장소 또는 WorktreeCreate 훅이 필요합니다. | `/batch src/를 JavaScript에서 TypeScript로 이전`. |
| `/fork`<br>`[prompt]` | fork<br>포크 (복제) | 대화를 새 백그라운드 세션으로 복사하고, 사용자는 여기서 계속 작업할 수 있습니다. 프롬프트를 주면 복사본이 바로 시작하며, 보통 먼저 자체 worktree를 만들도록 지시받습니다. | 기능 A를 작업하면서 작은 수정도 동시에 하고 싶을 때: `/fork 푸터 정렬 고쳐 줘`. |
| `/list-agents`<br>v2.1.224 이상 필요 | list agents<br>에이전트 목록 | Claude가 메시지를 보낼 수 있는 서브에이전트, 팀원, 다른 세션을 각각 부를 이름과 함께 나열합니다. 세션 간 메시지 기능이 켜진 곳에서만 쓸 수 있습니다.<br>별칭: `/peers` | 여러 세션을 함께 운영할 때 각각의 이름을 확인합니다. |
| `/stop` | stop<br>정지 | 연결된 백그라운드 세션을 정지합니다. 대화 기록과 worktree는 남습니다. 정지하지 않고 분리만 하려면 `/exit`를 쓰거나 `←`를 누르세요. | 백그라운드 작업이 엉뚱한 방향으로 갈 때: `/stop`. |
| `/subtask`<br>`<task>` | subtask<br>하위 작업 | 대화를 물려받는 포크된 서브에이전트를 만들고, 결과를 이곳에 보고하게 합니다. `/fork`와의 차이: `/subtask`는 결과를 이곳에 보고하고, `/fork`는 별도의 세션을 만듭니다. | 코딩을 계속하면서: `/subtask 이 API 엔드포인트들 문서화해 줘`. |
| `/tasks` | tasks<br>작업 목록 | 이 세션의 백그라운드 작업을 보고 관리합니다. 끝난 서브에이전트도 포함됩니다.<br>별칭: `/bashes` | 백그라운드에서 돌리는 테스트나 서브에이전트의 진행 상황을 `/tasks`로 확인합니다. |
| `/workflow-authoring`<br>스킬 | workflow authoring<br>워크플로 작성 | 동적 워크플로 스크립트를 작성하기 위한 참고 자료를 불러옵니다. 보통은 Claude가 알아서 불러오며, 저장된 스크립트를 직접 고치기 전에 실행하세요. 동적 워크플로가 켜진 곳에서만 쓸 수 있습니다. | 저장된 워크플로 스크립트를 직접 고치기 전에. |
| `/workflows` | workflows<br>워크플로 | 워크플로 진행 화면을 열어, 실행 중이거나 완료된 워크플로를 지켜보고, 일시 정지, 재개, 저장할 수 있습니다. | 오래 걸리는 워크플로를 지켜볼 때 사용합니다. |

## 자동화와 예약

일정 간격으로 반복하고, 예약 실행하고, Pull Request를 자동 수정합니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/loop`<br>`[interval] [prompt]`<br>★ · 스킬 | loop<br>반복 | 세션이 열려 있는 동안 프롬프트를 반복해서 실행합니다. 간격을 생략하면 Claude가 스스로 속도를 정하고, 프롬프트를 생략하면 기본 제공 유지 관리 프롬프트나 `loop.md`를 실행합니다.<br>별칭: `/proactive` | `/loop 5m 배포가 끝났는지 확인해 줘`. 컴퓨터가 꺼져 있어도 계속 실행하려면 `/schedule`을 사용하세요. |
| `/autofix-pr`<br>`[prompt]`<br>↗ 외부로 데이터 전송 | auto-fix PR<br>PR 자동 수정 | 현재 브랜치의 PR을 지켜보다가 CI 실패나 리뷰 댓글이 생기면 수정을 푸시하는 클라우드 세션을 시작합니다. `gh` CLI와 클라우드 세션이 필요합니다. | `/autofix-pr lint와 타입 오류만 고쳐 줘`. |
| `/deep-research`<br>`<question>`<br>워크플로 | deep research<br>심층 리서치 | 웹 검색을 여러 갈래로 수행하고, 출처를 가져와 교차 확인한 뒤, 출처가 달린 보고서를 쓰는 기본 제공 워크플로입니다. 백그라운드에서 실행됩니다. | `/deep-research 주요 AI 영상 도구의 가격과 품질 비교`. |
| `/schedule`<br>`[description]` | schedule<br>예약·일정 | 안내형 대화를 통해 클라우드 예약 작업(이전 이름: routines)을 만들고, 수정하고, 나열하고, 실행합니다. Console API 키로는 사용할 수 없습니다.<br>별칭: `/routines` | `/schedule 평일 매일 오전 9시에 저장소의 새 이슈를 요약해 줘`. |

## 아티팩트, 슬라이드, 디자인

공유할 수 있는 페이지, 발표 자료, 디자인, 차트를 만듭니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/artifact-capabilities`<br>스킬 | artifact capabilities<br>아티팩트 기능 | 커넥터 호출이나 다운로드 제공 같은 아티팩트 실행 기능에 대한 참고 자료와, 내 계정에서 쓸 수 있는 기능을 불러옵니다. 보통은 Claude가 알아서 불러옵니다. | 여러 사람이 입력하는 페이지를 만들기 전에. |
| `/artifact-diagramming`<br>스킬 · v2.1.221 이상 필요 | artifact diagramming<br>아티팩트 다이어그램 | 아티팩트용 다이어그램 안내를 불러옵니다: 다이어그램이 도움이 되는 경우, 무엇을 그릴지, 밝은 테마와 어두운 테마 모두에서 잘 보이는 SVG. | 알아보기 쉬운 아키텍처 다이어그램이 필요할 때. |
| `/artifacts` | artifacts<br>아티팩트 (공개 페이지) | 내가 소유하거나 공유받은 아티팩트를 나열하고, 하나를 연결하거나, 열거나, 링크를 복사합니다. 아티팩트를 쓸 수 있는 곳에서만 동작합니다. | 지난주에 만든 대시보드를 찾아 이어서 편집합니다. |
| `/dataviz`<br>`[request]`<br>스킬 | data visualization<br>데이터 시각화 | 차트 디자인 안내: 차트 형태를 고르고, 역할에 따라 색을 지정하며, 함께 제공되는 스크립트로 색맹 안전성과 대비를 기준으로 팔레트를 검증합니다. | `/dataviz 이 월별 매출 표를 추이 차트로 만들어 줘`. |
| `/design`<br>`[brief]`<br>스킬 · v2.1.265 이상 필요 | design<br>디자인 | UI 목업, 화면 흐름, 랜딩 페이지, 포스터를 하나의 캔버스 위 아트보드로 초안 작성합니다(Claude Design 아티팩트). 데스크톱 브라우저에서 편집하고 PNG나 PDF로 내보냅니다. Bedrock, Vertex 등 서드파티 플랫폼에서는 사용할 수 없습니다. | `/design 모바일 뱅킹 앱의 설정 화면`. |
| `/design consent` | consent / revoke<br>동의 / 철회 | Claude의 Claude Design 접근을 허용하거나 철회합니다. Claude가 `/design consent`를 실행하라고 하면 직접 입력하세요.<br>별칭: `/design revoke` | 요청을 받으면 `/design consent`를 직접 입력합니다. |
| `/design-login` | design login<br>디자인 로그인 | `/design-sync`나 `/design consent`가 요청할 때, claude.ai 계정으로 `/design-sync`의 디자인 시스템 접근을 승인합니다. | `/design-sync`가 로그인을 요청할 때 실행합니다. |
| `/design-sync`<br>`[hint]`<br>스킬 · ↗ 외부로 데이터 전송 | design sync<br>디자인 동기화 | 저장소의 React 디자인 시스템을 변환해 Claude Design에 업로드하여, 디자인에 실제 컴포넌트가 쓰이게 합니다. 큰 저장소에서는 첫 동기화에 몇 시간이 걸릴 수 있습니다. 대상은 독립된 claude.ai/design 사이트이며, 이 사이트는 2026년 12월 14일까지 종료됩니다. | `/design-sync Acme DS` (위의 종료 날짜에 주의하세요). |
| `/slides`<br>`[brief]`<br>스킬 · v2.1.265 이상 필요 | slides<br>슬라이드 | 요청 내용을 바탕으로 Claude Slides 아티팩트를 만듭니다. 아티팩트를 쓸 수 있는 세션과 Slides 템플릿을 쓸 수 있는 계정이 필요합니다. | `/slides 경영진용 분기 리뷰, 8장`. |

## 플러그인, 스킬, 연동

플러그인, 스킬, MCP 서버, 브라우저와 IDE 연동으로 Claude의 기능을 넓힙니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/mcp`<br>`[reconnect (<server>\|all)\|enable\|disable [<server>\|all]]`<br>★ | MCP (Model Context Protocol)<br>MCP (Model Context Protocol, 외부 도구 연결 표준) | MCP 서버 연결과 OAuth를 관리합니다. 인수 없이 실행하면 목록이 열리고, `reconnect`, `enable`, `disable`에 서버 이름이나 `all`을 붙이면 바로 실행합니다. | 커넥터가 실패했거나 인증이 필요할 때: `/mcp reconnect all`. |
| `/chrome` | Chrome<br>Chrome 브라우저 | Claude in Chrome 설정을 구성합니다. | Chrome 확장 프로그램을 처음 연결할 때. |
| `/claude-api`<br>`[subcommand]`<br>스킬 | Claude API<br>Claude API | 프로젝트 언어에 맞는 Claude API와 Managed Agents 참고 자료를 불러옵니다. 코드가 `anthropic`을 import하면 자동으로 활성화됩니다. 하위 명령으로 `migrate`, `upgrade`, `cost-optimize`, `build-eval`, `prompt-audit` 등이 있습니다. | 앱의 API 비용을 줄이고 싶을 때: `/claude-api cost-optimize`. |
| `/claude-in-chrome`<br>`[task]`<br>스킬 · ↗ 외부로 데이터 전송 | Claude in Chrome<br>Chrome에서 동작하는 Claude | Claude in Chrome을 통해 브라우저에서 Claude가 작업을 수행하게 합니다. 예: 페이지 테스트, 콘솔 로그 읽기. Chrome 연동이 필요합니다(예: `claude --chrome`). | `/claude-in-chrome 로컬 사이트에서 회원가입 흐름을 테스트하고 오류를 알려 줘`. |
| `/ide` | IDE (integrated development environment)<br>IDE (통합 개발 환경, 코드 편집기) | IDE 연동을 관리하고 상태를 보여 줍니다. | 편집기에 Claude의 수정 내용이 보이지 않을 때 연결을 확인합니다. |
| `/install-github-app`<br>↗ 외부로 데이터 전송 · ⚑ 안전 설정 변경 | install GitHub app<br>GitHub 앱 설치 | 저장소에 Claude GitHub App을 설치하고, 원하면 GitHub Actions 워크플로와 시크릿도 설정합니다. github.com 전용입니다. | 이슈와 PR에서 Claude를 멘션해 그곳에서 작업하게 하고 싶을 때. |
| `/install-slack-app` | install Slack app<br>Slack 앱 설치 | 브라우저 OAuth 과정을 통해 Claude Slack 앱을 설치합니다. | 팀에서 Slack으로 Claude를 쓰고 싶을 때. |
| `/plugin`<br>`[subcommand]` | plugin<br>플러그인 | 플러그인을 관리합니다. 인수 없이 실행하면 메뉴가 열리고, `list`, `install`, `enable`, `disable`은 바로 실행합니다. 설치 요약에 안내가 나오면 `/reload-plugins`를 실행하세요. | `/plugin`으로 둘러보고 내 작업에 맞는 플러그인을 설치합니다. |
| `/plugin-authoring`<br>스킬 · v2.1.287 이상 필요 | plugin authoring<br>플러그인 작성 | mod(확장) 작성용 참고 자료를 불러옵니다. 기본 제공 플러그인에 들어 있는 스킬이며, `/plugin`에서 끌 수 있습니다. | 채팅 옆에 항상 떠 있는 작은 패널을 만들고 싶을 때. |
| `/reload-plugins`<br>`[--force]` | reload plugins<br>플러그인 다시 불러오기 | 재시작 없이 활성 플러그인을 다시 불러오고, 불러오기 오류를 알려 줍니다. 다시 불러오면 로드된 MCP 도구가 바뀌어 프롬프트 캐시가 무효화되는 경우, `--force`를 주지 않는 한 경고하고 건너뜁니다. | 플러그인을 설치한 직후, 다시 불러오라는 안내가 나올 때. |
| `/reload-skills` | reload skills<br>스킬 다시 불러오기 | 스킬과 명령 폴더를 다시 검색해서, 세션 중에 추가하거나 바꾼 스킬을 재시작 없이 쓸 수 있게 합니다. | 직접 만든 스킬을 방금 작성했고 바로 쓰고 싶을 때. |
| `/skill-doctor`<br>v2.1.252 이상 필요 | skill doctor<br>스킬 진단 | 각 스킬의 컨텍스트 비용과 사용량을 보여 주어, 꺼도 될 스킬을 찾게 해 줍니다. | 주기적으로 실행해 안 쓰는 스킬을 정리합니다. |
| `/skills` | skills<br>스킬 | 스킬 목록을 필터와 함께 보여 줍니다. `t`는 토큰 수로 정렬하고, `Space`/`Enter`는 스킬이 Claude와 `/` 메뉴에 보이는 방식을 순서대로 바꾸며, `Esc`는 저장하고 닫습니다. | 스킬이 너무 많을 때: `/skills`에서 `t`를 눌러 정렬하고, 무겁고 안 쓰는 스킬을 숨깁니다. |

## 권한과 안전

Claude가 할 수 있는 일과 내 승인이 필요한 일을 정합니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/permissions`<br>★ · ⚑ 안전 설정 변경 | permissions<br>권한 | 도구에 대한 허용, 확인, 거부 규칙을 관리합니다: 범위별로 보기, 규칙 추가·삭제, 작업 폴더 관리, 최근 자동 모드 거부 내역과 분류기 규칙 검토.<br>별칭: `/allowed-tools` | 매번 `npm test` 실행을 승인하기 귀찮다면 여기서 허용합니다. |
| `/auto-mode-setup`<br>⚑ 안전 설정 변경 | auto mode setup<br>자동 모드 설정 | 프로젝트와 최근 세션을 바탕으로 `autoMode.environment` 항목 초안을 만들어, 검토 후 저장할 수 있게 합니다. 버전과 플랜 요구 사항이 있습니다. | 자동 모드가 평소 하는 작업을 계속 막을 때. |
| `/fewer-permission-prompts`<br>스킬 · ⚑ 안전 설정 변경 | fewer permission prompts<br>권한 확인 줄이기 | 대화 기록에서 자주 쓰는 읽기 전용 Bash 및 MCP 호출을 찾아, 우선순위가 매겨진 허용 목록을 프로젝트 `.claude/settings.json`에 추가합니다. | 승인 요청이 계속 작업을 끊을 때 한 번 실행합니다. |
| `/hooks` | hooks<br>훅 (정해진 시점에 자동 실행되는 스크립트) | 훅 설정을 보여 줍니다. | 훅 때문에 수정할 때마다 문제가 생기는 것 같을 때, 무엇이 설정되어 있는지 확인합니다. |
| `/privacy-settings` | privacy settings<br>개인정보 설정 | 개인정보 설정을 보고 변경합니다. Pro, Max, Ultra 전용입니다. | 내 데이터가 어떻게 쓰이는지 확인할 때. |
| `/sandbox`<br>⚑ 안전 설정 변경 | sandbox<br>샌드박스 (격리 환경) | 샌드박스 모드를 켜고 끕니다. 지원되는 플랫폼에서만 쓸 수 있습니다. | 잘 모르는 스크립트를 실행하기 전에 켭니다. |
| `/update-config`<br>`[request]`<br>스킬 · ⚑ 안전 설정 변경 | update config<br>설정 업데이트 | 설정 변경 내용(명령 허용, 환경 변수 설정, 훅 추가)을 말로 설명하면, Claude가 해당 `settings.json`을 편집합니다. 테마와 모델은 `/config`를 사용하세요. | `/update-config 파일을 수정할 때마다 prettier 실행`. |

## 설정과 화면

테마, 색, 상태 표시줄, 단축키, 음성

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/color`<br>`[color\|default]` | color<br>색 | 이 세션의 프롬프트 바 색을 정합니다: `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` 중 하나. `default`는 초기화하고, 인수 없이 실행하면 무작위 색을 고릅니다. | 운영 환경을 다루는 세션은 `/color red`로 표시해 둡니다. |
| `/config`<br>`[key=value ...]` | config<br>설정 | 테마, 모델, 출력 스타일 등을 바꾸는 설정 화면을 열거나, `key=value` 형식으로 바로 설정합니다. 예: `/config theme=dark`. `/config --help`는 키 목록을 보여 줍니다.<br>별칭: `/settings` | `/config theme=dark`. |
| `/focus` | focus<br>집중 보기 | 마지막 프롬프트, 한 줄짜리 도구 요약, 최종 응답만 보여 주는 화면을 켜고 끕니다. 전체 화면 렌더링에서만 쓸 수 있습니다. | 중간 과정은 숨기고 결과만 보고 싶을 때. |
| `/keybindings` | keybindings<br>키 바인딩 (단축키 설정) | 키보드 단축키 파일을 엽니다. | 익숙한 키로 동작을 다시 지정합니다. |
| `/scroll-speed` | scroll speed<br>스크롤 속도 | 마우스 휠 스크롤 속도를 조절합니다. 전체 화면 렌더링에서만 쓸 수 있으며, JetBrains 터미널에서는 안 됩니다. | 휠을 한 칸 굴렸는데 너무 많이 넘어갈 때 느리게 합니다. |
| `/statusline` | status line<br>상태 표시줄 | 상태 표시줄을 설정합니다. 원하는 내용을 설명하거나, 인수 없이 실행하면 셸 프롬프트를 바탕으로 만들어 줍니다. | `/statusline 모델과 git 브랜치 표시`. |
| `/terminal-setup` | terminal setup<br>터미널 설정 | VS Code, Cursor, Devin Desktop, Alacritty, Zed에서 줄바꿈용 Shift+Enter를 설정합니다. Apple Terminal에서는 Option+Enter를 켜고 경고음을 끄며, iTerm2에서는 `/copy`를 위한 클립보드 접근을 허용합니다. | Enter를 누르면 쓰다 만 프롬프트가 자꾸 전송될 때: 한 번 실행합니다. |
| `/theme` | theme<br>테마 | 색 테마를 바꿉니다: `auto`, 밝은 테마와 어두운 테마, 색맹 친화 테마, ANSI 테마, 사용자 지정 테마. | 밤에는 어두운 테마로 바꿉니다. |
| `/tui`<br>`[default\|fullscreen]` | TUI (text user interface)<br>TUI (텍스트 사용자 인터페이스) | 터미널 렌더러를 정하고, 대화를 유지한 채 다시 실행합니다. `fullscreen`은 화면 깜박임이 없는 렌더러입니다. 인수 없이 실행하면 현재 렌더러를 보여 줍니다. | 화면이 깜박일 때: `/tui fullscreen`. |
| `/voice`<br>`[hold\|tap\|off]` | voice<br>음성 | 음성 받아쓰기를 켜고 끄거나 모드(`hold`, `tap`)를 정합니다. Claude.ai 계정이 필요합니다. | 타이핑 대신 말로 지시합니다. |

## 계정과 사용량

로그인, 한도와 비용 확인, 업그레이드

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/usage`<br>★ | usage<br>사용량 | 세션 비용, 플랜 사용 한도, 활동 통계를 보여 줍니다. 구독 플랜에서 무엇이 한도에 포함되는지도 표시합니다. `/stats`는 Stats 탭을 엽니다.<br>별칭: `/cost`, `/stats` | 더 저렴한 모델로 바꿀지 정하기 전에 `/usage`를 확인합니다. |
| `/login` | log in<br>로그인 | Anthropic 계정에 로그인합니다. | 새 컴퓨터를 쓸 때나 세션이 만료되었을 때. |
| `/logout` | log out<br>로그아웃 | Anthropic 계정에서 로그아웃합니다. | 공용 컴퓨터를 쓴 뒤에. |
| `/passes` | passes<br>초대 패스 | 친구에게 Claude Code 무료 1주일 이용권을 공유합니다. 자격이 있는 계정에만 표시됩니다. | 친구가 써 볼 수 있게 초대합니다. |
| `/rate-limit-options` | rate limit options<br>사용 한도 대처 방법 | claude.ai 한도에 걸려 작업이 막혔을 때 계속하는 방법을 보여 줍니다: 기다렸다가 자동으로 이어서 하기, 사용량 크레딧 추가, 업그레이드. claude.ai 구독이 필요합니다. | 밤새 작업이 막혔다면: 한도가 초기화된 뒤 자동으로 이어서 하기를 선택합니다. |
| `/status` | status<br>상태 | 설정 화면의 Status 탭을 엽니다: 버전, 모델, 계정, 연결 상태. Claude가 응답하는 중에도 동작합니다. | 도움을 요청하기 전에 `/status` 화면을 캡처해 둡니다. |
| `/upgrade` | upgrade<br>업그레이드 | 브라우저에서 업그레이드 페이지를 엽니다. | 한도에 자주 걸릴 때. |
| `/usage-credits`<br>¥ 비용이 들 수 있음 | usage credits<br>사용량 크레딧 | 사용량 크레딧을 설정하거나 요청합니다. 결제 권한이 없는 Team 및 Enterprise 구성원은 관리자에게 요청을 보냅니다. 이전 이름은 `/extra-usage`입니다. | 팀의 사용량이 바닥나면 관리자에게 크레딧을 요청합니다. |

## 클라우드, 원격, 다른 기기

데스크톱, 모바일, 웹, 클라우드 사이에서 작업을 주고받으며 이어 갑니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/desktop` | desktop<br>데스크톱 앱 | Claude Code Desktop 앱에서 세션을 이어갑니다. macOS 또는 x64 Windows와 Claude 구독이 필요합니다.<br>별칭: `/app` | 터미널에서 데스크톱 앱으로 옮겨 갈 때. |
| `/mobile` | mobile<br>모바일 (스마트폰) | Claude 모바일 앱을 내려받을 수 있는 QR 코드를 보여 줍니다.<br>별칭: `/ios`, `/android` | 휴대폰으로 진행 상황을 따라가고 싶을 때. |
| `/remote-control`<br>↗ 외부로 데이터 전송 | remote control<br>원격 조작 | 이 세션을 claude.ai에서 Remote Control로 조작할 수 있게 합니다. claude.ai 구독이 필요합니다.<br>별칭: `/rc` | 작업을 실행해 둔 채 휴대폰으로 지시하고 싶을 때: `/rc`. |
| `/remote-env` | remote environment<br>원격 환경 | CLI에서 시작하는 클라우드 세션의 기본 클라우드 환경을 고릅니다. | 환경이 여러 개일 때 기본값을 정합니다. |
| `/setup-bedrock` | set up Bedrock<br>Bedrock 설정 | 마법사를 통해 Amazon Bedrock 인증, 리전, 모델 고정을 설정합니다. `CLAUDE_CODE_USE_BEDROCK=1`을 설정하기 전에는 메뉴에 보이지 않으니 전체 이름을 직접 입력하세요. | 회사에서 AWS를 통해 Claude를 쓸 때. |
| `/setup-vertex` | set up Vertex<br>Vertex 설정 | 마법사를 통해 Google Cloud의 Agent Platform을 설정합니다. `CLAUDE_CODE_USE_VERTEX=1`을 설정하기 전에는 보이지 않으니 전체 이름을 직접 입력하세요. | 회사에서 Google Cloud를 통해 Claude를 쓸 때. |
| `/teleport` | teleport<br>텔레포트 (순간 이동) | 클라우드 세션을 이 터미널로 가져오고, 그 브랜치와 대화를 받아옵니다. claude.ai 구독이 필요합니다.<br>별칭: `/tp` | 웹에서 시작한 작업을 로컬에서 이어서 합니다. |
| `/web-setup` | web setup<br>웹 설정 | 로컬 `gh` 인증 정보를 사용해 클라우드 세션용 GitHub를 연결합니다. | 처음 클라우드 세션을 쓰기 전에. |

## 진단과 피드백

문제가 생기면 여기서 시작하세요

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/doctor`<br>`[prompt-audit [path]]`<br>★ · 스킬 | doctor<br>닥터 (건강 진단) | 설치, 설정, 확장 기능, `CLAUDE.md`를 점검하고 수정안을 제안하며, 확인하면 Claude가 적용합니다. `prompt-audit`을 붙이면 대신 내 지침을 점검합니다.<br>별칭: `/checkup` | 뭔가 고장 난 것 같을 때: 먼저 `/doctor`부터. |
| `/help`<br>★ | help<br>도움말 | 도움말과 사용할 수 있는 명령을 보여 줍니다. | 명령 이름이 기억나지 않을 때: `/help`, 또는 `/`와 몇 글자를 입력합니다. |
| `/powerup`<br>★ | power up<br>파워업 | 애니메이션 데모로 Claude Code 기능을 가르쳐 주는 대화형 레슨입니다. | 처음 시작하는 사람에게 가장 체계적인 출발점입니다. |
| `/bug`<br>`[report]`<br>↗ 외부로 데이터 전송 · ⚿ 비밀 정보 노출 가능 | bug<br>버그 | 버그를 신고하거나 대화를 공유합니다. 기록을 얼마나 포함할지 직접 고르고, 전송 전에 확인합니다.<br>별칭: `/share` | Claude Code 자체가 이상하게 동작할 때. |
| `/debug`<br>`[description]`<br>스킬 | debug<br>디버그 | 지금부터 디버그 로그를 켜고, 세션 디버그 로그를 읽어 문제를 해결합니다. 문제 내용을 설명할 수도 있습니다. | `/debug MCP 서버 연결이 계속 실패해`. |
| `/exit` | exit<br>종료 | CLI를 종료합니다. 연결된 백그라운드 세션에서는 분리만 되고 세션은 계속 실행됩니다.<br>별칭: `/quit` | 오늘 작업을 마칠 때. |
| `/feedback`<br>`[report]`<br>↗ 외부로 데이터 전송 · ⚿ 비밀 정보 노출 가능 | feedback<br>피드백 | `/bug`와 같은 대화상자와 동의 단계를 거쳐 제품 피드백을 보냅니다. | 원하는 기능을 요청합니다. |
| `/heapdump`<br>⚿ 비밀 정보 노출 가능 | heap dump<br>힙 덤프 (메모리 기록) | 메모리 사용량이 높을 때 진단할 수 있도록 힙 스냅샷과 메모리 내역을 바탕 화면(Desktop 폴더)에 저장합니다. `-diagnostics.json`만 공유하세요. `.heapsnapshot`에는 대화 내용과 인증 정보가 들어 있습니다. 메뉴에는 보이지 않습니다. | 메모리 사용량이 폭증했을 때 신고용으로. |
| `/release-notes` | release notes<br>릴리스 노트 | 버전 선택 화면에서 변경 내역을 봅니다. 내용은 Claude의 컨텍스트에 들어가지 않습니다. | 업데이트 후 새로운 점을 확인합니다. |
| `/restart`<br>v2.1.288 이상 필요 | restart<br>재시작 | 설치된 업데이트를 적용하기 위해 Claude Code를 재시작하고 세션을 이어갑니다. Pro, Max 또는 Ultra와 macOS·Linux 네이티브 설치(WSL 제외)가 필요합니다.<br>별칭: `/update` | 업데이트 후 하단에 안내가 나올 때. |

## 기타

작은 부가 기능

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/radio` | radio<br>라디오 | 브라우저에서 Claude FM lo-fi 라디오를 열거나, 스트림 URL을 출력합니다. | 작업 중 배경 음악으로. |
| `/stickers` | stickers<br>스티커 | Claude Code 스티커를 주문합니다. | 노트북을 꾸밉니다. |

## 제거됨

예전 가이드에는 나오지만 이제는 쓸 수 없습니다

| 명령 | 영어 단어 | 하는 일 | 추천 사용법 |
|---|---|---|---|
| `/pr-comments`<br>`[PR]`<br>v2.1.91에서 제거됨 | PR comments<br>PR 댓글 | v2.1.91에서 제거되었습니다. Pull Request 댓글을 보려면 Claude에게 직접 부탁하세요. | 평소 말로 부탁하세요. |
| `/ultraplan`<br>`<prompt>` | ultra plan<br>울트라 플랜 | 제거되었습니다. 대신 계획 모드(`/plan`)를 사용하세요. | `/plan`을 사용하세요. |
| `/vim`<br>v2.1.92에서 제거됨 | Vim<br>Vim (키보드 중심 편집 방식) | v2.1.92에서 제거되었습니다. `/config` → Editor mode를 사용하세요. | `/config`를 사용하세요. |

## 면책 조항

1. **비공식 프로젝트**: 커뮤니티가 만든 프로젝트로, Anthropic과 제휴하거나 후원 또는 보증을 받지 않았습니다. “Claude”, “Claude Code” 및 관련 표장은 Anthropic의 상표이며, 여기서는 설명하는 제품을 가리키기 위해서만 사용합니다.
2. **오래되었거나 틀릴 수 있음**: 모든 설명은 공식 문서를 쉽게 풀어 쓴 것이며, 명시적이든 묵시적이든 어떠한 보증도 없이 “있는 그대로” 제공됩니다. Claude Code는 자주 바뀌며, 명령이 추가되거나 이름이 바뀌거나 제거됩니다. 이 프로젝트와 공식 문서가 다르면 공식 문서가 우선합니다.
3. **사용에 따른 책임은 본인에게 있음**: 일부 명령은 파일을 바꾸거나 되돌리고, 명령을 실행하고, 코드를 푸시하고, 외부 서비스로 데이터를 보내거나, 유료 사용량을 소비합니다. 명령이 무엇을 하는지 이해한 뒤 실행하고, 먼저 커밋하거나 백업하세요. 검토 없이 운영 시스템, 중요한 데이터, 다른 사람의 저장소에 사용하지 마세요.
4. **비밀 정보와 개인정보 보호**: API 키, 비밀번호, 토큰, 다른 사람의 개인정보를 프롬프트에 넣지 마세요. 내보낸 대화, 버그 신고, 메모리 스냅샷에 이런 정보가 들어 있을 수 있으니 공유하기 전에 검토하세요.
5. **예시는 참고용**: “추천 사용법”의 예시는 용도를 설명하기 위한 것이며, 사용자 환경에 맞춘 지시가 아닙니다. 사용할 수 있는지는 버전, 플랜, 플랫폼, 조직 정책에 따라 다릅니다.
6. **이 페이지는 사용자를 추적하지 않음**: 이 페이지는 쿠키, 분석 도구, 서드파티 스크립트나 글꼴을 사용하지 않습니다. 언어와 테마 설정만 브라우저에 로컬로 저장합니다.
7. **책임의 제한**: 법이 허용하는 최대 범위에서, 작성자와 기여자는 이 프로젝트의 사용으로 생긴 어떠한 손해(데이터 손실, 요금, 보안 사고, 서비스 중단 포함)에 대해서도 책임지지 않습니다.

## 이 프로젝트에 대해

- **출처**: 공식 [명령 참고 문서](https://code.claude.com/docs/en/commands)를 바탕으로 풀어 썼습니다(확인일 2026-11-03). 설명은 간략화한 것이며 공식 번역이 아닙니다. 차이가 있으면 공식 문서가 우선합니다.
- **데이터**: 모든 내용은 [`data/commands.json`](data/commands.json)에서 생성됩니다. JSON을 편집한 뒤 `python3 scripts/build.py`를 실행하세요.
- **기여**: [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.
- **라이선스**: 내용은 [CC BY 4.0](LICENSE-CONTENT), 코드는 [MIT](LICENSE).
