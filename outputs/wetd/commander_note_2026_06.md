# WETD Commander Note — 2026-06-25

## Executive read

This is a monthly batch early-warning run. It does not predict war; it identifies whether economic allocation is moving from market pricing toward security permissioning, stockpiling, rerouting, and defense allocation.

## Highest Base WET scores

- ARE: 76.6
- CHN: 76.2
- CAN: 71.4
- NLD: 64.6
- KOR: 64.6

## Highest theater-adjusted scores

- CHN / taiwan_strait: 94.11
- TWN / taiwan_strait: 80.86
- IRN / middle_east: 78.72
- USA / taiwan_strait: 69.03
- KOR / taiwan_strait: 67.18

## Data quality notes

- UN Comtrade: missing_key, rows=0 — COMTRADE_SUBSCRIPTION_KEY not set; UN Comtrade returned 401 when tested without a key.
- World Bank trade fallback: ok, rows=185 — Loaded no-auth trade proxy indicators for immediate WETD execution.
- Federal Register: ok, rows=25 — Loaded term 'semiconductor export control'.
- Federal Register: ok, rows=25 — Loaded term 'artificial intelligence data center'.
- Federal Register: ok, rows=25 — Loaded term 'foreign investment semiconductor'.
- Federal Register: ok, rows=25 — Loaded term 'advanced computing export'.
- Treasury OFAC SDN: ok, rows=25 — Loaded sanctions rows from official OFAC CSV fallback.
- USAspending: ok, rows=25 — Loaded public procurement rows without authorization.
- EIA Open Data: missing_key, rows=0 — EIA_API_KEY not set; EIA official docs require an API key. World Bank fallback used.
- World Bank energy/minerals: ok, rows=16 — Loaded no-auth energy/minerals fallback indicators.
- NSIDC Sea Ice Index v4: ok, rows=2 — Loaded latest Arctic daily extent 2026-06-23.

## Decision use

Use top scores as a queue for analyst review, not as automatic alarms. Check source_row_refs and missing_signal_types before escalating a country/theater note.
