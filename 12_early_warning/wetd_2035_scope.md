# WETD-2035 Scope and Theater Framework

Status: 🟢 Drafted 2026-06-25

## Purpose

WETD-2035 is a **War-Economy Transition Dashboard** for the 2026-2035 world-model period.

The dashboard does **not** attempt to predict war directly. Its purpose is to detect whether a market-based peacetime economy is shifting toward a war-economy configuration: strategic self-reliance, stockpiling, route rewiring, access controls, sanctions adaptation, and national-security allocation of civilian technology.

## Core claim

By 2035, AI compute, semiconductor manufacturing capacity, energy, critical minerals, grid equipment, data-center cooling, Arctic access, sanctions networks, and dual-use defense AI may behave as one connected economic-security system. A conflict signal will often appear first as an economic coordination pattern rather than as a direct military signal.

## Commander's intent

Build a monthly early-warning system that tracks:

1. which countries are moving strategic technology and resources out of open markets;
2. which chokepoints are becoming national-security allocation points;
3. which transit states are becoming rerouting corridors;
4. which theaters multiply otherwise-normal economic stress into strategic risk; and
5. how present-state signals map to 2035 downside scenarios and response options.

## Minimum data MVP scope

### Primary monitored actors

| Group | Countries / areas | Role in model |
|---|---|---|
| Core powers | United States, China, Russia | AI, military, sanctions, energy, and war-economy transition centers |
| G7 / advanced-economy bloc | United States, Japan, Germany, United Kingdom, France, Italy, Canada, European Union | Rulemaking, export controls, sanctions, industrial policy, financial controls |
| Frontline tech allies | Taiwan, South Korea, Japan, Germany / European Union, Netherlands | Leading-edge semiconductors, memory, tools, EUV, metrology, and industrial equipment chokepoints |
| Added MVP actors | Taiwan, South Korea, Netherlands | Required because G7 alone misses the semiconductor production and EUV/tooling bottleneck |

The minimum implementation set is:

```text
United States
China
Russia
Japan
Germany
United Kingdom
France
Italy
Canada
European Union
Taiwan
South Korea
Netherlands
```

### Corridor watch states

| Corridor | Why it is monitored |
|---|---|
| Taiwan | Production chokepoint and theater risk sensor |
| Singapore | Finance, logistics, data-center, and high-value transshipment hub |
| Malaysia | Semiconductor assembly, test, electronics, and rerouting candidate |
| United Arab Emirates | Finance, compute, energy, and sanctions-rerouting corridor |
| Vietnam | Friend-shoring, electronics production relocation, and third-country route candidate |

Corridor watch states are not treated only as countries. They are **sensors for route rewiring**: re-export, indirect procurement, mirror-trade gaps, sanctions adaptation, and supply-chain rerouting.

## Strategic goods scope

### AI and semiconductor-centered goods

| Category | What to track | Measurement approach |
|---|---|---|
| HBM / high-bandwidth memory proxy | Memory ICs, high-performance DRAM trade, AI server memory exposure | HS-code proxy, company-level policy events, export-control language |
| GPU / AI accelerator proxy | Servers, accelerators, high-performance computing systems | HS-code proxy plus export-control and procurement keywords |
| Semiconductor equipment | Wafer fab equipment, lithography, deposition, etch, inspection | HS 8486 and related machinery categories |
| EUV and metrology | Lithography, inspection, optical measurement, precision instruments | Equipment HS categories plus policy-event tagging |
| EDA proxy | Design software, IP licensing, semiconductor design workflow controls | Policy-event, sanctions, export-control, and procurement keyword proxy |

### War-economy-centered goods

| Category | Why it matters |
|---|---|
| Energy | Compute and industry depend on oil, LNG, electricity, and grid stability |
| Rare earths | Defense, electronics, motors, and strategic equipment inputs |
| Copper | Grid, data-center, defense, and electrification bottleneck |
| Power equipment | Transformers, grid equipment, and high-load data-center enablement |
| Data-center cooling | Liquid cooling, HVAC, and heat rejection as compute capacity constraints |

## Five WET signals

| Signal | Core question | Typical evidence |
|---|---|---|
| Autarky | Is the country reducing dependence on open-market supply? | Import dependence decline, subsidy events, technical-sovereignty language |
| Strategic stockpiling | Is the country buying or storing strategic goods despite weak economic logic? | Import volume anomaly, stock-to-use increase, price-insensitive buying |
| Trade rewiring | Are direct routes being replaced by third-country or trusted-corridor routes? | Mirror-trade gaps, corridor-state import/export surges, partner-share shifts |
| Capital and access control | Is market access being replaced by national permission? | FDI screening, sanctions, Entity List entries, compute/API/model restrictions |
| Civilian-to-military allocation | Are civilian technologies moving into defense or intelligence priority allocation? | Defense AI procurement, secure cloud contracts, ISR/C2/autonomy spending |

Base WET Score should initially weight these five signals equally. The equal weighting is a design default, not a claim that each signal has identical causal force.

```text
Base WET Score =
20% Autarky
+ 20% Strategic Stockpiling
+ 20% Trade Rewiring
+ 20% Capital and Access Control
+ 20% Civilian-to-Military Allocation
```

