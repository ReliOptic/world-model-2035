# WETD-2035 Data Schema

Status: 🟢 Drafted 2026-06-25

## Purpose

This file defines the data contract for a monthly War-Economy Transition Dashboard. It is designed to support a first implementation using official or high-reliability APIs and public datasets.

The implementation goal is not a black-box war predictor. It is an auditable, source-linked dashboard that converts country, product, corridor, theater, policy, procurement, and physical-access data into monthly WET signal scores.

## Design principles

1. Use official or primary sources first.
2. Store raw source fields before scoring.
3. Separate observed data from inferred signal scores.
4. Separate base WET signals from theater multipliers.
5. Preserve a 2026-present fact layer and a 2035 scenario-mapping layer.
6. Every computed score must be decomposable into source rows.

## Minimum entity model

```text
dim_country
├─ dim_theater
├─ dim_product
├─ dim_corridor
├─ fact_trade
├─ fact_policy_event
├─ fact_sanctions
├─ fact_procurement
├─ fact_energy_minerals
├─ fact_arctic_access
├─ fact_wet_signal_score
├─ fact_theater_multiplier
└─ fact_2035_scenario_mapping
```

## Dimension tables

### dim_country

| Field | Type | Required | Notes |
|---|---|---:|---|
| country_iso3 | string | yes | ISO-3 country or pseudo-code for EU |
| country_name | string | yes | Canonical display name |
| country_group | enum | yes | core_power, g7_advanced_bloc, frontline_tech_ally, corridor_watch, sanctioned_adaptation, middle_east_node, polar_actor |
| alliance_status | string | no | model-specific grouping, not a legal claim |
| is_mvp_country | boolean | yes | true for MVP countries |
| notes | text | no | explanatory notes |

Initial rows:

```csv
country_iso3,country_name,country_group,is_mvp_country
USA,United States,core_power,true
CHN,China,core_power,true
RUS,Russia,core_power,true
JPN,Japan,g7_advanced_bloc,true
DEU,Germany,g7_advanced_bloc,true
GBR,United Kingdom,g7_advanced_bloc,true
FRA,France,g7_advanced_bloc,true
ITA,Italy,g7_advanced_bloc,true
CAN,Canada,g7_advanced_bloc,true
EUU,European Union,g7_advanced_bloc,true
TWN,Taiwan,frontline_tech_ally,true
KOR,South Korea,frontline_tech_ally,true
NLD,Netherlands,frontline_tech_ally,true
SGP,Singapore,corridor_watch,false
MYS,Malaysia,corridor_watch,false
ARE,United Arab Emirates,corridor_watch,false
VNM,Vietnam,corridor_watch,false
IRN,Iran,middle_east_node,false
ISR,Israel,middle_east_node,false
```

### dim_theater

| Field | Type | Required | Notes |
|---|---|---:|---|
| theater_id | string | yes | taiwan_strait, middle_east, arctic |
| theater_name | string | yes | Display name |
| theater_type | enum | yes | keystone, escalation_belt, spatial_multiplier |
| default_multiplier_low | decimal | yes | Initial multiplier lower bound |
| default_multiplier_high | decimal | yes | Initial multiplier upper bound |
| primary_risk | text | yes | Short description |

Initial rows:

```csv
theater_id,theater_name,theater_type,default_multiplier_low,default_multiplier_high
taiwan_strait,Taiwan Strait,keystone,1.2,1.5
middle_east,Middle East,escalation_belt,1.1,1.4
arctic,Arctic,spatial_multiplier,1.1,1.3
```

### dim_product

| Field | Type | Required | Notes |
|---|---|---:|---|
| product_id | string | yes | Stable slug |
| product_group | enum | yes | ai_semiconductor, war_economy |
| product_name | string | yes | Display name |
| hs_codes | array | no | HS-code proxies where available |
| proxy_method | enum | yes | hs_code, policy_keyword, procurement_keyword, mixed_proxy |
| ai_relevance_score | integer | no | 1-5 qualitative score |
| war_economy_relevance_score | integer | no | 1-5 qualitative score |
| notes | text | no | Limits of the proxy |

Initial product seed:

