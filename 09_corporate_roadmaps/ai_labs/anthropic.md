# Anthropic
**정보 신선도:** 🟡  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-07

## 2026년 4월 현재 상태
- Anthropic는 `Claude Opus 4.5` (`2025년 11월 24일` 출시), `Claude Sonnet 4.5`, `Claude Sonnet 4`, `Claude Opus 4` 라인으로 전면 개편을 끝냈다. `Opus 4.5`는 `SWE-bench Verified 80.9%`로 업계 최초 `80%` 돌파를 기록했고, 가격은 `$5/$25 per M tokens`로 직전 Opus 대비 `약 67%` 인하됐다.
- 매출 급증이 회사 궤적을 바꿨다. `2025년 말` 기준 run-rate revenue가 `약 90억 달러`였는데, Sacra 추정 기준 `2026년 3월` 연환산 `약 300억 달러`로 YoY `약 1,400%` 성장했다. 기업 고객 `30만+`, `$100K+` 런레이트 대형 계정은 최근 1년간 `약 7배` 증가했다. Claude Code 단독 ARR은 `약 25억 달러` 수준이다.
- 자본조달도 같은 곡선이다. `2025년 9월 Series F $130억 (post-money $1,830억)`, `2026년 2월 Series G $300억 (post-money $3,800억, GIC·Coatue 주도)`로 두 번 연속 대형 라운드를 닫았다.
- 컴퓨트는 3축 다변화다. (1) AWS — Project Rainier는 `Indiana, $110억` 규모 캠퍼스로 `2025년 10월` 완전가동, `Trainium2` `약 50만 개`에서 `연말까지 100만 개` 증설. `5GW` 확장과 `2026 상반기 Trainium2` 신규분 + `2026 연말까지 Trainium2/3 약 1GW` 추가 계약. (2) Google Cloud — `2025년 10월 23일` 발표로 `TPU 최대 100만 칩, 1GW+` 규모 확장. (3) Broadcom — `2026년 4월` Google과 함께 `2027년부터 3.5GW` TPU 용량을 추가 확보.
- 안전·정책 스택은 `Responsible Scaling Policy v3.0` (2025 개정판) 위에 놓여 있다. `ASL-3` 보호 조치는 `2025년 5월 Opus 4` 출시와 함께 실제 활성화됐고, `CBRN 능력 임계치`와 `AI R&D 자동화 임계치`가 신규 분리됐다. Constitutional Classifiers++(유니버설 탈옥 방어) 및 내부 probe 기반 해석가능성 스택이 배포 게이트의 일부가 됐다.
- 경쟁 좌표는 단순히 "OpenAI와 2위 경쟁"이 아니다. 엔터프라이즈 코딩/에이전트 워크로드에서 1위 포지션, 소비자 ChatGPT 규모에서는 OpenAI에 뒤처짐, 멀티모달·소비자 제품에서는 Google과 정면 경쟁.

