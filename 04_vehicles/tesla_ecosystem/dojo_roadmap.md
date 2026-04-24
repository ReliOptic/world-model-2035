# Tesla Dojo 로드맵
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Tesla의 Dojo 프로젝트는 `2025년 8월` Bloomberg 보도에 따라 사실상 해체됐다. Elon Musk는 `2026년 1월` 새로운 칩 반복(Dojo 3 / AI7 검토)으로 Dojo를 재시작하겠다고 발표했으나 구체적 양산 일정과 규모는 확정되지 않았다.
- Tesla의 실질 AI 훈련 인프라는 Dojo가 아니라 **Cortex GPU 클러스터**로 이동했다. Cortex는 `2025년 Q3` 기준 `H100 등가 약 81,000개`의 GPU를 보유한 것으로 보고됐으며, 최종 목표는 `H100/H200 최대 100,000개`다. Cortex는 세계 최대급 Hopper 기반 GPU 클러스터 중 하나다.
- Dojo D1 칩 원래 설계는 TSMC `7nm`, `500억 트랜지스터`, `645mm²` 다이, ExaPOD는 120타일로 `1.1 ExaFLOPS(BF16)` 성능을 목표로 했다. ExaPOD 개념은 실증됐으나 대규모 배포는 진행되지 않았다.
- Tesla는 현재 AI 추론용 전용 실리콘(AI4/AI5) 개발에 집중하고 있으며, 훈련은 NVIDIA GPU에 의존하는 구조가 `2026-2027`의 현실적 기반이다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Tesla AI Day 2021/2022 | Dojo D1 칩, ExaPOD 구조, 1 ExaFLOPS 목표 | ExaPOD 개념은 실증됐으나 대규모 배포로 이어지지 않았다. 목표 달성률은 낮다 | 2025년 사실상 해체가 이를 보여준다 |
| TechCrunch Dojo timeline | 2025년 해체, 2026년 1월 Musk 재시작 발표 | Dojo 재시작이 실제 제품으로 이어질 확률은 낮다. Cortex가 실질 훈련 인프라 | Musk 발표와 실제 실행 사이의 간극이 반복적으로 관찰됨 |
| Semi-Analysis / Tesla 실적 발표 | Cortex가 H100/H200 기반으로 81,000+ GPU 클러스터 구축 | Cortex는 실재하는 인프라다. NVIDIA 의존 구조는 비용 상승 리스크가 있다 | 실적 발표에서 Cortex 확장 계획이 언급됨 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Cortex 100,000 GPU 목표 달성, Dojo 재시작은 탐색 단계, AI5 추론 칩 양산 준비 | Dojo AI7 칩 설계 확정 및 TSMC 테이프아웃 | Dojo 재시작 발표가 실행으로 이어지지 않고 폐기 | 70% Cortex 목표 달성 |
| 2027 | Cortex가 AI 훈련의 핵심 인프라로 고정, Dojo는 틈새 실험 역할 | Dojo AI7이 추론·로보틱스 특화 칩으로 재포지셔닝 성공 | NVIDIA 공급 병목으로 Cortex 확장이 지연 | 65% |
| 2028 | Tesla가 자체 훈련용 칩 전략을 재검토하거나 차세대 Dojo로 재투자 결정 | Tesla 자체 AI 훈련 칩이 소량 양산 진입 | NVIDIA H200/B200 대비 성능 격차를 좁히지 못해 Dojo 재투자 취소 | 40% Dojo 재투자 |
| 2029 | 추론 전용 칩(AI5·AI6)과 훈련 인프라(Cortex/외부 클라우드)의 이원 구조 고착 | Tesla가 추론·훈련 통합 칩 전략 발표 | AI 훈련 비용 급등으로 Tesla FSD·Optimus 개발 속도 제약 | 55% |
| 2030 | 차세대 AI 인프라 전략이 확정되며 Tesla의 자체 실리콘 포트폴리오가 명확해짐 | Dojo 후속 칩이 NVIDIA 경쟁 영역에 진입 | NVIDIA/AMD/맞춤형 AI 칩 시장이 성숙해 Tesla 자체 훈련 칩의 ROI가 낮아짐 | 50% |
| 2031 | Tesla AI 인프라는 FSD·Optimus·에너지 최적화를 통합 지원하는 구조 | 자체 훈련+추론 통합으로 AI 개발 비용 대폭 절감 | 지정학 규제로 TSMC 의존 칩 공급에 차질 | 50% |
| 2032 | AI 추론 성능과 전력 효율이 Tesla 제품 경쟁력의 핵심 지표 | 온디바이스 모델이 클라우드 의존 없이 고도 자율성 구현 | 전력 밀도 제약으로 차량용 칩 성능 향상이 정체 | 55% |
| 2033 | Tesla 차량·로봇·에너지 제품 전반에 통합 AI 칩 아키텍처 적용 | AI 칩 내재화 완성으로 NVIDIA 의존 완전 탈피 | 경쟁사(NVIDIA, Google, Amazon)의 추론 칩이 외부 배포로 비용 역전 | 45% |
| 2034 | Tesla AI 칩이 자사 제품에 최적화된 도메인 특화 프로세서로 자리잡음 | 제3자 라이선스 또는 공급 계약으로 수익화 | 반도체 지정학 위기로 공급망 불안정 | 45% |
| 2035 | Tesla는 FSD·Optimus·에너지 AI를 자체 실리콘으로 구동하는 수직 통합 AI 기업 구조 완성 | Tesla 칩이 산업 표준 추론 플랫폼 중 하나로 부상 | 미세화 한계·패키징 비용으로 자체 칩 ROI 의문 지속 | 55% |

