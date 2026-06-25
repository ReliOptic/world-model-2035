# War-Economy Transition Dashboard (WETD) Data Schema

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## Purpose

This is a non-forecast data contract for the War-Economy Transition Dashboard (WETD). It defines stable keys, source-row references, bridge tables, score-completeness guards, and scenario-mapping tables. The framework name is WETD; War-Economy Transition is the scored phenomenon; `2026–2035` is the model period used by the adjacent forecast documents.

## 연결 문서

- [wetd_2035_scope.md](wetd_2035_scope.md) — forecast-heavy scope and annual 2026–2035 logic.
- [wetd_theater_scenarios.md](wetd_theater_scenarios.md) — theater narratives that consume this schema.
- [wetd_etl_dashboard_contract.md](wetd_etl_dashboard_contract.md) — ETL and dashboard implementation contract.
- [CONTEXT.md](../CONTEXT.md) — War-Economy Transition Dashboard rows are `Divergence Signal` evidence within a `Coupling Map`.

## Contract conventions

- Every fact table has a stable primary key ending in `_id`.
- Every ingested row stores `source_name`, `source_url`, `retrieved_at`, and where possible `source_record_id`.
- `source_row_refs` is an array of strings formatted as `<table_name>:<primary_key>`, for example `fact_trade:trade_uncomtrade_2026_04_USA_CHN_8542_import`.
- Analyst-derived scores must reference source rows; raw source rows must not depend on score rows.
- War-Economy Transition Dashboard-specific seeds and calibration live in `dim_*`, `config_*`, or `seed_*` tables, not in generic source fact tables.

## Entity model

```text
dim_country
dim_product
dim_corridor
dim_theater
country_theater_exposure
config_signal_weight
config_warning_threshold
fact_trade
fact_policy_event
fact_sanctions
fact_procurement
fact_energy_minerals
fact_arctic_access
fact_wet_signal_score
fact_theater_multiplier
fact_2035_scenario_mapping
vw_country_month_wet_score
vw_theater_adjusted_score
```

## Dimension and configuration tables

### dim_country

| Field | Type | Required | Notes |
|---|---|---:|---|
| country_iso3 | string | yes | ISO-3 or repo pseudo-code such as `EUU` for European Union actor |
| country_name | string | yes | Display name |
| country_group | enum | yes | core_power, g7_advanced_bloc, frontline_tech_ally, corridor_watch, middle_east_node, arctic_actor |
| is_mvp_country | boolean | yes | Included in first dashboard score |

### dim_theater

| Field | Type | Required | Notes |
|---|---|---:|---|
| theater_id | string | yes | Stable slug: taiwan_strait, middle_east, arctic |
| theater_name | string | yes | Display name |
| theater_type | enum | yes | keystone, escalation_belt, spatial_multiplier |
| default_multiplier_low | decimal | yes | Calibration draft lower bound |
| default_multiplier_high | decimal | yes | Calibration draft upper bound |
| primary_risk | text | yes | Short risk description |

### country_theater_exposure

First-class bridge table used by theater-adjusted views.

| Field | Type | Required | Notes |
|---|---|---:|---|
| country_iso3 | string | yes | FK to dim_country |
| theater_id | string | yes | FK to dim_theater |
| exposure_weight | decimal | yes | 0.0–1.0 share of exposure; calibration draft |
| exposure_type | enum | yes | production, corridor, military, energy, finance, sanctions, arctic_access |
| effective_from | date | yes | Start date |
| effective_to | date | no | Null means current |
| rationale | text | yes | Human-readable reason |
| source_url | text | yes | Source or repo anchor URL/path |
| retrieved_at | timestamp | yes | Ingestion/review time |

Primary key: `(country_iso3, theater_id, exposure_type, effective_from)`.

### config_signal_weight

| Field | Type | Required | Notes |
|---|---|---:|---|
| config_id | string | yes | Stable version, e.g. `wetd_default_2026q2` |
| signal_type | enum | yes | autarky, stockpiling, trade_rewiring, capital_access_control, civilian_military_allocation |
| weight | decimal | yes | Starts at 0.20 each; must sum to 1.0 per config_id |
| effective_from | date | yes | Start date |
| effective_to | date | no | End date |
| rationale | text | yes | Why this weight is used |
| source_url | text | no | Calibration evidence or repo anchor |

### config_warning_threshold

| Field | Type | Required | Notes |
|---|---|---:|---|
| threshold_id | string | yes | Stable version |
| min_signal_count_for_complete_score | integer | yes | Default 5 |
| min_rising_signals_for_warning | integer | yes | Default 3 |
| allow_theater_shock_rule | boolean | yes | Default true |
| rationale | text | yes | Calibration hypothesis |

