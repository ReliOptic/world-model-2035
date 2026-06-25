# War-Economy Transition Dashboard (WETD) Theater Scenarios

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## Purpose

This file maps the War-Economy Transition Dashboard (WETD) into three theater-level scenarios for the 2026–2035 model period. The framework name is WETD; the scenarios are 2035 outcomes. Each theater uses the same five War-Economy Transition signals but interprets them through a different geopolitical multiplier.

## 연결 문서

- [wetd_2035_scope.md](wetd_2035_scope.md) — scope, signals, calibration hypotheses, and annual War-Economy Transition Dashboard forecast.
- [wetd_data_schema.md](wetd_data_schema.md) — tables that keep theater exposure, weights, and source references auditable.
- [wetd_etl_dashboard_contract.md](wetd_etl_dashboard_contract.md) — monthly ETL/dashboard contract.
- [CONTEXT.md](../CONTEXT.md) — `Coupling Map`, `Map Slice`, `Divergence Signal`, and scenario terminology.
- [../19_logistics_and_trade/supply_chain_fragmentation.md](../19_logistics_and_trade/supply_chain_fragmentation.md) — route-rewiring anchor.

## 2026년 4월 현재 상태

**Present-state source-backed facts.** The theater layer should use official trade, policy, procurement, sanctions, sea-ice, energy, and minerals sources listed below. Taiwan Strait evidence must separate semiconductor production/tooling concentration from sovereignty narrative. Middle East evidence must separate energy, sanctions, and dual-use procurement. Arctic evidence must separate physical access, route use, infrastructure, and military procurement.

**Repo inference.** A theater is not a product category. It is a multiplier over the strategic meaning of otherwise ordinary rows: a trade anomaly, procurement award, sanctions row, or sea-ice metric becomes more important when it aligns with a theater exposure table.

**Scenario boundary.** The downside cases below are conditional 2035 narratives. They do not assert that a theater conflict is inevitable.

## Scenario method

| Layer | Meaning | Evidence discipline |
|---|---|---|
| 2026 observable base | Current measurable row or official policy/procurement event | Source row with URL and retrieved date |
| Early-warning signal | One of the five War-Economy Transition signals moves | Score row with source_row_refs and confidence |
| 2030 transition pathway | Plausible intermediate state | Repo inference, marked separately from facts |
| 2035 scenario | Base/Upside/Downside outcome | Scenario, not measurement |

## Theater 1: Taiwan Strait

### 2026 observable base

Taiwan is treated as a semiconductor keystone theater, not only as a sovereignty risk. The monitored system includes Taiwan, China, United States, South Korea, Japan, Netherlands, and European Union exposure to HBM, AI accelerators, semiconductor equipment, EUV/metrology, EDA proxy, advanced packaging, and shipping/insurance stress.

### Early-warning signals

| War-Economy Transition signal | Taiwan Strait indicator candidates |
|---|---|
| Autarky | Semiconductor self-reliance programs intensify in China, US, Japan, Korea, EU, and Taiwan |
| Strategic stockpiling | HBM, memory IC, GPU, AI-server, and semiconductor-equipment imports rise above demand proxies |
| Trade rewiring | Taiwan-linked semiconductor flows shift toward Singapore, Malaysia, Vietnam, Japan, or Korea routes |
| Capital and access control | AI-chip, EDA, semiconductor-equipment, and foundry-service access controls expand |
| Civilian-to-military allocation | Secure compute, hardened fabs, defense microelectronics, and protected supply programs rise |

### Response concept

- Build allied compute and semiconductor redundancy metrics.
- Track Taiwan exposure separately from China exposure.
- Treat Korea, Japan, Netherlands, and Taiwan as a single production-tooling-metrology dependency graph.
- Include corridor watch states in every Taiwan Strait run.

## Theater 2: Middle East

### 2026 observable base

The Middle East theater links energy shocks, sanctions, dual-use AI and defense technology, drone/missile procurement, cyber capabilities, and compute investment. Israel is modeled as a dual-use AI/defense node; Iran is modeled as a sanctioned procurement and escalation node. UAE, Saudi Arabia, Qatar, and Turkey act as corridor, capital, energy, logistics, or defense-industrial connectors.

### Early-warning signals

| War-Economy Transition signal | Middle East indicator candidates |
|---|---|
| Autarky | Iran and regional actors expand domestic substitutes; Gulf states pursue sovereign AI infrastructure |
| Strategic stockpiling | Oil, LNG, critical components, drone/missile inputs, and compute capacity show abnormal accumulation |
| Trade rewiring | UAE, Turkey, China, and other corridors show mirror-trade gaps around dual-use electronics |
| Capital and access control | OFAC, EU, UN, BIS, and CSL sanctions/control events rise; AI-chip and cloud controls become region-specific |
| Civilian-to-military allocation | AI, cyber, ISR, air defense, drones, secure cloud, and command-and-control procurement rise |

