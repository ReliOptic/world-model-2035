# Starship Roadmap
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- SpaceX의 공식 Starship 페이지 기준으로 Starship/Super Heavy는 `완전 재사용`을 목표로 하며, Starship은 `100~150t` fully reusable, `250t` expendable payload를 제시한다. 시스템 전체 높이는 `123m`다.
- SpaceX는 Super Heavy를 `71m`, `33 Raptor engines`, `7,590 tf` thrust로 설명하고, 양 단계 모두 `catch` 후 빠른 재발사를 지향한다고 적시한다.
- SpaceX의 2025 공식 연간 패치·티셔츠 상품 설명 기준으로 2025년에는 `Flight 7 (1/16)`, `Flight 8 (3/6)`, `Flight 9 (5/27)`, `Flight 10 (8/26)`, `Flight 11 (10/13)`까지 시험 비행이 진행됐다. 즉 2025년은 시험 빈도를 크게 끌어올린 해였다.
- `Flight 9` 공식 패치 설명은 해당 비행이 `처음으로 재비행한 Super Heavy booster`를 사용했다고 적시한다. 완전 재사용까지는 아니어도 부스터 재사용 검증은 실제 단계에 들어갔다.
- FAA의 Boca Chica 관련 문서는 2022년에는 연 `5`회 orbital launch, 2025년 Tiered EA/FONSI-ROD에서는 연 `25`회 orbital launch/landing 계획까지 검토 범위를 넓혔다. 2026년 2월 Final Tiered EA는 추가 launch trajectories와 `Starship Return to Launch Site` mission profile까지 다뤘다.
- NASA는 2025년 3월 Starship을 `NLS II` 계약의 신규 launch service로 추가했고, 2025년 8월 갱신된 HLS 페이지는 Starship HLS가 `Artemis III`와 `Artemis IV` 달 착륙 수단이라고 명시한다.
- NASA의 2026년 3월 Artemis architecture update는 `Artemis III를 2027년`, `Artemis IV를 2028년 초`로 잡고, 이후 매년 최소 한 번의 달 표면 착륙을 목표로 제시했다.
- 현재 상태 해석:
  - 확인된 사실: 2025년 시험 cadence는 빨라졌고, 부스터 재비행까지 진입했다
  - 확인된 사실: NASA의 달 프로그램과 일반 발사 서비스 편입이 동시에 진행 중이다
  - 확인된 사실: FAA 환경심사는 2026년 3월에도 계속 열려 있다
  - 이 레포의 추론: 2026년 Starship의 핵심 병목은 "로켓 성능"보다 "규제 승인, 발사장 처리량, 재사용 운영 안정화"다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| SpaceX `Starship` page | 완전 재사용, 대형 payload, on-orbit refilling, Moon/Mars 수송 플랫폼 제시 | 장기 비전은 일관되지만, 2030 이전에는 지상 운영과 재사용 turnaround가 더 큰 판단 변수 | 공식 사양과 목표가 가장 직접적으로 제시된 출처 |
| FAA Boca Chica review documents | 2022년 5회에서 2025년 25회 annual orbital launches 검토, 2026년 RTLS mission profile 추가 | 발사 cadence 상향은 기술보다 FAA 승인 범위 확대가 선행 조건 | 2022-2026 문서 연속선 확인 |
| NASA `Human Landing System` | Starship HLS를 Artemis III·IV 달 착륙 수단으로 유지 | NASA 프로그램 자금과 일정이 Starship 신뢰성 검증을 지속 강제 | 유인 달 탐사 수요가 장기적 학습곡선 제공 |
| NASA `NLS II` modification | Starship을 NASA launch services offering에 추가 | 과학·국가임무 발사 진입은 상업시장 외 추가 수요를 열지만, 임무 신뢰성 기준이 더 엄격 | 2025-03-28 공식 계약 수정 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | FAA의 higher-cadence/RTLS 승인 경로를 고정하고 시험비행을 누적 | cadence가 눈에 띄게 상승하고 부스터 reuse가 반복 검증 | 승인 지연이나 큰 mishap으로 cadence가 다시 꺾임 | 82% |
| 2027 | NASA의 Artemis III 목표연도에 맞춰 HLS 통합 요구가 가장 강한 해가 됨; Artemis III crewed lunar 2027 확률 30~40% | crewed-orbit rendezvous·docking 체계까지 신뢰성 축적 | Artemis III와 Starship 통합 일정이 다시 미뤄짐 | 65% |
| 2028 | NASA의 Artemis IV 목표연도에 맞춰 달 착륙 파생형의 실전 준비가 진행; Starship 발사 cadence 목표 약 24회/년 | 달 임무가 데모에서 반복 운영 단계로 넘어감 | HLS 일정이 더 뒤로 밀리며 화성 서사 대비 실사용은 늦어짐 | 38% |
| 2029 | Starship은 상업 대형발사와 정부 탐사 사이 이중 포지션을 확보 시도 | 위성 대량배치·국가임무 발사에서 실수요 확대 | Falcon 계열 대체 속도가 느리고 임무군이 제한적 | 52% |
| 2030 | 완전 재사용의 경제성보다 높은 cadence와 임무 신뢰성이 사업성 판단 기준이 됨; 글로벌 우주 경제 ~$1T 중 발사 인프라 비중 구조적 상수 | 대형 우주인프라와 심우주 cargo 시장의 기본 플랫폼으로 자리잡음 | 회수는 가능하지만 turnaround 비용이 예상보다 높음 | 48% |
| 2031 | 달 프로그램과 저궤도 대형구조물 수요가 Starship 실사용 범위를 넓힘 | 탱커·보급·달물류 체계가 초기 형태로 안정화 | 정부 예산·정책 변화로 탐사 수요가 흔들림 | 45% |
| 2032 | Starship은 발사체라기보다 궤도 물류 시스템으로 평가받기 시작 | 궤도 refilling과 대형 cargo 운송이 반복 임무로 정착 | 발사장·공급망·보험비용이 운영 규모 확대를 제한 | 42% |
| 2033 | 화성보다는 달과 cislunar logistics가 더 실질적 시장으로 남음 | 달 인프라 선점으로 장기 탐사 표준 지위 강화 | 화성 서사는 유지되지만 실제 매출은 제한적 | 38% |
| 2034 | 완전 재사용의 핵심은 정비 최소화와 회전율 증명으로 압축됨 | Starship이 중량물 수송의 기본 OS가 됨 | 반복 정비와 규제 감시가 원가를 높게 유지 | 35% |
| 2035 | Starship은 대형 우주물류의 핵심 플랫폼이지만, 화성 이주보다는 지구궤도-달 경제에 더 깊게 묶여 있을 가능성이 높음 | 달 물류·대형위성·국가탐사에서 사실상 표준 시스템이 됨 | 기술은 남지만 상업경제성이 과장됐다는 평가가 강해짐 | 62% |

