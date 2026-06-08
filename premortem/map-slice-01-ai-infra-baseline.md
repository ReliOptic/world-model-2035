# Map Slice 01 — AI 인프라 빌드아웃 (Base 2035)

> **이것은 무엇인가:** [CONTEXT.md](../CONTEXT.md)의 **Coupling Map** schema를 *Base Case 시나리오*에 인스턴스화한 첫 **Map Slice**다. 방법론은 [ADR 0001~0003](../docs/adr/) 참조. 주간 디스커션의 **화두(Seeder)** 이자, 공모전 '예견된 실패' 후보를 *발견*하는 장치.
> **읽는 법:** 행=행위자(비대칭 게임), 열=자원 어휘 v1(고정 좌표축). 셀=그 행위자가 그 자원을 어떻게 청구/통제하나 + 이 시나리오에서의 강조. **Hub는 고르지 않고 발견한다** — 결합이 가장 몰린 열이 표적.

## 슬라이스 격자 (행위자 × 자원 v1)

행위자 = **하이퍼스케일러**(민간 속도) · **미국**(공공 속도: 그리드·인허가·정책) · **한국**(반도체·연금자본·수출의존). 강조는 Base 2035 빌드아웃 기준.

| | ⚡ 전력 | 🧮 compute(GPU/HBM) | 💰 자본·조달 | 🪨 구리 | 🧠 숙련노동 |
|---|---|---|---|---|---|
| **하이퍼스케일러** (민간) | 청구 폭발: 美 contracted load >15GW→**50GW+**(2035). 자체 PPA·SMR LOI로 *민간 속도* 우회 | 통제 강: 칩 구매예산이 HBM4→HBM7+ 수요 견인. 단 CoWoS·HBM 할당이 외부 병목 | 통제 강: CAPEX >$400B→**$2T+**, FCF로 자기조달 | 무인지: 구리를 *간접* 소비(그리드·DC 배선)하나 직접 관리 안 함 → **저평가의 진원** | 청구: AI 엔지니어 확보엔 우위, 그러나 전력·건설 *현장* 숙련은 외부 의존 |
| **미국** (공공) | **병목 보유**: 그리드 접속 대기 PJM/ERCOT **4-7년**, 송전 리드타임 10년+. 민간 속도를 *못 따라감* | 정책 통제: 수출통제("Wider Yard")로 compute 흐름 규율, 단 첨단 칩 >90% 대만 의존 | 거시 제약: 부채/GDP **130-145%**(2035), 이자비용 $1.5-2T → 보조금 여력 압박 | 공급 부재: 정제·제련 캐파 부족, 광산 인허가 10-20년. IRA 수요는 키우나 공급 못 키움 | 정책 청구: 재훈련·이민정책 쥐나 *공공 속도*로 느림 |
| **한국** (수출·자본) | 기회+노출: 두산·HD현대 SMR 공급망 수출 기회 / 국내 전력도 동시 경합 | **통제 최강**: SK하이닉스 HBM **1위**, 삼성 HBM+파운드리. compute 자원의 핵심 길목 | **이중 노출**: 국민연금 **1,200조원**, 2030까지 주식 55%·해외·대체 45-50%+ → AI capex 붐에 *과배분 위험* | 전량 수입 의존: 배터리·전선(LS·대한전선) 원료로 구리 경합에 직접 노출 | 제조 숙련 우위 / 고령화 세계 최고속도로 숙련노동 풀 침식 |

## Hub 발견 — 결합이 어디에 몰리나

열을 가로질러 *몇 명의 행위자가 동시에 binding되는가*를 본다:

- **⚡ 전력 — 3/3 행위자 모두 binding.** 하이퍼스케일러는 폭발 청구, 미국은 병목 보유, 한국은 기회+국내경합. **그리고 여기서 민간 속도(DC 1-2년) vs 공공 속도(그리드 4-7년+)의 비대칭이 가장 날카롭다.** → **Hub 후보 #1 (게임 엔진 최선명).** FLP 파일럿이 이미 정량화: AI인프라 체인 **divergence +38.7%, signal=overheated, binding=grid/transformer**([fundamental_line_pilot_ai_infra](../13_scenarios/fundamental_line_pilot_ai_infra.md)).
- **🪨 구리 — 3/3 binding이나 *아무도 가격에 반영 안 함*.** 전기화되는 *모든 것*(그리드·DC·EV·국방·재생e)이 같은 구리풀을 경합하는데 광산 리드타임 10-20년, 하이퍼스케일러는 *무인지*. **결합은 가장 깊고 합의는 가장 저평가** → **Hub 후보 #2 (통찰력 최대, 가장 덜 뻔함).**
- 🧮 compute·💰 자본·🧠 숙련노동 — binding이나 전력/구리만큼 *상관*을 만들진 않음(부분 결합).

