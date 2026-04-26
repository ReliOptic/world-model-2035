# OpenAI — 기술 프로파일 (Foundation Models / Tech-Angle)
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

> 이 파일은 모델 아키텍처·역량·추론 시스템·훈련 인프라 각도에서 OpenAI를 다룬다.

## 2026년 4월 현재 상태
- `GPT-5`는 `2025년 8월 7일` 라이브스트림 발표로 출시됐다. 아키텍처는 GPT-4 기반 transformer에서 "다음 단어" 대신 "다음 생각"을 예측하도록 확장됐으며, System 1(GPT-4o 계열 빠른 추론)과 System 2(o1/o3 계열 느린 추론)를 단일 모델로 통합한다. GPT-5 API는 reasoning effort(low/medium/high/minimal)와 verbosity 파라미터를 노출한다.
- 주요 벤치마크(출시 시점): AIME 2025 `94.6%`(도구 없음), SWE-bench Verified `74.9%`, Aider Polyglot `88%`, MMMU `84.2%`, VideoMMMU `84.6%`, HealthBench Hard `46.2%`.
- 추론 모델 계보: `o3`와 `o4-mini`(2025 출시) — o4-mini는 수학·코딩·시각 추론 최적화 소형 모델. o-시리즈는 대규모 강화학습으로 학습 컴퓨트와 추론 컴퓨트를 동시에 스케일링하며 "compute = performance" 곡선을 RL 영역으로 연장했다.
- `GPT-5.2`(2026)는 GPT-5에서 소폭 업그레이드된 버전으로 공개됐다.
- 훈련 인프라: Stargate 프로젝트 — 텍사스 Abilene 시설이 `5GW` 전력 소비에 근접, 전용 재생에너지 팜과 소형모듈원전(SMR) 병행 건설. 설계 목표는 GPT-6 학습.
- 자체 추론 칩: Broadcom·TSMC `3nm` 공정으로 첫 자체 추론 전용 칩 설계 완료, `2026년` 대량 생산 목표 — NVIDIA 의존도 감소 전략.
- 소비자 플랫폼: ChatGPT `800M+ WAU` (2026-Q1 기준), 업계 최대 소비자 규모 유지.

## 공식 로드맵 / 기술 이정표
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| OpenAI `Introducing GPT-5` (2025-08) | System 1+2 통합, 멀티모달 네이티브, reasoning effort API, SWE-bench `74.9%` | GPT-5는 실제 배포됨. 소비자·엔터프라이즈 채택 속도는 가격 정책이 관건 | OpenAI 공식 발표 확인 |
| OpenAI `o3 / o4-mini` (2025) | RL 스케일링으로 AIME `93%+`, GPQA `87%+` 달성 | o-시리즈 RL 패러다임은 코딩·수학·시각 추론에서 확실한 우위. 비용-성능 곡선이 핵심 변수 | openai.com 공식 릴리즈 |
| OpenAI `Stargate` (2025 발표) | Abilene `5GW` AI 팩토리, SMR 병행, GPT-6 학습 목표 | 규모 자체는 실물이나, 전력·부지·SMR 인허가 지연 리스크 존재 | CNBC·Bloomberg 복수 확인 |
| OpenAI 자체 추론 칩 (2026 목표) | Broadcom+TSMC `3nm`, `2026` 대량 생산 | 첫 칩은 추론 전용. 학습 칩 자체화까지는 3-5년 추가 필요 | The Information + CB Insights |
| OpenAI `GPT-5.2` (2026) | GPT-5 소폭 업그레이드 | 빠른 반년 사이클 패턴 확립 | openai.com 확인 |

## 1년 단위 전망 (2026→2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | GPT-6 학습 시작(Stargate Abilene ~5GW), 자체 추론 칩(Broadcom+TSMC 3nm) 대량 배포, o-시리즈 RL 패러다임 API 표준화; ChatGPT 1B+ WAU 진입 목표; 추론 비용 연간 60-80% 하락 | Stargate 전력 램프업이 예정대로 되면 GPT-6 학습 일정 단축 | SMR 인허가·전력 인입 지연 시 GPT-6 출시 `1-2년` 밀림 | 82% |
| 2027 | GPT-6 출시 시나리오, System 1+2 통합 아키텍처 2세대, 에이전트 오케스트레이션 API 표준화; AI 소프트웨어 시장 ~$300B 규모에서 OpenAI API 점유율 30%+ 유지 목표 | GPT-6이 현 GPT-5 대비 `100x` 역량 주장 실현 | 규제(EU AI Act 고위험 분류) 또는 안전 평가 지연 | 78% |
| 2028 | ChatGPT 에이전트가 기업 핵심 워크플로우에 통합, 추론 비용 현재의 `1/5` 이하 달성(연간 60-80% 하락 복리); Fortune 500 기업 50%+ ChatGPT Enterprise 계약 | 멀티모달 실시간 에이전트가 소비자 OS 수준의 플랫폼으로 발전 | Anthropic·Google 코딩/과학 세그먼트 역전 가능성 | 70% |
| 2029 | 자체 칩(학습 포함) 내재화 2세대, NVIDIA 의존도 `<50%` | 하드웨어-소프트웨어 수직 통합으로 단위 경제성 개선 | 칩 설계 실수 또는 TSMC 캐파 부족으로 지연 | 50% |
| 2030 | AGI 인접 역량 논쟁에서 OpenAI가 de facto 평가 기준 설정 시도 | 안전 프레임웍 없이도 배포 → 정책 리스크 | 규제 기관과 충돌 시 특정 시장 진입 제한 | 38% |
| 2031 | 소비자 플랫폼(ChatGPT) + 엔터프라이즈 API + 추론 하드웨어 3층 구조 완성 | 3층 수직 통합이 경쟁사 진입 장벽 형성 | 반독점 규제가 모델-앱 수직 통합 해제 요구 | 60% |
| 2032 | 추론 비용 경쟁에서 오픈소스(Meta Llama, DeepSeek)가 API 가격에 강한 압박 | 프리미엄 역량(최고 지능) 세그먼트에서 가격 방어 성공 | 오픈소스 역량이 GPT-5 수준에 도달 시 API 매출 압박 | 35% |
| 2033 | 멀티모달 실시간 에이전트가 물리 세계(로봇·자율주행)와 연결 | 피지컬 AI 시대 소프트웨어 플랫폼 표준 선점 | 하드웨어 플레이어(Tesla, Boston Dynamics 등)가 독자 AI 스택 유지 | 55% |
| 2034 | GPT-n 계열이 `AGI-near` 역량 공식 주장. 규제·사회적 수용이 병목 | AI 거버넌스에서 OpenAI의 "안전+성능" 통합 서사가 인정받음 | 선도 AI 사고 발생 시 ChatGPT 배포 규모가 역풍의 진원지 | 50% |
| 2035 | OpenAI는 ChatGPT 소비자 플랫폼 + GPT API 생태계 + 추론 하드웨어 3강 중 1위 | Stargate 이후 컴퓨트 리더십이 2035년까지 유지 | Anthropic·Google·오픈소스가 동시 우위 확보 시 점유율 분산 | 65% |

