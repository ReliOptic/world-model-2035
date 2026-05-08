# Fundamental Line Prediction
**정보 신선도:** 🟢  |  **최종 갱신:** 2026-05  |  **다음 갱신:** 2026-08

## Purpose

A fundamental line is the deterministic baseline path that this repository uses to compare current expectations against the 2035 world model.

The goal is not to predict one exact future. The goal is to calculate a reproducible normal path from sourced inputs, then measure how far a current market price, policy target, investment announcement, or news reaction has moved away from that path.

```text
Current state anchor -> 2030 checkpoint -> 2035 Base Case
                                  \-> Upside / Downside / Shock bands
```

## 2026년 4월 현재 상태

- The repository already tracks source-backed 2035 scenarios across technology, energy, geopolitics, economics, defense, science, and opportunity intelligence.
- The missing piece is a deterministic bridge from those scenario files to a repeatable divergence signal.
- This file defines that bridge as a formula-first method: fixed inputs, fixed normalization, fixed bottleneck aggregation, fixed thresholds, and separate analyst commentary.

## Deterministic calculation contract

The same versioned input table must produce the same fundamental line and the same divergence signal.

Narrative analysis may explain the result, but it must not change the deterministic output unless the input table or formula version changes.

### Formula version

Use this identifier until the method changes:

```text
fundamental_line_formula_version = FLP-0.1
```

Any later change to normalization, aggregation, weights, missing-data rules, or signal thresholds must increment the version and preserve the prior method in git history or an issue comment.

## Required input schema

Each variable row must contain:

| Field | Required | Description |
|---|---:|---|
| `variable_id` | yes | Stable identifier, e.g. `grid_transformer_lead_time` |
| `sector` | yes | Sector or dependency chain owner |
| `source_value` | yes | Raw sourced value |
| `unit` | yes | MW, GW, TWh, USD, years, index, percent, etc. |
| `as_of_date` | yes | Date or month of the input |
| `source_url` | yes | Primary or official source URL when possible |
| `normalization_min` | yes | Pessimistic or low-bound anchor |
| `normalization_base` | yes | Base-case anchor |
| `normalization_max` | yes | Optimistic or high-bound anchor |
| `direction` | yes | `higher_is_capacity` or `higher_is_constraint` |
| `weight` | yes | Decimal weight inside a group; group weights should sum to 1.0 |
| `confidence` | yes | 0-1 evidence confidence, not forecast probability |
| `missing_policy` | yes | `block`, `use_base`, or `impute_from_peer` |

## Normalization

All inputs are converted to a 0-1 score.

For variables where higher values increase capacity:

```text
normalized = clamp(
  (source_value - normalization_min)
  / (normalization_max - normalization_min),
  0,
  1
)
```

For variables where higher values increase constraint severity:

```text
normalized = 1 - clamp(
  (source_value - normalization_min)
  / (normalization_max - normalization_min),
  0,
  1
)
```

Interpretation:

```text
1.0 = unconstrained / strongly supportive
0.5 = base-case constraint
0.0 = binding bottleneck
```

## Group scores

Each sector or dependency chain should define three groups.

```text
demand_score
capacity_score
finance_score
```

Weighted group score:

```text
group_score = sum(normalized_i * weight_i * confidence_i)
              / sum(weight_i * confidence_i)
```

If all variables in a group are missing, the group cannot be calculated unless the issue explicitly allows `use_base` for that group.

## Fundamental line

The fundamental line is the constrained path, not the unconstrained demand story.

```text
constraint_score = min(capacity_score, finance_score)
fundamental_score = min(demand_score, constraint_score)
```

When the model has a physical unit target, calculate the physical line as:

```text
fundamental_value_year = unconstrained_demand_value_year * fundamental_score_year
```

When the model is still index-based, use:

```text
fundamental_index_year = 100 * fundamental_score_year
```

## Scenario bands

Base, Upside, Downside, and Shock are deterministic transformations of the same input schema.

```text
Base     = use `normalization_base` anchors and current source values
Upside   = replace selected constraints with `normalization_max` path values
Downside = replace selected constraints with `normalization_min` path values
Shock    = apply explicit shock multipliers from the relevant scenario issue
```

