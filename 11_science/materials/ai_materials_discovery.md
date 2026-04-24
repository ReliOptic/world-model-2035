# AI 소재 발견 (AI Materials Discovery)
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-10

## 2026년 4월 현재 상태
- Google DeepMind의 `GNoME`(Graph Networks for Materials Exploration)는 2023년 11월 Nature에 발표됐다. 17일 만에 `220만 개`의 안정적 무기 결정 구조를 예측했으며, 이 중 `38만 개`는 합성 가능한 유력 후보로 분류됐다. 기존 과학 문헌 기반 발견량의 약 800년치에 해당하는 규모다.
- GNoME 발견 물질 중 700개 이상이 이미 독립 실험에서 검증됐고, 그래핀과 유사한 층상 구조 물질 `5만 2,000개`와 리튬이온 전도체 `528개` 등이 포함된다. 리튬이온 전도체 후보 수는 기존 연구의 25배에 달한다.
- Microsoft Research의 `MatterGen`은 특정 물성(전도도, 자성, 안정성)을 역으로 지정해 신소재를 생성하는 generative AI 모델이다. 특정 목표 속성을 역설계(inverse design)하는 방향으로 GNoME의 탐색 접근을 보완한다.
- `Materials Project`(Berkeley Lab)는 DeepMind의 발견 물질 중 38만 개를 데이터베이스에 통합해 공개했다. 연구자들이 AI 후보 물질에 접근해 실험 우선순위를 정하는 공개 인프라로 기능한다.
- `ALIGNN`(Atomistic Line Graph Neural Network, NIST) 등 여러 기관의 그래프 신경망이 소재 특성 예측 정확도를 높이고 있다. 자율 실험실(self-driving lab) 개념이 대학·국가연구소에서 시험 운영 단계에 들어갔다.
- 중요한 한계: The Stack Technology 등 독립 분석에서는 "GNoME 후보 물질 중 상당수는 아직 실험 합성이 검증되지 않았으며, 예측 안정성과 실제 합성 성공률은 다른 지표"라는 비판이 제기됐다. 발견(discovery)과 실용화(industrialization)의 간극은 여전히 크다.
- 현재 상태 해석:
  - 확인된 사실: AI 기반 소재 후보 생성 속도는 전통 방식 대비 수 자릿수 이상 빠르다
  - 확인된 사실: 700개 이상의 독립 실험 검증은 실제 발견 효용의 초기 증거다
  - 열린 가설: 배터리·반도체·초전도체 등 핵심 응용 분야에서 AI 발견이 제품화로 연결되는 첫 사례가 언제 나올지는 아직 불분명하다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| DeepMind — GNoME (Nature 2023) | 220만 개 안정 결정 구조 예측; 700개 이상 실험 검증 | 후보 생성 단계는 성숙; 합성·스케일업은 별도 병목 | 동료검토 Nature 논문 + 독립 검증 증거 |
| Microsoft Research — MatterGen | 목표 속성 역설계 소재 생성 AI | GNoME와 상호 보완적; 두 접근 모두 실험 재현 검증 필요 | 독립 Microsoft Research 시스템 |
| Materials Project (Berkeley Lab) | GNoME 38만 개 후보 물질 공개 데이터베이스 통합 | 공개 데이터 인프라로서 연구 가속에 기여 | 국가 연구소 운영 공개 인프라 |
| NIST — ALIGNN | 그래프 신경망 기반 특성 예측 정확도 향상 | 기존 DFT보다 100-1,000배 빠른 특성 스크리닝 가능 | 공공 기관 발표 모델 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | GNoME 후보 물질 중 추가 수백 개의 독립 실험 검증 보고; 배터리·촉매 분야 첫 상업 적용 후보 공개 | 배터리 전해질 AI 발견 후보가 스타트업 합성 실증 성공 | 합성 성공률이 낮아 실용화 기대 하향 조정 | 60% |
| 2027 | 자율 실험실(self-driving lab) 첫 연간 독립 운영 성과 발표 | 자율 실험실이 인간 연구자 주도 대비 50% 이상 빠른 검증 달성 | 자율 실험실의 실패 사례가 신뢰도 우려 야기 | 50% |
| 2028 | MatterGen류 역설계 모델로 발견된 고성능 촉매 물질의 실험실 검증 | 질소 고정 또는 수소 생산 촉매 분야 AI 발견 첫 실험 성공 | 역설계 모델이 계산 데이터 편향으로 외삽 실패 | 45% |
| 2029 | AI 발견 소재의 첫 파일럿 제조 단계 진입 (배터리 전해질 또는 반도체 기판) | 파일럿 제조 결과가 기존 소재 대비 10% 이상 성능 개선 증명 | 파일럿 수율 문제로 상용화 일정 지연 | 40% |
| 2030 | AI 소재 discovery가 배터리·반도체·촉매 R&D 파이프라인의 표준 단계로 편입 | 주요 소재 기업이 AI discovery를 100% 내재화 | 전통 방식과의 통합 어려움으로 채택이 제한적 | 55% |
| 2031 | AI 발견 물질 기반 상용 제품 첫 출시 (배터리 전해질 또는 열전소재) | 시장 출시 제품이 성능과 비용 모두 경쟁력 증명 | 제조 공정 통합이 병목으로 남아 출시 지연 | 40% |
| 2032 | 고엔트로피 합금, 2D 소재, 페로브스카이트 등 복합 구조 AI 탐색 본격화 | 복합 소재 탐색에서 GNoME급 결과 반복 | 복잡계 소재의 DFT 학습 데이터 품질 한계 | 45% |
| 2033 | AI 발견 소재의 환경·독성·공급망 리스크 자동 평가 도구 표준화 | 안전·규제·공급 일체 평가로 개발 속도 추가 향상 | 안전 데이터 부족으로 규제 승인 병목 | 50% |
| 2034 | AI 소재 발견 분야 특허 분쟁 및 지식재산 표준화 논쟁 본격화 | 오픈 사이언스 프레임이 공공재로서 기반 소재 데이터 공유 보장 | 기업 독점으로 공개 데이터 생태계 약화 | 45% |
| 2035 | AI 소재 발견은 배터리·반도체·촉매 분야에서 R&D 표준 도구가 됐지만, 발견-합성-제조-상용화 전환율은 여전히 낮다 | AI 발견 소재 기반 제품이 다수 카테고리에서 시장 진입 | 후보 생성은 폭발적이지만 실질 제품화는 소수 틈새에 한정 | 중 |

