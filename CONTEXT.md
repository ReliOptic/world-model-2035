# The World in 2035 — Forecasting Context

소스 기반 2026→2035 세계 모델. 공개된 로드맵을 결정론적 기준 경로로 통합하고, 현재의 기대치가 그 경로에서 얼마나 벗어났는지를 측정한다. 이 파일은 그 작업에서 쓰는 **용어 사전**이다(구현·수식 아님).

## Language

### 예측 방법 (Forecasting method)

**Fundamental Line** (펀더멘탈 라인):
소스 입력에서 재현 가능하게 계산한, 병목이 작용한 *제약된* 기준 경로 — demand/capacity/finance 중 가장 약한 것에 의해 결정된다. 하나의 미래를 맞히는 게 아니라 '정상 경로'를 계산하는 것.
_Avoid_: prediction, forecast(더 넓은 말), 수식어 없는 "the line"

**Composite Fundamental Line** (복합 펀더멘탈 라인):
다중 섹터 의존 체인(예: AI/DC→그리드→반도체→건설→금융)에 걸쳐 집계한 Fundamental Line. 체인의 가장 약한 고리가 경로를 정한다.
_Avoid_: "복합 라인"만 단독 사용

**Base Case** (표준 2035):
base-case 앵커로 그린 Fundamental Line — 즉 '표준적인 2035의 모습'. 도메인 교차 정합 기준 문서는 `13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md`(마스터 앵커).
_Avoid_: "표준 2035 / standard scenario"를 별개 개념처럼 쓰는 것 — 그것이 곧 Base Case다

**Scenario Band** (시나리오 밴드):
같은 입력의 결정론적 변형 — Base / Upside / Downside / Shock.
_Avoid_: best/worst case

**Binding Constraint** (병목):
Fundamental Line을 결정하는 가장 약한 고리(최저 점수). 경로의 천장을 정한다. binding constraint가 **공통 자원**일 때, divergence는 그 자원에 의존하는 모든 체인에서 *상관되어* 나타난다(네트워크 효과).
_Avoid_: limit, ceiling

**Shared Resource / Coupling Node** (공통 자원 / 결합 노드):
여러 의존 체인이 동시에 끌어다 쓰는 제약 입력. **단일 자원일 수도, 다차원 *구성(configuration)* 셀일 수도 있다** — 예: (국가 × 섹터 × 공공·정치 배열 × 자원 × 현재상태). 분석 표적은 임의로 고른 한 변수가 아니라 결합이 가장 몰리는 **Hub** 이며, 지도를 그려 *발견*한다.
**자원 어휘 v1(고정 좌표축, 버전관리 / ADR 0003):** 전력 · compute(GPU/HBM) · 자본·조달 · 핵심광물(구리) · 숙련 인지노동. 새 자원이 나오면 축에 추가하고 버전업.
_Avoid_: 단일 변수로의 조기 수렴 — legible한 것으로 환원하는 안티패턴(아이러니하게 AI 실패 양식 그 자체)

**Coupling Map** (결합 지도):
**안정 골격(schema)** — 축 유형(행위자 × 자원 × 시간) + 자원 어휘목록 + 방법(FLP 척추 + 게임 인과프레임 + Hub 발견) + 폭 예산(패스당 ≥5×5). 고정 표가 아니라 *렌즈*. 버전관리한다.
_Avoid_: 단일 도메인 지도; 폭 없이 곧장 변수로 수렴; 5×5를 영구 고정표로 취급

**Map Slice** (시나리오별 슬라이스):
들어온 시나리오 하나에 대해 Coupling Map을 인스턴스화한 5×5(이상) 단면 — *이* 시나리오에서 결합이 가장 몰리는 행위자·자원·시점을 골라 채운다. 취약 **Hub**는 슬라이스에서 *발견*된다. 새 시나리오가 어휘에 없는 자원을 끌어내면 자원 어휘가 버전업된다.
_Avoid_: 슬라이스를 schema와 혼동 — 슬라이스는 가변, schema는 안정