## Theater structure

WETD-2035 uses three theater scenarios. Theater variables are not ordinary commodities. They multiply the risk meaning of the same base signal.

### 1. Taiwan Strait theater

Taiwan is an independent theater, not merely an ally entry in the country table.

| Field | Model treatment |
|---|---|
| Role | Semiconductor keystone theater |
| Main risk | Leading-edge semiconductor production chokepoint and AI-compute supply shock |
| Relevant actors | Taiwan, China, United States, South Korea, Japan, Netherlands, European Union |
| Relevant goods | HBM, GPU, AI servers, semiconductor equipment, EUV, metrology, EDA proxy |
| Theater multiplier | 1.2-1.5 initial placeholder |

The Taiwan Strait multiplier should rise when semiconductor trade concentration, export controls, military exercises, shipping disruption, or emergency stockpiling rise together.

### 2. Middle East theater

The Middle East theater is split into role-specific nodes:

| Node | Model role |
|---|---|
| Israel | Dual-use AI / Defense Node |
| Iran | Sanctioned Procurement and Escalation Node |
| United Arab Emirates | Finance, compute, energy, and re-export corridor |
| Saudi Arabia / Qatar | Energy and AI-infrastructure capital nodes |
| Turkey | Defense-industrial and logistics corridor |

| Field | Model treatment |
|---|---|
| Main risk | Energy shock, sanctions bypass, drone/missile procurement, cyber/AI defense diffusion |
| Relevant goods | Energy, dual-use electronics, AI compute, UAV/missile components, secure cloud |
| Theater multiplier | 1.1-1.4 initial placeholder |

### 3. Arctic theater

The Arctic is a spatial multiplier, not a normal commodity bucket.

| Field | Model treatment |
|---|---|
| Role | Polar Strategic Theater |
| Main risk | Sea-route opening, resource access, military presence, undersea infrastructure, ISR |
| Relevant actors | United States, Canada, Denmark / Greenland, Norway, Iceland, Finland, Sweden, Russia, China as near-Arctic actor |
| Relevant variables | Sea ice, shipping activity, resource claims, military procurement, ports, cables, energy infrastructure |
| Theater multiplier | 1.1-1.3 initial placeholder |

The Arctic multiplier should not be buried inside the energy indicator. It is a spatial risk amplifier that changes the strategic meaning of energy, shipping, minerals, and military access.

## Theater-adjusted score

```text
Final WET Score = Base WET Score × Theater Multiplier
```

The first implementation should compute:

1. Base WET Score by country-month;
2. theater multiplier by theater-month;
3. theater-adjusted score for countries and goods exposed to the relevant theater; and
4. a qualitative commander note explaining why the score moved.

## 2035 scenario table contract

Every monthly dashboard should update a companion table:

| 2026 signal | 2030 transition pathway | 2035 downside | Response concept |
|---|---|---|---|
| Taiwan dependence remains concentrated | Allied relocation and redundancy fail to absorb shock | AI-compute block formation | Allied compute and semiconductor redundancy pool |
| HBM / GPU buying surges despite high prices | National compute hoarding begins | Foundation-model capability gap hardens | Compute reserve and allocation transparency |
| Corridor re-export patterns grow | Sanctions and export controls lose enforcement power | Dual-use supply chain splits into opaque blocs | Mirror-trade detection and corridor audits |
| Iran procurement networks expand | Dual-use components diffuse through rerouting states | Middle East energy and defense-tech shock combine | Sanctions analytics plus chokepoint monitoring |
| Arctic access rises with military presence | Shipping, resource, and ISR competition grow | Polar theater becomes a military-economic escalation zone | Arctic route, cable, and resource governance |

## Model discipline

The dashboard must distinguish:

- official present-state data;
- inferred signal scores;
- theater multipliers;
- 2035 scenarios; and
- recommended response concepts.

A signal is not an alarm by itself. A WET warning should require either:

1. at least three of five WET signals rising together; or
2. one major theater multiplier shock plus two rising base signals.

## Known failure modes

| Failure mode | Mitigation |
|---|---|
| Overbroad geopolitical scope | Keep MVP to defined actors, corridors, goods, and three theaters |
| Treating all stockpiling as war preparation | Compare against demand, price, and industrial output proxies |
| Confusing sanctions compliance with escalation | Separate policy-event count from trade rerouting effect |
| Overweighting official military data | Use military/procurement data only as one of five signals |
| Hiding assumptions in the score | Publish score components and confidence for each country-month |

## 정보 출처

- Repository principle: every forecast must distinguish present-state facts from 2035 scenarios; see `README.md`.
- UN Comtrade API documentation: https://comtradeapi.un.org/
- U.S. Census International Trade API: https://www.census.gov/data/developers/data-sets/international-trade.html
- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- Trade.gov Consolidated Screening List API: https://www.trade.gov/consolidated-screening-list
- USAspending API: https://api.usaspending.gov/
- SAM.gov API documentation: https://open.gsa.gov/api/get-opportunities-public-api/
- NSIDC Sea Ice Index: https://nsidc.org/data/seaice_index
- EIA Open Data API: https://www.eia.gov/opendata/
- USGS Mineral Commodity Summaries: https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