## 물리적/구조적 한계
- 데이터 병목:
  - 계산 데이터(DFT) 편향 — 실험 데이터와 괴리 존재
  - 음성 결과(합성 실패) 데이터가 학습 데이터에서 과소 표현됨
  - 합성 가능성을 직접 예측하는 모델은 아직 미성숙
- 모델 병목:
  - 외삽 영역에서의 불확실성 과소평가
  - 다성분계·복합 구조 소재로의 적용 한계
- 전환 병목:
  - 실험실 검증 → 파일럿 제조 → 양산으로 이어지는 각 단계의 독립적 병목
  - 원자재 공급망과 공정 통합 비용
  - 규제·안전 검증 요구

## 기술 현실론 보정
- 낙관론 측 근거:
  - GNoME는 800년치 발견을 17일에 달성했다 — 후보 탐색 속도는 혁명적이다
  - 700개 이상의 독립 실험 검증은 단순 컴퓨팅 주장이 아닌 실증 증거다
  - 자율 실험실과 AI discovery의 결합이 검증 속도도 높이고 있다
- 현실론 측 반론:
  - 예측 안정성 ≠ 합성 가능성; 발견과 실용화의 간극은 여전히 수년~수십 년
  - 220만 개 중 실제 제품화에 연결될 소재는 극소수일 것이다
  - "scant evidence" 비판처럼 AI chemistry 주장의 과장이 반복되는 역사가 있다
- 균형 판단:
  - AI 소재 발견은 R&D 파이프라인의 탐색 단계를 혁신했다; 그러나 산업 임팩트는 합성·제조·상용화 단계의 성숙도가 결정한다

## 2035 전망 요약
- Base: AI 소재 발견은 핵심 응용 분야(배터리, 반도체, 촉매) R&D의 표준 첫 단계가 되지만, 후보→제품 전환율은 낮은 상태를 유지한다
- Upside: 자율 실험실 + AI 역설계 + 공개 데이터 인프라가 결합해 배터리·촉매 분야에서 게임체인저 소재가 실제 제품으로 출시된다
- Downside: 발견 속도는 계속 빠르지만 합성·제조 병목이 해소되지 않아 실질 산업 임팩트는 2040년대로 지연된다

## 연결 문서
- [superconductor.md](superconductor.md)
- [../physics/unification_ai_attempt.md](../physics/unification_ai_attempt.md)
- [../../02_technology/semiconductors/roadmap_annual.md](../../02_technology/semiconductors/roadmap_annual.md)

## 정보 출처
- [DeepMind — Millions of new materials discovered with deep learning (Nature 2023)] [https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/] [2026-04-23]
- [Nature — Scaling deep learning for materials discovery (GNoME)] [https://www.nature.com/articles/s41586-023-06735-9] [2026-04-23]
- [Berkeley Lab — Google DeepMind Adds Nearly 400,000 New Compounds to Materials Project] [https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project/] [2026-04-23]
- [VentureBeat — Google DeepMind's materials AI has already discovered 2.2 million new crystals] [https://venturebeat.com/ai/google-deepminds-materials-ai-has-already-discovered-2-2-million-new-crystals] [2026-04-23]
- [The Stack Technology — Scant evidence: Google's AI chemistry claims misleading] [https://www.thestack.technology/scant-evidence-googles-ai-chemistry-claims-were-misleading/] [2026-04-23]
- Inference note: 2026-2035 annual milestones are repository inferences anchored to GNoME publication, Materials Project integration, and known materials TRL progression rates.