## Source fact tables

### fact_trade

Primary key: `trade_id`. Source examples: UN Comtrade, U.S. Census International Trade API, Eurostat, IMF trade data.

| Field | Type | Required | Notes |
|---|---|---:|---|
| trade_id | string | yes | Stable key derived from source, month, reporter, partner, flow, HS code |
| source_record_id | string | no | Native source row ID if provided |
| date_month | date | yes | Month bucket |
| reporter_iso3 | string | yes | Reporting country |
| partner_iso3 | string | yes | Partner country |
| flow | enum | yes | import, export, re_export if available |
| hs_code | string | yes | HS code |
| product_id | string | no | FK to dim_product |
| value_usd | decimal | yes | USD value |
| quantity | decimal | no | Physical quantity if available |
| quantity_unit | string | no | Unit |
| source_name | string | yes | Source system |
| source_url | text | yes | Query or source URL |
| retrieved_at | timestamp | yes | Ingestion time |

### fact_policy_event

Primary key: `policy_event_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| policy_event_id | string | yes | Stable key from source/date/agency/title hash |
| source_record_id | string | no | Federal Register docket/document number or source-native ID |
| event_date | date | yes | Publication or effective date |
| country_iso3 | string | yes | Issuing country/authority |
| agency | string | no | Agency or ministry |
| event_type | enum | yes | export_control, subsidy, fdi_screening, data_center_rule, ai_policy, sanctions_policy, industrial_policy |
| title | text | yes | Event title |
| summary | text | no | Normalized summary |
| affected_products | array | no | dim_product IDs |
| affected_countries | array | no | Target countries |
| keywords | array | yes | Normalized keywords |
| severity_hint | integer | no | Analyst label, not final score |
| source_name | string | yes | Source system |
| source_url | text | yes | Official source URL |
| retrieved_at | timestamp | yes | Ingestion time |

### fact_sanctions

Primary key: `sanctions_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| sanctions_id | string | yes | Stable key from source/list/entity/program/date hash |
| source_record_id | string | no | Native list ID if provided |
| listed_date | date | no | Original listed date when available |
| effective_month | date | yes | Month bucket used for growth metrics |
| date_quality | enum | yes | exact, month_only, publication_date, retrieved_date_fallback |
| date_imputed | boolean | yes | True when effective_month is inferred |
| entity_name | string | yes | Restricted party |
| country_iso3 | string | no | Associated country |
| list_source | string | yes | CSL, OFAC SDN, BIS Entity List, EU list, etc. |
| program | string | no | Sanctions/export-control program |
| reason | text | no | Listed reason if available |
| product_tags | array | no | AI, semiconductor, UAV, missile, energy, etc. |
| source_name | string | yes | Source system |
| source_url | text | yes | Source API or record URL |
| retrieved_at | timestamp | yes | Ingestion time |

### fact_procurement

Primary key: `procurement_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| procurement_id | string | yes | Stable key from source/notice/award ID |
| source_record_id | string | no | Native award or notice ID |
| award_or_notice_date | date | yes | Award or notice date |
| country_iso3 | string | yes | Procurement country |
| agency | string | yes | Buying agency |
| supplier | string | no | Awardee if available |
| value_usd | decimal | no | Normalized value |
| title | text | yes | Notice or award title |
| description | text | no | Text for keyword tagging |
| defense_flag | boolean | yes | Derived keyword/agency flag |
| ai_compute_flag | boolean | yes | Derived keyword flag |
| product_tags | array | no | Strategic goods |
| source_name | string | yes | Source system |
| source_url | text | yes | Source URL |
| retrieved_at | timestamp | yes | Ingestion time |

### fact_energy_minerals

Primary key: `energy_minerals_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| energy_minerals_id | string | yes | Stable key from source/month/country/commodity/metric |
| source_record_id | string | no | Native source row ID |
| date_month | date | yes | Month bucket |
| country_iso3 | string | yes | Country |
| commodity | string | yes | oil, LNG, copper, rare_earths, etc. |
| metric_name | string | yes | inventory, production, import, price, stock_to_use, etc. |
| value | decimal | yes | Measured value |
| unit | string | yes | Unit |
| source_name | string | yes | Source system |
| source_url | text | yes | Source URL |
| retrieved_at | timestamp | yes | Ingestion time |

### fact_arctic_access

