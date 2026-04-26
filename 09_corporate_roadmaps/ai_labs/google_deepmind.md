# Google DeepMind
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Google DeepMind는 2023년 4월 Google Brain과 DeepMind의 통합으로 설립됐다. 2026년 4월 현재 Demis Hassabis가 CEO를 맡으며 Alphabet의 핵심 AI 연구·제품 조직으로 기능한다.
- 모델 라인업: `Gemini 2.5 Pro`(2025년 3월)는 AIME 2025, GPQA 등 수학·과학 벤치마크에서 업계 최상위를 기록했다. `Gemini 3`은 2025년 11월 LMArena 리더보드 1,501 Elo 달성, `Gemini 3.1 Pro`는 2026년 2월 기업용 딥 리즈닝 특화 모델로 출시됐다. Gemini Deep Think 고급 버전은 2025년 IMO에서 35점(금메달 기준)을 달성해 최초 금메달 수준 수학 AI가 됐다.
- TPU v7 `Ironwood`는 2025년 Google Cloud Next에서 공개됐다. 칩당 `4,614 TFLOPs FP8`, `192 GB HBM3e`, `7.4 TB/s 메모리 대역폭`, 단일 Superpod `9,216칩 = 42.5 exaflops`. TPU v5p 대비 칩당 성능 `10x`, 전 세대 Trillium(v6e) 대비 `4x+`. Google은 2026~2028년 TPU 총 출하를 `5,000만 유닛`으로 계획하고 있으며 2026년 단독 `430만 유닛` 예정.
- 수학·과학 AI: `AlphaProof` + `AlphaGeometry 2` 콤보는 2024년 IMO 6문제 중 4문제 풀이(실버 메달 수준), `Nature` 2025년 게재. Gemini Deep Think는 2025년 자연어 기반 IMO 금메달 달성으로 별도 언어 변환 없이 4.5시간 내 풀이 완료.
- `Project Astra`는 범용 멀티모달 AI 비서 연구 프로토타입이다. 2025년 3월 Gemini Live 구독자에게 라이브 비디오·화면 공유 기능 일부가 롤아웃됐다. 완전 범용 비서로의 전환 시점은 미정.
- 현재 상태 해석:
  - 확인된 사실: Gemini 3 계열이 추론 벤치마크에서 선두, Ironwood TPU 양산 진입, AlphaProof 수학 AI 성과
  - 이 레포의 추론: 2026년 Google DeepMind는 연구 우위를 Gemini/Vertex 제품으로 빠르게 상용화하는 구조로 전환 중이나, 소비자 AI 어시스턴트에서 OpenAI, 엔터프라이즈 에이전트에서 Anthropic과 동시에 경쟁하는 이중 압박에 놓여 있다.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Google DeepMind `Gemini 3.1 Pro` (2026-02) | 기업 딥 리즈닝 특화 출시, LMArena 최상위 | Gemini 계열의 추론 경쟁력은 실물이나 OpenAI/Anthropic 대비 엔터프라이즈 채택에서 여전히 격차 존재 | 벤치마크 선두 ≠ 기업 워크플로우 침투율 |
