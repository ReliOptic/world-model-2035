# Positive Surprises
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- 이 문서의 목적은 블랙스완의 대칭 항이다. 다수 예측 모델은 정책·거시 변수에 편향되어 있어, AlphaFold 계열의 "과학적 비연속(scientific discontinuity)"을 과소반영한다. 여기서는 "이미 실증 데이터가 있고 2035 전에 2-3배 스케일 확장이 있을 법한" 상방을 분야별로 집계한다.
- 소재·화학: DeepMind `GNoME`(2023)는 `2.2M` 신규 결정 후보를 예측, 이 중 `380,000`개가 안정 후보. `2024-08` 기준 convex hull `1 meV/atom` 이내 소재 `520,000+`개 공개, 외부 연구진이 이미 `736`개를 실험적으로 합성했다. AI-유도 합성은 `2030-2033`에 배터리·촉매·광전소재에서 새 성능 기록을 만들 가능성이 높다.
- 의약·생명: Isomorphic Labs `IsoDDE`(2026-02)는 AlphaFold 3의 단백질-리간드 예측 정확도를 `2배 초과`, Phase 1 첫 AI 설계 항암제가 `2026년 초` 시작. Eli Lilly·Novartis와 `~$3B` 계약. AlphaFold 3 자체는 이미 생물학 연구 표준으로 자리잡아 "AlphaFold 4"에 해당하는 IsoDDE가 인실리코 약물 디자인을 일상화시킬 가능성이 있다.
- 수학·알고리즘: DeepMind `FunSearch`(2023-12)는 LLM과 진화탐색을 결합해 수학·조합최적화에서 새로운 해를 발견했다. `2024-12` arXiv 보고서는 combinatorial competitive programming에서 인간 성능을 증폭하는 결과를 보였다. `AI 수학자/과학자`가 `2028-2030`에 노벨급·필즈급 기여를 공저할 가능성이 현실적 상방이다.
- 에너지: CFS SPARC `Q>1`(2027 목표), Helion Orion `50MW+`(2028 목표)가 모두 예정 범위 안에서 성공할 경우, `2030-2032` ARC/후속 플랜트 그리드 연결이 "상업 핵융합 실증"을 연다. 이 경로는 `2035-2040` 핵융합 상업화 가시권을 의미한다.
- 양자: Google Willow(2024-12)는 표면부호 `below threshold`를 최초 실증. IBM Starling(2029)이 `logical qubits 200, 100M gate operations`를 계획대로 낸다면 소재·암호·최적화 영역에서 `2030-2033`에 상업적 돌파가 나올 수 있다.
- 기후 모니터링: AlphaFold 수준의 관측 혁신이 이미 진행 중이다. ESA `Biomass` 위성(2025 발사), NASA-ISRO `NISAR`(2025 발사) 등이 탄소·수자원·빙권 관측 해상도를 단계별로 `10배+` 올린다. AI-위성 조합이 MRV(Measurement, Reporting, Verification)를 상용화하면 배출권·기후 금융의 정확도가 질적 전환을 겪는다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| DeepMind GNoME Nature 2023 | `2.2M` 신규 결정, `380K` 안정 후보, `520K+` 공개 | `2030`까지 실험 검증 `1-2%` 진행, `10,000+` 후보 실증 예상 | Nature 게재 + 외부 lab `736` 합성 확인 |
| Isomorphic Labs IsoDDE 2026-02 | AlphaFold 3 대비 예측 `2배`, Phase 1 AI 항암제 | 2028-2030에 Phase 2-3 다수 진입 | 27쪽 기술보고서, Eli Lilly·Novartis `$3B` 계약 |
| DeepMind FunSearch 2023-12 | 수학·알고리즘 신 해 발견, 경쟁 프로그래밍 인간 증폭 | 2028-2030에 AI 공저 노벨·필즈급 기여 가능 | Nature + arXiv 2024-12 |
| CFS SPARC / ARC | `Q>1` 2027, ARC `400MW` 2030s 초 | 2030-2032 ARC 실운전, 2034-2035 상업 2호기 | `$863M` 자본, NVIDIA·Siemens 디지털트윈 |
| Helion Orion | `50MW+` 2028 온라인 | 2028 PPA 이행 시 2031-2032 2호기 | Microsoft PPA, `$425M Series F` |
| Google Willow / IBM Starling | Willow below-threshold, Starling `200 logical qubits` 2029 | 2030-2033 신약·촉매·암호 응용 상용화 | Nature 2024, IBM 공식 로드맵 |
| ESA Biomass / NASA-ISRO NISAR | 2025 발사, 탄소·수자원 관측 해상도 수직상승 | 2028-2030 AI-위성 MRV 상용화 | ESA/NASA 공식 프로젝트 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 (돌파) | 지연 시나리오 (무산) | 확률 |
|---|---|---|---|---|
| 2026 | SPARC 첫 플라즈마, IsoDDE Phase 1, GNoME 실험 검증 누적 | Willow 후속칩이 `105→1,000` qubit 스케일 실증 | 핵융합 공학 지연, 임상 실패, AI 약물 파이프라인 정체 | 85% |
| 2027 | SPARC `Q>1`, AI 과학자 공저 논문 주요 학술지 다수 진입 | 첫 AI 설계 신약 2상 긍정 중간결과 | 규제·안전 이슈로 AI 설계 신약 임상 지연 | 80% |
| 2028 | Helion Orion `50MW` 온라인, GNoME 유래 신소재 배터리·촉매 상용 시제품 | 고체전지·Li-황 등 한 개 이상 학습곡선 재점화 | 신소재 스케일업 실패, 공급망 단절 | 65% |
| 2029 | IBM Starling `200 logical qubits`, 첫 AI 설계 신약 3상 진입 | 양자-고전 하이브리드가 신약·촉매·최적화에서 5-10배 가속 | 양자 결맞음·제조 지연, 임상 3상 실패 | 60% |
| 2030 | ARC 그리드 연결 시도, AI-위성 MRV가 `$100B+` 배출권 시장 재설계 | 핵융합 상업 2호기 착공, MRV 기반 기후금융 표준화 | 핵융합 상업성 미달, 기후금융 표준 분절 | 55% |
| 2031 | AI 과학자가 단독·주저자급 기여, AI 설계 신약 FDA 승인 사례 | 2-3개 과학 분야에서 "AI 촉매 패러다임" 공식 인정 | 과학계 역풍, AI 저자성 논쟁 장기화 | 50% |
| 2032 | 핵융합 PPA 확대, 양자 금융·물류 상업응용 `5-10개`, AI 설계 신약 시장 `$10B+` | LCOE 기준 핵융합이 가스복합보다 저렴한 구간 진입 | 가스·원자력이 더 빨리 확장되어 핵융합 상업화 지연 | 35% |
| 2033 | IBM Blue Jay 로드맵 `2000+ logical qubits`, 양자 내성 암호 전환 완료 | 양자가 소재·의약·재료에서 1세대 산업혁신 확정 | 양자 상업화가 소수 응용에 국한 | 55% |
| 2034 | AI+로봇이 건설·농업·돌봄에서 노동 부족 완화, 상업 핵융합 1호기 운전 | 질병 부담 상위 10개 중 3-4개에서 AI 설계 치료제 시판 | 기술 편익이 고소득국 편중, 분배 역풍 | 50% |
| 2035 | 과학적 비연속 3-5건 누적, 장기 성장률 추정 상향 가능 | `GNoME + IsoDDE + FunSearch + 핵융합 + 양자` 복수 조합 실현 | 여러 돌파가 기대에 못 미쳐 Hype Cycle 바닥 재진입 | 35% |

