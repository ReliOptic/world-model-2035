#!/usr/bin/env python3
"""Audit deterministic FLP chart artifacts for the AI infrastructure pilot."""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
INPUT = ROOT / "13_scenarios/inputs/flp_ai_infra_inputs.csv"
OUTPUT = ROOT / "13_scenarios/outputs/flp_ai_infra_calculated.csv"
CHART = ROOT / "13_scenarios/charts/flp_ai_infra.svg"
GENERATOR = ROOT / ".github/scripts/flp_chart_generator.py"
YEARS = [str(y) for y in range(2026, 2036)]
REQUIRED_INPUT = {
    "year",
    "scenario",
    "group",
    "variable_id",
    "source_value",
    "normalization_min",
    "normalization_base",
    "normalization_max",
    "direction",
    "weight",
    "confidence",
    "source_url",
}
REQUIRED_OUTPUT = {
    "year",
    "demand_score",
    "capacity_score",
    "finance_score",
    "fundamental_score",
    "base_value",
    "upside_value",
    "downside_value",
    "current_implied_value",
    "divergence_pct",
    "signal",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def main() -> int:
    errors: list[str] = []
    for path in (GENERATOR, INPUT, OUTPUT, CHART):
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")

    if INPUT.exists():
        fields, rows = read_csv(INPUT)
        missing = REQUIRED_INPUT - set(fields)
        if missing:
            errors.append(f"input missing columns: {', '.join(sorted(missing))}")
        input_years = {row.get("year", "") for row in rows}
        for year in YEARS:
            if year not in input_years:
                errors.append(f"input missing year {year}")
        for group in ("demand", "capacity", "finance"):
            if not any(row.get("group") == group for row in rows):
                errors.append(f"input missing group {group}")
        for i, row in enumerate(rows, start=2):
            if row.get("direction") not in {"higher_is_capacity", "higher_is_constraint"}:
                errors.append(f"input row {i} invalid direction {row.get('direction')!r}")
            if not row.get("source_url", "").startswith("https://"):
                errors.append(f"input row {i} source_url must be https")

    if OUTPUT.exists():
        fields, rows = read_csv(OUTPUT)
        missing = REQUIRED_OUTPUT - set(fields)
        if missing:
            errors.append(f"output missing columns: {', '.join(sorted(missing))}")
        output_years = {row.get("year", "") for row in rows}
        for year in YEARS:
            if year not in output_years:
                errors.append(f"output missing year {year}")
        valid_signals = {"overheated", "neutral", "undervalued", "unscorable"}
        for i, row in enumerate(rows, start=2):
            if row.get("signal") not in valid_signals:
                errors.append(f"output row {i} invalid signal {row.get('signal')!r}")
            for col in REQUIRED_OUTPUT - {"year", "signal"}:
                try:
                    float(row.get(col, ""))
                except ValueError:
                    errors.append(f"output row {i} {col} is not numeric")

    if CHART.exists():
        text = CHART.read_text(encoding="utf-8", errors="ignore")
        for token in ("Base", "Upside", "Downside", "Current implied", "2026", "2035"):
            if token not in text:
                errors.append(f"chart missing label {token!r}")

    print(f"FLP chart audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
