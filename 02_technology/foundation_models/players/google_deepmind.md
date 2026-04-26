# Google DeepMind — 기술 프로파일 (Foundation Models / Tech-Angle)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

> 이 파일은 모델 아키텍처·과학 AI·Project Astra 등 기술 각도를 다룬다. 기업 재무·Google 클라우드 포지셔닝은 `02_technology/bigtech_positioning/google.md` 참조.

## 2026년 4월 현재 상태
- 현행 최상위 라인은 `Gemini 2.5 Pro`(2025-03 출시)와 `Gemini 2.5 Flash`다. `2.5 Pro`는 컨텍스트 `1M 토큰`(2M 근접 예고), 하이브리드 Thinking 모드를 탑재했다. 벤치마크: AIME 2024 `92.0%`, GPQA Diamond `84.0%`, SWE-bench Verified `63.8%`(커스텀 에이전트), Humanity's Last Exam `18.8%`.
- `2.5 Flash`는 1M 토큰 컨텍스트 + Thinking 기능을 탑재한 첫 Flash 모델로, 비용-성능 균형 포지션.
- `Gemini 3 Pro`가 `2025년 11월 18일` 출시됐다. 완전 멀티모달 추론 모델.
- **Project Astra**: 실시간 멀티모달 범용 AI 어시스턴트 연구 프로토타입. Gemini Live, Search 및 안경 등 신형 폼팩터로 역량을 이전하는 로드맵.
- **AlphaProof + AlphaGeometry**: 2024 국제수학올림피아드(IMO)에서 은메달 수준 문제 해결 달성. AI가 수학 올림피아드 문제를 실버 수준으로 자동 증명한 첫 사례.
- **AlphaFold 3**: 단백질·핵산·소분자·이온 등 전 생물분자 간 구조 및 상호작용 예측. Isomorphic Labs IsoDDE(2026-02)로 발전해 `AF3` 대비 단백질-리간드 구조 예측 정확도 2배 이상.
- 훈련 인프라: Anthropic과 최대 `100만 TPU, 1GW+` 공동 확장 계약 체결(Google Cloud 제공자 입장). Broadcom과 2027- `3.5GW` 신규 TPU 용량.

## 공식 로드맵 / 기술 이정표
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Google DeepMind `Gemini 2.5` (2025-03) | Thinking 모드 탑재, `1M` 컨텍스트, AIME `92%`, GPQA `84%` | 수학·과학 추론에서 동급 최강. SWE-bench는 Anthropic 대비 열세 — 코딩 세그먼트 격차 | Google DeepMind 블로그 확인 |
| Google I/O 2025 | `Gemini 2.5 Pro` 업데이트, Veo 3 비디오 생성, Android XR | 멀티모달 폭(텍스트·이미지·비디오·오디오)에서 업계 최광 | Google I/O 2025 공식 발표 |
| Google `Gemini 3 Pro` (2025-11) | 완전 멀티모달 추론 모델 | 2.5 → 3 전환이 실제로 이뤄졌음. 4.0 세대 로드맵 예상 | DeepMind 위키피디아 확인 |
| DeepMind `AlphaProof + AlphaGeometry` (2024) | IMO 은메달 수준 수학 증명 | AI for Science의 증명 방식이 화학·생물로 확장 중 | DeepMind 공식 블로그 |
| DeepMind `AlphaFold 3` (2024-05) | 전 생물분자 구조 예측, Isomorphic Labs 파트너십 | 2026 IsoDDE가 AF3 정확도를 2배 이상 개선. Phase I 임상 `2026` 진입 | DeepMind + Isomorphic Labs 공식 |
| DeepMind `Project Astra` | 범용 AI 어시스턴트 프로토타입, Gemini Live·안경으로 이전 | 실시간 멀티모달 에이전트의 상업화 채널 구체화 중 | DeepMind project-astra 페이지 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Gemini 4 세대 출시, Project Astra 기반 스마트글라스 제한 배포, AlphaFold-IsoDDE 파이프라인 Phase I 진입 | 수학·과학 추론에서 AlphaProof 계열이 화학·재료로 확장 | 조직 복잡성(Google + DeepMind 통합) 또는 규제(EU AI Act) 지연 | 82% |
| 2027 | Gemini 4 Pro가 컨텍스트 `10M+`, 음성·비디오 실시간 에이전트 API 표준화 | Project Astra 기반 안경이 소비자 출시 → 피지컬 AI 플랫폼 | 멀티모달 에이전트 안전 사고 시 제품 배포 속도 제한 | 76% |
| 2028 | AI for Science(구조생물학·재료·기후) 파이프라인에서 최소 1개 임상 Phase II 진입 | AlphaFold 계열이 제약사 전체 타깃 발굴 파이프라인을 대체 | AI 약물 설계의 임상 성공률이 기대에 미달 | 55% |
| 2029 | TPU 자체 학습 인프라 + Gemini 생태계로 외부 API 의존 최소화 | 구글 Search + Cloud + Workspace 통합이 엔터프라이즈 잠금 효과 | 반독점 규제가 Search-AI 번들링 해제 요구 | 60% |
| 2030 | 수학·과학 자동화 에이전트가 학계 연구 생산성을 가속하는 실증 사례 축적 | IMO 금메달 수준 + 새 수학 정리 발견 사례 | 수학 자동화가 연구 과정이 아닌 도구 수준에 머무름 | 38% |
| 2031 | Gemini 플랫폼이 소비자(Android/Search) + 기업(Workspace/Cloud) 동시 지배 | 두 채널 시너지로 MAU 기준 단일 최대 AI 플랫폼 | OpenAI ChatGPT 소비자 점유율 유지로 소비자 채널 반분 | 65% |
| 2032 | AI for Science 파이프라인에서 DeepMind 기원 약물/재료 첫 시장 승인 | 과학 AI 리더십이 Google 주가와 연결되는 새 서사 | 경쟁자(Anthropic·OpenAI·전문 바이오 AI)가 동급 성과 | 30% |
| 2033 | Project Astra 계열이 안경·차량·가전 등 멀티 폼팩터로 확산 | 피지컬 AI 플랫폼의 글로벌 표준 선점 | 애플·Meta의 XR 디바이스 생태계가 경쟁 차단 | 50% |
| 2034 | Gemini 계열이 AGI 인접 역량 논쟁에서 AlphaProof 계보를 증거로 제시 | 과학적 추론 AI의 대표 브랜드 확립 | 조직 분열·인재 이탈로 연구 일관성 저하 | 55% |
| 2035 | Google DeepMind는 AI for Science + 멀티모달 소비자 AI + 클라우드 인프라 3축의 단일 최대 수직 통합 플레이어 | 수직 통합 우위가 경쟁사가 따라갈 수 없는 해자 형성 | 반독점 분리 명령 또는 대형 안전 사고로 구조 재편 | 60% |

