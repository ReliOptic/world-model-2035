#!/usr/bin/env python3
"""Audit internal markdown links and optionally normalize bare connection bullets.

Checks:
- conventional markdown links whose local target does not exist
- bare connection bullets such as `- [../path/file.md]`

The fixer is intentionally conservative: it only converts single-item bullets that
contain one bracketed path and are not task-list checkboxes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDED_DIRS = {".git", ".omx", ".omc", "node_modules", "dist", "build", ".cache"}
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
BARE_BULLET_RE = re.compile(r"^(?P<indent>\s*)-\s+\[(?P<target>[^\]]+)\]\s*$")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "#")

# Known path migrations or shorthand aliases observed in the corpus.
REWRITES = {
    "../02_technology/ai_frontier.md": "../02_technology/foundation_models/agentic_os.md",
    "../06_geopolitics/02_china/tech_decoupling.md": "../06_geopolitics/02_china/semiconductor_self_reliance.md",
    "../09_corporate_roadmaps/openai.md": "../09_corporate_roadmaps/ai_labs/openai.md",
    "../07_defense/space_defense/": "../05_space/geopolitics_space/dual_use.md",
    "../11_science/biosecurity/": "../11_science/biosecurity/pandemic_early_warning.md",
    "../../07_defense/space_defense/": "../../05_space/geopolitics_space/dual_use.md",
}


def iter_markdown(root: Path):
    for path in root.rglob("*.md"):
        rel_parts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        yield path


def split_target(target: str) -> tuple[str, str]:
    """Return path part and suffix (`#anchor` or query) for a local target."""
    for sep in ("#", "?"):
        if sep in target:
            before, after = target.split(sep, 1)
            return before, sep + after
    return target, ""


def is_local_target(target: str) -> bool:
    stripped = target.strip()
    return bool(stripped) and not stripped.startswith(SKIP_SCHEMES)


def target_exists(source: Path, target: str) -> bool:
    path_part, _ = split_target(unquote(target.strip()))
    if not path_part:
        return True
    candidate = Path(path_part)
    if candidate.is_absolute():
        return candidate.exists()
    return (source.parent / candidate).resolve().exists()


def normalize_file(path: Path, rewrite_known: bool, fix_bare: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if rewrite_known:
        for old, new in REWRITES.items():
            text = text.replace(f"]({old})", f"]({new})")
            text = text.replace(f"[{old}]", f"[{new}]")

    if fix_bare:
        lines = []
        for line in text.splitlines():
            m = BARE_BULLET_RE.match(line)
            if not m:
                lines.append(line)
                continue
            target = m.group("target").strip()
            lowered = target.lower()
            if target in {"x", " ", ""} or lowered in {"x", "done"}:
                lines.append(line)
                continue
            if target.startswith(("x ", "X ")):
                lines.append(line)
                continue
            url = REWRITES.get(target, target) if rewrite_known else target
            lines.append(f"{m.group('indent')}- [{target}]({url})")
        # Preserve final newline if present.
        text = "\n".join(lines) + ("\n" if original.endswith("\n") else "")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def audit(root: Path) -> tuple[list[tuple[str, int, str]], list[tuple[str, int, str]]]:
    broken: list[tuple[str, int, str]] = []
    bare: list[tuple[str, int, str]] = []
    for path in iter_markdown(root):
        rel = path.relative_to(root).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
            m = BARE_BULLET_RE.match(line)
            if m:
                target = m.group("target").strip()
                if target not in {"x", " ", ""} and not target.startswith(("x ", "X ")):
                    bare.append((rel, lineno, target))
            for label, target in MD_LINK_RE.findall(line):
                target = target.strip()
                if not is_local_target(target):
                    continue
                if not target_exists(path, target):
                    broken.append((rel, lineno, target))
    return broken, bare


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix-bare", action="store_true", help="Convert bare `- [path]` bullets to markdown links")
    parser.add_argument("--rewrite-known", action="store_true", help="Apply known stale path rewrites")
    args = parser.parse_args()

    changed = 0
    if args.fix_bare or args.rewrite_known:
        for path in iter_markdown(REPO_ROOT):
            changed += int(normalize_file(path, args.rewrite_known, args.fix_bare))

    broken, bare = audit(REPO_ROOT)
    print(f"Files changed: {changed}")
    print(f"Bare connection bullets: {len(bare)}")
    print(f"Broken internal links: {len(broken)}")

    if bare:
        print("\n## Bare connection bullets")
        for rel, line, target in bare[:200]:
            print(f"{rel}:{line}: [{target}]")
        if len(bare) > 200:
            print(f"... {len(bare) - 200} more")
    if broken:
        print("\n## Broken internal links")
        for rel, line, target in broken[:200]:
            print(f"{rel}:{line}: {target}")
        if len(broken) > 200:
            print(f"... {len(broken) - 200} more")
    return 1 if broken or bare else 0


if __name__ == "__main__":
    sys.exit(main())
