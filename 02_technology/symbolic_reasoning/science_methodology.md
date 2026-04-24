# 기호추론과 과학 방법론
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Royal Society `Science in the Age of AI`(2024-05 보고서)는 AI 연구 도구의 불투명성이 과학적 재현성과 신뢰를 훼손할 수 있다고 공식 경고했다. Black-box AI의 모델 가중치·코드·데이터·계산 자원 비공개가 재현성을 구조적으로 제약한다고 명시했다.
- Royal Society와 Google DeepMind가 공동 주최한 `AI for Science Forum`은 가설 생성·실험 설계·검증 루프에서 AI의 역할이 재정의되는 방향을 체계화했다.
- Nature가 발간한 `AI for Science 2025` 특집은 AI가 화학·재료·생명과학에서 autonomous 실험 실행과 실시간 데이터 기반 파라미터 조정까지 진입했음을 확인했다.
- UC Berkeley `A-Lab`은 GNoME가 예측한 신소재 후보를 자율 합성 로봇이 인간 개입 없이 합성·특성화·피드백 루프로 처리하는 폐쇄 루프 자율 실험실 개념을 실증했다.
- AI 기반 가설 생성의 미해결 과제: AI는 패턴 귀납 속도는 압도적이지만 "왜 이 패턴이 인과적인가"를 설명하는 기계적 이해(mechanistic understanding)가 부재하다. Royal Society가 명시한 이 간극은 저장소 thesis `epistemology break`의 핵심이다.
- PMC 2025 리뷰는 AI와 자동화 로봇의 결합이 화학·재료 연구에서 고처리량·데이터 기반 실험을 가능하게 하며, 이를 통한 reinforcement learning 기반 폐쇄 루프 시스템이 실험 설계와 실행을 자율화하고 있음을 확인했다.

## 방법론 프레임
| 단계 | 자동화 가능 영역 | 인간 개입 필요 영역 | 병목 | 메모 |
|---|---|---|---|---|
| 가설 생성 | 대규모 데이터 패턴 귀납, 문헌 합성, 후보 생성(GNoME·FunSearch) | 인과 메커니즘 해석, 윤리·안전 우선순위 결정 | black-box 해석 불가 | AI 속도 > 인간 해석 속도 |
| 실험 설계 | 실험 공간 탐색 최적화, 고처리량 파라미터 조정 | 실험 목적·기준 정의, 위험 평가 | 설계 자동화 표준 미비 | A-Lab 류 폐쇄 루프 |
| 데이터 수집 | 자율 로봇 합성·측정, 고처리량 스크리닝 | 측정 기기 캘리브레이션·이상치 판단 | 합성 속도 < AI 예측 속도 | backlog 축적 위험 |
| 데이터 해석 | 패턴 인식, 이상치 탐지, 통계 분석 | 인과 추론, 반직관 결과 검토 | 고차원 결과 인간 재구성 한계 | epistemology break 핵심 |
| 결과 검증 | 자동화 재현 실험, 형식 증명(수학 분야) | peer-review, 안전성 평가, 책임 소재 | 구시대 peer-review 체계 | Royal Society 경고 영역 |
| 지식 편입 | 데이터베이스 갱신, 문헌 자동 요약 | 패러다임 판단, 교과서 편입, 사회적 합의 | AI-derived 지식의 권위·신뢰 기준 미비 | 장기 병목 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Nature/Science/Cell이 AI 기반 연구에 대한 공식 재현성·검증 가이드라인 채택 | 가이드라인 채택이 AI-driven 과학의 신뢰 회복 전환점이 됨 | 대형 AI 기반 retraction이 1건+ 발생하면 체계적 불신 증가 | 80% |
| 2027 | A-Lab 계열 자율 실험실이 재료·단백질·소분자 3개 분야에서 동시 운용 | 자율 실험실 네트워크가 글로벌로 연결되어 실험 처리량이 종래 대비 10배+ | 물리 합성·실험 단계가 AI 예측 속도를 따라가지 못해 백로그 축적 | 70% |
| 2028 | AI 발견이 인간 해석 능력을 초과하는 영역(고차원 상호작용, 대규모 시뮬)이 주요 저널에 명확히 드러남 | 해석가능성 연구가 circuit-level 이해와 도메인 과학을 결합해 black-box를 부분 완화 | SAE·circuit tracing이 실용 규모로 확장되지 못해 black-box 고착 | 55% |
| 2029 | 노벨상급 발견 중 최소 1건이 AI-assisted임이 공식 인정 | peer-review가 AI-assisted를 별도 평가하는 체계를 갖추어 신뢰 보존 | 저자권·기여도·책임 소재 혼란이 학계 거버넌스 위기 | 35% |
| 2030 | AI가 제안한 가설 중 인간이 직관적으로 재구성하지 못하는 사례가 주요 저널에 빈발 | human-in-the-loop 재구성 연구가 제도화되어 epistemology break 부분 가교 | 재구성 연구 실패 시 과학 지식 일부가 "AI만 이해하는 영역"으로 구조화 | 38% |
| 2031 | 폐쇄 루프 자율 실험실이 약학·재료·에너지 3개 산업의 초기 발견 파이프라인에 통합 | 자율 실험이 인간 실험 대비 특정 분야에서 비용 1/10·속도 10배 실증 | 실험 자동화 비용·표준화·데이터 품질이 산업 채택의 구조 장벽 | 55% |
| 2032 | AI-derived 발견이 직접 양산 파이프라인에 통합되어 임상·안전 검증 프레임워크가 표준화 | AI 발견 기반 신약·소재가 규제 승인 트랙의 단축 경로로 인정 | 규제·검증이 뒤따르지 못해 안전 사고 시 전체 분야 신뢰 충격 | 60% |
| 2033 | AI-derived 수학 정리 중 인간이 검증만 하고 이해는 제한적인 사례가 일상화 | Lean/Coq 기반 형식 검증이 수학 지식의 기계 검증 표준이 되어 신뢰 가능 | formal verification 확장 실패 시 수학계 내부 분열 가능 | 50% |
| 2034 | AI for Science가 국가 연구 정책의 중심축으로 자리잡고, 연구자 역할이 가설 제시에서 해석·선택·검증으로 재정의 | 과학 교육·연구 평가가 이 전환에 맞춰 개편되어 AI-native 연구자 세대 성장 | 제도·평가가 구시대에 머물면 세대 간 역량 격차 확대 | 55% |
| 2035 | 인간이 가설 없이도 법칙을 귀납할 수 있는 영역이 단백질·재료·수학·기후 분야에 존재. 그 지식의 해석·검증·책임은 여전히 인간에게 남음 | 해석가능성·검증·거버넌스 3축이 동시에 성숙해 epistemology break가 "확장된 인식론"으로 흡수 | 3축 중 하나라도 실패하면 과학 지식이 "인간 이해 프론티어"와 "AI 귀납 영역"으로 이원화 | 60% |

