# AlphaFold 계보와 기호추론
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `AlphaFold 2`(2020 CASP14)는 단백질 단일 도메인 구조 예측에서 인간 전문가 수준을 최초로 달성했다. MSA(다중 서열 정렬)와 어텐션 트랜스포머를 결합한 구조로, 기존 물리 기반 예측의 패러다임을 데이터 기반 학습으로 전환했다.
- `RoseTTAFold`(Baker lab, 2021 Science)는 1D 서열·2D 거리 지도·3D 좌표 간 정보가 상호 흐르는 3-track 신경망을 사용했다. 단일 도메인 정확도는 AF2보다 낮지만 단백질 복합체 모델링에서 보완적 강점을 보였다. `RoseTTAFold All-Atom`으로 확장되어 소분자·핵산·금속을 포함하는 복합 구조 예측이 가능해졌다.
- `ESMFold`(Meta, 2022)는 MSA를 사용하지 않고 단백질 언어 모델(ESM-2) 만으로 구조를 예측하는 접근법이다. MSA 없이 단일 서열로도 예측이 가능하여 대규모 게놈 수준 스크리닝에 속도 이점을 제공한다.
- `AlphaFold 3`(DeepMind·Isomorphic, 2024-05 Nature)는 구조 모듈을 diffusion 모듈로 교체하여 단백질·DNA·RNA·리간드·금속·수정 잔기를 단일 시스템에서 예측한다. 원자 좌표 직접 예측이 가능하며, 기존 docking 도구 대비 `50%` 이상 정확도가 개선됐다.
- `Isomorphic Labs Drug Design Engine(IsoDDE)`은 AF3를 넘어 단백질-리간드 구조 정확도를 2배+ 향상하고, 결합 친화도 예측과 신규 결합 포켓 탐색을 추가한다. 다국적 제약사(Eli Lilly·Novartis)와의 파이프라인에 실제로 사용 중이다.
- 이 계보 전체가 공통으로 남기는 함의: 기호적 물리 규칙 없이 데이터 기반 학습만으로 분자 구조 예측이 가능함을 증명했다. 그러나 예측한 구조가 왜 그런 생물학적 기능을 갖는지는 여전히 인간 해석이 필요하다.

## 계보 프레임
| 시스템/단계 | 해결 문제 | 기호성 요소 | 한계 | 메모 |
|---|---|---|---|---|
| AlphaFold 2 (2020) | 단백질 단일 도메인 구조 예측 | MSA(진화 정보), 기하 제약 | 복합체·리간드·핵산 미포함 | CASP14 혁명적 정확도 달성 |
| RoseTTAFold (2021) | 복합체 포함 단백질 구조 예측 | 3-track 정보 흐름(1D/2D/3D) | 단일 도메인 정확도 AF2 대비 낮음 | Baker lab, 복합체 강점 |
| ESMFold (2022) | MSA 없는 고속 단일 서열 예측 | 단백질 언어 모델만 사용 | 정확도 AF2 대비 낮지만 속도 대폭 향상 | 게놈 규모 스크리닝 적합 |
| RoseTTAFold All-Atom (2024) | 소분자·핵산·금속 포함 복합 구조 | 원자 수준 다체 상호작용 표현 | 계산 비용 증가 | Baker lab 확장 |
| AlphaFold 3 (2024) | 단백질+핵산+리간드 공동 구조 | diffusion 아키텍처, 원자 좌표 직접 예측 | 동적 구조·IDPs 여전히 어려움 | 50%+ 정확도 개선 |
| IsoDDE (2025+) | 결합 친화도·포켓 탐색 포함 | AF3 상위 레이어, 약물 설계 특화 | 임상 검증은 별도 과제 | Isomorphic Labs 내부 시스템 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | AF3 기반 파이프라인이 글로벌 상위 10개 제약사 내부 구조 예측 표준으로 확정 | IsoDDE 또는 동급 시스템이 AF3 대비 3배+ 정확도 달성을 공개 발표 | AF3의 동적 구조·IDPs 한계가 주요 타겟 클래스에서 파이프라인 재검토 요인이 됨 | 85% |
| 2027 | RoseTTAFold All-Atom 계열이 소분자+단백질+핵산 3체 복합 구조 예측에서 실험 검증 데이터를 다수 확보 | Baker lab 시스템이 특정 RNA-단백질 복합체에서 cryo-EM을 선행하는 예측 정확도 달성 | 다체 복합 구조의 데이터 부족이 훈련 품질 한계로 작용해 정확도 정체 | 78% |
| 2028 | AF 계열 다음 세대(AF4 또는 동급)가 단백질 역동성(conformational ensemble) 예측을 포함 | 역동성 예측이 알로스테릭 타겟 발굴을 대폭 확장하여 신약 설계 분야 폭발적 성장 | 역동성 계산 비용이 너무 높아 실용 규모 배포 제한 | 50% |
| 2029 | 구조 예측 기반 신약 후보 중 AF 계열 예측이 핵심 근거가 된 사례가 FDA IND 3개+ 달성 | AF 기반 예측이 임상 1상 성공률을 실증적으로 높임이 공개 데이터로 확인 | 예측-합성-임상 연결 병목이 지속되어 구조 예측의 임상 가치 논쟁 | 35% |
| 2030 | 막 단백질·IDPs·클라이언트-샤페론 복합체 등 난이도 높은 구조군의 예측 정확도가 실용 수준 도달 | 기존 구조 미결정 타겟 500개 이상이 AI 예측으로 처음 해결 | 막 단백질의 지질 이중층 환경·동적 구조가 in silico 예측의 구조적 한계로 고착 | 30% |
| 2031 | 단백질 설계(inverse folding)가 치료 항체·효소·바이오소재 3개 분야에서 상업 파이프라인 표준화 | de novo 설계된 단백질 기반 촉매가 화학 산업 공정에서 실용화 | 설계 공간의 광대함으로 인해 최적 후보 탐색이 계산·실험 병목 지속 | 55% |
| 2032 | ESM 계열 단백질 언어 모델이 게놈 규모 변이 해석(functional annotation)에서 임상 진단 표준으로 진입 | 단백질 언어 모델이 전장 게놈 변이의 임상 의미 예측에서 유전 카운슬링 자동화 | 희귀 변이 학습 데이터 부족으로 임상 관련 변이 해석 정확도가 규제 기준 미달 | 45% |
| 2033 | 구조 예측·설계·기능 예측이 통합된 단일 플랫폼이 의약품·소재·식품 3개 산업의 표준 R&D 인프라 | 통합 플랫폼이 기존 분야 경계를 허물어 생명공학-소재-화학의 R&D 수렴 가속 | 플랫폼 독점화로 소수 기업만 접근 가능해지면서 과학의 개방성 약화 | 55% |
| 2034 | AlphaFold 계보가 세포 수준·조직 수준 멀티스케일 시뮬레이션으로 확장 시도 | 세포 내 전체 단백질 상호작용 네트워크 시뮬레이션이 질병 메커니즘 이해를 혁파 | 세포 수준 복잡성이 원자 수준 예측 정확도로 해결될 수 없음이 명확해짐 | 40% |
| 2035 | AlphaFold 계보는 단백질·핵산·소분자의 구조 예측을 과거의 X선 결정학처럼 일상 도구화하고, 다음 과제는 기능·동역학·맥락 예측으로 이동 | 구조→기능→동역학→세포 맥락 전 주기 예측이 AI-native 생명과학 R&D의 기반이 됨 | 구조 예측은 성숙하지만 그 위에 올라서는 기능·임상 번역 병목이 2035년에도 핵심 제약으로 남음 | 65% |