Primary key: `arctic_access_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| arctic_access_id | string | yes | Stable key from source/month/zone/metric |
| source_record_id | string | no | Native source row ID |
| date_month | date | yes | Month bucket |
| arctic_zone | string | no | Route or zone if available |
| metric_name | string | yes | sea_ice_extent, sea_ice_anomaly, ship_count, icebreaker_procurement, radar_procurement |
| value | decimal | yes | Measured value |
| unit | string | yes | Unit |
| source_name | string | yes | Source system |
| source_url | text | yes | Source URL |
| retrieved_at | timestamp | yes | Ingestion time |

## Score and scenario tables

### fact_wet_signal_score

Primary key: `wet_signal_score_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| wet_signal_score_id | string | yes | Stable key from config/month/country/product/signal |
| config_id | string | yes | FK to config_signal_weight version |
| date_month | date | yes | Month bucket |
| country_iso3 | string | yes | Country |
| product_id | string | no | Optional product scope |
| signal_type | enum | yes | One of five War-Economy Transition signals |
| raw_value | decimal | no | Source-specific statistic |
| z_score | decimal | no | Anomaly score |
| normalized_score | decimal | yes | 0-100 score |
| confidence | enum | yes | low, medium, high |
| explanation | text | yes | Human-readable reason |
| source_row_refs | array | yes | `<table_name>:<primary_key>` references |

### fact_theater_multiplier

Primary key: `theater_multiplier_id`.

| Field | Type | Required | Notes |
|---|---|---:|---|
| theater_multiplier_id | string | yes | Stable key from theater/month/config |
| date_month | date | yes | Month bucket |
| theater_id | string | yes | dim_theater ID |
| multiplier_value | decimal | yes | Current multiplier |
| confidence | enum | yes | low, medium, high |
| explanation | text | yes | Why multiplier changed |
| source_row_refs | array | yes | `<table_name>:<primary_key>` references |

### fact_2035_scenario_mapping

Primary key: `scenario_mapping_id`. This table includes Base/Upside/Downside instead of a downside-only field.

| Field | Type | Required | Notes |
|---|---|---:|---|
| scenario_mapping_id | string | yes | Stable slug |
| theater_id | string | yes | Mapped theater |
| present_signal | text | yes | Observed 2026 signal |
| transition_2030 | text | yes | Transition pathway |
| base_2035 | text | yes | Base scenario |
| upside_2035 | text | yes | Upside scenario |
| downside_2035 | text | yes | Downside scenario |
| response_concept | text | yes | Response option |
| linked_signal_types | array | yes | War-Economy Transition signal types |
| last_reviewed | date | yes | Review date |

## Initial dashboard views

### vw_country_month_wet_score

Complete score guard: do not emit a complete Base War-Economy Transition Score unless all five signals are present for the country-month/config. Expose `signal_count` and `missing_signal_types` for incomplete rows.

```sql
WITH expected AS (
  SELECT DISTINCT config_id, signal_type
  FROM config_signal_weight
  WHERE effective_to IS NULL
), scored AS (
  SELECT
    s.date_month,
    s.country_iso3,
    s.config_id,
    s.signal_type,
    s.normalized_score,
    w.weight
  FROM fact_wet_signal_score s
  JOIN config_signal_weight w
    ON s.config_id = w.config_id
   AND s.signal_type = w.signal_type
), agg AS (
  SELECT
    date_month,
    country_iso3,
    config_id,
    COUNT(DISTINCT signal_type) AS signal_count,
    SUM(normalized_score * weight) / NULLIF(SUM(weight), 0) AS weighted_wet_score,
    ARRAY_AGG(DISTINCT signal_type) AS present_signal_types
  FROM scored
  GROUP BY 1, 2, 3
)
SELECT
  a.date_month,
  a.country_iso3,
  a.config_id,
  a.signal_count,
  ARRAY(
    SELECT e.signal_type
    FROM expected e
    WHERE e.config_id = a.config_id
      AND NOT e.signal_type = ANY(a.present_signal_types)
  ) AS missing_signal_types,
  CASE WHEN a.signal_count >= 5 THEN a.weighted_wet_score END AS base_wet_score,
  a.signal_count >= 5 AS is_complete_score
FROM agg a;
```

### vw_theater_adjusted_score

```sql
SELECT
  c.date_month,
  c.country_iso3,
  e.theater_id,
  c.base_wet_score,
  c.signal_count,
  c.missing_signal_types,
  c.is_complete_score,
  e.exposure_weight,
  t.multiplier_value,
  CASE
    WHEN c.is_complete_score THEN c.base_wet_score * e.exposure_weight * t.multiplier_value
  END AS final_wet_score
FROM vw_country_month_wet_score c
JOIN country_theater_exposure e
  ON c.country_iso3 = e.country_iso3
 AND c.date_month >= e.effective_from
 AND (e.effective_to IS NULL OR c.date_month <= e.effective_to)
JOIN fact_theater_multiplier t
  ON c.date_month = t.date_month
 AND e.theater_id = t.theater_id;
```

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
