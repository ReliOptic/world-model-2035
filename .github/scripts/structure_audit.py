#!/usr/bin/env python3
"""Audit repository markdown files for the world-model content contract."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDED_DIRS = {".git", ".omx", ".omc", "node_modules", "dist", "build", ".cache", ".github"}
GLOBAL_EXCLUDED_FILES = {
    "README.md",
    "METHODOLOGY.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "progress.md",
    "The world in 2035.md",
}
NON_FORECAST_PATHS = {
    "00_foundations/arctic_integration_memo.md",
    "00_foundations/axioms.md",
    "00_foundations/biases.md",
    "00_foundations/file_template.md",
    "00_foundations/scoring.md",
    "00_foundations/source_policy.md",
    "00_foundations/tech_realism_framework.md",
    "00_foundations/update_freshness.md",
    "06_geopolitics/SYNTHESIS.md",
    "14_predictions_log/2026_predictions.md",
    "14_predictions_log/template.md",
}
REQUIRED_COMMON = ["**정보 신선도:**", "## 연결 문서", "## 정보 출처"]
REQUIRED_FORECAST = ["## 2026년 4월 현재 상태", "## 1년 단위 전망", "## 2035 전망 요약"]
URL_RE = re.compile(r"https?://\S+")
YEAR_ROW_RE = re.compile(r"\|\s*(20[2-3][0-9])\s*\|")


def iter_markdown():
    for path in REPO_ROOT.rglob("*.md"):
        rel_parts = path.relative_to(REPO_ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in GLOBAL_EXCLUDED_FILES:
            continue
        yield path


def source_url_count(text: str) -> int:
    if "## 정보 출처" not in text:
        return 0
    return len(URL_RE.findall(text.split("## 정보 출처", 1)[1]))


def is_forecast(path: Path) -> bool:
    rel = path.relative_to(REPO_ROOT).as_posix()
    if rel in NON_FORECAST_PATHS:
        return False
    if rel.startswith("00_foundations/"):
        return False
    if rel.startswith("14_predictions_log/"):
        return False
    return True


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    total = 0
    forecast_total = 0
    for path in iter_markdown():
        total += 1
        rel = path.relative_to(REPO_ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in REQUIRED_COMMON:
            if token not in text:
                errors.append(f"{rel}: missing `{token}`")
        if source_url_count(text) == 0 and rel not in NON_FORECAST_PATHS:
            warnings.append(f"{rel}: source section has no URL")
        if not is_forecast(path):
            continue
        forecast_total += 1
        for token in REQUIRED_FORECAST:
            if token not in text:
                errors.append(f"{rel}: missing `{token}`")
        years = set(YEAR_ROW_RE.findall(text))
        missing_years = [str(year) for year in range(2026, 2036) if str(year) not in years]
        if missing_years:
            errors.append(f"{rel}: missing annual rows for {', '.join(missing_years)}")
        if not all(word in text for word in ("Base", "Upside", "Downside")):
            errors.append(f"{rel}: missing Base/Upside/Downside terminology")

    print(f"Markdown content files scanned: {total}")
    print(f"Forecast files scanned: {forecast_total}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if errors:
        print("\n## Errors")
        for item in errors[:300]:
            print(f"- {item}")
        if len(errors) > 300:
            print(f"- ... {len(errors) - 300} more")
    if warnings:
        print("\n## Warnings")
        for item in warnings[:200]:
            print(f"- {item}")
        if len(warnings) > 200:
            print(f"- ... {len(warnings) - 200} more")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