## 물리적/구조적 한계
- 동적 구조(conformational ensemble): 단백질은 고정 구조가 아니라 다수의 형태를 넘나든다. 현재 AF 계열은 대표 구조 하나를 예측하며, 동적 앙상블 예측은 계산 비용이 크다.
- 고유 무질서 단백질(IDPs): 안정 구조가 없는 단백질은 현재 예측 방법론의 기본 가정(구조 형성)에 맞지 않는다.
- 막 단백질: 지질 이중층 환경을 모델에 포함하지 않으면 실제 세포 내 구조와 차이가 난다.
- 함수→기능 번역: 구조가 정확해도 "어떤 기능을 하는가"를 아는 것은 별도의 생물학적 지식이 필요하다.

## 기술 현실론 보정
- 낙관론 측 근거: AF2·AF3·RoseTTAFold All-Atom·ESMFold·IsoDDE는 모두 실물 발표와 데이터가 있는 실진척이다. AF3은 Nature peer-reviewed이고 IsoDDE는 상업 파이프라인에 실제 적용 중이다.
- 현실론 측 반론: 구조 예측 정확도와 신약 임상 성공률은 직접 연결되지 않는다. 기능·ADME·독성은 별도 모델과 실험이 필요하다.
- 균형 판단: AlphaFold 계보는 구조생물학의 X선 결정학처럼 표준 도구가 되는 방향이 확실하다. 다음 10년의 경쟁은 구조→기능→임상 번역 파이프라인을 얼마나 빠르게 검증하느냐다.

## 2035 전망 요약
- Base: AlphaFold 계보는 단백질·핵산·소분자 구조 예측을 일상 도구로 만들고, 다음 경쟁은 구조 위에 기능·동역학·임상 번역을 얼마나 자동화하느냐로 이동한다.
- Upside: 통합 구조-기능-설계 플랫폼이 생명공학·소재·화학 R&D를 수렴시키며 AI-native 과학 시대를 연다.
- Downside: 구조 예측은 성숙하지만 기능·임상 번역 병목이 해소되지 않아 R&D 속도 개선의 실질 한계가 드러난다.

## 연결 문서
- [./epistemology_break.md](./epistemology_break.md)
- [./roadmap_annual.md](./roadmap_annual.md)
- [./science_methodology.md](./science_methodology.md)
- [../biotech/alphafold_downstream.md](../biotech/alphafold_downstream.md)
- [../../09_corporate_roadmaps/ai_labs/google_deepmind.md](../../09_corporate_roadmaps/ai_labs/google_deepmind.md)

## 정보 출처
- AlphaFold 3 Nature (2024-05) https://www.nature.com/articles/s41586-024-07487-w 2026-04 확인
- AlphaFold 3 addendum Nature (2024-11) https://www.nature.com/articles/s41586-024-08416-7 2026-04 확인
- RoseTTAFold Science (2021) https://www.science.org/doi/10.1126/science.abj8754 2026-04 확인
- AlphaFold and what is next bridging biology (2025) https://www.tandfonline.com/doi/full/10.1080/14789450.2025.2456046 2026-04 확인
- Deep Learning AF2 RoseTTAFold overview https://www.researchgate.net/publication/386648348_Deep_Learning_Models_for_Protein_Structure_Prediction_AlphaFold2_and_RoseTTAFold 2026-04 확인
- Isomorphic Labs Drug Design Engine https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier 2026-04 확인
- AlphaFold Protein Structure Database 2025 NAR https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaf1226/8340156 2026-04 확인
- FEBS Open Bio outlook structural biology after AlphaFold 2025 https://febs.onlinelibrary.wiley.com/doi/10.1002/2211-5463.13902 2026-04 확인