## 물리적/구조적 한계
- AI 훈련용 맞춤 칩은 NVIDIA의 생태계(CUDA, 소프트웨어 스택, 공급망)와 경쟁해야 하며, 단순 성능 우위만으로는 전환이 어렵다.
- 맞춤 칩 개발에는 수년의 설계·검증·양산 사이클이 필요하며 중간 실패 리스크가 상존한다.
- Cortex는 대규모 GPU 클러스터이지만 NVIDIA 공급·가격 정책에 종속돼 장기 비용 구조가 불확실하다.

## 기술 현실론 보정
- 낙관론 측 근거: Cortex는 실재하는 대규모 훈련 인프라이며 AI5 추론 칩 개발은 진행 중이다. Tesla는 자체 실리콘 역량을 실증했다.
- 현실론 측 반론: Dojo D1/ExaPOD 전략의 사실상 포기는 맞춤 훈련 칩이 생각보다 어렵다는 것을 보여준다. 재시작 발표는 실행 보장이 아니다.
- 균형 판단: Tesla의 실리콘 전략은 추론 칩(AI4/AI5)에서는 실적이 있지만 훈련 칩에서는 NVIDIA 의존이 현실이다.

## 2035 전망 요약
- Base: Tesla는 차량·로봇·에너지 추론에 자체 칩을 사용하고 훈련은 대형 GPU 클러스터(내부 Cortex 또는 외부 클라우드)에 의존하는 이원 구조를 유지한다.
- Upside: Dojo 후속 칩이 훈련과 추론을 통합하고 Tesla가 AI 인프라에서 NVIDIA 의존을 의미 있게 낮춘다.
- Downside: Dojo 재시작이 실행으로 이어지지 않고 NVIDIA GPU 비용 상승이 Tesla AI 개발 속도를 제약한다.

## 연결 문서
- [chip_factcheck.md](chip_factcheck.md)
- [optimus_roadmap.md](optimus_roadmap.md)
- [../../../02_technology/semiconductors/roadmap_annual.md](../../../02_technology/semiconductors/roadmap_annual.md)