| Google Cloud Next 2025 `TPU v7 Ironwood` | 칩당 10x 성능 향상, 9,216칩 Superpod | 자체 칩 인프라 강화는 Google Cloud AI 마진 개선에 기여하나, 고객 채택은 CUDA 생태계 관성과 경쟁 | 대형 외부 고객 채택 속도는 GCP 점유율 확대 속도에 의존 |
| DeepMind `AlphaProof + AlphaGeometry 2` (Nature 2025) | IMO 실버 수준, 형식 수학 추론 자동화 | 과학 AI 선두 포지션 확인, 단 산업용 상용화 경로는 미개척 | 연구 돌파 → 상품화에 3~5년 지연이 전형적 |
| DeepMind `Project Astra` 2025 MWC | 라이브 비디오·화면 공유 Gemini Live 롤아웃 | 범용 비서로 발전하는 연구는 진행 중이나, 소비자 사용 스케일에서 ChatGPT와 격차 존재 | 기능 릴리스와 일상 비서 채택률은 별개 지표 |
| Alphabet 10-K FY2025 | Google Cloud 연간 매출 `$43B+`, AI 인프라 CAPEX 급증 | AI 수요는 견조하나 CAPEX 증가로 단기 마진 압박 | Google Cloud는 AWS/Azure 대비 3위 유지 중 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Gemini 3.1 Pro 기업 채택 확산, Ironwood Superpod GCP 롤아웃, AlphaProof 과학 AI 파이프라인 일부 상용화 | Gemini가 Vertex AI 통해 엔터프라이즈 코딩·분석 주력 플랫폼이 됨 | Google 내부 제품 우선순위 갈등(Search vs. AI 어시스턴트)으로 외부 채택 속도 둔화 | 82% |
| 2027 | TPU v8 Sunfish/Zebrafish(TSMC 2nm) 개발 진행, Gemini 4 계열 출시, Project Astra 기능 Gemini 앱 전면 통합 | AlphaProof 계열이 제약·재료 발견 파이프라인에 내재화됨 | 규제(EU AI Act 고위험 분류) 또는 Search 광고 마진 압박이 AI R&D 예산을 제약 | 78% |
| 2028 | Gemini 기반 에이전트 워크플로우가 Google Workspace에 깊이 통합, 기업 AI 어시스턴트 표준화 | Google이 Search+Workspace+Gemini 삼축 결합으로 기업 생산성 플랫폼 지위 확보 | OpenAI/Anthropic의 엔터프라이즈 에이전트가 먼저 기업 IT 예산을 잠금효과 형성 | 60% |
| 2029 | AI for Science 축(의약품·기후·재료)이 DeepMind 상업 매출의 구분 가능한 비중 차지 | Gemini+AlphaProof 계열이 분자설계·수학증명 SaaS로 제약/보험 시장 진입 | AI for Science 상용화가 기대보다 느리고, 과학 연구 SaaS 시장 자체가 소규모에 머무름 | 35% |
| 2030 | Google DeepMind는 Alphabet 내 핵심 R&D 자산으로 지위 유지, Gemini API가 Google 외부 개발자 생태계의 주요 축 중 하나 | 만약 Gemini가 모바일 OS 수준의 AI 기반 인프라로 진화하면 소비자-기업 동시 잠금효과 | 지정학 분절로 Google의 중국·러시아 외 일부 시장 접근 제한, EU 반독점으로 Gemini 번들 제약 | 55% |
| 2031 | AI 하드웨어(TPU) + AI 소프트웨어(Gemini) + 클라우드 인프라(GCP) 삼중 수직통합 완성 | Google이 에너지·TPU 자체 설계로 토큰당 비용을 OpenAI/Anthropic 대비 의미 있게 낮춤 | 자체칩 생태계가 NVIDIA CUDA 대비 소프트웨어 호환성 부족으로 외부 고객 채택 저조 | 50% |
| 2032 | DeepMind 연구 조직이 AGI-근접 연구의 핵심 기관 중 하나로 공인, 안전 프레임워크 구체화 | AI 안전 연구에서 Anthropic과 공동 표준 설정 역할 | Anthropic이 안전 프레임 선점으로 규제 시장 포지션 우선 확보 | 35% |
| 2033 | Gemini 계열이 5개 이상 수직 산업(법률·의료·금융·과학·교육)에서 특화 에이전트로 독립 매출 형성 | AI-first 기업 소프트웨어에서 Salesforce/SAP 수준의 대체 역할 | 중국 AI 기업의 글로벌 진출이 Gemini의 신흥국 시장 점유를 압박 | 48% |
| 2034 | Google DeepMind는 Alphabet의 2030년대 수익 다각화 핵심 축으로, Search 광고 의존도를 구조적으로 줄이는 역할 | AI 어시스턴트 + 과학 AI + 클라우드가 새로운 3대 수익 축 형성 | 검색 광고의 AI 기반 침식이 예상보다 빠르면 내부 자원 재배분 압박 | 52% |
| 2035 | Google DeepMind는 OpenAI·Anthropic과 함께 세계 3대 프론티어 AI 기관 중 하나로, 수직통합 인프라와 과학 AI에서 가장 폭넓은 포지션 보유; Alphabet 총 매출 ~$600-800B(도메인 앵커) | Gemini 생태계가 Android 수준의 AI 플랫폼 표준으로 자리잡음 | 조직 내부 우선순위 갈등과 규제 압박이 실행 속도를 OpenAI 대비 지속 지연 | 60% |

