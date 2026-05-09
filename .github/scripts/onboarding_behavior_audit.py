#!/usr/bin/env python3
"""Audit behavior-oriented onboarding artifacts for World Model 2035."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ONBOARDING = ROOT / "docs/onboarding"
DESIGN = ROOT / "docs/design"

FILES = {
    "paths": ONBOARDING / "reader_contributor_analyst_paths.md",
    "sector template": ONBOARDING / "sector_how_to_use_template.md",
    "domain protocols": ONBOARDING / "domain_forecast_protocols.md",
    "failure modes": ONBOARDING / "sector_failure_modes.md",
    "close checklist": ONBOARDING / "close_evidence_checklist.md",
    "navigation prd": DESIGN / "world_model_navigation_prd.md",
    "sector index": DESIGN / "sector_index_design.md",
    "dashboards": DESIGN / "prediction_freshness_dashboards.md",
}

REQUIRED = {
    "paths": [
        "Reader path",
        "Contributor path",
        "Analyst path",
        "open an issue",
        "run audits",
        "prediction log",
        "close with evidence",
    ],
    "sector template": [
        "How to use this sector",
        "Current state",
        "Official roadmap",
        "Base / Upside / Downside",
        "Bottlenecks",
        "Prediction candidates",
        "When to open a sector issue",
    ],
    "domain protocols": [
        "Common protocol",
        "Technology and infrastructure",
        "Geopolitics",
        "Labor and economics",
        "Biotech and health",
        "Climate, science, and international organizations",
    ],
    "failure modes": [
        "Reject conditions",
        "source-free forecast",
        "missing Base/Upside/Downside",
        "missing prediction-log candidate",
        "stale source",
        "dashboard-summary drift",
    ],
    "close checklist": [
        "Close evidence checklist",
        "Changed files",
        "Audit commands",
        "Known gaps",
        "Prediction-log impact",
        "stale/insufficient",
    ],
    "navigation prd": [
        "World Model landing page",
        "FLP pilot viewer",
        "separate roles",
        "implementation blocked",
        "sector index",
        "predictions",
        "freshness",
    ],
    "sector index": [
        "Sector index grouping",
        "sector",
        "core question",
        "latest freshness",
        "key bottleneck",
        "prediction-log link",
        "roadmap",
    ],
    "dashboards": [
        "Prediction dashboard",
        "Freshness dashboard",
        "pending",
        "Hit",
        "Miss",
        "Mixed",
        "Unscorable",
        "green/yellow/red",
    ],
}

ENTRY_POINTS = {
    "README.md": "docs/onboarding/reader_contributor_analyst_paths.md",
    "CONTRIBUTING.md": "docs/onboarding/close_evidence_checklist.md",
    "AGENTS.md": "docs/onboarding/sector_how_to_use_template.md",
    "docs/user_guide_advisory_report.md": "docs/onboarding/reader_contributor_analyst_paths.md",
}


def main() -> int:
    errors: list[str] = []
    for label, path in FILES.items():
        if not path.exists():
            errors.append(f"missing {label}: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in REQUIRED[label]:
            if token not in text:
                errors.append(f"{path.relative_to(ROOT)} missing token: {token}")
        for common in ("**정보 신선도:**", "## 연결 문서", "## 정보 출처"):
            if common not in text:
                errors.append(f"{path.relative_to(ROOT)} missing {common}")

    for rel, token in ENTRY_POINTS.items():
        path = ROOT / rel
        if not path.exists() or token not in path.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"{rel} missing onboarding link token: {token}")

    print(f"Onboarding behavior audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