## 물리적/구조적 한계
- **조직 복잡도**: Google Brain + DeepMind 통합은 연구 우선순위 충돌과 제품 일관성 문제를 내재한다.
- **SWE-bench 격차**: `2.5 Pro` `63.8%`는 Anthropic `Opus 4.7` `87.6%` 대비 코딩 세그먼트에서 큰 격차.
- **반독점 리스크**: Search-Gemini 번들링은 EU·미국 규제 당국의 주요 심사 대상.
- **AlphaFold 상업화 속도**: 구조 예측 정확도가 높아도 임상 성공률은 별도 문제. 제약 파트너십 성과가 느릴 수 있음.
- **TPU 소프트웨어 스택**: JAX/XLA 생태계는 PyTorch 대비 커뮤니티 규모가 작아 외부 연구자 진입 장벽.

## 기술 현실론 보정
- **낙관론 측 근거**: AlphaFold 3 → IsoDDE 진화, AlphaProof IMO 은메달, Gemini 2.5 Pro 수학·과학 벤치마크 1위는 모두 실물 진척. 멀티모달 폭(텍스트·이미지·비디오·오디오·코드)은 업계 최광.
- **현실론 측 반론**: 코딩 에이전트 세그먼트에서 Anthropic에 뒤처지며, Google 내부 제품 실행 복잡성이 연구→제품 전환 속도를 늦춘다. 반독점 소송은 Search-AI 통합 전략의 지속성을 위협.
- **균형 판단**: 과학 AI와 멀티모달 역량에서 가장 광범위한 포트폴리오를 가지나, 단일 코딩·에이전트 세그먼트 리더십은 Anthropic에게, 소비자 규모는 OpenAI에게 뒤처진다.

## 2035 전망 요약
- **Base**: Google DeepMind는 AI for Science의 대표 브랜드이자 멀티모달 AI 플랫폼의 글로벌 2-3위. 연구·인프라·배포 3축의 유일한 완전 수직 통합 플레이어.
- **Upside**: AlphaFold 계열 약물/재료 시장 승인, Project Astra 멀티폼팩터 확산, Gemini 플랫폼 소비자 1위 탈환 시 시장가치 `$3조+`.
- **Downside**: 반독점 분리 + 코딩 격차 미해소 + AI for Science 임상 실패 겹치면 연구소로서의 위상은 유지하되 상업 AI 플랫폼 1위 포기.

## 연결 문서
- [../scaling_laws.md](../scaling_laws.md)
- [../slm_roadmap.md](../slm_roadmap.md)
- [../../on_device_ai/roadmap_annual.md](../../on_device_ai/roadmap_annual.md)
- [../../biotech/alphafold_downstream.md](../../biotech/alphafold_downstream.md)
- [./anthropic.md](./anthropic.md)

## 정보 출처
- Google DeepMind `Gemini 2.5 thinking updates` https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/ 2026-04 확인
- Google DeepMind `Project Astra` https://deepmind.google/technologies/gemini/project-astra/ 2026-04 확인
- Google I/O 2025 recap https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-updates-io-2025/ 2026-04 확인
- Gemini Wikipedia https://en.wikipedia.org/wiki/Gemini_(language_model) 2026-04 확인
- Google DeepMind Wikipedia https://en.wikipedia.org/wiki/Google_DeepMind 2026-04 확인
- Isomorphic Labs `IsoDDE` https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier 2026-04 확인
- Fortune `AlphaFold five years` https://fortune.com/2025/11/28/google-deepmind-alphafold-science-ai-killer-app/ 2026-04 확인
- DataCamp `Gemini 2.5 Pro` https://www.datacamp.com/blog/gemini-2-5-pro 2026-04 확인