```csv
product_id,product_group,product_name,proxy_method
hbm_proxy,ai_semiconductor,HBM / high-bandwidth memory proxy,mixed_proxy
gpu_ai_accelerator_proxy,ai_semiconductor,GPU / AI accelerator proxy,mixed_proxy
semiconductor_equipment,ai_semiconductor,Semiconductor equipment,hs_code
euv_metrology_proxy,ai_semiconductor,EUV and metrology proxy,mixed_proxy
eda_proxy,ai_semiconductor,EDA proxy,policy_keyword
energy,war_economy,Energy,mixed_proxy
rare_earths,war_economy,Rare earths,hs_code
copper,war_economy,Copper,hs_code
power_equipment,war_economy,Power equipment,hs_code
data_center_cooling,war_economy,Data-center cooling,mixed_proxy
```

### dim_corridor

| Field | Type | Required | Notes |
|---|---|---:|---|
| corridor_id | string | yes | Stable slug |
| country_iso3 | string | yes | ISO-3 country |
| corridor_role | enum | yes | production_chokepoint, finance_logistics, semiconductor_backend, compute_energy, friendshoring |
| watched_for | text | yes | What rerouting behavior to monitor |

Initial rows:

```csv
corridor_id,country_iso3,corridor_role
corridor_taiwan,TWN,production_chokepoint
corridor_singapore,SGP,finance_logistics
corridor_malaysia,MYS,semiconductor_backend
corridor_uae,ARE,compute_energy
corridor_vietnam,VNM,friendshoring
```

## Fact tables

### fact_trade

Source examples: UN Comtrade, U.S. Census International Trade API, Eurostat, IMF trade data.

| Field | Type | Required | Notes |
|---|---|---:|---|
| date_month | date | yes | Month bucket |
| reporter_iso3 | string | yes | Reporting country |
| partner_iso3 | string | yes | Partner country |
| flow | enum | yes | import, export, re_export if available |
| hs_code | string | yes | HS code |
| product_id | string | no | mapped strategic product |
| value_usd | decimal | yes | USD value |
| quantity | decimal | no | physical quantity if available |
| quantity_unit | string | no | unit |
| source_name | string | yes | source system |
| source_url | text | yes | query or source URL |
| retrieved_at | timestamp | yes | ingestion time |

Derived fields should not be stored here. Store them in signal tables.

### fact_policy_event

Source examples: Federal Register, WTO I-TIP, OECD.AI, official ministry releases, Global Trade Alert as secondary source.

| Field | Type | Required | Notes |
|---|---|---:|---|
| event_date | date | yes | publication or effective date |
| country_iso3 | string | yes | issuing country/authority |
| agency | string | no | agency or ministry |
| event_type | enum | yes | export_control, subsidy, fdi_screening, data_center_rule, ai_policy, sanctions_policy, industrial_policy |
| title | text | yes | event title |
| summary | text | no | short normalized summary |
| affected_products | array | no | mapped dim_product IDs |
| affected_countries | array | no | target countries |
| keywords | array | yes | normalized keywords |
| severity_hint | integer | no | 1-5 analyst label, not final score |
| source_url | text | yes | official source URL |
| retrieved_at | timestamp | yes | ingestion time |

### fact_sanctions

Source examples: Trade.gov Consolidated Screening List, OFAC, EU consolidated sanctions list.

| Field | Type | Required | Notes |
|---|---|---:|---|
| listed_date | date | no | date listed if available |
| entity_name | string | yes | restricted party |
| country_iso3 | string | no | associated country |
| list_source | string | yes | CSL, OFAC SDN, BIS Entity List, EU list, etc. |
| program | string | no | sanctions/export-control program |
| reason | text | no | listed reason if available |
| product_tags | array | no | AI, semiconductor, UAV, missile, energy, etc. |
| source_url | text | yes | source API or record URL |
| retrieved_at | timestamp | yes | ingestion time |

### fact_procurement

Source examples: USAspending, SAM.gov, TED, UK Contracts Finder.

| Field | Type | Required | Notes |
|---|---|---:|---|
| award_or_notice_date | date | yes | award or notice date |
| country_iso3 | string | yes | procurement country |
| agency | string | yes | buying agency |
| supplier | string | no | awardee if available |
| value_usd | decimal | no | normalized value |
| title | text | yes | notice or award title |
| description | text | no | text for keyword tagging |
| defense_flag | boolean | yes | derived keyword/agency flag |
| ai_compute_flag | boolean | yes | derived keyword flag |
| product_tags | array | no | mapped strategic goods |
| source_name | string | yes | source system |
| source_url | text | yes | source URL |
| retrieved_at | timestamp | yes | ingestion time |