## 물리적/구조적 한계
- 극복된 것:
  - 연구 조직과 제품 조직을 단일 DeepMind 브랜드로 통합, 모델-클라우드-칩의 수직통합 구조 완성
  - AlphaFold, AlphaProof 등 선도적 과학 AI 성과로 연구 신뢰도 확보
  - TPU 자체 설계로 NVIDIA 의존도를 단계적 분산 중
- 미해결:
  - 조직 내부 우선순위: Search 광고 보호 vs. AI 제품 우선성 갈등
  - Project Astra의 범용 비서 전환은 기술 완성도와 소비자 습관 형성이 모두 필요
  - EU AI Act, 반독점 압력(Gemini 번들링 제약 위험)
  - 엔터프라이즈 AI 채택에서 Anthropic·OpenAI 대비 뒤처진 에이전트 플랫폼 생태계
- 극복 시나리오:
  - Workspace AI 통합이 G Suite 기반 기업 고객에게 자연스러운 채택 경로를 만들 때 엔터프라이즈 우위가 커진다

## 기술 현실론 보정
- 낙관론 측 근거:
  - Gemini 3 계열 추론 벤치마크 선두, Ironwood TPU 성능 10x 이상, IMO 금메달 수학 AI는 모두 측정된 실물 진척이다
  - Google은 세계에서 가장 많은 AI 사용자(Search, YouTube, Maps, Workspace)에게 접근하는 배포 채널을 보유하고 있다
- 현실론 측 반론:
  - 기술 우위가 제품 채택으로 이어지는 속도가 OpenAI·Anthropic에 비해 느리다는 패턴이 2023~2025년에 반복됐다
  - 조직 규모와 Search 이해충돌이 AI 제품 속도를 구조적으로 억제한다
  - 과학 AI 상용화는 긴 주기를 가지며 단기 수익원이 아니다
- 균형 판단:
  - Google DeepMind의 2035 포지션은 "연구 최강"과 "배포 최다"의 결합이 언제 실현되느냐에 달려 있다. 기술 측면의 우위는 실물이나, 제품 실행과 조직 집중도에서 지속적인 보정이 필요하다.

## 2035 전망 요약
- Base: Google DeepMind는 Alphabet 내 핵심 AI 엔진으로, Gemini 생태계가 소비자·기업·과학 AI에 걸쳐 가장 넓은 포트폴리오를 가진 3강 중 하나가 된다.
- Upside: Gemini+TPU+Workspace 수직통합이 Android처럼 플랫폼 표준이 되고, 과학 AI 상용화로 제약·재료 분야에서 별도 수익 축 형성.
- Downside: 조직 우선순위 갈등·규제 압박·엔터프라이즈 에이전트 후발이 지속되어 연구 최강이지만 수익 측면에서 2위 포지션에 머무름.

## 연결 문서
- [./openai.md](./openai.md)
- [./anthropic.md](./anthropic.md)
- [./meta_ai.md](./meta_ai.md)
- [../cloud_hyperscalers/google_cloud.md](../cloud_hyperscalers/google_cloud.md)
- [../../02_technology/semiconductors/roadmap_annual.md](../../02_technology/semiconductors/roadmap_annual.md)

## 정보 출처
- Google DeepMind `Gemini 2.5 Updates at Google I/O 2025` https://blog.google/technology/google-deepmind/google-gemini-updates-io-2025/ 2026-04 확인
- Google DeepMind `Gemini 2.5 Pro` https://deepmind.google/en/models/gemini/pro/ 2026-04 확인
- Google DeepMind `Advanced Gemini Deep Think achieves IMO gold-medal standard` https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ 2026-04 확인
- Google DeepMind `AlphaProof and AlphaGeometry 2` https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/ 2026-04 확인
- Google DeepMind `Project Astra` https://deepmind.google/models/project-astra/ 2026-04 확인
- Google Cloud / The Next Web `Ironwood TPU v7 launch` https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next 2026-04 확인
- SemiAnalysis `TPUv7: Google Takes a Swing` https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the 2026-04 확인
- Google Cloud Next 2026 coverage https://oplexa.com/google-cloud-next-2026/ 2026-04 확인
- IntuitionLabs `Google TPU Architecture for Gemini 3` https://intuitionlabs.ai/articles/google-tpu-architecture-gemini-3 2026-04 확인
- Inference note: 2026-2035 annual milestones are repository inferences anchored to official Google DeepMind model releases, TPU roadmap announcements, and Alphabet financial disclosures.