## 공식 로드맵
| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| Anthropic `Claude Opus 4.5` (2025-11) | `SWE-bench Verified 80.9%`, `OSWorld 66.26%`, `ARC-AGI-2 37.6%`, Chrome/Excel 통합 | `2026-2027` Anthropic의 기술적 우위 축은 여전히 코딩·에이전트·툴사용이다. 멀티모달·음성은 여전히 OpenAI/Google 대비 지연 | 벤치마크는 강하지만 제품 카테고리 폭은 좁다 |
| Anthropic + AWS `Project Rainier` & 5GW 확장 | Trainium2 `100만 칩 규모`, `2026 상반기` Trainium2 증설, `2026 연말까지 Trainium2/3 약 1GW` | 컴퓨트 병목은 `2026-2027` 구간에서 부분적으로 완화되지만, 전력·부지·변압기 병목이 새로운 제약이 된다 | AWS 공식 발표 + 현장 건설 진척 확인 |
| Anthropic + Google Cloud TPU (2025-10) | `최대 100만 TPU, 1GW+` 용량, `2026` 내 온라인 | 3축(AWS·GCP·NVIDIA) 하드웨어 다변화는 공급 리스크 분산에는 효과적이나 소프트웨어 스택 복잡도가 급증 | 공식 press release 확인 |
| Anthropic + Broadcom/Google TPU (2026-04) | `2027-` `3.5GW` 차세대 TPU | 2027 이후 컴퓨트 규모 곡선의 상방은 이 계약 실행에 직접 연동. 전력 공급이 새 병목 | Broadcom·Google 공식 + Anthropic 발표 |
| Anthropic `Responsible Scaling Policy v3.0` | ASL-3 실제 활성화, CBRN·AI R&D 임계치 재정의, 배포 전제조건 재구성 | 공식적 안전 서약은 강하지만 국제 규제와 경쟁사 속도에 따라 실효 구속력은 가변 | 정책 개정과 ASL-3 실제 활성화는 실행된 사실 |
| Series F/G 자본 (2025-09, 2026-02) | `$183B` -> `$380B` valuation | `2026-2028`에 자본 여력은 경쟁사 중 최상위, 다만 연간 컴퓨트 지출이 `수백억 달러` 규모로 올라감 | Anthropic 공식 + Goldman/CNBC 확인 |

## 1년 단위 전망 (2026->2035)
| 연도 | Base 마일스톤 | 낙관 시나리오 | 지연 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | Claude 5 세대 출시, 연간 ARR `$400억+` 도달, 에이전트형 코딩/지식작업 유즈케이스가 엔터프라이즈 기본 구매가 된다 | 만약 `Trainium2 1GW` + `TPU 1GW`가 예정대로 램프업되면 학습·추론 동시 확장이 가능해진다 | 만약 전력 인입이나 HBM 공급이 밀리면 Rainier II 및 TPU 확장이 `2~3분기` 지연된다 | 80% |
| 2027 | Broadcom/Google `3.5GW` TPU 용량 초기 온라인, ASL-4 정의 및 공식 채택 여부가 업계 기준이 된다 | 만약 해석가능성 연구가 deployment gate를 실질적으로 설계하는 단계로 진입하면 regulator 신뢰를 선점 | 만약 ASL-4 기준 합의가 늦어지고 CBRN uplift 사건이 발생하면 대형 고객 배포가 정지 | 78% |
| 2028 | 에이전트 워크플로우가 S&P 500의 `30%+` 핵심 프로세스에 통합, API/직접판매 mix가 매출의 주축 | 만약 장기 기억·다중 에이전트 협업 아키텍처가 안정화되면 화이트칼라 TAM이 재평가 | 만약 기업 내부 도입 ROI가 Acemoglu류 실증에 더 가깝게 나오면 enterprise 갱신률이 꺾인다 | 60% |
| 2029 | IPO 혹은 대규모 secondary 이벤트 가능성, 연간 매출 `$1,000억` 근접 시나리오에 진입 | 만약 Anthropic이 해석가능한 reasoning 모델의 de facto 표준이 되면 규제 시장(금융·의료·정부)의 프리미엄 차지 | 만약 OpenAI/Google이 멀티모달·소비자·AI for Science에서 동시 우위를 유지하면 Anthropic은 `enterprise niche`로 수렴 | 50% |
| 2030 | RSP v4/v5 세대가 정의되고 최소 한 번의 ASL-4 수준 역량 선언 사례가 발생 | 만약 AI 안전 과학이 peer-reviewed 분야로 성숙하면 Anthropic의 선점 자산이 가치 재평가된다 | 만약 선도 사고(incident)가 한 차례 발생하면 전체 frontier 배포가 정치적으로 위축된다 | 38% |
| 2031 | 수평 플랫폼(모델) + 수직 제품(Claude Code, Chrome/Excel 통합 등) 혼합 포트폴리오로 구조화 | 만약 자체 인퍼런스 실리콘 참여(Trainium 공동설계) 수준이 올라가면 단위 토큰 원가가 의미있게 하락 | 만약 전력·컴퓨트 확장이 계속 AWS·GCP에 의존하면 스택 독립성이 제한됨 | 60% |
| 2032 | 과학용 에이전트(단백질·재료·기후 모델링)가 Anthropic의 새로운 성장축 | 만약 AlphaFold류 과제를 Claude 기반 에이전트가 산업 pipeline으로 내재화하면 비코딩 과학 매출 비중 상승 | 만약 DeepMind/OpenAI가 AI for Science 분야의 기술적·조직적 우위를 굳히면 과학 세그먼트는 후발 포지션 | 35% |
| 2033 | AGI-근접 역량 논쟁에서 Anthropic의 safety framing이 정책 및 보험 산업의 기준 템플릿이 된다 | 만약 국제 AI safety 조약(예: UK AISI+US AISI+EU AI Office 공동 평가)이 성립되면 RSP 계열이 regulatory shortcut | 만약 지정학 분절이 더 깊어지면 중국권·미국권·EU권이 각기 다른 평가체계로 파편화 | 50% |
| 2034 | 회사 구조는 `safety-forward lab` 이미지를 유지한 채 수익 측면은 Big Tech 경쟁자 수준의 현금창출 기업 | 만약 public mission + for-profit 이중 구조가 안정적으로 정착하면 거버넌스 모델이 산업 표준이 된다 | 만약 거버넌스·투자자·미션 간 충돌이 가시화되면 내부 이탈 및 상업 노선 전환 리스크 | 55% |
| 2035 | Anthropic은 `OpenAI-Google-Anthropic` 3강 중 안전·엔터프라이즈·해석가능성 축의 대표 브랜드로 자리잡는다 | 만약 안전 연구가 실제 catastrophic risk를 지연/방지한 사례로 문서화되면 역사적 포지션이 공고화 | 만약 추론 비용 경쟁에서 OpenAI·Google 또는 중국권 대형 랩에 밀리면 하나의 세그먼트 특화 플레이어로 축소 | 60% |

