# AI 공격·방어 사이버 전망
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- DARPA `AIxCC` Final Competition은 AI 기반 취약점 탐지·자동패치 가능성을 실증했다. 최종 라운드에서 경쟁 CRS(Cyber Reasoning System)들이 합성 취약점의 `86%`를 발견하고 `68%`를 패치했으며, 오픈소스 프로젝트에서 `18개` 실 취약점을 추가 발견해 책임 공개 절차에 들어갔다. Team Atlanta(`$4M`), Trail of Bits(`$3M`), Theori(`$1.5M`)가 1·2·3위를 차지했다. 전 7개 결선팀 CRS는 OSI 승인 라이선스로 `오픈소스 공개`된다.
- CrowdStrike `2026 Global Threat Report`는 adversaries가 `90개+` 조직에서 합법 GenAI 도구에 프롬프트 인젝션을 해 자격증명/암호화폐 탈취 명령을 생성시켰고, AI 개발 플랫폼 취약점으로 랜섬웨어 지속화, 신뢰 서비스를 사칭한 악성 AI 서버 배포 등을 확인했다.
- Russia 연계 `FANCY BEAR`는 LLM 기반 말웨어 `LAMEHUG`를 배포해 정찰과 문서 수집을 자동화했다. Adam Meyers(CrowdStrike SVP Counter Adversary Operations)는 "AI는 취약점 발견에도 이상적으로 적합"해 `zero-day 발견-exploit` 시간이 급격히 단축될 것이라고 공식 평가했다.
- 방어 측에서도 AI SOC가 본격화됐다. CrowdStrike는 `Shadow AI Discovery for Endpoint`로 LLM 런타임, MCP 서버, AI 에이전트를 엔드포인트에서 자동 검색하고 있다. Meta+CrowdStrike `CyberSOCEval`은 SOC 업무 기준 LLM 평가 벤치마크를 공개했고, AWS·Anthropic·Microsoft·Google 등 대형 벤더가 동참한 방어 협력체 `Mythos Preview`도 출범했다.
- Anthropic은 `2026년 4월` `Project Glasswing`을 통해 AI로 사이버 방어를 강화하는 이니셔티브를 발표했다. 산업 공감대는 "AI는 공격과 방어 모두를 가속하며, 우위는 조직 실행력이 결정한다"는 CrowdStrike의 공식 전망에 수렴.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| DARPA AIxCC | CRS로 취약점 `86%` 발견/`68%` 패치, 결선팀 오픈소스 공개 | `2026-2028` 오픈 CRS를 기반으로 대기업/정부 도입 가속 | 공식 결과 발표 |
| CrowdStrike 2026 Threat Report | GenAI 악용, LLM 말웨어, AI SOC 필요성 명시 | 대형 기업 SOC는 `2027+` AI 에이전트 기반으로 전환 | 공식 보고서 |
| Anthropic Project Glasswing | AI 방어 강화 이니셔티브 출범 | 상용 LLM 벤더 주도 방어 툴 생태계 형성 | Anthropic 발표 |
| Meta/CrowdStrike CyberSOCEval | SOC용 LLM 벤치마크 공개 | AI SOC 품질 평가가 표준화되며 선별 가속 | GitHub 공개 |
| CISA/NCSC advisories | Living-off-the-Land 가이던스 지속, AI 악용 지침 추가 | 공공부문도 AI 공격·방어 대응 프레임 필수 | 정부 advisory |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | AIxCC 결과 오픈소스화, AI SOC 파일럿이 대기업 수십 곳 진입; 사이버 전쟁 시장 ~$300bn 방향 | CRS가 OSS 프로젝트 CI에 상시 통합 | AI 오탐/조직 통합 지연 | 82% |
| 2027 | LLM 기반 zero-day 발견-공개 프로세스 제도화 | 소프트웨어 공급망 전반에 자동 패치 파이프라인 | 모델 제공자 간 계약·책임 분쟁 | 79% |
| 2028 | AI 공격자는 `scripted`에서 `agentic`으로 전환, 방어도 동일 | 방어 우위로 breach dwell time `50%+` 단축 | AI 공격 속도에 방어 자동화가 못 따라감 | 55% |
| 2029 | AI 에이전트 기반 SOC가 대기업 대부분에 표준 | FedRAMP·국방·금융권 AI SOC 의무 | AI 가용성 리스크(공급자 장애)가 보안 리스크화 | 60% |
| 2030 | 국가급 사이버 공방이 AI-vs-AI 구도로 완전 전환; 사이버 전쟁 시장 ~$300bn 달성 | 방어 자동화가 중소기업까지 확산 | 규제·책임 공백이 adoption 지연 | 55% |
| 2031 | zero-day 발견 속도가 패치 배포 속도를 상회 | 자동 패치 + verified fix 체인이 표준 | 패치 자동화 실패 시 공급망 대형 사고 | 38% |
| 2032 | AI 사이버 능력이 국가 경제안보 지표로 편입 | 국제 규범 초안 출현 | 규범 공백 + 공격·방어 경쟁 심화 | 35% |
| 2033 | 저비용 AI 공격 툴이 범죄·국가 사이 경계 흐림 | 국제 공조로 범죄 AI 툴 제재 체제 성립 | 비국가 AI 공격자의 산업 피해 급증 | 50% |
| 2034 | 사이버 방어의 비용-효과 곡선이 AI로 급진 개선 | 보험·감사 시장이 AI 기반으로 재편 | AI 의존의 시스템적 단일 실패점 노출 | 55% |
| 2035 | AI 사이버는 일상 인프라의 보이지 않는 층. 공격·방어 모두 자동화 기본 | 공급망 전반의 적응형 보안 체제 완성 | AI 공격의 자동화 속도가 인간 통제 범위 초과 | 60% |

