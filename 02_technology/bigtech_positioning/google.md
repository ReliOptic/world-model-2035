# Google / Alphabet 포지셔닝
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- `Alphabet`의 `2025 회계연도` 연간 매출은 `402.8B 달러`로 `15%` 성장, 순이익 `132.2B 달러`로 `32%` 증가했다. `Google Cloud`는 Q4에 `48%` 성장해 `17.7B 달러`를 기록했고 연간 `run rate 70B 달러`에 도달했다 (Alphabet Q4 2025 press release).
- `Gemini app`은 월간 활성 사용자 `750M` 이상, 1P 모델이 API를 통해 분당 `10B 토큰` 이상을 처리한다. `AI Mode`는 40개 언어로 확장되어 DAU `75M`을 돌파했고 검색 query volume을 끌어올리고 있다 (Alphabet Q4 2025 earnings).
- `Gemini 3.0 Flash`는 `2025년 12월 17일`에 출시되어 기존 `2.5 Flash`를 대체했고, `Gemini 3.1 Pro Preview`는 `2026년 2월 19일`에 공개되어 현 플래그십이다. `Nano Banana 2`(3.1 Flash Image 기반)가 `2026년 2월 26일` Gemini, Search AI Mode, Lens에 통합됐다 (Google blog, Gemini release notes).
- `Waymo`는 `2025년` 동안 `14M 트립` 이상을 수행해 전년 대비 3배 이상 성장했고, 주간 `450K 유료 탑승`을 돌파했다. `2026년 2월` Dallas·Houston·San Antonio·Orlando로 확장했고, London·Tokyo 국제 시장을 준비 중이다. Q4 `Other Bets` 영업손실 `3.61B 달러`, Waymo는 `16B 달러` 밸류에이션으로 자금 조달했다 (Waymo blog, CNBC, Alphabet Q4 2025).
- `TPU v7 Ironwood`는 `2025년 4월` Google Cloud Next에서 GA됐다. 칩당 FP8 `4.6 PFLOPS`, HBM3e `192GB`, 대역폭 `7.37 TB/s`. `9,216칩 superpod`는 `42.5 EFLOPS`를 제공하며, `Anthropic`이 2026년 내 최대 `1M 칩 + 1GW+ 용량` 계약(첫 단계 400K칩, Broadcom 10B 달러 규모)을 체결해 marquee customer가 됐다 (datacenterfrontier, nextweb).
- 현재 상태 해석:
  - 확인된 사실: AI Overviews/AI Mode가 search volume을 증가시키고 있으며, Cloud는 AI 워크로드로 40%대 성장, TPU는 Anthropic으로 외부 검증을 받았다
  - 이 레포의 추론: Alphabet은 인프라(TPU)·모델(Gemini)·앱(Search/YouTube/Waymo) 스택을 모두 소유한 유일한 빅테크이며, 2026-2030 AI 전환의 구조적 승자 후보다

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Alphabet Q4 2025 earnings | Cloud `run rate 70B 달러`, Q4 매출 `48%` 성장, 2026 CAPEX 대폭 증가 | `2026-2028` Cloud 매출은 `100-150B 달러`로 확장될 가능성이 높으나, Oracle/Azure와의 AI infra 경쟁으로 점유율 게임은 치열하다 | AI infra 수요 backlog은 실제 계약 기반으로 검증됨 |
| Gemini 3 series | `Gemini 3 Flash` GA, `3.1 Pro` 플래그십, Nano Banana 2 image | Gemini는 GPT-5/Claude 대비 multimodal·long-context에서 동급 이상이며, Search·YouTube 통합이 차별점 | 외부 벤치마크보다 사용자 규모(750M MAU)가 더 큰 해자 |
| Waymo expansion | 주간 `450K` rides, `14M` 연간 트립, London·Tokyo 국제 진출 | `2027-2028`까지 주간 `1-2M` 트립 가능성, 그러나 `Other Bets` 연간 영업손실 `15B+` 달러는 장기 부담 | Tesla FSD/Robotaxi, Zoox 대비 기술 격차는 유지 중 |
| TPU v7 Ironwood | 9,216칩 superpod `42.5 EFLOPS`, Anthropic 1M칩 계약 | TPU는 NVIDIA 대체재에서 '병행재'로 진화하며, Google Cloud의 차별화 요소로 굳어짐 | Anthropic deal이 외부 표준화 증거 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Gemini 3.x가 Search/Workspace 전반에 통합, Cloud `run rate 90-100B 달러` 돌파 | AI Mode가 전통 search query를 빠르게 대체하며 ad revenue가 더 빨리 회복 | AI Overviews가 publisher traffic을 삭감해 반독점 압력이 커짐 | 80% |
| 2027 | Waymo 주간 `1M+` rides, TPU v8/Ironwood Ultra로 NVIDIA 대안 강화 | DeepMind 연구 성과(AlphaFold 후속, AlphaProof 등)가 상용화로 이어짐 | 자율주행 책임/규제, EU DMA 집행이 Cloud/Search 마진을 압박 | 78% |
| 2028 | Gemini 4 세대와 agentic capabilities가 Search를 '질문응답+실행' 플랫폼으로 전환 | Agent SDK가 enterprise에서 표준화 | OpenAI/Anthropic이 consumer agent 시장에서 선점 | 65% |
| 2029 | Waymo가 미국 상위 20개 도시에서 상용 운영 | 자율주행 단위 경제성이 Uber/Lyft를 압도 | 사고·규제 이벤트로 확장 속도 둔화 | 60% |
| 2030 | Alphabet 매출 구성에서 Cloud 비중이 Search에 근접 | Multi-modal AI에서 구조적 선도 유지 | 검색 광고 수익 구조 해체가 예상보다 빠름 | 55% |
| 2031 | DeepMind 기반 과학 연구 상용화(신약, 재료, 수학)가 유의미한 매출원 | Isomorphic Labs 임상 성공으로 신약 수익 발생 | 연구→매출 전환이 10년+ 더 걸림 | 35% |
| 2032 | Waymo/TPU/DeepMind가 각각 분사 또는 대형 사업부로 독립 운영 | Alphabet 구조 재편으로 주주가치 극대화 | 조직 관성으로 통합 상태 유지 | 38% |
| 2033 | AI 에이전트가 Search trust layer로 고착 | Gemini가 iOS/Android 모두에서 기본 | Apple/Anthropic/OpenAI가 기기 레이어 장악 | 50% |
| 2034 | TPU가 글로벌 AI 인프라의 30%+ 점유 | 외부 고객(Anthropic, Meta 외) 확대 | NVIDIA Rubin/Feynman 세대 격차로 TPU 경쟁력 약화 | 40% |
| 2035 | Google은 AI·자율주행·양자컴퓨팅을 아우르는 '기초 과학 플랫폼'으로 재포지셔닝 | AGI 후보 레이어에서 선두 | 분할 명령/구조조정으로 응집력 상실 | 45% |

