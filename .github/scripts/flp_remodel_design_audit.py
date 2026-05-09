#!/usr/bin/env python3
"""Audit design-first acceptance criteria for the FLP UX remodel issues."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DESIGN_DIR = ROOT / "docs/design"
FILES = {
    "visual metaphor": DESIGN_DIR / "flp_visual_metaphor.md",
    "above fold": DESIGN_DIR / "flp_above_fold_composition.md",
    "interaction model": DESIGN_DIR / "flp_interaction_model.md",
    "audit gates": DESIGN_DIR / "flp_remodel_ux_audit_gates.md",
}

REQUIRED_TOKENS = {
    "visual metaphor": [
        "Primary visual object",
        "Constrained Path",
        "Demand",
        "Capacity",
        "Finance",
        "Current implied line",
        "Divergence corridor",
        "Rejected metaphors",
    ],
    "above fold": [
        "Above-the-fold hierarchy",
        "Line/gap visual first",
        "Headline",
        "Subtitle",
        "Signal",
        "Binding bottleneck",
        "Moves below the fold",
        "ASCII wireframe",
    ],
    "interaction model": [
        "Hover year",
        "Scenario toggle",
        "Bottleneck inspection",
        "Formula reveal",
        "Mobile fallback",
    ],
    "audit gates": [
        "fundamental line visual is primary",
        "divergence is visually represented",
        "table/prose are below",
        "interaction hooks exist",
        "stale dashboard patterns are absent",
        "Future implementation audit contract",
    ],
}

CROSS_DOC_TOKENS = ["#21", "#22", "#23", "#24", "#25", "Do not implement the remodel"]


def main() -> int:
    errors: list[str] = []
    combined = ""
    for label, path in FILES.items():
        if not path.exists():
            errors.append(f"missing {label} design doc: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        combined += "\n" + text
        for token in REQUIRED_TOKENS[label]:
            if token not in text:
                errors.append(f"{path.relative_to(ROOT)} missing token: {token}")
        if "## 연결 문서" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing 연결 문서")
        if "## 정보 출처" not in text:
            errors.append(f"{path.relative_to(ROOT)} missing 정보 출처")

    for token in CROSS_DOC_TOKENS:
        if token not in combined:
            errors.append(f"design package missing cross-doc token: {token}")

    # Ensure at least two rejected metaphors are explicitly listed.
    visual = FILES["visual metaphor"]
    if visual.exists():
        text = visual.read_text(encoding="utf-8", errors="ignore")
        rejected = re.findall(r"^- \*\*Rejected:", text, flags=re.M)
        if len(rejected) < 2:
            errors.append("visual metaphor doc must list at least 2 rejected metaphors")

    print(f"FLP remodel design audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
