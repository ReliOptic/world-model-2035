#!/usr/bin/env python3
"""Audit the deployed root GitHub Pages landing page."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
INDEX = ROOT / "index.html"

REQUIRED_TOKENS = {
    "meta description": '<meta name="description"',
    "canonical pages link": 'https://relioptic.github.io/world-model-2035/',
    "correct repo link": 'https://github.com/ReliOptic/world-model-2035',
    "how to use link": 'docs/user_guide_advisory_report.md',
    "onboarding paths link": 'docs/onboarding/reader_contributor_analyst_paths.md',
    "sector template link": 'docs/onboarding/sector_how_to_use_template.md',
    "FLP pilot link": 'docs/index.html',
    "methodology link": 'METHODOLOGY.md',
    "predictions link": '14_predictions_log/2026_predictions.md',
    "freshness dashboard design link": 'docs/design/prediction_freshness_dashboards.md',
    "skip link": 'class="skip-link"',
    "quick links section": 'id="start-here"',
    "start copy": 'Start here',
}

FORBIDDEN = [
    "github.com/ReliOptic/world-in-2035",
    "00_foundations/methodology.md",
]


def main() -> int:
    errors: list[str] = []
    if not INDEX.exists():
        errors.append("missing root index.html")
    else:
        text = INDEX.read_text(encoding="utf-8", errors="ignore")
        for label, token in REQUIRED_TOKENS.items():
            if token not in text:
                errors.append(f"missing landing token: {label} -> {token}")
        for token in FORBIDDEN:
            if token in text:
                errors.append(f"forbidden stale landing token: {token}")
        if not re.search(r"<a[^>]+href=\"#hero\"[^>]*>\s*Skip", text, flags=re.I | re.S):
            errors.append("skip link should target #hero and say Skip")

    print(f"Pages landing audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