### Response concept

- Separate Israel as a dual-use capability node and Iran as a sanctioned procurement node.
- Monitor UAE and Turkey as high-priority corridor states.
- Link energy shock indicators to compute-infrastructure costs.
- Add dual-use procurement networks to the same dashboard as trade and sanctions events.

## Theater 3: Arctic

### 2026 observable base

The Arctic theater is a spatial multiplier: lower sea ice, ship traffic, resource access, military infrastructure, undersea cables, ISR, and great-power presence can change the strategic meaning of otherwise normal energy and logistics indicators.

### Early-warning signals

| War-Economy Transition signal | Arctic indicator candidates |
|---|---|
| Autarky | Arctic states frame energy, ports, cables, and minerals as sovereign infrastructure |
| Strategic stockpiling | Energy, critical minerals, ice-class vessels, radar, and communications assets receive abnormal investment |
| Trade rewiring | Arctic routes and polar-adjacent ports gain shipping share |
| Capital and access control | Arctic mining, port, cable, LNG, and data infrastructure face foreign-investment screening |
| Civilian-to-military allocation | Icebreakers, radar, ISR, northern bases, satellites, and undersea infrastructure protection expand |

### Response concept

- Treat Arctic as a theater multiplier, not a normal sector.
- Track sea-ice access, vessel traffic, resource projects, military procurement, and infrastructure screening together.
- Do not fold Arctic into the energy signal alone.

## 1년 단위 전망

| Year | Base | Upside | Downside |
|---|---|---|---|
| 2026 | Three theater definitions and exposure tables are drafted as WETD hypotheses. | The theater layer remains transparent about source-backed facts versus repo inference. | Multipliers are mistaken for measured probabilities. |
| 2027 | Taiwan, Middle East, and Arctic source feeds start producing monthly theater notes. | Missing data is explicit, reducing false precision. | Sparse feeds push analysts toward narrative scoring. |
| 2028 | Theater exposure begins changing how country-month War-Economy Transition scores are interpreted. | Taiwan semiconductor, Middle East energy/sanctions, and Arctic spatial variables stay separable. | One theater storyline crowds out cross-theater comparison. |
| 2029 | Corridor-state evidence improves route-rewiring detection. | Early corridor anomalies trigger audit, not automatic escalation. | Re-export and mirror-trade gaps become opaque enough to weaken controls. |
| 2030 | Intermediate pathways show whether strategic goods remain market-allocated or permission-allocated. | Redundancy investments reduce Taiwan Strait compute shock severity. | AI compute hoarding and emergency allocation become normalized. |
| 2031 | Middle East procurement, sanctions, energy, and compute signals are read as one coupled system when evidence supports it. | Sanctions analytics and corridor audits limit leakage. | Dual-use supply chains split into opaque blocs. |
| 2032 | Arctic route and infrastructure signals are separated from generic energy monitoring. | Governance catches cable, port, and resource-risk buildup early. | Polar access competition becomes a persistent military-economic risk lane. |
| 2033 | Cross-theater compression becomes measurable through simultaneous signal movement. | WETD supports targeted buffers and avoids broad exclusion. | Energy, compute, and defense-procurement shocks reinforce each other. |
| 2034 | Theater notes become scenario-maintenance records rather than one-off essays. | Calibration reviews reduce overreaction to single events. | Theater multipliers rise faster than institutions can verify. |
| 2035 | WETD can explain which theater changed a War-Economy Transition score and why. | Transparency creates de-escalatory response concepts. | Three-theater compression turns compute, energy, routes, and dual-use tech into strategic allocation systems. |

## 2035 전망 요약

**Base.** WETD treats theaters as explicit multipliers over source-backed economic-security signals. Taiwan Strait, Middle East, and Arctic remain separate lenses with shared data discipline.

**Upside.** Theater-specific transparency allows redundancy, corridor audits, and Arctic governance to reduce escalation before shocks become systemic.

**Downside.** Taiwan Strait compute scarcity, Middle East energy/sanctions volatility, and Arctic route/resource militarization compress into one war-economy transition pattern. The result is not one event but a shift from commercial allocation to strategic permission allocation.

## 정보 출처

- UN Comtrade API documentation: https://comtradeapi.un.org/
- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- Trade.gov Consolidated Screening List API: https://www.trade.gov/consolidated-screening-list
- USAspending API: https://api.usaspending.gov/
- SAM.gov API documentation: https://open.gsa.gov/api/get-opportunities-public-api/
- NSIDC Sea Ice Index: https://nsidc.org/data/seaice_index
- EIA Open Data API: https://www.eia.gov/opendata/
- USGS Mineral Commodity Summaries: https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