## 게임 프레임 적용 (ADR 0002 인과 프레임)

> **비대칭 내시균형:** 하이퍼스케일러는 민간 자본·속도로 전력(과 그 배후 구리)을 *최선의 수*로 과잉청구한다. 국가는 공공 속도로 그리드·공급을 못 따라간다. 누구도 비합리적이지 않다 — 각자 최적 대응이다. **그러나 균형의 총합이 가능성 천장(Fundamental Line)을 +38.7% 초과(Overshoot)한다.** 그 초과분이 Divergence Signal로 측정되고, 전력·구리 Hub에서 청산(Resource Contention Cascade)되는 순간이 2036년의 실패다.

**= price of anarchy의 물리적 구현.** "AI가 오작동해서"가 아니라 "모두가 합리적으로 같은 자원을 과청구한 균형 자체가 실패"였다.

## 주간 디스커션 화두 (Seeder 출력 — 팀이 고를 fork point)

이 슬라이스가 **던지는 질문**, 모임에서 1개로 수렴:

1. **Hub를 전력으로?** → 게임 비대칭이 가장 선명, FLP 정량앵커 즉시 사용가능. 약점: '전력' 자체는 다소 뻔함 → 비대칭 속도 프레임으로 차별화 필요.
2. **Hub를 구리로?** → 가장 덜 뻔함(통찰력 35점 최대), 가장 깊은 다중결합. 약점: 정량앵커가 전력보다 약함(구리 FLP 라인 미작성 → research 필요).
3. **한국 앵글:** 국민연금 1,200조원이 AI capex 붐에 과배분 → 전력/구리 Hub에서 overshoot 청산 시 **미래 은퇴 세대가 손실 귀속**(Chain B 분배 왜곡). 공모전 공감대(20점·10점) 최대.

## 여기서 떠오른 실패 장면 후보

> **C6 (지도 발견형):** 2036년, 2020년대 말 합리적 과청구가 누적된 전력·구리 Hub가 동시에 조인다. 좌초된 데이터센터·지연된 그리드·청산되는 자산가격이 **상관되어** 터지고(아무도 단독으론 막을 수 없었다 — 각자 최적이었으니까), 국민연금이 떠안은 AI 인프라 익스포저가 은퇴 세대를 직격한다. **균형이 곧 실패였다.**

이 C6은 기존 [failure-candidates.md](failure-candidates.md)의 C1~C5와 달리 *단일 서사가 아니라 Coupling Map이 발견한 상관 실패*다 — "AI×실패"의 인과를 게임이론으로 구현한 가장 비-뻔한 후보.

## 다음 액션
- [ ] 모임에서 Hub 1개 수렴(전력 / 구리 / 융합) → `selected` 라벨
- [ ] 선택 Hub의 FLP 라인 보강(구리 선택 시 `copper.md` 입력테이블 작성, `research`)
- [ ] 한국 앵글(국민연금 익스포저) 정량화 여부 결정
- [ ] 다음 시나리오(Delayed/Bifurcated)로 Map Slice 02 인스턴스화 → 같은 좌표축에서 Hub 이동 비교(ADR 0003 누적 통찰)

## 정보 출처
- 행위자×자원 앵커는 레포 소스백 파일 집계: [bottleneck_map.md](../15_opportunity_intelligence/bottleneck_map.md)(병목 1·3·10, 누가아픈가/누가돈내나/한국기회), [fundamental_line_pilot_ai_infra.md](../13_scenarios/fundamental_line_pilot_ai_infra.md)(divergence 38.7%), [SYNTHESIS_2035_QUANTITATIVE.md](../13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md)(거시·반도체·전력 앵커), [copper.md](../17_materials_and_mining/copper.md), [electrical_equipment.md](../16_industrial_base/electrical_equipment.md), [nps_scenarios.md](../06_geopolitics/06_korea/nps_scenarios.md)(국민연금 1,200조·자산배분 2030).
- 1차 출처(글로벌 고신뢰): IEA *Energy and AI* / *Electricity 2026: Grids* / *Global Critical Minerals Outlook 2025*, IMF WEO — 각 도메인 파일의 `정보 출처`에 보존.
- Slice 강조·Hub 발견·게임 프레임 해석은 repo inference(ADR 0001~0003 방법론). divergence 38.7%는 FLP-0.1 결정론적 출력.