## 물리적/구조적 한계
- 극복된 것:
  - 초대형 발사체 반복 시험비행 자체는 2025년 다섯 차례 cadence로 진전
  - 부스터 재비행이 공식 상품 설명에도 반영될 정도로 가시 단계에 진입
- 미해결:
  - 완전 재사용 turnaround 시간
  - 궤도 refilling과 도킹의 반복 신뢰성
  - FAA·환경심사와 발사장 운영 승인
  - 발사 cadence 증가 시 안전성과 보험 비용
- 극복 시나리오:
  - 시험 성공률보다 운영 일관성이 높아지고, 발사장 처리량과 규제 승인 프로세스가 동시에 안정화되어야 한다

## 기술 현실론 보정
- 낙관론 측 근거:
  - 2025년 다섯 번의 시험비행은 과거 대비 학습 속도가 확실히 빨라졌음을 보여준다
  - NASA HLS와 NLS II 편입은 외부 고객이 Starship을 실제 프로그램 자산으로 보기 시작했다는 뜻이다
- 현실론 측 반론:
  - SpaceX의 장기 비전은 항상 공격적이었고, 운영 안정화는 설계 성공보다 훨씬 느리게 온다
  - FAA 환경심사가 2026년 3월에도 열려 있다는 사실 자체가 비기술 병목을 보여준다
- 균형 판단:
  - Starship은 실패한 과장 프로젝트가 아니라 실제로 진전 중인 초대형 시스템이다
  - 다만 2035까지의 핵심 질문은 "화성 가능 여부"가 아니라 "고빈도 재사용 우주물류가 경제적으로 안정화되는가"다

## 2035 전망 요약
- Base: Starship은 달·저궤도 중심의 대형 우주물류 플랫폼으로 자리잡지만, 화성 이주 서사는 여전히 앞서 나가 있다
- Upside: 회수·재비행·탱커 운용이 빠르게 안정화되며 대형 발사와 cislunar logistics의 표준이 된다
- Downside: 규제·안전·운영비 병목으로 기술적 가능성은 입증해도 경제성은 제한된다

## 연결 문서
- [starlink.md](starlink.md)
- [mars_timeline.md](mars_timeline.md)
- [../competitors/blue_origin.md](../competitors/blue_origin.md)

## 정보 출처
- [SpaceX Starship] [https://www.spacex.com/vehicles/starship/] [2026-04-21]
- [FAA Environmental Review for Starship/Super Heavy at Boca Chica] [https://www.faa.gov/space/stakeholder_engagement/spacex_starship/environmental_review] [2026-04-21]
- [SpaceX Starship at Boca Chica] [https://www.faa.gov/space/stakeholder_engagement/spacex_starship] [2026-04-21]
- [License Review Process] [https://www.faa.gov/space/stakeholder_engagement/spacex_starship/license_review_process] [2026-04-21]
- [Final Tiered EA for Additional Launch Trajectories and Starship RTLS Mission Profiles] [https://www.faa.gov/space/stakeholder_engagement/spacex_starship/Final_Tiered_EA_Additional_Launch_Trajectories_Starship_RTLS_mission_profiles_SpaceX_Starship-Super_Heavy_Boca_Chica.pdf] [2026-04-21]
- [Human Landing System] [https://www.nasa.gov/hls] [2026-04-21]
- [NASA Strengthens Artemis: Adds Mission, Refines Overall Architecture] [https://www.nasa.gov/directorates/esdmd/nasa-strengthens-artemis-adds-mission-refines-overall-architecture/] [2026-04-21]
- [NASA Awards Launch Services Contract for SpaceX Starship] [https://www.nasa.gov/news-release/nasa-awards-launch-services-contract-for-spacex-starship/] [2026-04-21]
- [STARSHIP 2025 YEARLY MISSION PATCH] [https://shop.spacex.com/products/starship-2025-yearly-mission-patch] [2026-04-21]
- [UNISEX STARSHIP YEARLY 2025 T-SHIRT] [https://shop.spacex.com/collections/trending/products/unisex-starship-yearly-2025-t-shirt] [2026-04-21]
- [Starship Flight 9 Mission Patch] [https://shop.spacex.com/products/starship-flight-9-mission-patch] [2026-04-21]
- Inference note: 2026-2035 annual milestones are repository inferences anchored to SpaceX official materials, FAA review status, and NASA program documents.
