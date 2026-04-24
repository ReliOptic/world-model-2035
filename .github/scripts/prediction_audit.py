#!/usr/bin/env python3
"""Scan 2026_predictions.md for entries whose evaluation window has closed.

Outputs:
- Writes pipe-separated records of due predictions to `$RUNNER_TEMP/due_predictions.txt`
- Emits GitHub Actions output `due_count`
"""
from __future__ import annotations

import os
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TODAY = date.today()
PRED_FILE = REPO_ROOT / "14_predictions_log" / "2026_predictions.md"

ROW_RE = re.compile(
    r"\|\s*(P26-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*"
    r"by\s*`(\d{4}-\d{2}-\d{2})`\s*\|\s*`(\d+)%`\s*\|\s*`([^`]+)`\s*\|\s*"
    r"(pending|Hit|Miss|Mixed|Unscorable)\s*\|"
)


def write_output(key: str, value: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as handle:
        handle.write(f"{key}={value}\n")


def output_path() -> Path:
    base = os.environ.get("RUNNER_TEMP") or "/tmp"
    return Path(base) / "due_predictions.txt"


def sanitize(text: str) -> str:
    return text.replace("|", "/").replace("\n", " ").strip()


def main() -> int:
    if not PRED_FILE.exists():
        print(f"No prediction file at {PRED_FILE}")
        write_output("due_count", "0")
        return 0

    text = PRED_FILE.read_text(encoding="utf-8")
    due = []

    for match in ROW_RE.finditer(text):
        pid, topic, statement, deadline_str, confidence, source, status = match.groups()
        if status.strip() != "pending":
            continue
        year, month, day = map(int, deadline_str.split("-"))
        deadline = date(year, month, day)
        if deadline > TODAY:
            continue
        due.append(
            (
                pid.strip(),
                sanitize(topic),
                sanitize(statement),
                deadline_str,
                confidence.strip(),
                sanitize(source),
            )
        )

    op = output_path()
    op.parent.mkdir(parents=True, exist_ok=True)
    with op.open("w", encoding="utf-8") as handle:
        for row in due:
            handle.write("|".join(row) + "\n")

    write_output("due_count", str(len(due)))
    write_output("output_path", str(op))
    print(f"Predictions due for resolution: {len(due)}")
    for row in due:
        print(f"  {row[0]} {row[3]} -> {row[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
