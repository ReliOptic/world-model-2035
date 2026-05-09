# World Model 2035 Repository – User Guide & Advisory Report
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08  
**문서 성격:** 사용자 가이드 + 자문 보고서  |  **적용 범위:** `2026 -> 2035` 연간 전망 리포지토리

## 프로젝트 목표
`ReliOptic/world-model-2035`는 2026년부터 2035년까지 세계의 주요 변화 축을 **연간 해상도**로 추적하는 source-based forecast 저장소다. 목표는 단일한 미래 예언이 아니라, 공식 자료·1차 자료·검증 가능한 예측 로그를 기반으로 여러 부문이 어떻게 상호작용하는지 관찰하고 수정 가능한 세계 모델을 만드는 것이다.

## 핵심 주장
이 리포지토리의 중심 가설은 다음 네 흐름의 수렴이다.

- 온디바이스 AI와 ubiquitous inference
- 물리 시스템 전반의 고밀도 센서 네트워크
- 원자료(raw data)에 대한 상징적 추론
- 양자 및 고해상도 시뮬레이션

이 수렴은 기후과학, 에너지, 산업 역량, 지정학, 노동시장, 과학 방법론을 동시에 재편할 수 있다. 다만 기술 가능성은 곧 사회적 배치가 아니다. 전력, 물, 소재, 규제, 자본지출, 제도 마찰을 함께 보정해야 한다.

## 리포지토리 기본 원칙
- **Source-first:** 실질 주장에는 공식·기관·1차 출처를 우선 사용한다.
- **연간 해상도:** 핵심 전망은 `2026 -> 2035` 연도별 마일스톤으로 작성한다.
- **분리 원칙:** 현재 상태, 공식 로드맵, 자체 forecast를 구분한다.
- **Freshness metadata:** 각 실질 문서는 `정보 신선도`, `최종 갱신`, `다음 갱신`을 표시한다.
- **Bias correction:** 상용화 지연, 중국 기술 역량 과소평가, 에너지·물리 제약 무시, 미국 전략 지속성 과대평가, 제도 마찰 과소평가를 보정한다.
- **Realism vs optimism:** 낙관 시나리오를 남기되, 달성률 할인과 구조적 병목을 함께 기록한다.
- **Prediction evaluation:** 예측은 조건, 평가 창, 신뢰도, 판정 기준을 갖춰 사후 평가 가능해야 한다.

## 구조: 디렉토리와 핵심 문서 이해
| 위치 | 용도 |
|---|---|
| [`../METHODOLOGY.md`](../METHODOLOGY.md) | 작성 규칙, 출처 위계, 신선도 정책, forecast 템플릿 |
| `../00_foundations/` | axioms, biases, scoring, 기술 현실론 프레임워크 |
| `../02_technology/` | 온디바이스 AI, 반도체, 센서, 상징추론, 양자 등 기술 로드맵 |
| `../03_energy/` | SMR, fusion 등 에너지 전환·전력 병목 |
| `../06_geopolitics/` | 국가·지역별 지정학 리스크와 정책 경로 |
| `../13_scenarios/` | 복합 시나리오와 와일드카드 영향 |
| `../14_predictions_log/` | 검증 가능한 예측과 판정 기록 |

특히 `roadmap_annual.md` 파일은 각 도메인의 2026–2035 연도별 전망을 읽는 기본 단위다. 예: `../02_technology/on_device_ai/roadmap_annual.md`, `../02_technology/sensors/roadmap_annual.md`, `../02_technology/symbolic_reasoning/roadmap_annual.md`, `../02_technology/quantum/roadmap_annual.md`.

## 사용법: 리포지토리에서 정보 찾고 활용하기
1. [`../METHODOLOGY.md`](../METHODOLOGY.md)를 먼저 읽어 forecast 형식과 출처 기준을 확인한다.
2. `../00_foundations/axioms.md`와 `../00_foundations/biases.md`에서 기본 가정과 보정해야 할 편향을 확인한다.
3. 관심 분야의 `roadmap_annual.md`를 열어 현재 상태, 공식 로드맵, Base/Upside/Downside 경로를 비교한다.
4. 관련 산업·에너지·지정학 문서를 함께 읽어 한 부문의 전망이 다른 부문 병목에 막히는지 확인한다.
5. 주장을 인용하거나 의사결정에 쓰기 전, 문서 하단의 `정보 출처`와 신선도 메타데이터를 확인한다.

## 예측 로그 활용
[`../14_predictions_log/2026_predictions.md`](../14_predictions_log/2026_predictions.md)는 예측 품질을 사후 평가하기 위한 핵심 문서다.

- `Statement`가 관측 가능한 조건인지 확인한다.
- `Evaluation Window`가 닫히기 전에는 `pending` 상태를 기본으로 본다.
- `Hit`, `Miss`, `Mixed`, `Unscorable` 판정은 공개 관측자료와 source file을 함께 확인해 내린다.
- 신뢰도 변화가 있으면 왜 이전 판단이 이동했는지 revision log에 남긴다.

