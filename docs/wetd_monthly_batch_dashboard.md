# War-Economy Transition Dashboard (WETD) Monthly Batch Runbook

**정보 신선도:** 🟢 | **최종 갱신:** 2026-06 | **다음 갱신:** 2026-09

## 목적

War-Economy Transition Dashboard(WETD, 전쟁경제 전환 대시보드) 월간 배치 대시보드는 `12_early_warning/wetd_data_schema.md`의 계약을 실제 DuckDB 파이프라인으로 실행한다. 목표는 전쟁 예측이 아니라, 평시 시장 배분이 안보 허가·비축·우회 경로·민군 배분으로 이동하는지를 월별로 관찰하는 것이다.

## 연결 문서

- [../12_early_warning/wetd_2035_scope.md](../12_early_warning/wetd_2035_scope.md) — War-Economy Transition Dashboard scope와 forecast discipline.
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

현재 구현은 월간 배치형 분석 제품의 첫 실행 가능한 버전이다. DuckDB schema, seed tables, public-source ingestion, War-Economy Transition score calculation, complete-score guard, data-quality board, HTML export, commander note generation이 모두 한 명령으로 실행된다.

## 추론 레이어

대시보드는 “제재가 있으면 위험하다”처럼 인과관계가 너무 선명한 문장을 나열하지 않는다. 유의미한 사용 지점은 개별 원자료가 아니라 다음의 조합 추론이다.

- **Co-movement:** 한 국가에서 접근통제, 조달, 무역/비축 proxy, 에너지·광물 row가 동시에 움직이는지 본다.
- **Theater lift:** 같은 국가 점수가 Taiwan Strait, Middle East, Arctic 노출 그래프 안에서 얼마나 다르게 해석되는지 본다.
- **Confidence constraint:** 높은 점수라도 low/fallback confidence면 확신이 아니라 검토 우선순위로 읽는다.
- **Data gap as finding:** Comtrade/EIA 같은 key-gated source가 빠지면 결론의 상한을 낮추고 fallback proxy라고 표시한다.

## Dashboard MECE layout

HTML dashboard는 네 층으로만 읽게 재배치한다.

1. **Metric:** country score bar와 theater bubble은 “무엇이 움직였나”만 보여준다.
2. **Narrative:** country accordion은 “어떤 체제 준비 가설인가”를 국가별로 접었다 펼쳐 보여준다.
3. **Evidence:** provenance cards는 official rows, fallback proxy, key-gated source를 분리한다.
4. **Action:** commander note와 CSV artifacts는 analyst review에 넘긴다.

사우디아라비아는 Middle East energy/capital connector로 seed와 theater exposure에 포함한다. 기본 화면에서 Saudi Arabia accordion을 열어 두며, `체제 준비`, `관측 동향`, `왜 단순 인과가 아닌가`, `검증해야 할 것`, `5-signal fingerprint`를 한 장표 안에서 확인한다.

## 5개 War-Economy Transition signal

| Signal | Plain meaning | 국가별 부연에서 확인할 내용 |
|---|---|---|
| Autarky / self-reliance pressure | 시장 조달보다 국내 대체·자립·주권 언어가 강해지는가 | 해당 국가의 정책 event와 에너지/광물 dependency row가 같이 점수를 만들었는지 |
| Strategic stockpiling | 상업적 재고 보충이 아니라 안보 목적의 비축처럼 보이는가 | trade proxy, Arctic/energy access row, corridor 여부가 점수에 어떻게 반영됐는지 |
| Trade rewiring | 직접 경로 대신 제3국·우회 corridor로 흐름이 바뀌는가 | corridor watch state인지, sanctions/access-control 압력과 같이 움직이는지 |
| Capital and access control | 시장 접근이 허가·제재·심사·수출통제로 대체되는가 | Federal Register, OFAC, 정책 event가 어떤 confidence로 연결됐는지 |
| Civilian-to-military allocation | 민간 AI/compute/cloud/전자기술이 국방·정보 우선순위로 들어가는가 | USAspending 조달 row와 defense-allocation keyword가 있는지 |

## 1년 단위 전망

| Year | Base | Upside | Downside |
|---|---|---|---|
| 2026 | Public/no-auth fallback으로 월간 War-Economy Transition Dashboard run을 재현한다. | UN Comtrade/EIA keys가 붙어 고해상도 trade/energy rows가 추가된다. | fallback proxy를 실제 trade value처럼 오독한다. |
| 2027 | score weights와 theater exposure를 분기별로 검토한다. | backtest로 false positive를 줄인다. | equal-weight baseline이 관성적으로 굳어진다. |
| 2028 | corridor watch와 sanctions/procurement joins가 안정화된다. | Taiwan/Middle East/Arctic notes가 의사결정 큐로 쓰인다. | source coverage gaps가 국가별 비교를 왜곡한다. |
| 2029 | dashboard가 월간 governance artifact가 된다. | commander note가 response concept와 직접 연결된다. | data-quality board 없이 점수만 유통된다. |
| 2030 | transition pathway rows가 실제 monthly facts와 연결된다. | strategic reserve/corridor audit decisions에 쓰인다. | 허가경제 전환을 뒤늦게 해석한다. |
| 2031 | API-keyed high-resolution sources가 기본값이 된다. | score confidence가 source depth를 반영한다. | 공개 source만으로 민감 chokepoint를 놓친다. |
| 2032 | theater multipliers가 empirical calibration을 갖는다. | Arctic route/resource signals가 별도 board로 확장된다. | theater narrative가 raw data보다 앞선다. |
| 2033 | country-theater exposure가 monthly revision history를 갖는다. | analyst review queue가 자동 생성된다. | exposure weights가 검증 없이 정치화된다. |
| 2034 | WETD가 scenario maintenance layer가 된다. | 정책/투자/공급망 대응이 row-level 근거에 연결된다. | 단일 black-box score로 축약된다. |
| 2035 | War-Economy Transition Dashboard는 price allocation이 permission allocation으로 바뀌는 증거를 설명한다. | transparency가 과잉 반응을 줄인다. | compute/energy/sanctions/corridor shocks가 결합될 때 늦게 감지한다. |

## 2035 전망 요약

**Base.** War-Economy Transition Dashboard(WETD)는 공개 source 기반 월간 조기경보 큐로 남고, analyst가 `source_row_refs`, `missing_signal_types`, data-quality rows를 확인한 뒤 해석한다.

**Upside.** API-keyed 고해상도 소스가 붙으면서 country-month score가 실제 trade/procurement/sanctions movement에 더 가까워지고, theater-adjusted score가 정책·공급망 대응을 앞당긴다.

**Downside.** fallback proxy를 실측처럼 받아들이거나, complete-score guard/data-quality board 없이 점수만 공유하면 War-Economy Transition Dashboard가 조기경보가 아니라 가짜 확신 장치가 된다.

## 정보 출처

- Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
- USAspending API documentation: https://api.usaspending.gov/docs/endpoints
- Treasury OFAC sanctions list service: https://www.treasury.gov/ofac/downloads/sdn.csv
- NSIDC Sea Ice Index archive: https://nsidc.org/data/seaice_index/data-and-image-archive
- World Bank API: https://api.worldbank.org/v2/
- EIA Open Data documentation: https://www.eia.gov/opendata/documentation.php
- UN Comtrade API portal: https://comtradedeveloper.un.org/
