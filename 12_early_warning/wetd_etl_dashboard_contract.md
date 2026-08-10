# WETD-2035 ETL and Dashboard Contract

Status: 🟢 Drafted 2026-06-25

## Purpose

This document defines the first monthly ETL and dashboard contract for WETD-2035. It turns the WETD scope into implementation work without overbuilding the system.

The first implementation should be a monthly analytical dashboard, not a real-time alerting platform.

## Data-source priority

| Priority | Source class | Examples | Use |
|---|---|---|---|
| A | Official APIs | UN Comtrade, U.S. Census, Federal Register, Trade.gov CSL, USAspending, EIA | Primary quantitative and event data |
| B | Official downloads | USGS minerals, NSIDC Sea Ice Index, national statistics | Monthly or annual supporting data |
| C | Specialized monitoring databases | Global Trade Alert, WTO I-TIP, OECD.AI | Policy-event enrichment |
| D | News and market commentary | Financial press, analyst notes | Context only; not score input without corroboration |

## MVP data pipelines

### Pipeline 1: Strategic goods trade

| Field | Value |
|---|---|
| Main sources | UN Comtrade API, U.S. Census International Trade API, Eurostat where needed |
| Refresh cadence | Monthly |
| Key products | HBM proxy, GPU/AI accelerator proxy, semiconductor equipment, EUV/metrology proxy, EDA proxy, energy, rare earths, copper, power equipment, data-center cooling |
| Main outputs | `fact_trade`, import dependence, supplier HHI, direct/indirect route ratio, mirror-trade gap |
| Signals fed | Autarky, stockpiling, trade rewiring |

Starter product mapping:

| Product | Proxy approach |
|---|---|
| HBM | Memory IC proxy plus policy-event tagging |
| GPU / AI accelerator | Server / computing equipment proxy plus export-control tagging |
| Semiconductor equipment | Semiconductor machinery categories |
| EUV / metrology | Lithography, inspection, and measuring-equipment categories plus policy tagging |
| EDA | Export-control and software-policy keyword proxy |
| Energy | Oil, gas, LNG, electricity, uranium proxy where available |
| Rare earths | Rare-earth metals and compounds |
| Copper | Copper ores, refined copper, copper articles as needed |
| Power equipment | Transformers and grid equipment proxies |
| Data-center cooling | Cooling, HVAC, and liquid-cooling keyword/proxy categories |

### Pipeline 2: Policy, sanctions, and access controls

| Field | Value |
|---|---|
| Main sources | Federal Register API, Trade.gov CSL, OFAC/EU lists if added, OECD FDIRRI, OECD.AI |
| Refresh cadence | Monthly, with event-date preservation |
| Main outputs | `fact_policy_event`, `fact_sanctions`, policy keyword counts, restricted entity growth |
| Signals fed | Capital and access control, autarky, civilian-to-military allocation |

Keyword seed list:

```text
advanced computing
artificial intelligence
AI accelerator
GPU
high-bandwidth memory
HBM
semiconductor manufacturing equipment
EUV
lithography
metrology
EDA
model weights
cloud computing
data center
export control
Entity List
foreign direct investment
sanctions
UAV
missile
cyber
secure cloud
```

### Pipeline 3: Public procurement and military allocation

| Field | Value |
|---|---|
| Main sources | USAspending API, SAM.gov API, TED for EU, UK Contracts Finder if needed |
| Refresh cadence | Monthly |
| Main outputs | `fact_procurement`, defense AI procurement share, compute militarization ratio |
| Signals fed | Civilian-to-military allocation, capital and access control |

Keyword seed list:

```text
artificial intelligence
machine learning
foundation model
GPU
accelerator
HPC
cloud
data center
semiconductor
microelectronics
advanced packaging
ISR
command and control
C2
autonomous systems
cyber
secure cloud
classified
```

### Pipeline 4: Energy, minerals, and infrastructure inputs

| Field | Value |
|---|---|
| Main sources | EIA Open Data API, FRED, USGS Mineral Commodity Summaries, JODI where available |
| Refresh cadence | Monthly where possible; annual for some minerals |
| Main outputs | `fact_energy_minerals`, price-insensitive buying, stock-to-use proxy |
| Signals fed | Stockpiling, autarky, theater multipliers |

### Pipeline 5: Arctic spatial multiplier

| Field | Value |
|---|---|
| Main sources | NSIDC Sea Ice Index, Arctic ship traffic datasets, official procurement and defense documents |
| Refresh cadence | Monthly for sea ice; monthly/quarterly for shipping and procurement |
| Main outputs | `fact_arctic_access`, Arctic accessibility index, Arctic multiplier |
| Signals fed | Theater multiplier, trade rewiring, civilian-to-military allocation |

The Arctic pipeline must remain separate from ordinary energy monitoring. Arctic data modifies the strategic meaning of energy, shipping, cables, military infrastructure, and route access.

## Score-computation workflow

```text
1. Ingest raw API/download rows.
2. Normalize country, product, corridor, and theater keys.
3. Map goods and keywords to strategic product IDs.
4. Compute source-level metrics.
5. Convert metrics to 0-100 signal scores.
6. Compute country-month Base WET Score.
7. Compute theater-month multipliers.
8. Produce Final WET Score.
9. Update 2035 scenario mapping rows.
10. Generate commander note and dashboard export.
```

## Initial signal calculations