## 물리적/구조적 한계
- 검증 병목: AI는 후보 생성 속도가 실험·합성·증명 검증보다 훨씬 빠르다. GNoME `38만 개` 후보 대비 실제 합성 시도는 수천 건 수준이며, 구조적 backlog가 쌓인다.
- 해석 병목: 단백질 상호작용, 고차원 물리장, 대규모 시뮬레이션 결과는 인간의 직관적 재구성을 넘어선다. 해석가능성 연구가 도메인 과학 수준으로 내려오지 못하고 있다.
- 재현성 병목: 모델 가중치·코드·데이터·계산 자원 비공개가 재현성을 구조적으로 제약한다. AI-first 논문의 peer-review 절차는 여전히 실험을 전제로 설계된 구시대 체계다.
- 거버넌스 병목: AI-assisted 논문의 저자권·기여도·책임, AI가 발견한 지식의 라이선스·특허·안전 책임이 제도적 공백 상태다.
- 자원 병목: frontier AI for science는 소수 기관에 집중되어 과학의 개방성이 약화된다.

## 기술 현실론 보정
- 낙관론 측 근거: Royal Society 공식 보고서, A-Lab 자율 실험 시연, Nature AI for Science 2025 특집, GNoME·FunSearch·AlphaFold 3 등 복수의 peer-reviewed 진척이 실물 근거다.
- 현실론 측 반론: AI 도구 확산이 과학 생산성을 자동으로 높이지 않는다. 재현성·해석·거버넌스 3가지 병목이 해결되지 않으면 AI-driven science의 신뢰가 오히려 과학 기관의 권위를 약화할 수 있다.
- 균형 판단: `2026-2030`은 AI 발견 속도가 인간 해석·검증 속도를 앞서는 구조가 명확해지는 구간이다. `2030+`부터 해석가능성·자동검증·거버넌스 3축의 성숙도가 epistemology break를 흡수할지 이원화로 갈지를 결정한다.

## 2035 전망 요약
- Base: AI for Science가 가설 생성·실험 설계·데이터 해석을 자동화하되, 인과 해석·검증·책임은 인간이 담당하는 이중 구조가 제도화된다.
- Upside: 해석가능성·자동 검증·거버넌스가 동시에 성숙하여 AI-native 과학이 확장된 인식론 체계로 정착한다.
- Downside: 재현성·black-box·거버넌스 문제가 미해결 상태로 지속되면서 과학 지식이 "인간이 검증 가능한 전통 과학"과 "AI 귀납 영역"으로 이원화된다.

## 연결 문서
- [./epistemology_break.md](./epistemology_break.md)
- [./roadmap_annual.md](./roadmap_annual.md)
- [./alphafold_lineage.md](./alphafold_lineage.md)
- [../biotech/alphafold_downstream.md](../biotech/alphafold_downstream.md)
- [../../00_foundations/axioms.md](../../00_foundations/axioms.md)

## 정보 출처
- Royal Society Science in the Age of AI (2024-05) https://royalsociety.org/news-resources/projects/science-in-the-age-of-ai/ 2026-04 확인
- Royal Society AI research tools undermine trust https://royalsociety.org/news/2024/05/ai-research-tools-could-undermine-trust-accuracy-scientific-findings/ 2026-04 확인
- Royal Society AI for Science Forum YouTube https://www.youtube.com/playlist?list=PLqYmG7hTraZBwZQwCxzIlsyFxC3WKH_Ii 2026-04 확인
- Nature AI for Science 2025 https://www.nature.com/articles/d42473-025-00161-3 2026-04 확인
- PMC AI automation autonomous robotics science 2025 https://pmc.ncbi.nlm.nih.gov/articles/PMC12337156/ 2026-04 확인
- Royal Society Accelerating AI for science open data https://royalsocietypublishing.org/doi/10.1098/rsos.231130 2026-04 확인
- GNoME Nature (2023-11) https://www.nature.com/articles/s41586-023-06735-9 2026-04 확인
