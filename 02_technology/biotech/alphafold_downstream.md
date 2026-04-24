# AlphaFold 다운스트림 응용
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- AlphaFold 3는 2024년 5월 Nature에 발표되어 단백질·DNA·RNA·리간드·소분자·이온의 공동 구조 예측을 단일 diffusion 아키텍처로 수행한다. 기존 docking 도구 대비 정확도가 최소 `50%` 개선됐으며, 비상업 연구용 가중치는 `2024-11`부터 공개됐다.
- Isomorphic Labs는 AF3를 내부 Drug Design Engine(IsoDDE)으로 확장했다. IsoDDE는 단백질-리간드 구조 예측 정확도를 AF3 대비 2배 이상 높이고, 소분자 결합 친화도 예측과 신규 결합 포켓 탐색까지 통합한다. Eli Lilly·Novartis와 다중 파이프라인 협업이 진행 중이다.
- Generate:Biomedicines는 Novartis와 `$1B` 규모의 파트너십을 체결했다. 생성형 단백질 설계 플랫폼으로 항체·단백질 치료제를 de novo 생성하며, 구조 예측보다 생성 단계까지 파이프라인이 확장된 사례다.
- Absci는 생성형 AI + 습식 실험을 결합한 zero-shot 항체 설계를 2024년 Nature Biotechnology에 발표했다. AI가 설계한 항체를 실험 검증 없이 임상 후보까지 연결하는 파이프라인을 구축 중이다.
- AlphaFold Protein Structure Database는 2026년 초 재설계 인터페이스로 업데이트됐고, 구조 커버리지가 Uniprot의 대부분을 포함한다.
- 병목은 구조 예측에서 구조→기능→임상 연결로 이동했다. 예측 정확도 자체보다 "어떤 결합 포켓이 치료 관련성이 있는가"를 판단하는 생물학적 문맥 해석이 핵심 제약이다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| DeepMind AF3 Nature (2024-05) | 단백질-핵산-리간드 공동구조 예측, 비상업 가중치 공개 | `2026-2030` 구조생물학은 AI 예측이 선행하고 실험은 검증 단계로 역전 | Nature peer-reviewed |
| Isomorphic Labs IsoDDE | AF3 대비 2배+ 정확도, 결합 친화도·포켓 탐색 통합 | `2026-2028` 다국적 제약사와의 협업 파이프라인이 실제 임상 후보를 배출하는 첫 사례 등장 가능 | Isomorphic 공식 블로그 |
| Generate:Biomedicines | Novartis $1B 파트너십, de novo 단백질 생성 플랫폼 | 구조 예측→생성까지 파이프라인 확장이 확인됐지만, 임상 성공률이 검증 지표 | 공개 언론 보도 |
| Absci zero-shot 설계 | Nature Biotech 2024, AI 설계→임상 후보 연결 | 파이프라인 개념은 실증됐지만, 임상 2상 이상 성공이 실질 검증 | Nature Biotechnology |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | IsoDDE·Generate 등 2세대 AI 설계 도구가 다국적 제약사 파이프라인에 통합, 임상 후보 IND 신청 건수 증가 | AI 설계 후보의 1상 진입 속도가 기존 대비 30%+ 단축됨이 공개 데이터로 확인 | 예측-합성-검증 병목이 풀리지 않아 실제 IND는 소수에 그침 | 72% |
| 2027 | AI 설계 항체·단백질 치료제 중 최초 FDA IND 통과 + 1상 완료 사례 공개 | 복수 파이프라인이 1상에 진입해 AI 설계 플랫폼의 임상 신뢰도 확보 | 오프-타겟 효과 등 안전 데이터에서 예측 오류가 발견돼 파이프라인 재검토 | 60% |
| 2028 | AF3/IsoDDE 계열 구조 예측이 신약 설계 표준 인프라로 정착, 구조 예측 없이 설계를 시작하는 프로세스는 예외가 됨 | AI 파이프라인이 1상→2상 전환율을 업계 평균 대비 유의미하게 높임 | 임상 데이터 부족으로 AI 플랫폼의 실제 가치 논쟁이 지속 | 65% |
| 2029 | AI 기반 신약 후보 중 최초 FDA 승인 사례 (또는 승인 심사 단계 진입) | 만약 AI 설계 분자가 1개라도 NDA 승인되면 산업 패러다임 전환이 가속 | 임상 3상 실패로 AI 신약 설계의 예측력 한계가 재조명 | 35% |
| 2030 | 항체·소분자·RNA 치료제 3개 이상의 AI 설계 파이프라인이 임상 2상 이상 도달 | 다수 승인으로 AI-first 제약 플랫폼 기업 시가총액 급등 | 특허·지적재산 분쟁이 AI 설계 도구 보급을 늦춤 | 55% |
| 2031 | 구조 예측→생성→합성→임상의 전 주기 자동화 파이프라인(A-Lab 류)이 소형 타겟에서 표준화 | 폐쇄 루프 로봇 합성이 특정 계열에서 인간 개입 없이 후보를 배출 | 합성·품질 관리 병목이 풀리지 않아 여전히 인간 개입 필요 | 50% |
| 2032 | AF 계열 다음 세대(AF4 또는 동급) 시스템이 동적 구조·막 단백질·IDPs까지 커버 확대 | 동적 구조 예측이 활성화되어 알로스테릭 타겟 발굴이 급증 | 동적 계산 비용이 너무 높아 실용 규모 배포 제한 | 55% |
| 2033 | AI 신약 설계가 희귀질환·맞춤형 치료에서 단계적 표준이 됨 | 개인 게놈 기반 맞춤 분자 설계가 고소득 시장에서 상용화 | 보험·규제 미비로 맞춤형 AI 신약의 접근성 제한 | 60% |
| 2034 | AI 설계 플랫폼과 전통 제약사의 인수합병으로 산업 구조 재편 | 빅파마가 AI 플랫폼을 내재화해 외부 CRO 의존 급감 | 규제 프레임워크 미비로 AI 설계 책임 소재 불명확 | 55% |
| 2035 | AI 기반 구조 예측→설계→임상이 선도 제약사의 표준 R&D 경로가 되고, 전통적 HTS 스크리닝은 보완 수단으로 전락 | AI-first 신약 개발로 신약 실패율이 업계 평균 대비 유의미하게 개선됨 | AI 설계 분자의 장기 안전성 데이터 부족이 규제 승인 병목으로 고착 | 60% |