### Autarky signal

Candidate components:

```text
- import-dependence reduction for strategic goods
- supplier concentration HHI
- subsidy / industrial-policy event count
- technical-sovereignty keyword count
```

Interpretation rule:

Autarky rises when import dependence falls while policy events, subsidies, and sovereignty language rise. A plain import decline without policy backing may reflect recession rather than strategic self-reliance.

### Strategic stockpiling signal

Candidate components:

```text
- import volume z-score
- import value z-score
- price-insensitive buying score
- stock-to-use ratio where available
```

Interpretation rule:

Stockpiling risk rises when volume or inventory rises despite high prices or weak industrial-output demand proxies.

### Trade rewiring signal

Candidate components:

```text
- direct trade decline between restricted pairs
- corridor-state import and export surge in same product class
- mirror-trade gap
- partner-share entropy shift
```

Interpretation rule:

Trade rewiring is strongest when a direct route declines while an indirect corridor route rises in the same strategic product category.

### Capital and access control signal

Candidate components:

```text
- new restricted entities
- export-control event count
- FDI restrictiveness change
- compute/cloud/model-weight access-control event count
```

Interpretation rule:

Access-control risk rises when restrictions move from physical goods into compute access, cloud access, model weights, EDA, or data-center infrastructure.

### Civilian-to-military allocation signal

Candidate components:

```text
- defense AI procurement share
- secure-cloud and high-performance-compute procurement
- microelectronics and advanced packaging procurement
- ISR/C2/autonomy/cyber keyword spend
```

Interpretation rule:

Allocation risk rises when civilian compute, semiconductor, data-center, or AI capabilities become explicitly defense, intelligence, or national-security procurement priorities.

## Dashboard pages

### Page 1: Executive WET map

Required elements:

- country-month WET score;
- theater-adjusted WET score;
- top five movers month-over-month;
- highest-confidence signals;
- commander note.

### Page 2: Strategic goods monitor

Required elements:

- HBM/GPU/semiconductor equipment/EUV-metrology/EDA proxy panel;
- energy/rare earth/copper/power equipment/cooling panel;
- import dependence and supplier concentration views;
- stockpiling anomaly view.

### Page 3: Corridor watch

Required elements:

- Taiwan, Singapore, Malaysia, UAE, and Vietnam corridor rows;
- direct versus indirect route ratios;
- mirror-trade gap flags;
- China-, Russia-, Iran-, and Taiwan-linked route patterns.

### Page 4: Policy and access-control timeline

Required elements:

- export controls;
- sanctions and restricted entities;
- FDI restrictions;
- AI chip / cloud / model / data-center controls;
- event severity labels.

### Page 5: Theater scenarios

Required elements:

- Taiwan Strait multiplier;
- Middle East multiplier;
- Arctic multiplier;
- scenario table mapping 2026 signal to 2030 pathway and 2035 downside.

## Alerting rule draft

A country or theater should move from Watch to Warning when either condition holds:

```text
Condition A:
At least three of five WET signals rise above their trailing 24-month mean by 2 standard deviations.

Condition B:
One theater multiplier increases materially and at least two WET signals are above threshold.
```

The first implementation should show the condition state but avoid automated claims like "war likely." Use language such as:

- Normal
- Watch
- Warning
- Severe
- Crisis

## Monthly output package

Each monthly run should create:

1. `wet_score_country_month.csv`
2. `wet_signal_components.csv`
3. `theater_multipliers.csv`
4. `corridor_watch_flags.csv`
5. `policy_event_log.csv`
6. `procurement_signal_log.csv`
7. `arctic_access_metrics.csv`
8. `2035_response_table.md`
9. `commander_note.md`

## Non-goals for MVP

- No real-time alerting.
- No classified data assumption.
- No single-number war prediction.
- No unsourced LLM-only scoring.
- No collapsing Taiwan into China or EU into Germany.
- No treating Arctic as a normal commodity group.

## Acceptance checklist

- [ ] All data rows preserve source and retrieval date.
- [ ] Every WET score decomposes into five signal components.
- [ ] Taiwan, Middle East, and Arctic appear as separate theater objects.
- [ ] Taiwan, Singapore, Malaysia, UAE, and Vietnam appear in corridor watch.
- [ ] HBM/GPU/equipment/EUV-metrology/EDA proxy and energy/rare-earth/copper/power/cooling goods are included.
- [ ] The dashboard exports both a monthly score view and a 2035 response table.
- [ ] Present facts are separated from scenario assumptions.

## 정보 출처

- UN Comtrade API documentation: https://comtradeapi.un.org/
- U.S. Census International Trade API: https://www.census.gov/data/developers/data-sets/international-trade.html
- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- Trade.gov Consolidated Screening List API: https://www.trade.gov/consolidated-screening-list
- USAspending API: https://api.usaspending.gov/
- SAM.gov API documentation: https://open.gsa.gov/api/get-opportunities-public-api/
- TED API documentation: https://ted.europa.eu/en/api
- EIA Open Data API: https://www.eia.gov/opendata/
- NSIDC Sea Ice Index: https://nsidc.org/data/seaice_index
- USGS Mineral Commodity Summaries: https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries
- OECD FDI Regulatory Restrictiveness Index: https://www.oecd.org/en/topics/sub-issues/sustainable-investment/fdi-regulatory-restrictiveness-index.html
