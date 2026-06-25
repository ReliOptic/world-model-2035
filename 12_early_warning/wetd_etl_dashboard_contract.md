# WETD ETL and Dashboard Contract

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## Purpose

This is a non-forecast implementation contract for the first monthly WETD dashboard. The framework name is WETD; `2026–2035` belongs to adjacent forecast/scenario documents. The first implementation is a monthly analytical dashboard, not a real-time alerting platform.

## 연결 문서

- [wetd_2035_scope.md](wetd_2035_scope.md) — forecast-heavy scope and model discipline.
- [wetd_theater_scenarios.md](wetd_theater_scenarios.md) — theater scenario outputs consumed by the dashboard.
- [wetd_data_schema.md](wetd_data_schema.md) — source fact tables, keys, source references, weights, and complete-score guard.
- [CONTEXT.md](../CONTEXT.md) — WETD is a `Coupling Map` / `Divergence Signal` early-warning surface.
- [../docs/wetd_monthly_batch_dashboard.md](../docs/wetd_monthly_batch_dashboard.md) — executable DuckDB monthly batch runbook.

## Data-source priority

| Priority | Source class | Examples | Use |
|---|---|---|---|
| A | Official APIs | UN Comtrade, U.S. Census, Federal Register, Trade.gov CSL, USAspending, EIA | Primary quantitative and event rows |
| B | Official downloads | USGS minerals, NSIDC Sea Ice Index, national statistics | Monthly or annual supporting rows |
| C | Specialized monitoring databases | WTO I-TIP, OECD.AI, Global Trade Alert as secondary context | Policy-event enrichment with source labels |
| D | News and market commentary | Financial press, analyst notes | Context only; never score input without corroboration |

## MVP data pipelines

| Pipeline | Main sources | Main outputs | Signals fed |
|---|---|---|---|
| Strategic goods trade | UN Comtrade, U.S. Census, Eurostat where needed | `fact_trade`, import dependence, supplier HHI, direct/indirect route ratio, mirror-trade gap | Autarky, stockpiling, trade rewiring |
| Policy, sanctions, access controls | Federal Register, Trade.gov CSL, OFAC/EU/BIS lists if added, OECD FDIRRI, OECD.AI | `fact_policy_event`, `fact_sanctions`, event counts, restricted entity growth | Capital/access control, autarky, civilian-to-military allocation |
| Public procurement and military allocation | USAspending, SAM.gov, TED, UK Contracts Finder if added | `fact_procurement`, defense AI share, compute militarization ratio | Civilian-to-military allocation, capital/access control |
| Energy, minerals, infrastructure inputs | EIA, FRED, USGS, JODI where available | `fact_energy_minerals`, price-insensitive buying, stock-to-use proxy | Stockpiling, autarky, theater multipliers |
| Arctic spatial multiplier | NSIDC Sea Ice Index, Arctic ship traffic datasets, official procurement/defense documents | `fact_arctic_access`, Arctic accessibility index, Arctic multiplier | Theater multiplier, trade rewiring, civilian-to-military allocation |

The Arctic pipeline remains separate from ordinary energy monitoring because it changes the strategic meaning of route access, cables, military infrastructure, and resource claims.

## Score-computation workflow

```text
1. Ingest raw API/download rows with stable primary keys and source URLs.
2. Normalize country, product, corridor, and theater keys.
3. Map goods and keywords to strategic product IDs.
4. Compute source-level metrics.
5. Convert metrics to 0-100 WET signal scores with source_row_refs.
6. Apply config_signal_weight instead of hard-coded equal weights.
7. Emit Base WET Score only when all five signals are present; otherwise expose signal_count and missing_signal_types.
8. Compute theater-month multipliers.
9. Join country_theater_exposure to produce theater-adjusted scores.
10. Update Base/Upside/Downside 2035 scenario-mapping rows.
11. Generate commander note and dashboard export.
```

## Initial signal calculations

| Signal | Candidate components | Guardrail |
|---|---|---|
| Autarky | Import-dependence reduction, supplier HHI, subsidy/industrial-policy event count, sovereignty keyword count | Plain import decline may be recession, not self-reliance |
| Strategic stockpiling | Import volume/value z-score, price-insensitive buying, stock-to-use proxy | Require demand/price context before labeling stockpiling |
| Trade rewiring | Direct route decline, corridor-state surge, mirror-trade gap, partner-share entropy shift | Corridor evidence must be product-specific |
| Capital and access control | Restricted entities, export-control events, FDI restrictiveness, compute/cloud/model-weight controls | Separate compliance events from escalation interpretation |
| Civilian-to-military allocation | Defense AI procurement share, secure cloud/HPC, microelectronics, ISR/C2/autonomy/cyber spend | Defense flag is evidence, not sufficient alarm |

## Dashboard pages

| Page | Required elements |
|---|---|
| Executive WET map | Country-month WET score, theater-adjusted WET score, top movers, highest-confidence signals, commander note |
| Strategic goods monitor | HBM/GPU/equipment/EUV-metrology/EDA panel; energy/rare earth/copper/power equipment/cooling panel; import dependence and stockpiling anomalies |
| Corridor watch | Taiwan, Singapore, Malaysia, UAE, Vietnam rows; direct versus indirect route ratios; mirror-trade gap flags; China/Russia/Iran/Taiwan-linked route patterns |
| Policy and access-control timeline | Export controls, sanctions, FDI screening, data-center rules, AI/cloud/model restrictions with source URLs |
| Theater board | Taiwan Strait, Middle East, Arctic multipliers; exposure countries; source evidence; scenario mapping deltas |
| Data quality board | Signal_count, missing_signal_types, stale source rows, imputed sanction dates, low-confidence scores |

## Acceptance checklist

- Every source fact table row has a stable primary key and `source_url`.
- `source_row_refs` are formatted as `<table_name>:<primary_key>`.
- `country_theater_exposure` exists before `vw_theater_adjusted_score` is used.
- `config_signal_weight` is the only source of signal weights. Equal weights are a draft config, not a hard-coded model claim.
- `fact_sanctions` includes `effective_month`, `date_quality`, and `date_imputed`.
- `vw_country_month_wet_score` exposes `signal_count`, `missing_signal_types`, and does not emit a complete score with fewer than five signals.
- Scenario mapping includes Base, Upside, and Downside rows or fields.
- Commander notes distinguish present-state facts, repo inference, and 2035 scenarios.

## Non-goals for the first pass

- No real-time alerting.
- No classified or scraped-only source dependency.
- No single black-box WET score without components.
- No theater multiplier hidden inside a product category.
- No permanent assumption that equal weights are correct.

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
