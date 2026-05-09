#!/usr/bin/env python3
"""Audit repo-native advisory guide/onboarding artifacts."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
GUIDE = ROOT / "docs/user_guide_advisory_report.md"
README = ROOT / "README.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
AGENTS = ROOT / "AGENTS.md"
PAGES = ROOT / "docs/index.html"

GUIDE_TOKENS = {
    "title": "World Model 2035 Repository – User Guide & Advisory Report",
    "purpose": "프로젝트 목표",
    "core thesis": "핵심 주장",
    "principles": "리포지토리 기본 원칙",
    "structure": "구조: 디렉토리와 핵심 문서 이해",
    "usage": "사용법: 리포지토리에서 정보 찾고 활용하기",
    "prediction log": "예측 로그 활용",
    "freshness": "정보 신선도 확인 및 갱신 참여",
    "advice": "효과적으로 활용하기 위한 조언",
    "limits": "한계와 개선 방향",
    "socratic": "소크라테스식 질문",
    "mva": "아리스토텔레스식 실행",
    "conclusion": "결론",
    "methodology link": "../METHODOLOGY.md",
    "predictions link": "../14_predictions_log/2026_predictions.md",
}

ENTRY_LINK = "docs/user_guide_advisory_report.md"
PAGES_LINK = "user_guide_advisory_report.md"


def contains(path: Path, token: str) -> bool:
    return path.exists() and token in path.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    errors: list[str] = []
    if not GUIDE.exists():
        errors.append("missing docs/user_guide_advisory_report.md")
    else:
        text = GUIDE.read_text(encoding="utf-8", errors="ignore")
        for label, token in GUIDE_TOKENS.items():
            if token not in text:
                errors.append(f"guide missing {label}: {token}")
        if len(re.findall(r"^## ", text, flags=re.M)) < 8:
            errors.append("guide should have at least 8 second-level sections")

    for path, name in ((README, "README"), (CONTRIBUTING, "CONTRIBUTING"), (AGENTS, "AGENTS")):
        if not contains(path, ENTRY_LINK):
            errors.append(f"{name} missing guide link {ENTRY_LINK}")

    if not contains(PAGES, PAGES_LINK):
        errors.append(f"Pages app missing guide link {PAGES_LINK}")
    if not contains(PAGES, "How to use this repo"):
        errors.append("Pages app missing 'How to use this repo' entry point")

    print(f"Advisory guide audit errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors:
            print(f"- {err}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
