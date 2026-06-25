# WETD Monthly Batch Dashboard Runbook

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## 목적

WETD 월간 배치 대시보드는 `12_early_warning/wetd_data_schema.md`의 계약을 실제 DuckDB 파이프라인으로 실행한다. 목표는 전쟁 예측이 아니라, 평시 시장 배분이 안보 허가·비축·우회 경로·민군 배분으로 이동하는지를 월별로 관찰하는 것이다.

## 연결 문서

- [../12_early_warning/wetd_2035_scope.md](../12_early_warning/wetd_2035_scope.md) — WETD scope와 forecast discipline.
- [../12_early_warning/wetd_data_schema.md](../12_early_warning/wetd_data_schema.md) — DuckDB 구현의 데이터 계약.
- [../12_early_warning/wetd_etl_dashboard_contract.md](../12_early_warning/wetd_etl_dashboard_contract.md) — ETL/dashboard acceptance checklist.
- [../outputs/wetd/index.html](../outputs/wetd/index.html) — 최신 생성 대시보드.

## 실행 방법

```bash
python3 -m pip install -r requirements-wetd.txt
python3 scripts/wetd_pipeline.py run --as-of 2026-06-25 --limit 25
python3 -m http.server 8787 --bind 127.0.0.1
```

산출물:

```text
data/wetd/wetd.duckdb                         # 로컬 생성 DB, git ignore
outputs/wetd/index.html                       # 정적 대시보드
outputs/wetd/wetd_country_month_scores.csv
outputs/wetd/wetd_theater_adjusted_scores.csv
outputs/wetd/wetd_signal_scores.csv
outputs/wetd/wetd_data_quality.csv
outputs/wetd/commander_note_YYYY_MM.md
```

## 공개/무인증 소스와 key-gated 소스

현재 바로 실행되는 공개 소스:

| Source | Pipeline use |
|---|---|
| Federal Register API | policy/access-control events |
| USAspending API | procurement and civilian-to-military allocation |
| Treasury OFAC SDN CSV | sanctions/access-control rows |
| NSIDC Sea Ice Index v4 CSV | Arctic spatial multiplier |
| World Bank API | no-auth trade and energy/minerals fallback indicators |

현재 key가 있으면 고해상도로 대체되는 소스:

| Source | Environment variable | Fallback |
|---|---|---|
| UN Comtrade | `COMTRADE_SUBSCRIPTION_KEY` | World Bank trade indicators |
| EIA Open Data | `EIA_API_KEY` | World Bank energy indicators |
| U.S. Census trade API | future `CENSUS_API_KEY` connector | World Bank trade indicators |
| ITA CSL API | future API subscription connector | Treasury OFAC SDN CSV |

## 2026년 4월 현재 상태

현재 구현은 월간 배치형 분석 제품의 첫 실행 가능한 버전이다. DuckDB schema, seed tables, public-source ingestion, WET score calculation, complete-score guard, data-quality board, HTML export, commander note generation이 모두 한 명령으로 실행된다.

## 1년 단위 전망

| Year | Base | Upside | Downside |
|---|---|---|---|
| 2026 | Public/no-auth fallback으로 월간 WETD run을 재현한다. | UN Comtrade/EIA keys가 붙어 고해상도 trade/energy rows가 추가된다. | fallback proxy를 실제 trade value처럼 오독한다. |
| 2027 | score weights와 theater exposure를 분기별로 검토한다. | backtest로 false positive를 줄인다. | equal-weight baseline이 관성적으로 굳어진다. |
| 2028 | corridor watch와 sanctions/procurement joins가 안정화된다. | Taiwan/Middle East/Arctic notes가 의사결정 큐로 쓰인다. | source coverage gaps가 국가별 비교를 왜곡한다. |
| 2029 | dashboard가 월간 governance artifact가 된다. | commander note가 response concept와 직접 연결된다. | data-quality board 없이 점수만 유통된다. |
| 2030 | transition pathway rows가 실제 monthly facts와 연결된다. | strategic reserve/corridor audit decisions에 쓰인다. | 허가경제 전환을 뒤늦게 해석한다. |
| 2031 | API-keyed high-resolution sources가 기본값이 된다. | score confidence가 source depth를 반영한다. | 공개 source만으로 민감 chokepoint를 놓친다. |
| 2032 | theater multipliers가 empirical calibration을 갖는다. | Arctic route/resource signals가 별도 board로 확장된다. | theater narrative가 raw data보다 앞선다. |
| 2033 | country-theater exposure가 monthly revision history를 갖는다. | analyst review queue가 자동 생성된다. | exposure weights가 검증 없이 정치화된다. |
| 2034 | WETD가 scenario maintenance layer가 된다. | 정책/투자/공급망 대응이 row-level 근거에 연결된다. | 단일 black-box score로 축약된다. |
| 2035 | WETD는 price allocation이 permission allocation으로 바뀌는 증거를 설명한다. | transparency가 과잉 반응을 줄인다. | compute/energy/sanctions/corridor shocks가 결합될 때 늦게 감지한다. |

## 2035 전망 요약

**Base.** WETD는 공개 source 기반 월간 조기경보 큐로 남고, analyst가 `source_row_refs`, `missing_signal_types`, data-quality rows를 확인한 뒤 해석한다.

**Upside.** API-keyed 고해상도 소스가 붙으면서 country-month score가 실제 trade/procurement/sanctions movement에 더 가까워지고, theater-adjusted score가 정책·공급망 대응을 앞당긴다.

**Downside.** fallback proxy를 실측처럼 받아들이거나, complete-score guard/data-quality board 없이 점수만 공유하면 WETD가 조기경보가 아니라 가짜 확신 장치가 된다.

## 정보 출처

- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- USAspending API documentation: https://api.usaspending.gov/docs/endpoints
- Treasury OFAC sanctions list service: https://www.treasury.gov/ofac/downloads/sdn.csv
- NSIDC Sea Ice Index archive: https://nsidc.org/data/seaice_index/data-and-image-archive
- World Bank API: https://api.worldbank.org/v2/
- EIA Open Data documentation: https://www.eia.gov/opendata/documentation.php
- UN Comtrade API portal: https://comtradedeveloper.un.org/