## 물리적/구조적 한계
- 전력과 부지가 칩보다 더 앞선 병목이다. `3.5GW+` 단일 고객사 계약은 미국 내 송전·변전·토지 수용과 직접 충돌한다.
- 하드웨어 3축(Trainium, TPU, NVIDIA) 병행은 공급 리스크를 분산하지만 학습 프레임워크, 컴파일러, 분산 최적화, 모델 이식성에서 지속적인 엔지니어링 부담을 만든다.
- RSP 상위 임계치(ASL-4, ASL-5)는 아직 "실현 가능한 평가·완화 방법"이 부재한 상태다. Anthropic 스스로 `v3.0`에서 이를 공개적으로 인정했다.
- Anthropic은 아직 소비자 규모(월간 활성자 수, 디바이스 OS 통합)에서 OpenAI·Google 대비 열세이며, 이는 네트워크 효과 축적 속도를 제한한다.
- `$380B` 밸류에이션은 현재 ARR 배수로 볼 때 AI infra CAPEX 지속 투입을 전제로 한다. 자본시장 금리·경기가 바뀌면 조달·거버넌스 구조에 압력이 가해진다.

## 기술 현실론 보정
- 낙관론 측 근거: `Opus 4.5`의 `80.9% SWE-bench`, run-rate revenue `$30B`, `3.5GW` TPU 확보, `ASL-3` 실제 활성화는 모두 측정 가능한 실물 진척이다. 특히 코딩·에이전트 워크로드에서 Anthropic은 `2024년 Claude 3.5 Sonnet`부터 연속 우위를 유지 중이다.
- 현실론 측 반론: 매출 급증은 엔터프라이즈 AI 시장 자체의 공급자 보조(클라우드 크레딧, 초기 할인)와 결합돼 있다. Acemoglu/Brynjolfsson 계열 연구는 GPT 계열 생산성 효과가 보고된 것보다 낮고 불균등함을 지적한다. 엔터프라이즈 ROI가 기대에 미달하면 구매 사이클이 급격히 느려진다.
- 균형 판단: `2026-2028` 구간에서 Anthropic의 기술적·상업적 우위는 실물이다. 그러나 `2029+`의 궤적은 (1) ASL-4 수준 안전 문제, (2) 전력·부지 확장 실행, (3) 소비자 분야 OpenAI/Google과의 비대칭 극복 여부에 달려 있다. 저장소 기준 thesis는 "Anthropic은 frontier 3사 중 하나로 생존하지만, 특화 세그먼트(안전·엔터프라이즈 코딩·해석가능성)에서 리더, 종합 플랫폼에서는 2-3위"다.

