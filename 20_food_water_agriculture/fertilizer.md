# Food, water, and agriculture: fertilizer
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08

## 2026년 4월 현재 상태

- 이 파일은 issue-backed sector vertical slice의 일부이며, 2035 Fundamental State Map에서 실물 병목을 계산하기 위한 입력 레이어다.
- 핵심 제약은 natural gas, phosphate/potash supply, trade restrictions이다.
- 선행지표는 urea prices, gas prices, export controls, application rates이다.
- 의존 도메인은 Food security, energy, shipping, and geopolitics이다.
- 현재 값과 forecast 값은 출처값, repo inference, deterministic formula output을 분리해서 기록해야 한다.

## 공식 로드맵

| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| 공식/준공식 출처 | 2025-2026 기준 구조 변수와 병목을 제공 | Base line의 source anchor로 사용 | `정보 출처` URL 기준 |
| 산업/정책 로드맵 | CAPEX, 공급, 수요 목표를 제시 | Upside/Downside band 입력값으로 사용 | 계획은 지연 할인 후 반영 |
| repo inference | 여러 출처를 dependency graph로 연결 | deterministic calculation의 임시 변수로 사용 | 낮은 confidence와 missing policy 기록 |

## Deterministic input contract

| variable_id | group | unit | direction | missing_policy |
|---|---|---|---|---|
| `fertilizer_demand` | demand | index | higher_is_capacity | use_base |
| `fertilizer_capacity` | capacity | index | higher_is_capacity | block |
| `fertilizer_finance` | finance | index | higher_is_constraint | use_base |

## 2035 기준선 산출 방식

```text
capacity_score = normalized(fertilizer_capacity)
finance_score = normalized_inverse(fertilizer_finance)
demand_score = normalized(fertilizer_demand)
fundamental_score = min(demand_score, capacity_score, finance_score)
fundamental_line = unconstrained_demand_path * fundamental_score
```

Baseline formula: `min(feedstock supply, nutrient mining, logistics, farmer affordability)`.

## 1년 단위 전망 (2026->2035)

| 연도 | Base 마일스톤 | Upside 시나리오 | Downside 시나리오 | 확률 |
|---|---|---|---|---|
| 2026 | 기준 데이터와 2026 현재 병목을 확정한다 | 정책·CAPEX 공시가 조기 정렬된다 | 데이터 공백으로 baseline이 provisional에 머문다 | 82% |
| 2027 | 선행지표를 분기별로 추적한다 | 병목 완화 투자가 계획보다 빠르게 집행된다 | 금리·허가·공급망 지연이 누적된다 | 78% |
| 2028 | 2030 checkpoint의 1차 검증이 가능해진다 | 생산성·자동화가 capacity score를 끌어올린다 | 비용 상승이 demand score를 깎는다 | 62% |
| 2029 | Base path와 실제 투자의 괴리율을 산출한다 | 정책 보조와 민간 CAPEX가 동시에 증가한다 | 지정학 분절로 조달 비용이 상승한다 | 55% |
| 2030 | 2035 line의 중간 checkpoint를 재보정한다 | 병목 투자가 실물 capacity로 전환된다 | 주요 프로젝트가 1-2년 지연된다 | 48% |
| 2031 | 부족한 하위 병목을 별도 issue로 분해한다 | 표준화와 학습효과가 단가를 낮춘다 | 노동·인허가가 계속 binding constraint다 | 42% |
| 2032 | Base와 Downside의 분기 여부가 관측된다 | 공급망 이중화가 resilience를 높인다 | 자본비용이 높은 상태로 유지된다 | 38% |
| 2033 | 2035 physical ceiling을 재계산한다 | 병목 완화가 demand growth를 따라잡는다 | shock 시나리오가 Base를 압박한다 | 34% |
| 2034 | 2035 직전 line을 확정한다 | 확장 투자가 다음 10년 line으로 넘어간다 | 과잉 기대가 asset price divergence를 키운다 | 30% |
| 2035 | Base line과 실제 결과를 retrospective로 평가한다 | Upside band가 실현되어 capacity 상단을 검증한다 | Downside band가 실현되어 bottleneck model을 강화한다 | 26% |

## 물리적/구조적 한계

- Base: 현재 발표된 정책·CAPEX와 관측 가능한 capacity가 동시에 반영되는 경로다.
- Upside: 병목 투자가 조기 완공되고 financing이 유지되는 경로다.
- Downside: 인허가, 자본비용, 공급망, 숙련노동 중 하나 이상이 binding constraint가 되는 경로다.
- Shock: 지정학, 에너지, 금융, 기후 충격이 source anchor를 훼손하는 경우 별도 multiplier를 적용한다.

## 기술 현실론 보정

- 낙관론 측 근거: 정책 목표와 민간 CAPEX는 2035 line의 수요 측 상단을 만든다.
- 현실론 측 반론: 물리적 병목과 금융 제약은 demand story를 그대로 실현시키지 않는다.
- 균형 판단: 이 sector는 독립 예측이 아니라 dependency graph의 constraint input으로 쓰인다.

## 2035 전망 요약

- Base: min(feedstock supply, nutrient mining, logistics, farmer affordability)에 의해 2035 정상 경로를 산출한다.
- Upside: capacity score가 Base보다 높아져 demand-implied path에 가까워진다.
- Downside: capacity 또는 finance score가 낮아져 current expectation 대비 괴리율이 커진다.

## 연결 문서

- [overview_annual.md](../01_climate_and_nature/overview_annual.md)
- [green_hydrogen.md](../03_energy/hydrogen/green_hydrogen.md)
- [shipping.md](../19_logistics_and_trade/shipping.md)
- [fundamental_line_prediction.md](../00_foundations/fundamental_line_prediction.md)
- [SYNTHESIS_2035_QUANTITATIVE.md](../13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md)

## 정보 출처

- FAO SOFI 2025, https://www.fao.org/publications/home/fao-flagship-publications/the-state-of-food-security-and-nutrition-in-the-world, 2026-05 확인.
- UN World Water Development Report 2025, https://www.unwater.org/publications/un-world-water-development-report-2025, 2026-05 확인.
- UNESCO World Water Report 2025, https://www.unesco.org/en/world-water-report-2025, 2026-05 확인.
