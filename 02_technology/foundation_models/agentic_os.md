# Agentic OS
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Anthropic Claude Computer Use`는 2024년 10월 `Claude 3.5 Sonnet`에서 프리뷰로 도입된 뒤, `Claude Opus 4.6 (2026-02-05)`, `Claude Sonnet 4.6 (2026-02-17)`에서 에이전트 코딩·툴 사용·컴퓨터 사용 벤치마크를 석권했다. Sonnet 4.6은 `1M 토큰` 컨텍스트를 제공한다. Anthropic의 연매출은 `2026-02` 기준 약 `$14B` 수준까지 성장했다.
- `OpenAI Operator`는 `2025-01-23` 공개, Pro 유저 대상 `2025-02-01` 출시되었고, 내부적으로 `Computer-Using Agent (CUA)`를 사용한다. `2025-07-17` `ChatGPT Agent`로 통합되면서 `2025-08-31` Operator 별도 사이트는 종료, ChatGPT 내 `Agent mode` 툴로 Pro/Plus/Team 전원 접근 가능해졌다.
- `Google Project Mariner`는 Gemini 2.0 기반 웹 에이전트로, `WebVoyager` 벤치마크 `83.5%`를 기록하며 `2025-05` Google AI Ultra 구독자에 공개, Gemini API/Vertex AI에 통합되었다. 최대 `10개` 작업 동시 병렬 실행을 지원하며, Project Mariner 팀 상당수가 Gemini Agent 제품으로 흡수되었다.
- `Apple Intelligence`는 `iOS 26/iPadOS 26/macOS Tahoe 26/visionOS 2.4`에 확장되었고, Siri의 "앱을 지휘하는(orchestrating apps)" 컨텍스트 인지 시스템 에이전트로의 재정의가 진행 중이다. 다만 고급 기능 일부는 공식적으로 롤아웃 지연이 있었다.
- 현재 상태 해석:
  - 확인된 사실: 주요 4사가 모두 에이전트형 인터페이스를 제품 단계로 출시, 웹 자동화 벤치마크 `80%+` 진입
  - 이 레포의 추론: 2026년은 "데모"에서 "유료 제품"으로의 전환 시점이지만, 신뢰·보안·책임 구조는 아직 미성숙하다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Anthropic `Computer Use + Claude 4.6` | 에이전트 코딩·컴퓨터 사용 벤치마크 최상위, `1M` 컨텍스트 | 프런티어 에이전트 능력은 꾸준히 상승하나 배포 범위는 엔터프라이즈 중심 | 매출 `$14B` 수준과 제품 출시 가속 |
| OpenAI `ChatGPT Agent mode` | Operator 통합, Pro/Plus/Team 전면 공개 | 소비자 에이전트 접근성이 빠르게 확장 | 공식 릴리즈 노트 확인 |
| Google DeepMind `Project Mariner + Gemini Agent` | 10개 작업 동시, WebVoyager 83.5% | 웹 에이전트의 동시성·벤치마크 주도권 확보 중 | DeepMind 발표, Vertex AI 통합 |
| Apple `Apple Intelligence + Siri 26` | 앱 오케스트레이션, 3rd-party 프레임워크 개방 | iOS 생태계 내 UX 통합은 강점, 에이전트 자율성은 보수적 | iOS 26 공식 노트와 개발자 세션 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 에이전트 모드가 Pro 이상 티어의 기본 기능으로 정착, 웹/브라우저 자동화가 기업 워크플로우에 제한적 편입 | 신뢰 구조(감사 로그, 권한 샌드박스)가 빠르게 표준화 | 프롬프트 인젝션·오작동 사고로 기업 도입 지연 | 85% |
| 2027 | 운영 체제 수준의 에이전트(앱 지휘)가 iOS/Windows/Android에서 공식 기능으로 제공 | 3rd-party 앱 인텐트 표준이 플랫폼 간 합의 | 플랫폼마다 독자 표준으로 파편화 | 76% |
| 2028 | 에이전트가 단일 화면 자동화에서 "장시간 태스크" (시간 단위)를 안정적으로 실행 | 에이전트 오케스트레이션 플랫폼이 엔터프라이즈 CRM/ERP 대체 시작 | 장시간 태스크의 실패율·복구비용이 인간 대비 여전히 높음 | 60% |
| 2029 | 에이전트 비용 구조가 API 호출당에서 "목표 달성당"으로 전환, 결과 보증 계약이 일반화 | 에이전트 SLA와 보험 상품이 출현 | 책임 소재 규제 공백으로 기업이 전면 도입 주저 | 55% |
| 2030 | OS 레벨 에이전트가 다수 장치 간 상태를 공유하며 연속적 업무를 수행하는 "개인 지휘자" 모델 정착 | 프라이버시·데이터 주권 프레임이 성숙 | 감시형 에이전트에 대한 사회적 저항 확산 | 38% |
| 2031 | 엔터프라이즈 업무의 30-50%가 에이전트-인간 협업 형태로 재편 | 에이전트 생산성이 실물 경제 지표에 반영 | 노동·규제 이슈로 도입 속도 제한 | 55% |
| 2032 | 에이전트 간 통신 프로토콜(A2A)이 사실상 인터넷 표준으로 자리잡음 | 개방 표준이 주요 플랫폼에 채택 | 빅테크의 폐쇄 표준 경쟁으로 상호운용 실패 | 50% |
| 2033 | 소비자 디지털 활동 상당 부분이 에이전트에 위임, 인간은 결정·검토 계층에 집중 | 새로운 UX 표준(승인·취소·감사)이 폭넓게 채택 | 사용자 피로와 신뢰 문제로 도입률 정체 | 35% |
| 2034 | 에이전트 기반 스팸·사기와 방어 에이전트의 군비경쟁이 본격화 | 플랫폼 단에서 인증·서명 인프라 정비 | 방어 인프라가 따라오지 못해 디지털 환경 품질 저하 | 55% |
| 2035 | Agentic OS는 별도 제품이 아니라 주요 OS·브라우저의 기본 레이어가 되며, 경쟁 축은 모델보다 권한·감사·책임 구조로 이동 | 에이전트 운영 표준이 글로벌 규제와 조화 | 플랫폼 독점과 규제 파편화로 사용자 단에 여러 에이전트를 중복 사용 | 60% |

## 물리적/구조적 한계
- 극복된 것: 단일 태스크 웹 자동화, 코드/문서 도구 사용, 병렬 태스크 실행은 2025-2026년에 제품 수준으로 진입.
- 미해결: 프롬프트 인젝션, 장시간 태스크 실패 복구, 권한 세분화, 책임 소재, 감사 가능성.
- 극복 시나리오: OS 레벨 샌드박스, 서명된 인텐트 표준, 에이전트 행동 감사 로그가 플랫폼 기본으로 제공되어야 대규모 자율 배포가 가능.

## 기술 현실론 보정
- 낙관론 측 근거: WebVoyager `83.5%`, Claude 4.6/4.x의 벤치마크 석권, ChatGPT Agent의 범용 공개는 실제 제품 단계 진입.
- 현실론 측 반론: 실사용에서는 여전히 잘못된 클릭·이중 결제·인젝션 공격 사례가 누적되며, 책임·보험·감사 인프라가 초기 단계.
- 균형 판단: `2026-2028`은 신뢰-배포 속도의 긴장이 가장 심한 구간이며, `2029+`에 표준과 규제가 안정되어야 대규모 운용이 가능.

## 2035 전망 요약
- Base: Agentic OS는 플랫폼의 기본 레이어로 흡수되어, 개별 제품이 아닌 OS·브라우저 기능으로 사용자 상호작용을 매개한다.
- Upside: 개방 표준과 규제 정비로 에이전트가 주요 디지털 노동을 위임받고, 생산성 측정 지표가 실질 상승한다.
- Downside: 프롬프트 인젝션·책임 공백·플랫폼 독점이 결합돼 에이전트는 특정 고부가 업무에만 제한 사용된다.

## 연결 문서
- [./scaling_laws.md](./scaling_laws.md)
- [./slm_roadmap.md](./slm_roadmap.md)
- [../on_device_ai/architecture_shifts.md](../on_device_ai/architecture_shifts.md)
- [../on_device_ai/aui.md](../on_device_ai/aui.md)
- [../../09_corporate_roadmaps/ai_labs/openai.md](../../09_corporate_roadmaps/ai_labs/openai.md)

## 정보 출처
- Anthropic `Introducing computer use, a new Claude 3.5 Sonnet` https://www.anthropic.com/news/3-5-models-and-computer-use 2026-04 확인
- Anthropic `Computer use tool docs` https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool 2026-04 확인
- OpenAI `Introducing Operator` https://openai.com/index/introducing-operator/ 2026-04 확인
- OpenAI `Introducing ChatGPT agent` https://openai.com/index/introducing-chatgpt-agent/ 2026-04 확인
- OpenAI `Computer-Using Agent` https://openai.com/index/computer-using-agent/ 2026-04 확인
- Google DeepMind `Project Mariner` https://deepmind.google/models/project-mariner/ 2026-04 확인
- Google `Gemini universal AI assistant (I/O 2025)` https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-universal-ai-assistant/ 2026-04 확인
- TechCrunch `Google rolls out Project Mariner` https://techcrunch.com/2025/05/20/google-rolls-out-project-mariner-its-web-browsing-ai-agent/ 2026-04 확인
- Apple `New Apple Intelligence features are available today` https://www.apple.com/newsroom/2025/09/new-apple-intelligence-features-are-available-today/ 2026-04 확인
- Apple iOS official page https://www.apple.com/ios/ 2026-04 확인
