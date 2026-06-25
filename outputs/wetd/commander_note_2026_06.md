# War-Economy Transition Dashboard (WETD) Commander Note — 2026-06-25

## Executive read

This is a monthly batch early-warning run. It does not predict war; it identifies whether economic allocation is moving from market pricing toward security permissioning, stockpiling, rerouting, and defense allocation.

Data basis: 152 official API/CSV rows plus 201 World Bank fallback proxy rows. Key-gated sources are visible in the data-quality notes instead of being hidden.

## Highest Base War-Economy Transition scores

- United Arab Emirates (ARE): 76.6
- China (CHN): 76.2
- Canada (CAN): 71.4
- Netherlands (NLD): 64.6
- Japan (JPN): 64.6

## Highest theater-adjusted scores

- China (CHN) / taiwan_strait: 94.11
- Taiwan (TWN) / taiwan_strait: 80.86
- Iran (IRN) / middle_east: 78.72
- United States (USA) / taiwan_strait: 69.03
- South Korea (KOR) / taiwan_strait: 67.18

## What inference this adds

- Co-movement: a country enters the review queue when multiple independent signals appear together, not because one obvious causal fact exists.
- Theater lift: the same country-month row can mean more or less depending on Taiwan Strait, Middle East, or Arctic exposure.
- Confidence constraint: fallback or low-confidence rows create review priority, not certainty.
- Data gap as finding: missing key-gated sources bound what the dashboard is allowed to claim.

## Five War-Economy Transition signals

- Self-reliance pressure (`autarky`): Is a country reducing dependence on open-market supply through subsidies, domestic substitution, or sovereignty framing? Evidence used: Policy events, energy/mineral dependency rows, and strategic-sector keywords.
- Strategic stockpiling (`stockpiling`): Is buying or inventory behavior becoming security-driven rather than ordinary commercial replenishment? Evidence used: Trade proxy rows, Arctic/energy access rows, and abnormal accumulation candidates.
- Route rewiring (`trade_rewiring`): Are flows moving through third countries, corridors, or indirect routes rather than direct market routes? Evidence used: Trade proxy rows plus sanctions/access-control pressure that can explain rerouting.
- Permissioning and access control (`capital_access_control`): Is market access being replaced by state permission, sanctions, screening, export controls, or compute/cloud restrictions? Evidence used: Federal Register policy events, sanctions rows, and restricted-access evidence.
- Civilian-to-military allocation (`civilian_military_allocation`): Are civilian technologies, compute, cloud, AI, or microelectronics entering defense/intelligence priority lanes? Evidence used: USAspending procurement rows and defense-allocation keywords.

## Country signal drilldown sample

- Canada (CAN) / Self-reliance pressure: score=82.0, confidence=medium
- Canada (CAN) / Permissioning and access control: score=75.0, confidence=medium
- Canada (CAN) / Civilian-to-military allocation: score=65.0, confidence=medium
- Canada (CAN) / Strategic stockpiling: score=75.0, confidence=medium
- Canada (CAN) / Route rewiring: score=60.0, confidence=medium
- China (CHN) / Self-reliance pressure: score=90.0, confidence=medium
- China (CHN) / Permissioning and access control: score=81.0, confidence=high
- China (CHN) / Civilian-to-military allocation: score=65.0, confidence=medium
- China (CHN) / Strategic stockpiling: score=75.0, confidence=medium
- China (CHN) / Route rewiring: score=70.0, confidence=medium
- United Arab Emirates (ARE) / Self-reliance pressure: score=70.0, confidence=medium
- United Arab Emirates (ARE) / Permissioning and access control: score=75.0, confidence=medium
- United Arab Emirates (ARE) / Civilian-to-military allocation: score=75.0, confidence=medium
- United Arab Emirates (ARE) / Strategic stockpiling: score=85.0, confidence=medium
- United Arab Emirates (ARE) / Route rewiring: score=78.0, confidence=medium

## Data quality notes

- UN Comtrade: missing_key, rows=0 — COMTRADE_SUBSCRIPTION_KEY not set; UN Comtrade returned 401 when tested without a key. Source: https://comtradeapi.un.org/
- World Bank trade fallback: ok, rows=185 — Loaded no-auth trade proxy indicators for immediate War-Economy Transition Dashboard execution. Source: https://api.worldbank.org/v2/
- Federal Register: ok, rows=25 — Loaded term 'semiconductor export control'. Source: https://www.federalregister.gov/api/v1/documents.json?per_page=25&order=newest&conditions%5Bterm%5D=semiconductor+export+control
- Federal Register: ok, rows=25 — Loaded term 'artificial intelligence data center'. Source: https://www.federalregister.gov/api/v1/documents.json?per_page=25&order=newest&conditions%5Bterm%5D=artificial+intelligence+data+center
- Federal Register: ok, rows=25 — Loaded term 'foreign investment semiconductor'. Source: https://www.federalregister.gov/api/v1/documents.json?per_page=25&order=newest&conditions%5Bterm%5D=foreign+investment+semiconductor
- Federal Register: ok, rows=25 — Loaded term 'advanced computing export'. Source: https://www.federalregister.gov/api/v1/documents.json?per_page=25&order=newest&conditions%5Bterm%5D=advanced+computing+export
- Treasury OFAC SDN: ok, rows=25 — Loaded sanctions rows from official OFAC CSV fallback. Source: https://www.treasury.gov/ofac/downloads/sdn.csv
- USAspending: ok, rows=25 — Loaded public procurement rows without authorization. Source: https://api.usaspending.gov/api/v2/search/spending_by_award/
- EIA Open Data: missing_key, rows=0 — EIA_API_KEY not set; EIA official docs require an API key. World Bank fallback used. Source: https://www.eia.gov/opendata/documentation.php
- World Bank energy/minerals: ok, rows=16 — Loaded no-auth energy/minerals fallback indicators. Source: https://api.worldbank.org/v2/
- NSIDC Sea Ice Index v4: ok, rows=2 — Loaded latest Arctic daily extent 2026-06-24. Source: https://noaadata.apps.nsidc.org/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v4.0.csv

## Decision use

Use top scores as a queue for analyst review, not as automatic alarms. Check source_row_refs, source URLs, proxy/fallback labels, and missing_signal_types before escalating a country/theater note.
