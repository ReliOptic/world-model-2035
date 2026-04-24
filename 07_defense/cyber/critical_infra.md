# 핵심 인프라 사이버 전망
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- CISA/NSA/FBI는 PRC 연계 `Volt Typhoon`이 미국 `통신·에너지·교통·상하수도` 섹터 IT 네트워크에 `최소 5년` 이상 접속을 유지하며 OT 자산 횡적 이동을 위한 `pre-positioning`을 수행 중이라고 high confidence로 평가했다. 이는 위기·분쟁 시 파괴적 사이버 공격 준비로 해석된다.
- CISA 권고(`AA24-038A`)는 `Living-off-the-Land` 기법 대응 지침과 함께 연방 기관·ICS 사업자에게 MFA, EDR, 중앙 로깅, 잦은 자격증명 갱신, 알려진 익스플로잇 취약점(KEV) 우선 패치를 의무화하는 방향으로 확대됐다.
- `2025-2026` AI 에이전트 확산은 공격면과 방어면을 동시에 바꿨다. CrowdStrike `2026 Threat Report`는 GenAI 악용 증가를 확인했고, CISA는 AI 서비스·개발 플랫폼도 critical infra 범주로 검토 중이다.
- 실물 피해 사례의 교훈은 여전히 유효하다. `Colonial Pipeline(2021)` 사건 이후 미국 연료 파이프라인 보안 지침(TSA SD Pipeline-2021-01)과 NERC CIP 규정이 강화됐으나, 물 섹터·중소 지자체의 보안 격차는 여전히 큰 취약점으로 남아있다.
- NCSC UK, ENISA, 일본 NISC 등은 Volt Typhoon 및 Salt Typhoon(통신사 대상) 관련 경보를 공동 발령해 `Five Eyes + EU` 공동 인지가 정착됐다. 통신사 메타데이터·OT 네트워크 보호가 최우선 의제.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| CISA AA24-038A Volt Typhoon | 5년+ 접속 유지, OT 횡이동 준비 확인 | 분쟁 시점(`2027-2030`) 디스럽션 이벤트 실제 발생 가능성 상존 | 공동 advisory |
| CISA KEV catalog | 알려진 익스플로잇 즉시 패치 의무 | 기관 이행률 지속 증가 but 중소 지자체는 지연 | 공공 이행 대시보드 |
| TSA SD Pipeline / NERC CIP | 파이프라인·전력 규정 강화 | 대형 사업자 준수율 높으나 계약업체·레거시 시스템이 취약점 유지 | 규제 집행 기록 |
| Mythos Preview 연합 | 대형 AI 벤더가 AI critical infra 보호 공동 행동 | `2026-2028` AI 공급망 차원 방어 원칙 정립 | 공식 출범 |
| ENISA/NCSC 공동 advisory | Salt Typhoon 통신사 사례 공유 | Five Eyes + EU 정보공유 상설화 | 공동 발표 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Volt/Salt Typhoon 후속 공동 advisory 갱신, 통신사·전력사 OT 격리 정책 강화 | AI SOC 파일럿 효과로 dwell time 감소 | 중소 지자체 보안 격차 사고로 드러남 | 80% |
| 2027 | 파이프라인·수도·전력 사업자 zero-trust 의무화 | 민관 위협 인텔 공유 실시간화 | 규제 이행 지연으로 사고 증가 | 60% |
| 2028 | PRC 관련 사이버 사건이 외교·경제 대응 카드로 공식화 | 동맹 차원 제재·재보복 원칙 합의 | 충돌 국면에서 사이버 에스컬레이션 역설 | 55% |
| 2029 | OT 네트워크의 AI 행동분석이 표준 | 공급망 소프트웨어 SBOM + 자동검증 의무 | 레거시 OT 업그레이드 재정 부담 | 60% |
| 2030 | 핵심 인프라 복원력 기준(RTO/RPO)이 법제화 | 국가급 사이버 훈련 상시화 | 사이버 보험 시장 경색 | 55% |
| 2031 | OT 자가치유(self-healing) 제어계통 초기 보급 | AI 기반 자동 복구가 주요 grid에 배치 | 자가치유 오작동 리스크 문제 | 55% |
| 2032 | 통신·전력·수도 섹터에 AI 취약점 점검 의무화 | SBOM/SaaS 감사 전면 일원화 | 중소 벤더 컴플라이언스 부담 급증 | 60% |
| 2033 | 통신·전력 섹터에서 양자내성 암호(PQC) 전환 완료 구간 진입 | NIST PQC 표준의 critical infra 전면 적용 | PQC 전환 중 상호운용성 문제 발생 | 55% |
| 2034 | OT + IT + AI 통합 방어 centralization 진행 | 민-공공 인프라의 사이버 복원 공통 프레임 | 집중화된 방어의 단일 실패점 리스크 | 50% |
| 2035 | 핵심 인프라 사이버는 국가안보의 일상 운영 layer | 사이버-물리 이중화가 표준 | 대형 disruption 사건이 한 차례 이상 발생 | 65% |