## 물리적/구조적 한계
- 탐지 한계: 좋은 뉴스는 과대선전(hype)과 구분이 필요하다. LK-99 같은 상온 초전도 주장은 `2023-2025` 반복적으로 재현 실패했다. 긍정 서프라이즈는 "계속 스케일업되는 공식 로드맵이 있는 항목"에 한정해야 한다.
- 확산 한계: 돌파가 있어도 제도·인프라 확산은 느리다. AlphaFold 3가 신약 시판으로 이어지려면 임상 3상·규제·제조·유통 `7-10년` 파이프라인이 필요하다.
- 분배 한계: 긍정적 돌파도 편중될 수 있다. AI 설계 신약, 핵융합 전력은 고소득 시장에서 먼저 상용화되고, 글로벌 확산은 `2040+` 단위가 될 수 있다.
- 자원 한계: 돌파가 스케일업되려면 물·토지·희소금속·숙련인력이 필요하다. `2030년대 초` 전력·토지·용수 병목이 과학 돌파의 상업화를 제한할 수 있다.
- 제도 한계: AI 저자성, AI 설계 신약, 핵융합 안전 규제는 `2030년` 이전 표준화되지 않는다. 제도 지체가 잠재 편익의 현실화를 늦춘다.

## 기술 현실론 보정
- 낙관론 측 근거: GNoME·IsoDDE·FunSearch·Willow·SPARC·Polaris는 모두 `2020-2026` 사이 실증 데이터를 냈다. 과학 돌파의 "기반 기술 성숙도"가 이미 충분히 높다.
- 현실론 측 반론: 스케일업에는 자본·규제·소비자 수용이 필요하고, 이 세 가지는 기술보다 느리다. 상방이 2030년대 초에 완전히 현실화될 확률은 Base Case가 본 `~50%` 부근이다.
- 균형 판단: 긍정 서프라이즈는 "하나만" 현실화돼도 Base → Accelerated 전환을 야기한다. "둘 이상"이면 구조적 상방. 이것이 black_swans.md와 대칭적으로 중요한 이유다.