Shock multipliers must be named and sourced or explicitly labeled as repo inference.

## Divergence calculation

```text
divergence_pct =
  (current_implied_expectation - fundamental_line_value)
  / fundamental_line_value
```

If `fundamental_line_value` is zero or unavailable, the signal is `unscorable`.

## Signal classification

Fixed thresholds:

```text
divergence_pct >= +30%  -> overheated
 divergence_pct <= -30% -> undervalued
otherwise               -> neutral
```

Optional severity bands:

```text
+75% or more  -> extreme overheating
-75% or less  -> extreme undervaluation
```

## Missing-data rules

Use deterministic missing-data handling.

| Policy | Rule |
|---|---|
| `block` | Do not calculate the line until the variable is filled. |
| `use_base` | Substitute `normalization_base` and mark the result `provisional`. |
| `impute_from_peer` | Use a named peer variable and record the mapping. |

Never invent a number inside the prose. If a value is analyst judgment, put it in the input table as `repo_inference` with lower confidence.

## Pilot: AI infrastructure dependency chain

Pilot chain:

```text
AI/Data Center -> Power Grid -> Semiconductors -> Built Environment -> Financial Markets
```

Minimum input groups:

| Group | Example variables | Linked issues |
|---|---|---|
| Demand | data center electricity demand, AI CAPEX, cloud utilization | #12 |
| Capacity | grid connection capacity, transformer lead time, GPU/HBM supply, data center construction capacity | #2, #3, #4 |
| Finance | credit spreads, hyperscaler free cash flow, private credit availability, insurance/reinsurance costs | #8 |

Worked example format:

| variable_id | group | source_value | min | base | max | direction | weight | confidence | normalized |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| `dc_power_demand_index` | demand | 140 | 80 | 100 | 160 | higher_is_capacity | 0.40 | 0.70 | formula output |
| `grid_connection_index` | capacity | 90 | 50 | 100 | 150 | higher_is_capacity | 0.35 | 0.65 | formula output |
| `credit_spread_index` | finance | 120 | 80 | 100 | 180 | higher_is_constraint | 0.40 | 0.60 | formula output |

Then calculate:

```text
demand_score = weighted normalized demand variables
capacity_score = weighted normalized capacity variables
finance_score = weighted normalized finance variables
fundamental_score = min(demand_score, capacity_score, finance_score)
fundamental_line_value = unconstrained_demand_value * fundamental_score
divergence_pct = (current_implied_expectation - fundamental_line_value) / fundamental_line_value
signal = threshold(divergence_pct)
```

## Implementation boundary

This method is document-native first. A later software implementation may move the schema into CSV, JSON, or Python, but it must preserve:

- formula version
- input table version
- source URLs
- missing-data policy
- deterministic output
- separate commentary

## 2035 전망 요약

- **Base:** Fundamental lines become the default comparison layer for major sector forecasts and opportunity intelligence.
- **Upside:** Deterministic input tables allow quarterly recalculation and issue-linked audit trails across sectors.
- **Downside:** The method remains qualitative if sectors do not provide enough source-backed input variables.

## 연결 문서

- [scoring.md](scoring.md)
- [source_policy.md](source_policy.md)
- [tech_realism_framework.md](tech_realism_framework.md)
- [SYNTHESIS_2035_QUANTITATIVE.md](../13_scenarios/SYNTHESIS_2035_QUANTITATIVE.md)
- [early_signals_dashboard_spec.md](../15_opportunity_intelligence/early_signals_dashboard_spec.md)

## 정보 출처

- Repository method derived from issue #12, `Feature: Add fundamental line prediction for 2035 baseline divergence`, 2026-05-09.
- IEA, `Energy and AI`, https://www.iea.org/reports/energy-and-ai, 2026-05 확인.
- IEA, `Electricity 2026: Grids`, https://www.iea.org/reports/electricity-2026/grids, 2026-05 확인.
- IEA, `Global Critical Minerals Outlook 2025`, https://www.iea.org/reports/global-critical-minerals-outlook-2025, 2026-05 확인.
- IMF, `World Economic Outlook`, https://www.imf.org/en/Publications/WEO, 2026-05 확인.