**Resource Contention Cascade** (자원 경합 캐스케이드):
공통 자원이 여러 체인의 binding constraint가 *동시에* 되어, 상관된 divergence·실패가 한꺼번에 터지는 실패 양식. 합의는 각 도메인 수요를 따로 모델링해 이 상관을 저평가한다 → 비-뻔한 premortem의 표적.
_Avoid_: 단순 "연쇄 실패" — 핵심은 *공통 자원이 상관을 만든다*는 인과

### 게임 레이어 (behavioral) — 채택됨: 인과 프레임 (ADR 0002). 형식 솔버는 레포 장기 줄기.

**Strategic / Nash Equilibrium** (전략 균형 / 내시균형):
공통 자원(Hub)을 두고 경합하는 행위자들(국가·섹터·기업)의 비협조 게임에서 누구도 단독 이탈로 이득을 못 보는 **행동 결과**. *어디에 실제로 안착하는가*를 예측한다. **Fundamental Line(가능성 천장)과는 다른 객체** — 균형은 천장을 *초과*할 수 있다(과잉청구).
_Avoid_: "Fundamental Line = 내시균형" (범주 오류). 천장은 제약, 균형은 행동.

**Overshoot / Price of Anarchy** (과잉·무정부 비용):
비협조 내시균형과 협조적 사회최적(≈천장을 존중하는 경로) 사이의 격차. **Divergence Signal이 이 격차의 정량 측정**이며, 그 격차가 천장에 부딪혀 교정되는 것이 **Resource Contention Cascade**다.
_Avoid_: "격차"만 단독 — 핵심은 *합리적 행동의 총합이 집합적으로 실패*한다는 인과

**Players / 비대칭 게임** (행위자):
공통 자원을 경합하는 행위자 집합 — **빅테크(하이퍼스케일러)+국가 혼합**(ADR 0002). 민간은 자본·compute·전력을 *민간 속도*로, 국가는 그리드·인허가·분배를 *공공 속도*로 쥔다. **이 속도 비대칭이 overshoot의 엔진.** 1차 지도 행위자 = 하이퍼스케일러 × 미국 × 한국.
_Avoid_: "국가 대 국가" 또는 "AI 대 인간" 단순 대립 — 핵심은 *민간자본 대 공공인프라의 속도 비대칭*

**Roadmap Conflict** (교차 도메인 모순):
소스가 있는 두 로드맵·시나리오 사이의 모순. 미래가 갈라지는 결정/분기 지점이며 레포가 명시적으로 추적한다(SYNTHESIS의 "상위 교차 도메인 모순").
_Avoid_: inconsistency, error

**Divergence Signal** (괴리 신호):
현재의 시장가격·정책목표·투자발표가 Fundamental Line에서 얼마나 벗어났는지(overheated/neutral/undervalued). **지금 시점에 소스 앵커 대비 '정합성'을 시험할 뿐, 2035가 실제로 그렇게 되는지(진위)를 증명하지 않는다.**
_Avoid_: "증명(proof)", "참/진실(truth)" — 진위가 아니라 정합성 신호다

**Prediction Scoring** (예측 채점):
예측 대 실제 결과의 사후 대조(`14_predictions_log/`, `scoring.md`). *진위*를 시험하는 유일한 기제이며, 체크포인트 연도에만 해소된다.

### 도메인 렌즈 (분석 주제)

**Industrial Structural Imbalance** (산업 구조 불균형):
AI가 자본을 compute·인프라로 집중시키며 생기는 이중 왜곡 — **(A 실물 병목)** 전력·건설 등 보완 실물요소가 못 따라가 binding constraint에 막히고, **(B 분배 왜곡)** 그 이득이 자본에 귀속되어 중간인지 노동·세수 기반이 침식되는 상태. Chain A를 정량 척추(FLP-0.1 line), Chain B를 그 위 해석 레이어로 다룬다.
_Avoid_: 단순 "불평등" — 이건 AI 자본집중이 인과인 *구조적* 불균형이다

## Relationships