## 물리적/구조적 한계
- AI 기반 공격·방어는 모두 대형 모델에 의존하며 모델 공급자 장애·유출·오남용이 시스템 리스크화한다.
- AI SOC는 오탐·설명가능성·감사 가능성이 실전 배치 병목. 규제 강한 산업(금융/의료)일수록 도입 속도 느림.
- Adversarial ML(prompt injection, data poisoning)은 방어자가 반드시 풀어야 할 문제지만 완전한 해법은 아직 없다.

## 기술 현실론 보정
- 낙관론 측 근거: AIxCC의 공식 정량 지표(`86%` 발견/`68%` 패치)는 자동 사이버 방어의 실물 가능성을 확정.
- 현실론 측 반론: 대회 환경과 실제 프로덕션 환경은 다르다. 조직 내 배포·통합·감사는 수년이 걸린다.
- 균형 판단: `2026-2028`은 툴 보급, `2029-2032`는 조직 통합, `2033-2035`는 규범과 시장 재편 구간.

## 2035 전망 요약
- Base: AI는 사이버 공격·방어의 기본 레이어. 대기업 SOC는 AI 에이전트 기반이 표준이고 오픈소스 CRS가 CI에 상시 통합.
- Upside: 방어 자동화가 공격 자동화를 앞서 평균 dwell time이 구조적으로 하락.
- Downside: AI 공격의 속도·다양성이 방어를 구조적으로 추월하고 시스템 단일 실패점 리스크가 현실화.

## 연결 문서
- [./critical_infra.md](./critical_infra.md)
- [../autonomous_weapons/ai_targeting.md](../autonomous_weapons/ai_targeting.md)
- [../players/palantir.md](../players/palantir.md)
- [../../02_technology/foundation_models/agentic_os.md](../../02_technology/foundation_models/agentic_os.md)
- [../../13_scenarios/base_case.md](../../13_scenarios/base_case.md)

## 정보 출처
- DARPA AIxCC final results page https://aicyberchallenge.com/finals-winners-announcement/ 2026-04 확인
- DARPA AIxCC program page https://www.darpa.mil/research/programs/ai-cyber 2026-04 확인
- DARPA AIxCC results 2025 https://www.darpa.mil/news/2025/aixcc-results 2026-04 확인
- CrowdStrike 2026 Global Threat Report https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/ 2026-04 확인
- CrowdStrike endpoint AI security https://www.crowdstrike.com/en-us/press-releases/crowdstrike-establishes-the-endpoint-as-the-epicenter-for-ai-security/ 2026-04 확인
- Anthropic Project Glasswing ASIS https://www.asisonline.org/security-management-magazine/latest-news/today-in-security/2026/april/project-glasswing/ 2026-04 확인
- CyberSOCEval benchmark GitHub https://github.com/CrowdStrike/CyberSOCEval_data 2026-04 확인
- SecurityWeek Cyber Insights 2026 https://www.securityweek.com/cyber-insights-2026-malware-and-cyberattacks-in-the-age-of-ai/ 2026-04 확인
- Meritalk AIxCC winners https://www.meritalk.com/articles/darpa-announces-winners-of-ai-cyber-challenge/ 2026-04 확인
- Kiteworks CrowdStrike 2026 report analysis https://www.kiteworks.com/cybersecurity-risk-management/crowdstrike-2026-threat-report-breakout/ 2026-04 확인
