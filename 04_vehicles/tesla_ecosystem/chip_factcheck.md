# Tesla 칩 팩트체크
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- **AI4 (HW4):** 현재 Tesla 차량과 Cybercab에 탑재된 표준 FSD 컴퓨터다. 2026년 4월 Tesla는 **AI4+ (HW4.1)** 을 발표했다. AI4+는 RAM을 기존 16GB에서 32GB로 두 배 증가시켜 시스템 총 RAM을 64GB로 높였다. FSD v15는 AI4(HW4) 기준으로 `2026년 말 또는 2027년 초` 호환 예정이다.
- **AI5 (HW5):** 성능은 AI4 대비 `3~5배`, `2,000~2,500 TOPS`로 예상된다. 단일 AI5 SoC는 NVIDIA H100 1개와 유사한 성능, 듀얼 AI5는 NVIDIA B100/B200 수준으로 추정된다. 제조는 TSMC `N3P(3nm)` 공정, 대안으로 Samsung이 거론된다. 양산 진입은 `2026년 하반기`, 차량 탑재는 `2026년 말~2027년 초`가 목표다. Cybercab 초기 생산분은 AI5 대신 AI4로 출시된다.
- **HW4.5 (AI4.5):** AI5 출시 전 브리지 제품으로 `3칩 구성` HW4.5가 포착됐다. AI5 양산 준비 기간 동안의 과도기 제품으로 해석된다.
- **Dojo:** D1 칩(TSMC 7nm, 50B 트랜지스터, 645mm², BF16 기준 ExaPOD 1.1 ExaFLOPS)은 2021~2022년 AI Day에서 발표됐으나 대규모 배포 없이 2025년 사실상 해체됐다. Dojo D2(AI7) 재시작이 2026년 1월 발표됐으나 구체적 일정 없음.
- **공정 노드 팩트체크:** AI4는 Samsung SF4 공정으로 확인됐다(Semi-Analysis 분해 분석 기반). AI5는 TSMC N3P가 1차 공정이며 Samsung이 대안으로 거론된다. Dojo D1은 TSMC 7nm로 확인됐다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Tesla Q1 2026 실적 발표 | AI4+ 발표(RAM 64GB), Cybercab AI4 탑재, AI5 양산 준비 | AI4+ 발표는 확인됨. AI5 양산은 2026 하반기~2027 초가 현실적 | 발표된 스펙과 로드맵이 일치함 |
| notateslaapp AI5 보도 | AI5 양산 2H 2026, TSMC N3P, 2,000~2,500 TOPS, H100 급 성능 | 2026 하반기 양산 시작 가능성 있으나 차량 탑재는 2027 확률이 높음 | 설계 확정 확인, 실제 테이프아웃 여부 미공개 |
| Semi-Analysis 분해 분석 | AI4는 Samsung SF4, Dojo D1은 TSMC 7nm 확인 | 공정 노드 확인은 분해 기반 신뢰도가 높다 | 독립적 하드웨어 분석 |
| notateslaapp HW4.5 보도 | AI5 전 3칩 브리지 제품 HW4.5 포착 | 브리지 제품 존재는 AI5 양산 지연을 감안한 포석으로 해석 가능 | 규제 문서에서 포착된 정황 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | AI4+ 배포, AI5 양산 진입 시작, Cybercab AI4 탑재 | AI5 양산 H2 완료, 연말 AI5 탑재 차량 출하 시작 | AI5 수율 문제로 차량 탑재 2027년으로 이연 | 55% AI5 연내 양산 |
| 2027 | AI5 탑재 차량 본격 출하, HW3 교체 프로그램 진행, FSD v15 출시 | AI5 탑재 모든 신차 표준화 | Samsung AI5 대안 공정 수율 문제로 공급 병목 | 70% |
| 2028 | AI6 개발 발표, AI5 기반 FSD 소프트웨어 급성장 | AI6 TSMC N2 공정으로 설계 | AI5 세대가 예상보다 빠르게 교체 압박을 받음 | 55% AI6 발표 |
| 2029 | AI6 탑재 차량 출시, 추론 칩 성능 경쟁에서 NVIDIA와 간접 비교 | AI6 단일 칩이 현재 AI4 듀얼 시스템 대비 10배 성능 | TSMC N2 수율 문제로 AI6 양산 지연 | 60% |
| 2030 | Tesla 차량용 칩이 AI 추론 성능에서 산업 기준점이 됨 | Dojo AI7 양산으로 훈련+추론 통합 가속기 체제 | 지정학 리스크로 TSMC 독점 의존이 공급 불안으로 전환 | 55% |
| 2031 | Tesla AI 칩이 차량 외 로봇·에너지 장치에도 통합 배포 | 로봇용 AI8 칩 발표, 추론 전문화 심화 | 반도체 수출 통제 강화로 특정 시장 공급 제한 | 50% |
| 2032 | AI 추론 칩 세대 전환 주기가 2~3년으로 고정 | Tesla 칩이 소비자 AI 추론 시장의 표준 중 하나 | 경쟁사(Qualcomm, AMD) 차량용 칩과 공급 경쟁 | 50% |
| 2033 | 차량용 AI 칩에서 전력 효율이 성능보다 핵심 지표로 부상 | Tesla 칩 전력 효율이 업계 최고 수준 달성 | 패키징·열 설계 한계로 성능 향상 정체 | 50% |
| 2034 | 온디바이스 AI와 클라우드 AI 경계가 차량 칩에서 통합 | Tesla 차량이 이동 중 AI 추론 엣지 노드 역할 | 지정학 블록화로 공정 접근이 지역 제한됨 | 45% |
| 2035 | Tesla AI 칩은 차량·로봇·에너지 장치를 통합하는 수직 AI 실리콘 스택의 완성형 | Tesla 칩이 제3자 기기에도 공급되는 플랫폼화 | 미세화 한계와 전력 제약으로 칩 성능 향상이 둔화 | 50% |

