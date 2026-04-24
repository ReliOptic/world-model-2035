# Google Quantum AI
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Google Quantum AI는 `2024-12` `Willow` 프로세서(105큐비트)를 Nature에 발표했다. 핵심 성과는 두 가지다. 첫째, 서피스 코드 크기를 3×3→5×5→7×7로 키울 때마다 논리 오류율이 `2.14배` 억제되는 지수적 오류 억제를 처음 실증했다(임계값 이하 달성). 둘째, 무작위 회로 샘플링(RCS) 벤치마크에서 세계 최강 슈퍼컴퓨터가 10 자양(10²⁵)년에 완료할 계산을 5분 이내에 수행했다.
- 달성된 논리 오류율은 distance-7 코드에서 `0.143% ± 0.003%/사이클`이다. 실용적 양자 알고리즘 실행에 필요한 `10⁻⁶`/사이클 수준과는 수 자릿수 격차가 여전히 존재한다.
- Google의 내부 로드맵은 `2029년` 실용적 양자 우위를 첫 번째 의미 있는 현실 문제에서 달성하는 것을 목표로 한다. Boehringer Ingelheim과의 파트너십은 양자 화학 계산을 통한 신약 후보 발굴에 집중하고 있다.
- Google은 `Quantum Echoes` 방식을 통해 오류 정정을 실시간 디코딩과 결합하는 실험을 진행 중이며, 72큐비트 프로세서에서 실시간 디코딩 상태에서도 임계값 이하 동작을 유지했다.

## 평가 프레임
| 항목 | 현재 상태 | 강점 | 약점 | 검증 메모 |
|---|---|---|---|---|
| 하드웨어 | Willow 105큐비트, 임계값 이하 QEC 시연 | Nature 피어리뷰 기반 실증, Google 인프라 통합 | 논리 오류율과 실용 알고리즘 요구치 간 수 자릿수 간극 | Nature s41586-024-08449-y (2024-12) |
| 오류 정정 | 서피스 코드 임계값 이하 최초 달성, 실시간 디코딩 72큐비트 시연 | 지수적 오류 억제 실증이 가장 강력한 현재 공개 증거 | 0.143%/사이클 → 10⁻⁶/사이클 도달까지 수 세대 더 필요 | Google Research 블로그 2024 |
| 생태계 | Cirq 오픈소스 SDK, Google Cloud Quantum AI 서비스, 학술 파트너십 | GCP 연동으로 클라우드 통합 강점, 딥러닝과 결합 연구 활발 | IBM Qiskit 대비 개발자 커뮤니티 규모 작음 | Google Quantum AI 공식 사이트 |
| 상용화 경로 | Boehringer Ingelheim 파트너십(신약), 2029 실용 우위 목표 | 구체적 산업 파트너십 실증 | 2029 목표는 알고리즘 성숙에도 의존하며 하드웨어만으로 달성 불가 | HPCwire 2024-12 |

## 핵심 기술 지표
| 지표 | Willow (2024) | 목표(2029) | 격차 |
|---|---|---|---|
| 물리 큐비트 | 105 | ~1,000+ | ~10배 |
| 논리 오류율/사이클 | 0.143% | < 10⁻⁶ | ~10,000배 |
| 서피스 코드 distance | d=7 | d=15+ | 2배+ |

## 2035까지의 핵심 질문
- 2029년 실용적 양자 우위 주장이 독립 검증 가능한 실용 문제에서 재현될 수 있는가?
- Google의 하드웨어 내재화(내부 fabrication)와 GCP 통합 전략이 산업 채택을 IBM 대비 가속할 수 있는가?
- Willow 이후 다음 세대 칩에서 논리 오류율이 예측 곡선대로 개선되는가?

## 기술 현실론 보정
- 낙관론 측 근거: 지수적 오류 억제 실증은 이론 예측과 일치하는 가장 강력한 현재 증거다. Google의 전용 fabrication 역량과 Alphabet 재정이 지속 투자를 뒷받침한다.
- 현실론 측 반론: RCS 벤치마크는 실용 문제가 아니라 인공 벤치마크다. Forrester 등 독립 분석기관은 "양자 도약인가 양자 과장인가"를 공개 질문으로 제기했다.
- 균형 판단: Willow의 임계값 이하 달성은 실질 진척이지만 2029 실용 우위까지는 논리 오류율, 게이트 수, 알고리즘 성숙이 모두 동시에 개선돼야 한다.

## 2035 전망
- Base: Google은 2029-2031년 사이 화학 시뮬레이션 특정 문제에서 공개 검증 가능한 HPC 대비 우위를 달성하고, 2035년까지 Google Cloud를 통한 양자 화학 서비스 상용화.
- Upside: 2029 목표 조기 달성 시 Alphabet의 양자 사업부가 독립 수익 단위로 분리될 가능성.
- Downside: 논리 오류율 개선 속도 둔화 시 2029 목표가 2032+로 후퇴하고 산업 파트너십 회의론 확산.

## 연결 문서
- [../roadmap_annual.md](../roadmap_annual.md)
- [../physical_limits.md](../physical_limits.md)
- [../killer_apps.md](../killer_apps.md)

## 정보 출처
- Google Willow 블로그 https://blog.google/technology/research/google-willow-quantum-chip/ 2026-04 확인
- Willow Nature paper https://www.nature.com/articles/s41586-024-08449-y 2026-04 확인
- Google Research QEC 블로그 https://research.google/blog/making-quantum-error-correction-work/ 2026-04 확인
- HPCwire Willow 발표 https://www.hpcwire.com/2024/12/09/google-debuts-new-quantum-chip-error-correction-breakthrough-and-roadmap-details/ 2026-04 확인
- Forrester 분석 https://www.forrester.com/blogs/googles-willow-chip-quantum-leap-or-quantum-hype/ 2026-04 확인