## 2035 전망 요약
- Base: Anthropic는 `OpenAI-Google DeepMind-Anthropic` 3강 구도의 한 축으로, 엔터프라이즈 에이전트와 안전·해석가능성 분야의 대표 브랜드가 된다. 연매출 `$1,500-3,000억` 범위의 상장/준상장 기업.
- Upside: RSP 계열 기준이 국제 안전평가의 de facto 표준이 되고, Claude가 과학·코딩·의료 분야에서 수직 시장의 기본 인프라로 자리잡는다. 연매출 `$4,000억+`, 시장가치 `$1조+` 진입.
- Downside: 선도 AI 사고 한 번, 또는 OpenAI/Google/중국권 랩의 동시 기술 우위가 겹치면 Anthropic은 `enterprise niche` 또는 `safety consulting 색채의 보조 플레이어`로 축소된다.

## 연결 문서
- [./openai.md](./openai.md)
- [./google_deepmind.md](./google_deepmind.md)
- [./meta_ai.md](./meta_ai.md)
- [../semiconductors/nvidia.md](../semiconductors/nvidia.md)
- [../../02_technology/symbolic_reasoning/epistemology_break.md](../../02_technology/symbolic_reasoning/epistemology_break.md)
- [../../02_technology/semiconductors/roadmap_annual.md](../../02_technology/semiconductors/roadmap_annual.md)
- [../../12_wildcards/black_swans.md](../../12_wildcards/black_swans.md)
- [../../13_scenarios/base_case.md](../../13_scenarios/base_case.md)

## 정보 출처
- Anthropic `Introducing Claude Opus 4.5` https://www.anthropic.com/news/claude-opus-4-5 2026-04 확인
- Anthropic `Introducing Claude 4` (Opus 4 / Sonnet 4) https://www.anthropic.com/news/claude-4 2026-04 확인
- Anthropic `Introducing Claude Sonnet 4.5` https://www.anthropic.com/news/claude-sonnet-4-5 2026-04 확인
- Anthropic `Responsible Scaling Policy v3.0` https://www.anthropic.com/news/responsible-scaling-policy-v3 2026-04 확인
- Anthropic `Activating AI Safety Level 3 protections` https://www.anthropic.com/news/activating-asl3-protections 2026-04 확인
- Anthropic `Anthropic and Amazon expand collaboration for up to 5 gigawatts` https://www.anthropic.com/news/anthropic-amazon-compute 2026-04 확인
- Anthropic `Expanding our use of Google Cloud TPUs and Services` https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services 2026-04 확인
- Anthropic `Expands partnership with Google and Broadcom` https://www.anthropic.com/news/google-broadcom-partnership-compute 2026-04 확인
- Anthropic `Series F $13B at $183B` https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation 2026-04 확인
- Anthropic `Series G $30B at $380B` https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation 2026-04 확인
- About Amazon `AWS Project Rainier activated` https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster 2026-04 확인
- CNBC `Anthropic $30B run rate` https://www.cnbc.com/2026/02/12/anthropic-closes-30-billion-funding-round-at-380-billion-valuation.html 2026-04 확인
- Sacra `Anthropic revenue and funding` https://sacra.com/c/anthropic/ 2026-04 확인
- Anthropic `Constitutional Classifiers` https://www.anthropic.com/research/constitutional-classifiers 2026-04 확인