## 물리적/구조적 한계
- Search 광고 매출 의존도가 여전히 높고, AI Overviews/AI Mode가 CTR·publisher 생태계를 동시에 변형시켜 매출 구조 자체를 위협한다.
- Cloud는 Microsoft Azure와 AWS에 이은 3위 구조를 벗어나려면 TPU와 Gemini의 결합 우위를 더 확실히 보여야 한다.
- Waymo는 확장 속도와 단위 경제성 사이 trade-off가 크고, Other Bets 누적 손실은 주주 인내심의 한계에 접근 중이다.
- 미국·EU의 반독점 판결(검색, 광고 스택, Play Store)이 구조적 리스크로 계속 부각된다.

## 기술 현실론 보정
- 낙관론 측 근거: 연 `402.8B 달러` 매출 + `750M MAU Gemini` + 자체 TPU/자율주행 스택은 경쟁사가 복제 불가능한 조합이다.
- 현실론 측 반론: Search 매출 전환, Other Bets 수익성, 반독점 노출은 모두 2020년대 후반에 동시 터질 수 있는 리스크다.
- 균형 판단: Alphabet은 AI 스택 풀세트를 가진 유일 사업자라는 장점이 유지되지만, 2028-2030 구간에 매출 구조·규제·분할 중 최소 하나에서 중대한 시험을 맞는다.

## 2035 전망 요약
- Base: Google은 AI·Cloud·자율주행 모두에서 3대 플레이어 위치를 유지하되, 광고 단일 매출 의존에서 벗어나는 전환기를 거친다.
- Upside: TPU/Gemini/Waymo가 모두 동시 스케일업 되고 DeepMind 과학 사업이 의미 있는 매출로 전환되면 Alphabet은 2030년대의 범용 AI 인프라 표준이 된다.
- Downside: 반독점 분할, AI Mode로 인한 search 광고 붕괴, 자율주행 지연이 겹치면 매출 성장률이 한 자릿수로 둔화한다.

## 연결 문서
- [../semiconductors/roadmap_annual.md](../semiconductors/roadmap_annual.md)
- [../../09_corporate_roadmaps/semiconductors/nvidia.md](../../09_corporate_roadmaps/semiconductors/nvidia.md)
- [./nvidia.md](./nvidia.md)
- [./competitive_map.md](./competitive_map.md)

## 정보 출처
- Alphabet Q4 2025 press release https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm 2026-04 확인
- Alphabet Q3 2025 press release https://www.sec.gov/Archives/edgar/data/1652044/000165204425000087/googexhibit991q32025.htm 2026-04 확인
- Gemini 3 launch https://blog.google/products/gemini/gemini-3/ 2026-04 확인
- Waymo 2025 year in review https://waymo.com/blog/2025/12/2025-year-in-review/ 2026-04 확인
- Waymo expansion Dallas/Houston/San Antonio/Orlando https://waymo.com/blog/2026/02/dallas-houston-san-antonio-orlando/ 2026-04 확인
- Google TPU Ironwood Cloud Next https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next 2026-04 확인
- TPU v7 Ironwood specs https://howaiworks.ai/blog/google-tpuv7-ironwood-announcement-2025 2026-04 확인
- Alphabet Q4 2025 CNBC https://www.cnbc.com/2026/02/04/alphabet-googl-q4-2025-earnings.html 2026-04 확인
- Inference note: 2026-2035 연간 마일스톤은 Alphabet 공식 실적·로드맵에 기반한 저장소 추론이다.
