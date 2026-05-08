# Fundamental Line Pilot: AI Infrastructure Chain
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08

## 2026년 4월 현재 상태

- 이 pilot은 issue #12의 deterministic calculation requirement를 AI infrastructure dependency chain에 적용한다.
- Chain: AI/Data Center -> Power Grid -> Semiconductors -> Built Environment -> Financial Markets.
- 목적은 current implied expectation을 2035 fundamental line과 비교해 overheated, neutral, undervalued signal을 산출하는 것이다.
- 이 pilot은 투자 조언이 아니라 repo methodology 검증용 tracer bullet이다.

## 공식 로드맵

| 출처 | 발표 내용 | 달성률 할인 후 전망 | 근거 |
|---|---|---|---|
| IEA Energy and AI | 데이터센터 전력수요의 2030/2035 경로를 제시 | demand_score의 source anchor | AI 전력수요는 지역 grid 병목과 함께 해석 |
| IEA Electricity 2026 | grids and flexibility bottleneck을 제시 | capacity_score의 grid anchor | 접속 가능량이 demand path를 제한 |
| IMF WEO / BIS | 금융여건과 macro risk를 제공 | finance_score의 anchor | CAPEX 지속가능성은 금리·credit spread에 민감 |

## Deterministic input table FLP-0.1

| variable_id | group | source_value | min | base | max | direction | weight | confidence | normalized |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| `ai_dc_demand_index` | demand | 140 | 80 | 100 | 170 | higher_is_capacity | 0.40 | 0.70 | 0.667 |
| `hyperscaler_capex_index` | demand | 130 | 80 | 100 | 160 | higher_is_capacity | 0.35 | 0.65 | 0.625 |
| `enterprise_ai_adoption_index` | demand | 115 | 70 | 100 | 150 | higher_is_capacity | 0.25 | 0.55 | 0.563 |
| `grid_connection_index` | capacity | 90 | 50 | 100 | 150 | higher_is_capacity | 0.35 | 0.70 | 0.400 |
| `transformer_capacity_index` | capacity | 85 | 50 | 100 | 150 | higher_is_capacity | 0.25 | 0.65 | 0.350 |
| `gpu_hbm_supply_index` | capacity | 115 | 60 | 100 | 170 | higher_is_capacity | 0.25 | 0.65 | 0.500 |
| `construction_delivery_index` | capacity | 95 | 60 | 100 | 150 | higher_is_capacity | 0.15 | 0.60 | 0.389 |
| `credit_spread_stress_index` | finance | 120 | 80 | 100 | 180 | higher_is_constraint | 0.45 | 0.65 | 0.400 |
| `free_cash_flow_index` | finance | 125 | 70 | 100 | 160 | higher_is_capacity | 0.35 | 0.60 | 0.611 |
| `insurance_cost_stress_index` | finance | 115 | 80 | 100 | 170 | higher_is_constraint | 0.20 | 0.50 | 0.500 |

## Deterministic output

```text
demand_score   = 0.624
capacity_score = 0.412
finance_score  = 0.491
fundamental_score = min(0.624, 0.412, 0.491) = 0.412
unconstrained_demand_value = 140
fundamental_line_value = 140 * 0.412 = 57.68
current_implied_expectation = 80
divergence_pct = (80 - 57.68) / 57.68 = 38.7%
signal = overheated
```

The deterministic output says the pilot chain is ahead of its current capacity-constrained fundamental line. The binding constraint is capacity, especially grid connection and transformer availability. Analyst commentary may explain this, but must not change the signal unless the input table changes.

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

- Base: AI demand remains high, but grid and construction capacity limit realized deployment.
- Upside: grid-enhancing technologies, faster transformer production, and construction learning effects raise capacity_score.
- Downside: financing stress or interconnection delays pull the fundamental line below demand-implied expectations.
- Shock: export controls, power-market stress, or credit-market tightening force a formula-versioned recalculation.

## 기술 현실론 보정

- 낙관론 측 근거: AI CAPEX and cloud demand can keep demand_score elevated through 2030.
- 현실론 측 반론: physical connection, electrical equipment, and construction delivery are slower than narrative cycles.
- 균형 판단: the line should be recalculated quarterly once sector issues #2-#4 and #8 provide stronger source-backed inputs.

## 2035 전망 요약

- Base: AI infrastructure grows, but the realized line follows capacity and finance constraints rather than raw demand.
- Upside: capacity_score rises enough for the divergence signal to return to neutral without demand destruction.
- Downside: market-implied expectations stay above the physical buildout line, keeping the signal overheated.

## 연결 문서

- [fundamental_line_prediction.md](../00_foundations/fundamental_line_prediction.md)
- [datacenter_energy.md](../02_technology/compute_infrastructure/datacenter_energy.md)
- [ai_optimization.md](../03_energy/grid/ai_optimization.md)
- [roadmap_annual.md](../02_technology/semiconductors/roadmap_annual.md)
- [construction_capacity.md](../18_built_environment/construction_capacity.md)
- [credit_spreads.md](../22_financial_markets/credit_spreads.md)

## 정보 출처

- IEA Energy and AI, https://www.iea.org/reports/energy-and-ai, 2026-05 확인.
- IEA Electricity 2026 grids, https://www.iea.org/reports/electricity-2026/grids, 2026-05 확인.
- IMF World Economic Outlook, https://www.imf.org/en/Publications/WEO, 2026-05 확인.
