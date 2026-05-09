#!/usr/bin/env python3
"""Audit UX acceptance criteria for the Fundamental Line Pages app."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
INDEX = ROOT / "docs/index.html"

REQUIRED_TEXT = {
    "core question": "지금 AI 인프라 기대치는 2035 펀더멘털보다 앞서 있는가?",
    "one-line answer": "2035 기준선 대비 현재 내재 기대치는 중립권",
    "how to read": "How to read this",
    "deterministic label": "deterministic FLP-0.1",
    "base explanation": "Base는 현재 관측 가능한 제약을 반영한 정상 경로",
    "upside explanation": "Upside는 병목 완화가 빨라지는 경로",
    "downside explanation": "Downside는 병목이 오래 지속되는 경로",
    "current explanation": "Current implied는 현재 시장·정책·투자 기대가 암시하는 경로",
    "binding constraint": "Binding constraint",
    "signal badge": "signal-badge",
    "calculation transparency": "Calculation transparency",
    "deterministic output": "Deterministic output",
    "analyst interpretation": "Analyst interpretation",
    "regeneration order": "generator → copy docs assets → audit",
    "local preview": "python3 -m http.server 8000 --directory docs",
}

REQUIRED_STRUCTURE = {
    "summary cards": r"aria-label=\"2035 summary cards\"",
    "chart heading": r"id=\"chart-title\"",
    "data table caption": r"<caption>",
    "error state": r"data load failed|데이터 로드 실패",
    "mobile media query": r"@media \(max-width: 860px\)",
    "korean chart alt": r"alt=\"[^\"]*펀더멘털[^\"]*\"",
    "methodology link": r"fundamental_line_prediction\.md",
    "svg link": r"flp_ai_infra\.svg",
    "csv link": r"flp_ai_infra_calculated\.csv",
}


def main() -> int:
    errors: list[str] = []
    if not INDEX.exists():
        errors.append("missing docs/index.html")
        print(f"Pages UX audit errors: {len(errors)}")
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
        return 1

    text = INDEX.read_text(encoding="utf-8", errors="ignore")
    for label, token in REQUIRED_TEXT.items():
        if token not in text:
            errors.append(f"missing UX text: {label} -> {token}")
    for label, pattern in REQUIRED_STRUCTURE.items():
        if not re.search(pattern, text, flags=re.I | re.S):
            errors.append(f"missing UX structure: {label}")

    print(f"Pages UX audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