## 물리적/구조적 한계
- 구조 예측 정확도는 높아졌지만 "어떤 구조가 치료 활성을 갖는가"의 생물학적 판단은 여전히 인간이 담당한다.
- 단백질 역동성(IDPs, 구조 변화, 막 환경)은 AF3 diffusion 접근법도 다루기 어려운 영역으로 남아 있다.
- 합성 접근성, 독성, ADME 예측은 구조 예측과 별도 모델 계층이 필요하고 각각 검증 병목이 있다.
- 임상 데이터 피드백 루프가 느려 AI 플랫폼의 실제 예측력 교정에 수년이 걸린다.

## 기술 현실론 보정
- 낙관론 측 근거: AF3 Nature 발표, IsoDDE 2배+ 정확도 발표, Generate $1B 파트너십, Absci zero-shot 설계 Nature Biotech 발표는 모두 실물 진척이다.
- 현실론 측 반론: 구조 예측의 정밀도와 신약 임상 성공률은 직접 연결되지 않는다. 1상 진입까지의 속도는 개선될 수 있지만, 2·3상 성공률은 생물학적 복잡성에 지배된다.
- 균형 판단: `2026-2030`은 AI 설계 후보의 임상 진입이 가속하는 구간이며, `2030+`부터 임상 성공 데이터가 플랫폼 가치를 실질 검증하는 구간이다.

## 2035 전망 요약
- Base: AI 구조 예측·분자 생성이 선도 제약사의 표준 R&D 인프라가 되고, 전통 HTS는 보완 수단으로 후퇴한다.
- Upside: AI 설계 분자의 임상 성공률이 업계 평균을 유의미하게 상회하면서 AI-first 제약 플랫폼이 산업 주도권을 확보한다.
- Downside: 임상 실패 데이터가 축적되면서 AI 플랫폼의 예측력 한계가 드러나고, 규제 프레임워크 부재가 보급을 늦춘다.

## 연결 문서
- [./gene_editing.md](./gene_editing.md)
- [./longevity.md](./longevity.md)
- [../symbolic_reasoning/alphafold_lineage.md](../symbolic_reasoning/alphafold_lineage.md)
- [../symbolic_reasoning/science_methodology.md](../symbolic_reasoning/science_methodology.md)
- [../../13_scenarios/base_case.md](../../13_scenarios/base_case.md)

## 정보 출처
- AlphaFold 3 Nature (2024-05) https://www.nature.com/articles/s41586-024-07487-w 2026-04 확인
- AlphaFold 3 addendum Nature (2024-11) https://www.nature.com/articles/s41586-024-08416-7 2026-04 확인
- Isomorphic Labs Drug Design Engine https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier 2026-04 확인
- Isomorphic Labs AF3 rational drug design https://www.isomorphiclabs.com/articles/rational-drug-design-with-alphafold-3 2026-04 확인
- AlphaFold Protein Structure Database 2025 NAR https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkaf1226/8340156 2026-04 확인
- Generate:Biomedicines Novartis partnership (Drug Discovery News) https://www.drugdiscoverynews.com/ai-is-transforming-drug-discovery-16706 2026-04 확인
- DeepMind AlphaFold 3 blog https://blog.google/innovation-and-ai/products/google-deepmind-isomorphic-alphafold-3-ai-model/ 2026-04 확인