- **Composite Fundamental Line** 은 체인을 따라 섹터별 **Fundamental Line** 으로 구성되고, 그 경로는 **Binding Constraint** 가 정한다.
- **Base Case** 는 base 앵커 하의 **Fundamental Line** 이며, **Scenario Band** 는 그 결정론적 변형이다.
- **Divergence Signal** 은 현재 기대치를 **Fundamental Line** 과 비교한다(지금=정합성). **Prediction Scoring** 은 진위를 나중에 시험한다.
- **Roadmap Conflict** 는 **Scenario Band** 가 갈라지는 지점을 표시한다.
- **Shared Resource** 가 **Binding Constraint** 가 되면, 의존 체인들의 divergence가 상관되어 **Resource Contention Cascade** 를 일으킨다 — 합의가 저평가하는 비-뻔한 실패의 자리.
- **Fundamental Line**(가능성 천장) ≠ **Nash Equilibrium**(행동 결과). 균형이 천장을 초과한 분량 = **Overshoot**, 그 측정치가 **Divergence Signal**, 그 교정이 **Cascade**. 네 개념이 한 사슬.
- **Coupling Map** 축(레포 확인됨): 섹터(25 도메인) × 국가(21국) × 공공·정치(geopolitics+intl orgs+정책) × 현재상태(각 파일 2026 섹션) × 시간(2026→2035 연단위). 1차 폭 예산 = 최소 5×5.
- 들어온 **시나리오**(13_scenarios/ + SCENARIO_TRACKER)는 각각 하나의 **Map Slice** 를 인스턴스화한다. **Coupling Map**(schema)은 안정·버전관리, **Map Slice** 는 시나리오마다 재도출. 새 자원이 나오면 자원 어휘 버전업.

## Example dialogue

> **분석가:** "내 거시 시나리오가 '참'이라는 걸 객관적으로 보이고 싶다."
> **도메인:** "지금 보일 수 있는 건 진위가 아니라 **Divergence Signal** 이다 — 현재 기대치가 너의 **Composite Fundamental Line** 에서 X% 벗어났다는, 재현 가능한 진술. 진위(**Prediction Scoring**)는 2030/2035 체크포인트에서만 해소된다."
> **분석가:** "그럼 발표 마감 전에 쓸 수 있는 '객관성'은 정합성뿐이네."
> **도메인:** "맞다. 그게 약점이 아니라 **Binding Constraint** 와 **Roadmap Conflict** 를 짚는 논리적 백본이 된다."
> **분석가:** "그 백본을 실패 서사로 어떻게 바꾸나?"
> **도메인:** "행위자들이 공통 **Shared Resource**(Hub)를 두고 둔 **Nash Equilibrium** 이 가능성 천장을 **Overshoot** 한다 — 그 초과분이 곧 **Divergence Signal**. 천장에 부딪혀 **Resource Contention Cascade** 로 청산되는 게 2036년의 실패다. 아무도 비합리적이지 않았는데 균형 자체가 실패였다."

## Flagged ambiguities

- "객관적으로 증명(참/거짓)" — **해소됨:** 진위(Prediction Scoring)가 아니라 **정합성(Divergence Signal)** 을 뜻한다. 주간 디스커션에서 담화가 로드맵과 정합한지 점검하는 **가드레일** 용도. 진짜 진위는 체크포인트 연도에만 해소된다.
- 레포의 1차 목적(해소됨): 상시 **로드맵 기반 디스커션 엔진** — (1) 화두 던지기(Seeder: 복합 로드맵·교차 모순 제시), (2) 가드레일(Guardrail: 담화 정합성 점검). premortem 후보 선정/리뷰는 이 엔진의 한 출력.
- "표준적 2035" → **Base Case** (해소됨).
- "복합적 펀더멘탈 라인" → **Composite Fundamental Line** (해소됨).
- "산업 구조 불균형(Industrial Structural Imbalance)" — **해소됨:** Chain A(실물 병목, FLP-0.1 정량 척추) + Chain B(분배 왜곡, 해석 레이어) 융합. FLP-0.2(분배 전용 수식)는 B가 *주역*이 될 때만 도입(현재 보류).
- **조기 수렴 안티패턴(경계):** 조합적 안목을 단일 legible 변수로 접지 말 것. 수렴은 **Coupling Map** 으로 폭을 그린 *뒤* 허브를 발견하는 결과여야 한다. ※ 이 안티패턴 자체가 유력한 premortem 후보 — "AI 보조 판단이 계량 가능한 것으로 수렴하며 안목을 잃는 실패."
