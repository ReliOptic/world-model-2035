#!/usr/bin/env python3
"""Audit GitHub Pages static app for the FLP chart."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "index.html"
CHART = DOCS / "assets/flp_ai_infra.svg"
DATA = DOCS / "data/flp_ai_infra_calculated.csv"
REQUIRED_INDEX_TOKENS = [
    "2035 Fundamental Line",
    "FLP-0.1",
    "flp_ai_infra.svg",
    "flp_ai_infra_calculated.csv",
    "Base",
    "Upside",
    "Downside",
    "Current implied",
    "divergence",
    "signal",
]
REQUIRED_DATA_COLUMNS = {
    "year",
    "base_value",
    "upside_value",
    "downside_value",
    "current_implied_value",
    "divergence_pct",
    "signal",
}


def main() -> int:
    errors: list[str] = []
    for path in (INDEX, CHART, DATA):
        if not path.exists():
            errors.append(f"missing {path.relative_to(ROOT)}")

    if INDEX.exists():
        text = INDEX.read_text(encoding="utf-8", errors="ignore")
        for token in REQUIRED_INDEX_TOKENS:
            if token not in text:
                errors.append(f"docs/index.html missing {token!r}")
        for src in ("assets/flp_ai_infra.svg", "data/flp_ai_infra_calculated.csv"):
            if src not in text:
                errors.append(f"docs/index.html does not reference {src}")

    if CHART.exists():
        chart_text = CHART.read_text(encoding="utf-8", errors="ignore")
        if "<svg" not in chart_text:
            errors.append("chart asset is not SVG")
        for token in ("Base", "Upside", "Downside", "Current implied"):
            if token not in chart_text:
                errors.append(f"chart missing {token!r}")

    if DATA.exists():
        with DATA.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fields = set(reader.fieldnames or [])
            missing = REQUIRED_DATA_COLUMNS - fields
            if missing:
                errors.append(f"data missing columns: {', '.join(sorted(missing))}")
            rows = list(reader)
        if not any(row.get("year") == "2035" for row in rows):
            errors.append("data missing 2035 row")
        if len(rows) < 10:
            errors.append("data should contain 2026-2035 rows")

    print(f"Pages app audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
