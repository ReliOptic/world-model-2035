# WETD Scope and Theater Framework

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## Purpose

WETD means **War-Economy Transition Dashboard**. `WETD` is the framework name; `2026–2035` is the forecast period used by this repository. The dashboard does not predict war directly. It tracks whether open-market allocation is shifting toward national-security allocation: self-reliance, stockpiling, route rewiring, access controls, sanctions adaptation, and civilian technology moving into defense or intelligence priority lanes.

## 연결 문서

- [CONTEXT.md](../CONTEXT.md) — WETD is a `Map Slice` / `Coupling Map` early-warning surface; WET scores are `Divergence Signal` evidence, not facts by themselves.
- [METHODOLOGY.md](../METHODOLOGY.md) — forecast-heavy files must separate present facts, repo inference, and scenarios.
- [wetd_theater_scenarios.md](wetd_theater_scenarios.md) — theater narratives and annual forecast rows.
- [wetd_data_schema.md](wetd_data_schema.md) — non-forecast data contract for keys, facts, weights, and views.
- [wetd_etl_dashboard_contract.md](wetd_etl_dashboard_contract.md) — non-forecast ETL/dashboard contract.
- [../19_logistics_and_trade/supply_chain_fragmentation.md](../19_logistics_and_trade/supply_chain_fragmentation.md) — repo anchor for route rewiring and fragmentation logic.

## 2026년 4월 현재 상태

**Present-state source-backed facts.** WETD can start from official or primary-source feeds rather than analyst prose: UN Comtrade and national trade APIs for trade flows; Federal Register, Trade.gov CSL, OFAC/EU/BIS-style lists, and government procurement portals for access-control and defense-allocation events; NSIDC/EIA/USGS-style sources for Arctic, energy, and minerals variables. These sources prove observable rows, not 2035 outcomes.

**Repo inference.** The repository already treats compute, semiconductors, energy, logistics, and critical minerals as coupled constraints. WETD turns that inference into a monthly `Coupling Map` view: country-month signal rows, theater multipliers, and a commander note explaining why a score changed.

**Scenario boundary.** A WET warning should not fire from one noisy row. It requires either at least three of five WET signals rising together, or one major theater shock plus two rising base signals.

## MVP actor and goods scope

| Scope | Included in the first WETD pass | Why it stays in scope |
|---|---|---|
| Core powers | United States, China, Russia | AI, sanctions, energy, military, and war-economy transition centers |
| G7 / advanced bloc | United States, Japan, Germany, UK, France, Italy, Canada, EU | Rulemaking, export controls, sanctions, industrial policy, financial controls |
| Frontline tech allies | Taiwan, South Korea, Japan, Netherlands, Germany/EU | Semiconductor production, memory, EUV/tooling, metrology, industrial bottlenecks |
| Corridor watch states | Taiwan, Singapore, Malaysia, UAE, Vietnam | Route rewiring, re-export, finance/logistics, sanctions adaptation sensors |
| Strategic goods | HBM/GPU proxies, semiconductor equipment, EUV/metrology, EDA proxy, energy, rare earths, copper, power equipment, data-center cooling | Shared resource/coupling-node candidates |

## Five WET signals

| Signal | Core question | Example evidence |
|---|---|---|
| Autarky | Is dependence on open-market supply being reduced? | Import-dependence shift, subsidy event, sovereignty language |
| Strategic stockpiling | Is strategic buying rising despite weak commercial logic? | Import/inventory anomaly, price-insensitive buying, stock-to-use proxy |
| Trade rewiring | Are direct routes shifting through third countries or trusted corridors? | Mirror-trade gaps, corridor import/export surges, partner-share shifts |
| Capital and access control | Is market access replaced by state permission? | FDI screening, sanctions, export controls, compute/API/model restrictions |
| Civilian-to-military allocation | Are civilian technologies entering defense/intelligence priority allocation? | Defense AI procurement, secure cloud, ISR/C2/autonomy spending |

## Calibration draft / open hypotheses

The following values are starting hypotheses, not final model truths. They must stay editable in the config/weight tables described in [wetd_data_schema.md](wetd_data_schema.md).