## 물리적/구조적 한계
- **전력·부지**: Stargate Abilene `5GW`는 미국 전력망과 직접 충돌. SMR 인허가 일정이 학습 일정을 제약한다.
- **비용 구조**: GPT-5 추론 비용은 여전히 높다. 오픈소스(DeepSeek, Llama)의 가격 압박이 API 마진을 지속 잠식.
- **RL 스케일링 법칙 한계**: o3/o4 계열의 RL 패러다임은 현재 수학·코딩에서 강력하지만, 일반 추론 모든 도메인으로 일반화되는지는 미확인.
- **안전·정렬**: 소비자 배포 `800M WAU` 규모는 의도치 않은 사회적 영향 리스크를 증폭한다. Anthropic 대비 공개 안전 프레임웍이 약하다.
- **자체 칩 불확실성**: 첫 추론 칩의 소프트웨어 생태계(CUDA 대항마) 성숙에는 3-5년 추가 소요.

## 기술 현실론 보정
- **낙관론 측 근거**: GPT-5의 System 1+2 통합 아키텍처는 단순 벤치마크를 넘어 실제 제품에서 추론 품질을 높이는 검증된 설계다. ChatGPT `800M WAU`는 어떤 경쟁사도 현재 따라갈 수 없는 소비자 데이터 루프를 만든다. Stargate 컴퓨트 규모는 2027-2030 모델 세대의 상방을 열어둔다.
- **현실론 측 반론**: SWE-bench `74.9%`(GPT-5 출시 시점)는 Anthropic Opus 4.7의 `87.6%`에 뒤처진다. 코딩·에이전트 세그먼트에서 단기 기술 우위 격차 존재. 오픈소스 역량 상승이 API 비즈니스에 구조적 압박.
- **균형 판단**: OpenAI는 소비자 규모·추론 통합·컴퓨트 투자에서 업계 1위이나, 코딩·안전·해석가능성 세그먼트별로 Anthropic·Google에게 역전될 수 있다.

## 2035 전망 요약
- **Base**: OpenAI는 소비자 AI 플랫폼(ChatGPT) + GPT API 생태계의 글로벌 1위 브랜드. 연매출 `$2,000-4,000억` 범위의 상장 기업.
- **Upside**: Stargate 컴퓨트가 GPT-6/7 세대에서 경쟁사를 압도하고 추론 하드웨어 수직 통합으로 단위 경제성 개선. 시장가치 `$2조+` 진입.
- **Downside**: 오픈소스 역량 급상승 + 규제 압박 + 안전 사고가 겹치면 API 마진 붕괴 및 특정 시장 배제.

## 연결 문서
- [../scaling_laws.md](../scaling_laws.md)
- [../agentic_os.md](../agentic_os.md)
- [./anthropic.md](./anthropic.md)
- [./google_deepmind.md](./google_deepmind.md)
- [../../on_device_ai/architecture_shifts.md](../../on_device_ai/architecture_shifts.md)

## 정보 출처
- OpenAI `Introducing GPT-5` https://openai.com/index/introducing-gpt-5/ 2026-04 확인
- OpenAI `Introducing o3 and o4-mini` https://openai.com/index/introducing-o3-and-o4-mini/ 2026-04 확인
- OpenAI `Introducing GPT-5.2` https://openai.com/index/introducing-gpt-5-2/ 2026-04 확인
- OpenAI GPT-5 official page https://openai.com/gpt-5 2026-04 확인
- OpenAI `Introducing o3 and o4-mini` https://openai.com/index/introducing-o3-and-o4-mini/ 2026-04 확인
- GPT-5 Technical Overview https://cirra.ai/articles/gpt-5-technical-overview 2026-04 확인
- Sapphire Ventures `2026 Outlook` https://sapphireventures.com/blog/2026-outlook-10-ai-predictions-shaping-enterprise-infrastructure-the-next-wave-of-innovation/ 2026-04 확인