## 확률 근거 요약
- `≥75%`: Cortex 100,000 GPU 목표 2026년 달성 (기존 81,000 확인, 증설 계획 발표)
- `≥75%`: Tesla AI 훈련이 2026~2027년 NVIDIA GPU 기반 유지 (Dojo 재시작 실행 증거 없음)
- `<40%`: Dojo AI7 칩 2027년 내 테이프아웃 (재시작 발표만 있고 일정·사양 미공개)
- `<40%`: 2028년 이전 Tesla 자체 훈련 칩이 Cortex 내 NVIDIA GPU 10% 이상 대체 (생태계 전환 비용 큼)

## 주요 리스크 요약
- `실행 리스크`: Dojo 재시작 발표는 Musk 트위터 수준의 발표이며 실제 칩 테이프아웃·양산 계획이 공개되지 않았다. 과거 패턴을 감안하면 재시작 발표가 실행으로 이어지지 않을 가능성이 있다.
- `공급 리스크`: Cortex는 NVIDIA H100/H200 공급에 의존하며, NVIDIA 가격 인상이나 공급 병목이 Tesla AI 개발 속도에 직접 영향을 준다.
- `경쟁 리스크`: Google TPU·AWS Trainium 등 자체 훈련 칩 기업들이 이미 대규모 생태계를 구축했으며, Tesla가 같은 경쟁에 진입하려면 CUDA 생태계에 상응하는 소프트웨어 스택이 필요하다.

## Dojo vs Cortex: 전략 전환 배경
- Dojo D1 ExaPOD는 `1.1 ExaFLOPS` 목표로 설계됐으나, NVIDIA H100 클러스터 `81,000개`로 구성된 Cortex는 유사한 훈련 처리량을 소프트웨어 생태계 호환성과 함께 제공한다.
- Tesla가 Cortex로 전환한 핵심 이유는 CUDA 생태계, 공급 안정성, NVIDIA H100의 빠른 납기 대응으로 분석된다. 자체 칩 설계·검증에 `2~4년`이 소요되는 동안 AI 경쟁이 NVIDIA GPU 중심으로 고속화됐다.
- Dojo 재시작 발표(`2026년 1월`)는 로보틱스(Optimus)와 우주 기반 응용을 명분으로 제시했다. 로봇 작업 학습은 시뮬레이션 기반 대규모 합성 데이터를 요구해 전용 훈련 가속기의 논리가 있으나 실행 증거가 아직 없다.
- 경쟁 맥락: Google TPU, AWS Trainium, Microsoft Maia 등 빅테크의 자체 훈련 칩 전략은 성공했지만, 이들은 자체 클라우드 수요를 내부 소화하는 구조다. Tesla는 내부 수요만으로 자체 훈련 칩 ROI를 정당화해야 하며 이것이 더 어려운 조건이다.

## 정보 출처
- TechCrunch Tesla Dojo rise and fall https://techcrunch.com/2025/09/02/tesla-dojo-the-rise-and-fall-of-elon-musks-ai-supercomputer/ 2026-04 확인
- TechCrunch Tesla Dojo timeline https://techcrunch.com/2025/09/02/teslas-dojo-a-timeline/ 2026-04 확인
- VideoCardz D1 chip 50B transistors ExaPOD https://videocardz.com/newz/tesla-d1-chip-features-50-billion-transistors-scales-up-to-1-1-exaflops-with-exapod 2026-04 확인
- DataCenterDynamics Tesla Dojo deployments https://www.datacenterdynamics.com/en/news/tesla-details-dojo-supercomputer-reveals-dojo-d1-chip-and-training-tile-module/ 2026-04 확인
- notateslaapp AI5 production 2H 2026 https://www.notateslaapp.com/news/3519/teslas-ai5-to-enter-production-in-2h-2026-rivals-nvidias-30k-chip-in-performance 2026-04 확인
- Tesla Dojo Wikipedia https://en.wikipedia.org/wiki/Tesla_Dojo 2026-04 확인