## 2035 전망 요약
- Base: `GNoME·IsoDDE·FunSearch` 계열의 AI 과학 도구가 연구 표준이 된다. 핵융합 1-2기 상업 운전, 양자 5-10개 상업응용, AI 설계 신약 FDA 다수 승인. 과학적 비연속 3-5건 누적.
- Upside: 여러 S-curve가 한 번에 현실화돼 `2030년대 후반`에 장기 성장률 추정이 상향 조정된다. `accelerated.md` 경로로 수렴.
- Downside: 돌파들이 개별 기대에 못 미쳐 Hype Cycle `trough of disillusionment`를 거친다. 다만 기반 기술 성숙도가 이미 높으므로, 이 경우에도 2035년 Base 이하로 떨어지기는 어렵다.

## 연결 문서
- [black_swans.md](black_swans.md)
- [unknown_unknowns.md](unknown_unknowns.md)
- [interaction_effects.md](interaction_effects.md)
- [../13_scenarios/accelerated.md](../13_scenarios/accelerated.md)
- [../13_scenarios/base_case.md](../13_scenarios/base_case.md)
- [../11_science/biosecurity/pandemic_early_warning.md](../11_science/biosecurity/pandemic_early_warning.md)
- [../02_technology/semiconductors/roadmap_annual.md](../02_technology/semiconductors/roadmap_annual.md)
- [../03_energy/grid/ai_optimization.md](../03_energy/grid/ai_optimization.md)

## 정보 출처
- DeepMind GNoME materials discovery blog https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/ 2026-04 확인
- GNoME Nature paper https://www.nature.com/articles/s41586-023-06735-9 2026-04 확인
- Isomorphic Labs IsoDDE technical report https://www.isomorphiclabs.com/our-tech 2026-04 확인
- Scientific American AlphaFold 4 IsoDDE review https://www.scientificamerican.com/article/an-alphafold-4-scientists-marvel-at-deepmind-drug-spin-offs-exclusive-new-ai/ 2026-04 확인
- DeepMind FunSearch blog https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/ 2026-04 확인
- Commonwealth Fusion Systems SPARC https://cfs.energy/technology/sparc/ 2026-04 확인
- Helion Microsoft PPA https://www.helionenergy.com/articles/helion-announces-worlds-first-fusion-ppa-with-microsoft/ 2026-04 확인
- Google Willow quantum chip https://blog.google/technology/research/google-willow-quantum-chip/ 2026-04 확인
- IBM Quantum Roadmap https://www.ibm.com/roadmaps/quantum/ 2026-04 확인
- Nature quantum error correction below threshold https://www.nature.com/articles/s41586-024-08449-y 2026-04 확인
- LK-99 replication failure Physics World https://physicsworld.com/a/room-temperature-superconductor-lk-99-fails-replication-tests/ 2026-04 확인