## 물리적/구조적 한계
- AI5는 TSMC N3P 의존으로 TSMC 생산 용량과 수율이 공급량을 결정한다.
- Samsung 대안 공정은 존재하나 TSMC 대비 수율·성능 할인이 있을 가능성이 있다.
- Tesla 차량 탑재 칩은 차량 설계 주기(2~3년)에 묶이므로 반도체 세대 전환(1~2년)보다 느리게 갱신된다.

## 기술 현실론 보정
- 낙관론 측 근거: AI4+ 발표와 AI5 TSMC N3P 설계 확정은 Tesla 실리콘 로드맵이 실재함을 보여준다. AI4는 이미 전 세계 수백만 차량에 탑재된 검증 칩이다.
- 현실론 측 반론: Dojo D1/ExaPOD의 대규모 배포 실패는 Tesla 칩 로드맵이 항상 예정대로 실행되지 않음을 보여준다. AI5 차량 탑재 일정은 수율과 패키징에 달렸다.
- 균형 판단: Tesla의 추론 칩(AI4/AI5)은 실적이 있고 방향이 명확하다. 훈련 칩(Dojo)은 전략 변동성이 크다.

## 2035 전망 요약
- Base: AI5→AI6→AI7+ 세대 전환이 2~3년 주기로 이어지며 Tesla 차량·로봇·에너지 장치를 위한 전용 AI 추론 칩 스택이 완성된다.
- Upside: Dojo AI7 훈련 칩이 성공적으로 양산돼 Tesla가 NVIDIA 의존 없이 훈련+추론 통합 AI 인프라를 갖춘 최초 자동차 기업이 된다.
- Downside: TSMC 의존 집중, 지정학 공급 리스크, 패키징 병목이 AI5 이후 세대 전환을 늦추고 경쟁사 대비 칩 성능 우위가 약해진다.

## 확률 근거 요약
- `≥75%`: AI4+(HW4.1) 64GB RAM 구성 2026년 신차 적용 (Q1 2026 발표 확인)
- `≥75%`: Cybercab 초기 생산분 AI4 탑재 (Tesla Q1 2026 실적 발표 확인)
- `<40%`: AI5 탑재 신차 2026년 내 출하 개시 (설계 확정, 수율·양산 검증 미완)
- `<40%`: 2028년 이전 Tesla 자체 훈련 칩(Dojo AI7)이 NVIDIA 대비 가격·성능 동등 달성

## 주요 리스크 요약
- `TSMC 의존 리스크`: AI5가 TSMC N3P에 단일 의존하는 구조에서 대만 해협 지정학 리스크나 TSMC 생산 차질이 Tesla 차량 출하 일정에 직접 영향을 준다.
- `Samsung 대안 리스크`: Samsung SF4 기반 AI4의 수율 이력이 AI5 Samsung 대안 공정에 신뢰를 낮춘다. 대안 공정이 성능·수율 모두에서 TSMC와 격차가 있을 수 있다.
- `세대 전환 리스크`: AI4→AI5 전환 시 HW3→HW4 교체 프로그램과 유사한 호환성 단절이 발생할 수 있으며, 이는 고객 마찰과 소프트웨어 분기 비용을 높인다.
- `HW4.5 브리지 리스크`: HW4.5가 시장에 나올 경우 AI5 출시 전 혼란을 야기하고 소비자 구매 지연 현상이 발생할 수 있다.

## 연결 문서
- [dojo_roadmap.md](dojo_roadmap.md)
- [optimus_roadmap.md](optimus_roadmap.md)
- [../../../02_technology/semiconductors/roadmap_annual.md](../../../02_technology/semiconductors/roadmap_annual.md)

## 정보 출처
- notateslaapp AI5 production 2H 2026 TSMC N3P https://www.notateslaapp.com/news/3519/teslas-ai5-to-enter-production-in-2h-2026-rivals-nvidias-30k-chip-in-performance 2026-04 확인
- notateslaapp HW5 AI5 everything we know https://www.notateslaapp.com/news/2971/everything-we-know-about-hw5-ai5-teslas-next-gen-fsd-computer 2026-04 확인
- notateslaapp HW4.5 three-chip bridge https://www.notateslaapp.com/news/3529/tesla-fsd-hardware-45-appears-a-3-chip-upgrade-before-ai5 2026-04 확인
- notateslaapp AI4+ doubled memory https://www.notateslaapp.com/news/4032/tesla-announces-new-ai4-fsd-computer-with-more-memory-and-compute 2026-04 확인
- Electrek HW4 Plus upgrade announcement https://electrek.co/2026/04/23/tesla-hw4-plus-upgrade-will-hw4-follow-hw3/ 2026-04 확인
- Tesla Autopilot hardware Wikipedia https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware 2026-04 확인
- VideoCardz Dojo D1 50B transistors TSMC 7nm https://videocardz.com/newz/tesla-d1-chip-features-50-billion-transistors-scales-up-to-1-1-exaflops-with-exapod 2026-04 확인
- pcauto HW5 5x more power 2026 https://www.pcauto.com/my/news/teslas-next-generation-fsd-hardware-hw5-computing-performance-improved-by-5-times-mass-delivery-in-2026-16155 2026-04 확인