| Calibration item | Draft default | Why not final |
|---|---:|---|
| Five signal weights | 20% each | Useful baseline, but not evidence that all signals have equal causal force |
| Taiwan Strait multiplier | 1.20–1.50 | Needs empirical calibration against semiconductor concentration, military activity, insurance/shipping stress, and emergency procurement |
| Middle East multiplier | 1.10–1.40 | Needs calibration against energy, sanctions, procurement, and dual-use diffusion |
| Arctic multiplier | 1.10–1.30 | Needs calibration against sea ice, shipping, cable/resource projects, and military infrastructure |
| Warning threshold | 3 of 5 rising signals, or 1 theater shock + 2 base signals | Guardrail against single-source false alarms; should be backtested |

## 1년 단위 전망

| Year | Base | Upside | Downside |
|---|---|---|---|
| 2026 | WETD remains a prototype Map Slice: source feeds, signal definitions, and theater exposure tables are created. | Official APIs cover enough rows for transparent monthly scorecards. | Sparse source coverage forces analyst-heavy scoring and weak comparability. |
| 2027 | Semiconductor, sanctions, procurement, and energy feeds support the first country-month WET score. | Corridor watch states expose early route rewiring before policy shocks become visible. | Equal-weight defaults are mistaken for truth and hide uncertainty. |
| 2028 | Theater multipliers begin to show different meanings for the same base signal. | Taiwan, Middle East, and Arctic indicators are audited separately and kept explainable. | One theater dominates the narrative and crowds out cross-theater coupling. |
| 2029 | WETD becomes a repeatable monthly early-warning product with commander notes. | Backtesting separates noisy policy events from durable economic-security transition signals. | Data gaps around EDA, HBM, and dual-use procurement create false confidence. |
| 2030 | Intermediate transition pathways show whether markets are still allocating strategic goods or permission systems are taking over. | Allied redundancy and transparency reduce block-formation risk. | Hoarding and rerouting turn AI compute and semiconductor capacity into bloc-governed resources. |
| 2031 | WETD tracks how capital controls, sanctions, and procurement reinforce each other. | Shared metrics reduce surprise and support de-escalatory transparency. | Access controls expand from goods into compute, cloud, models, and data-center infrastructure. |
| 2032 | The dashboard distinguishes ordinary industrial policy from war-economy transition. | Weight/config revisions become evidence-driven rather than narrative-driven. | Strategic stockpiling and route rewiring become normal enough to escape alarm thresholds. |
| 2033 | Cross-theater comparison reveals whether shocks are local or system-wide. | Corridor audits reduce opaque rerouting and sanctions leakage. | Middle East energy/security shocks compound compute-infrastructure costs. |
| 2034 | WETD becomes a governance checklist for strategic goods transparency and redundancy. | Response concepts are linked to each measured signal, limiting overreaction. | Arctic, energy, cable, and military infrastructure indicators converge into a new escalation lane. |
| 2035 | The model separates observed WET transition from scenario interpretation. | WETD supports targeted buffers without defaulting to full bloc exclusion. | Strategic allocation replaces price allocation across compute, semiconductors, energy, and chokepoints. |

## 2035 전망 요약

**Base.** WETD is a transparent early-warning layer: it measures `Divergence Signal` movement across country-month facts, publishes calibration assumptions, and maps theater exposure without claiming deterministic war prediction.

**Upside.** The same data helps states identify redundancy, corridor transparency, and compute/semiconductor reserve needs early enough to dampen bloc formation.

**Downside.** AI compute, semiconductor tools, energy, minerals, logistics routes, and dual-use procurement behave as one connected economic-security system. Price allocation is gradually replaced by permission allocation, and a shock in one theater can propagate through supply chains before it is legible as military escalation.

## Model discipline

- Present-state facts are source rows or official policy/procurement events.
- Repo inference is the coupling claim that multiple sectors can become one economic-security system.
- 2035 scenarios are conditional narratives, not measurements.
- WET scores must expose signal count, missing signal types, source references, confidence, weights, and theater exposure.

## 정보 출처

- UN Comtrade API documentation: https://comtradeapi.un.org/
- U.S. Census International Trade API: https://www.census.gov/data/developers/data-sets/international-trade.html
- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- Trade.gov Consolidated Screening List API: https://www.trade.gov/consolidated-screening-list
- USAspending API: https://api.usaspending.gov/
- SAM.gov API documentation: https://open.gsa.gov/api/get-opportunities-public-api/
- NSIDC Sea Ice Index: https://nsidc.org/data/seaice_index
- EIA Open Data API: https://www.eia.gov/opendata/
- USGS Mineral Commodity Summaries: https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
