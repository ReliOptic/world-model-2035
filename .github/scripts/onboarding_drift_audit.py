#!/usr/bin/env python3
"""Audit cross-file onboarding consistency and FLP-vs-repo navigation separation."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CHECKS = {
    "README.md": ["Onboarding", "docs/onboarding/reader_contributor_analyst_paths.md"],
    "CONTRIBUTING.md": ["close evidence", "docs/onboarding/close_evidence_checklist.md"],
    "AGENTS.md": ["sector", "docs/onboarding/sector_how_to_use_template.md"],
    "docs/user_guide_advisory_report.md": ["reader_contributor_analyst_paths.md", "sector_how_to_use_template.md"],
    "docs/design/world_model_navigation_prd.md": ["World Model landing page", "FLP pilot viewer", "not the whole repo navigation"],
    "docs/design/sector_index_design.md": ["Sector index grouping", "prediction-log link"],
    "docs/design/prediction_freshness_dashboards.md": ["Prediction dashboard", "Freshness dashboard"],
}

ANTI_DRIFT = {
    "docs/design/world_model_navigation_prd.md": ["FLP app is not the whole repository", "implementation blocked"],
    "docs/onboarding/reader_contributor_analyst_paths.md": ["Reader path", "Contributor path", "Analyst path"],
    "docs/onboarding/close_evidence_checklist.md": ["Do not close", "audit evidence"],
}


def main() -> int:
    errors: list[str] = []
    for rel, tokens in CHECKS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing drift target: {rel}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in tokens:
            if token not in text:
                errors.append(f"{rel} missing consistency token: {token}")
    for rel, tokens in ANTI_DRIFT.items():
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in tokens:
            if token not in text:
                errors.append(f"{rel} missing anti-drift token: {token}")

    print(f"Onboarding drift audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
