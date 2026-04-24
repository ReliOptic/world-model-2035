#!/usr/bin/env python3
"""Audit markdown files for freshness and update status indicators in-place.

Rules:
- status becomes 🟢 when today's month is on or before the file's `다음 갱신` month
- status becomes 🟡 when today is up to 3 months past the `다음 갱신` month
- status becomes 🔴 when today is more than 3 months past the `다음 갱신` month

Outputs:
- Rewrites the `**정보 신선도:**` header of each file whose status is incorrect
- Writes a markdown report of stale (🟡 / 🔴) files to `$RUNNER_TEMP/freshness_report.md`
- Emits GitHub Actions outputs `changed` and `stale_count`
"""
from __future__ import annotations

import os
import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TODAY = date.today()
HEADER_RE = re.compile(
    r"(\*\*정보 신선도:\*\*\s*)(🟢|🟡|🔴)(\s*\|\s*\*\*최종 갱신:\*\*\s*)"
    r"(\d{4}-\d{2})(\s*\|\s*\*\*다음 갱신:\*\*\s*)(\d{4}-\d{2})"
)

EXCLUDED_DIRS = {".git", "node_modules", ".github", ".omc"}
EXCLUDED_FILES = {
    "README.md",
    "METHODOLOGY.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "MEMORY.md",
    "The world in 2035.md",
    "progress.md",
    "file_template.md",
}


def parse_ym(ym: str) -> date:
    year, month = map(int, ym.split("-"))
    return date(year, month, 1)


def months_delta(target: date, anchor: date) -> int:
    return (target.year - anchor.year) * 12 + (target.month - anchor.month)


def correct_status(next_ym: date) -> str:
    delta = months_delta(TODAY, next_ym)
    if delta <= 0:
        return "🟢"
    if delta <= 3:
        return "🟡"
    return "🔴"


def write_output(key: str, value: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as handle:
        handle.write(f"{key}={value}\n")


def report_path() -> Path:
    base = os.environ.get("RUNNER_TEMP") or "/tmp"
    return Path(base) / "freshness_report.md"


def iter_markdown(root: Path):
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        yield path


def main() -> int:
    changed: list[tuple[str, str]] = []
    stale: list[tuple[str, str, str]] = []

    for path in iter_markdown(REPO_ROOT):
        text = path.read_text(encoding="utf-8")
        match = HEADER_RE.search(text)
        if not match:
            continue

        pre1, current_status, pre2, last_ym, pre3, next_ym_str = match.groups()
        next_ym = parse_ym(next_ym_str)
        target = correct_status(next_ym)
        rel = path.relative_to(REPO_ROOT).as_posix()

        if target != current_status:
            new_text = (
                text[: match.start()]
                + pre1
                + target
                + pre2
                + last_ym
                + pre3
                + next_ym_str
                + text[match.end() :]
            )
            path.write_text(new_text, encoding="utf-8")
            changed.append((rel, f"{current_status} -> {target}"))
            current_status = target

        if current_status in ("🟡", "🔴"):
            stale.append((rel, current_status, next_ym_str))

    stale.sort(key=lambda item: (item[1] == "🟡", item[2], item[0]))

    rp = report_path()
    rp.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    lines.append(f"# Freshness audit {TODAY.isoformat()}")
    lines.append("")
    lines.append(
        f"Scanned {sum(1 for _ in iter_markdown(REPO_ROOT))} markdown files. "
        f"Status auto-updated on {len(changed)} files. "
        f"{len(stale)} files remain in 🟡 or 🔴 status."
    )
    lines.append("")
    if changed:
        lines.append("## Status transitions applied")
        for rel, transition in sorted(changed):
            lines.append(f"- `{rel}` ({transition})")
        lines.append("")
    if stale:
        lines.append("## Files needing refresh")
        lines.append("")
        lines.append("| Status | Next due | File |")
        lines.append("|---|---|---|")
        for rel, status, next_ym_str in stale:
            lines.append(f"| {status} | {next_ym_str} | `{rel}` |")
    else:
        lines.append("All files are 🟢. No refresh needed this cycle.")
    rp.write_text("\n".join(lines) + "\n", encoding="utf-8")

    write_output("changed", "true" if changed else "false")
    write_output("stale_count", str(len(stale)))
    write_output("report_path", str(rp))

    print(f"Changed headers: {len(changed)}")
    print(f"Stale (🟡/🔴) files: {len(stale)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
