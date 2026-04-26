# 2026 Predictions
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-04  |  **다음 갱신:** 2026-10

This file records testable predictions anchored in 2026 that can be scored against observed outcomes. Each entry has a subject, a falsifiable condition, an evaluation window, a confidence band, and a pointer to the source file that justifies it.

## Active predictions

| ID | Topic | Statement | Evaluation Window | Confidence | Source File | Status |
|---|---|---|---|---|---|---|
| P26-01 | Semiconductors | TSMC `N2` monthly wafer output exceeds `80k` wspm before end of `2026`, based on Q4 2025 ramp already announced. | by `2026-12-31` | `72%` | `02_technology/semiconductors/roadmap_annual.md` | pending |
| P26-02 | Semiconductors | Samsung Foundry books at least one major external HPC customer for `SF2` before end of `2026`. | by `2026-12-31` | `35%` | `02_technology/semiconductors/roadmap_annual.md` | pending |
| P26-03 | Energy (SMR) | A commercial SMR unit reaches fuel load in North America before end of `2027`, counting OPG Darlington BWRX-300 as the leading candidate. | by `2027-12-31` | `45%` | `03_energy/fission_smr/roadmap_annual.md` | pending |
| P26-04 | Energy (fusion) | Commonwealth Fusion Systems SPARC achieves `Q > 1` operating condition before end of `2028`. | by `2028-12-31` | `30%` | `03_energy/fusion/roadmap_annual.md` | pending |
| P26-05 | AI compute | Announced AI datacenter capacity in the US exceeds `15 GW` of contracted load by end of `2027`. | by `2027-12-31` | `80%` | `02_technology/compute_infrastructure/datacenter_energy.md` | Mixed |
| P26-06 | AI capability | At least one frontier model reaches a public, reproducible benchmark corresponding to `IMO silver medal` level mathematical reasoning before end of `2026`. | by `2026-12-31` | `70%` | `02_technology/symbolic_reasoning/roadmap_annual.md` | Hit |
| P26-07 | AI policy | EU AI Act high-risk system obligations become enforceable `2026-08-02` as scheduled and at least one formal supervisory action is opened in the first `6` months of enforcement. | by `2027-02-02` | `60%` | `06_geopolitics/04_eu/eu_ai_act.md` | pending |
| P26-08 | Geopolitics (Taiwan) | No cross-strait military quarantine, blockade, or kinetic event occurs through end of `2027`. | by `2027-12-31` | `85%` | `06_geopolitics/02_china/taiwan_scenarios.md` | pending |
| P26-09 | Climate | A full calendar year exceeds `1.5°C` above pre-industrial for the second time before end of `2028`, following `2024` as the first. | by `2028-12-31` | `80%` | `13_scenarios/climate_emergency.md` | pending |
| P26-10 | Robotics | At least one humanoid robot product has paid external deployments exceeding `1,000` units in manufacturing or logistics before end of `2027`. | by `2027-12-31` | `40%` | `02_technology/robotics/humanoid_roadmap.md` | pending |
| P26-11 | Space | SpaceX Starship achieves at least `10` successful upper-stage recoveries by end of `2027`. | by `2027-12-31` | `50%` | `05_space/spacex/starship_roadmap.md` | pending |
| P26-12 | Stablecoins | Global stablecoin supply exceeds `$400B` by end of `2026`, up from roughly `$250B` in early 2026. | by `2026-12-31` | `62%` | `08_economics/stablecoin_cbdc/tbill_demand_model.md` | pending |

## Resolution rules
- `Hit`: stated condition materially occurs inside the stated window with unambiguous public evidence.
- `Miss`: stated condition does not occur inside the stated window.
- `Mixed`: threshold crossed ambiguously or only partially.
- `Unscorable`: wording or measurement became invalid; revise with date noted.

## Revision log
- `2026-04-22` initial 12 predictions logged from source-backed files in this repository.
- `2026-04-27` 분기 재평가 — 2026년 4월 관측 근거 반영:
  - `P26-01` 신뢰도 `65% → 72%`. 근거: TSMC `N2` 2025-Q4 양산 개시 공식화, 램프 트래젝토리 양호. 80k wspm 절대수치는 미공개이나 방향성 긍정.
  - `P26-05` Status `pending → Mixed`. 근거: Microsoft `$80B+`, Amazon/Google/Meta 합산 발표 contracted load는 이미 `15GW` 초과. 다만 "contracted announcement" vs "operational by 2027"는 별개. 발표 기준은 사실상 Hit, 운전 기준은 Pending.
  - `P26-06` Status `pending → Hit`. 근거: DeepMind `AlphaProof` 2024-07 IMO 금메달급 수학추론 실증, 현 프론티어 모델군 다수가 IMO silver 이상 수학 벤치 통과. 공개·재현 조건 충족.
  - `P26-09` 신뢰도 `75% → 80%`. 근거: WMO `2024년 +1.55°C` 확정, 2026-2027 추가 초과 가능성 높음.
  - `P26-12` 신뢰도 `55% → 62%`. 근거: 2026-Q1 스테이블코인 총공급 `~$230B`, USDT 단독 `$150B+`, 성장률 추세상 연말 `$400B` 도달 가능구간.
  - `P26-02`, `P26-03`, `P26-04`, `P26-07`, `P26-08`, `P26-10`, `P26-11` 신뢰도·Status 유지.

## 연결 문서
- [template.md](./template.md)
- [../00_foundations/scoring.md](../00_foundations/scoring.md)

## 정보 출처
- 이 파일은 각 예측 행의 `Source File` 열에 연결된 repository source-backed 문서들을 집계한 scoring log다.
- 예측 해소 시점에는 해당 행의 source file과 공개 관측자료를 함께 확인해 `Hit` / `Miss` / `Mixed` / `Unscorable` 중 하나로 판정한다.