### fact_energy_minerals

Source examples: EIA, JODI, FRED, USGS, national statistical agencies.

| Field | Type | Required | Notes |
|---|---|---:|---|
| date_month | date | yes | Month bucket |
| country_iso3 | string | yes | country |
| commodity | string | yes | oil, LNG, copper, rare_earths, etc. |
| metric_name | string | yes | inventory, production, import, price, stock_to_use, etc. |
| value | decimal | yes | measured value |
| unit | string | yes | unit |
| source_name | string | yes | source system |
| source_url | text | yes | source URL |
| retrieved_at | timestamp | yes | ingestion time |

### fact_arctic_access

Source examples: NSIDC Sea Ice Index, Arctic ship traffic datasets, official defense/procurement data.

| Field | Type | Required | Notes |
|---|---|---:|---|
| date_month | date | yes | Month bucket |
| arctic_zone | string | no | route or zone if available |
| metric_name | string | yes | sea_ice_extent, sea_ice_anomaly, ship_count, icebreaker_procurement, radar_procurement |
| value | decimal | yes | measured value |
| unit | string | yes | unit |
| source_name | string | yes | source system |
| source_url | text | yes | source URL |
| retrieved_at | timestamp | yes | ingestion time |

## Scoring tables

### fact_wet_signal_score

| Field | Type | Required | Notes |
|---|---|---:|---|
| date_month | date | yes | Month bucket |
| country_iso3 | string | yes | country |
| product_id | string | no | optional product scope |
| signal_type | enum | yes | autarky, stockpiling, trade_rewiring, capital_access_control, civilian_military_allocation |
| raw_value | decimal | no | source-specific raw statistic |
| z_score | decimal | no | anomaly score |
| normalized_score | decimal | yes | 0-100 score |
| confidence | enum | yes | low, medium, high |
| explanation | text | yes | human-readable reason |
| source_row_refs | array | yes | references to source fact rows |

### fact_theater_multiplier

| Field | Type | Required | Notes |
|---|---|---:|---|
| date_month | date | yes | Month bucket |
| theater_id | string | yes | dim_theater ID |
| multiplier_value | decimal | yes | current multiplier |
| confidence | enum | yes | low, medium, high |
| explanation | text | yes | why multiplier changed |
| source_row_refs | array | yes | source fact row references |

### fact_2035_scenario_mapping

| Field | Type | Required | Notes |
|---|---|---:|---|
| scenario_id | string | yes | stable slug |
| theater_id | string | yes | mapped theater |
| present_signal | text | yes | observed 2026 signal |
| transition_2030 | text | yes | transition pathway |
| downside_2035 | text | yes | failure scenario |
| response_concept | text | yes | response option |
| linked_signal_types | array | yes | WET signal types |
| last_reviewed | date | yes | review date |

## Initial dashboard views

### vw_country_month_wet_score

Aggregates five equal-weighted WET signals by country-month.

```sql
SELECT
  date_month,
  country_iso3,
  AVG(normalized_score) AS base_wet_score
FROM fact_wet_signal_score
GROUP BY 1, 2;
```

### vw_theater_adjusted_score

Joins base country scores to relevant theater multipliers.

```sql
SELECT
  c.date_month,
  c.country_iso3,
  t.theater_id,
  c.base_wet_score,
  t.multiplier_value,
  c.base_wet_score * t.multiplier_value AS final_wet_score
FROM vw_country_month_wet_score c
JOIN country_theater_exposure e
  ON c.country_iso3 = e.country_iso3
JOIN fact_theater_multiplier t
  ON c.date_month = t.date_month
 AND e.theater_id = t.theater_id;
```

A `country_theater_exposure` bridge table should be added when implementation begins.

## Implementation notes

- Do not score raw policy documents directly without storing the event row.
- Do not collapse the European Union into Germany; keep `EUU` as a policy actor and member states as country actors.
- Treat Taiwan as a theater and a country-like actor for data purposes.
- Treat Arctic as a theater multiplier rather than a product group.
- Treat EDA as a proxy category because direct public trade statistics may be weak.

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
- OECD FDI Regulatory Restrictiveness Index: https://www.oecd.org/en/topics/sub-issues/sustainable-investment/fdi-regulatory-restrictiveness-index.html