## 정보 신선도 확인 및 갱신 참여
- `🟢`: 3개월 이내 갱신. 일반 활용 가능.
- `🟡`: 3~6개월 경과. 인용 전 주요 수치와 출처를 재확인한다.
- `🔴`: 6개월 초과. active work에 쓰기 전 갱신한다.

기여할 때는 PR에서 다음을 명확히 남긴다.

- 어떤 출처를 추가·교체했는가
- 현재 상태, 공식 로드맵, forecast 중 무엇이 바뀌었는가
- Base/Upside/Downside 또는 신뢰도가 왜 이동했는가
- 어떤 감사 또는 수동 검증을 실행했는가

## 효과적으로 활용하기 위한 조언
- 이 저장소를 “정답 모음”이 아니라 “업데이트 가능한 판단 체계”로 읽는다.
- 한 문서의 전망만 보지 말고 전력, 공급망, 규제, 지정학 문서를 함께 교차 확인한다.
- 기업 로드맵은 발표 시점의 전략적 커뮤니케이션일 수 있으므로 달성률 할인 후 사용한다.
- 2035 전망을 볼 때는 기술 성능보다 배치 속도, 인프라, 제도 수용성을 먼저 질문한다.
- 불확실한 수치나 사건은 예측 로그로 이동시켜 나중에 판정 가능하게 만든다.

## 한계와 개선 방향
- 빠르게 변하는 분야는 출처가 낡으면 전망 품질도 즉시 낮아진다.
- 2035 시나리오는 복합 시스템 전망이므로 단일 변수 정확도보다 상호작용 모델의 품질이 중요하다.
- 공개 자료는 비공개 투자, 군사 기술, 공급 계약, 정책 협상 정보를 완전히 반영하지 못한다.
- 개선 방향은 더 많은 1차 출처, 더 엄격한 예측 판정, 실패한 예측의 원인 분석, 부문 간 링크 강화다.

## 소크라테스식 질문
문서를 읽거나 갱신할 때 다음 질문으로 가정을 압박한다.

- 이 주장은 관측 사실인가, 공식 로드맵인가, 자체 forecast인가?
- 반대 증거가 있다면 어느 문단이 가장 먼저 수정되어야 하는가?
- 이 전망의 가장 약한 병목은 전력, 소재, 자본, 규제, 인재, 지정학 중 무엇인가?
- Base 시나리오가 낙관적 발표를 그대로 받아쓴 것은 아닌가?
- 평가 가능한 예측으로 바꾸려면 어떤 조건과 날짜가 필요한가?

## 아리스토텔레스식 실행
최소 실행 가능 분석(MVA: Minimum Viable Analysis)은 다음 순서로 수행한다.

1. 목적을 정의한다: “2035년에 무엇이 달라지는가?”
2. 현재 상태를 최신 출처로 고정한다.
3. 공식 로드맵과 실제 달성률 사이의 간극을 기록한다.
4. 2026–2035 연도별 Base/Upside/Downside 표를 만든다.
5. 물리적·제도적 제약을 별도 문단으로 분리한다.
6. 검증 가능한 핵심 예측 1~3개를 예측 로그 후보로 추출한다.

## 결론
`world-model-2035`는 기술 낙관론과 기술 현실론 사이의 긴장을 유지하면서, 2035년 세계를 연도별·출처 기반·사후 평가 가능한 방식으로 모델링하려는 작업이다. 좋은 사용자는 더 많은 주장을 추가하는 사람이 아니라, 오래된 출처를 갱신하고, 편향을 줄이고, 예측을 판정 가능하게 만드는 사람이다.

## 연결 문서
- [`../METHODOLOGY.md`](../METHODOLOGY.md)
- [`../14_predictions_log/2026_predictions.md`](../14_predictions_log/2026_predictions.md)
- [`../00_foundations/axioms.md`](../00_foundations/axioms.md)
- [`../00_foundations/biases.md`](../00_foundations/biases.md)
- [`../14_predictions_log/template.md`](../14_predictions_log/template.md)

## 정보 출처
- IPCC, AR6 Synthesis Report: https://www.ipcc.ch/report/ar6/syr/ [접근: 2026-05-09]
- International Energy Agency, World Energy Outlook 2025: https://www.iea.org/reports/world-energy-outlook-2025 [접근: 2026-05-09]
- World Meteorological Organization, State of the Global Climate: https://wmo.int/publication-series/state-of-global-climate [접근: 2026-05-09]
- Repository source files: [`../METHODOLOGY.md`](../METHODOLOGY.md), [`../14_predictions_log/2026_predictions.md`](../14_predictions_log/2026_predictions.md) [확인: 2026-05-09]