## 물리적/구조적 한계
- OT(산업제어) 시스템은 수명이 `20-30년`이라 레거시 프로토콜(Modbus, DNP3)의 보안 한계가 구조적이다.
- 민간 소유 인프라의 국가안보 책임 분담은 법적·경제적으로 여전히 모호하다. 인센티브·규제 균형 문제가 상존.
- 중소 지자체·수도·병원은 예산·인력 부족으로 보안 격차가 고착화.

## 기술 현실론 보정
- 낙관론 측 근거: CISA/NSA 공동 advisory, AI SOC 배치, NERC CIP 강화는 구조적 개선을 증명.
- 현실론 측 반론: Volt Typhoon이 `5년+` 지속 접속한 사실은 방어 감지 능력의 근본적 한계를 시사.
- 균형 판단: `2026-2028`은 상위 사업자 강화 + 중하위 격차 노출, `2029+`는 규제 의무화 + 자동화로 수렴.

## 2035 전망 요약
- Base: 핵심 인프라 방어는 상시 AI 보조 + zero-trust + PQC 전환이 기본. 대형 disruption은 간헐적 발생.
- Upside: 민관 정보공유와 자동화 방어로 dwell time과 피해 규모가 구조적으로 축소.
- Downside: 지정학 위기와 AI 공격 고도화가 동시 진행되어 대규모 민간 피해를 유발하는 사건이 반복 발생.

## 연결 문서
- [./ai_offense_defense.md]
- [../autonomous_weapons/counter_autonomous.md]
- [../nuclear/modernization.md]
- [../../03_energy/grid/ai_optimization.md]
- [../../13_scenarios/base_case.md]

## 정보 출처
- CISA Volt Typhoon AA24-038A https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a 2026-04 확인
- CISA partners fact sheet leaders https://www.cisa.gov/news-events/alerts/2024/03/19/cisa-and-partners-release-joint-fact-sheet-leaders-prc-sponsored-volt-typhoon-cyber-activity 2026-04 확인
- NSA Living off the Land PDF https://media.defense.gov/2023/May/24/2003229517/-1/-1/0/CSA_Living_off_the_Land.PDF 2026-04 확인
- CISA PRC state sponsored resource https://www.cisa.gov/resources-tools/resources/prc-state-sponsored-cyber-activity-actions-critical-infrastructure-leaders 2026-04 확인
- TechTarget 5 year access Volt https://www.techtarget.com/searchsecurity/news/366569227/CISA-Volt-Typhoon-had-access-to-some-US-targets-for-5-years 2026-04 확인
- TechTarget defensive actions Volt https://www.techtarget.com/searchsecurity/news/366574758/CISA-urges-defensive-actions-against-Volt-Typhoon-threats 2026-04 확인
- CrowdStrike 2026 threat report https://www.crowdstrike.com/en-us/press-releases/2026-crowdstrike-global-threat-report/ 2026-04 확인
- CISA AA23-144a living off the land https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a 2026-04 확인
- TSA CISA partners advisory https://www.tsa.gov/news/press/releases/2024/02/07/us-and-international-partners-publish-cybersecurity-advisory-peoples 2026-04 확인
- CISA PRC state sponsored PDF https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf 2026-04 확인
