#!/usr/bin/env python3
"""Audit source sections and optionally sample URL reachability.

The default mode is deterministic and network-free. `--check-urls` performs a
bounded HTTP reachability sample for high-risk domains or all files.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import re
import socket
import ssl
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
EXCLUDED_DIRS = {".git", ".omx", ".omc", "node_modules", "dist", "build", ".cache", ".github"}
EXCLUDED_FILES = {"README.md", "METHODOLOGY.md", "CLAUDE.md", "CONTRIBUTING.md", "progress.md", "The world in 2035.md"}
URL_RE = re.compile(r"https?://[^\s\])>]+")
HIGH_RISK_PATH_MARKERS = (
    "semiconductors",
    "foundation_models",
    "geopolitics",
    "tipping_points",
    "fission_smr",
    "fusion",
    "labor_markets",
    "climate_science",
)
LOW_AUTHORITY_DOMAINS = (
    "wikipedia.org",
    "phonearena.com",
    "teslarati.com",
    "techspot.com",
    "tomshardware.com",
    "interestingengineering.com",
    "carboncredits.com",
    "markets.financialcontent.com",
    "marketwise.com",
    "awesomeagents.ai",
    "dprk.news-pravda.com",
)

@dataclass(frozen=True)
class UrlRecord:
    file: str
    url: str


def iter_markdown():
    for path in REPO_ROOT.rglob("*.md"):
        rel_parts = path.relative_to(REPO_ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        yield path


def source_text(text: str) -> str:
    return text.split("## 정보 출처", 1)[1] if "## 정보 출처" in text else ""


def domain(url: str) -> str:
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def is_high_risk(rel: str) -> bool:
    return any(marker in rel for marker in HIGH_RISK_PATH_MARKERS)


def collect_urls(high_risk_only: bool) -> tuple[list[str], list[str], list[UrlRecord]]:
    errors: list[str] = []
    warnings: list[str] = []
    records: list[UrlRecord] = []
    for path in iter_markdown():
        rel = path.relative_to(REPO_ROOT).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "## 정보 출처" not in text:
            errors.append(f"{rel}: missing source section")
            continue
        sec = source_text(text)
        urls = URL_RE.findall(sec)
        if not urls and not rel.startswith(("00_foundations/", "14_predictions_log/")):
            errors.append(f"{rel}: source section has no URL")
        if is_high_risk(rel):
            suspicious = sorted({u for u in urls if any(domain(u).endswith(d) for d in LOW_AUTHORITY_DOMAINS)})
            if suspicious:
                warnings.append(f"{rel}: high-risk file uses lower-authority source(s): {', '.join(domain(u) for u in suspicious[:5])}")
        if not high_risk_only or is_high_risk(rel):
            records.extend(UrlRecord(rel, u) for u in urls)
    return errors, warnings, records


def check_url(record: UrlRecord, timeout: float) -> tuple[UrlRecord, str]:
    ctx = ssl._create_unverified_context()  # noqa: SLF001 - reachability audit, not trust validation
    for method in ("HEAD", "GET"):
        try:
            req = Request(record.url, headers={"User-Agent": "Mozilla/5.0 (compatible; world-model-2035-audit/1.0)"}, method=method)
            with urlopen(req, timeout=timeout, context=ctx) as resp:
                code = getattr(resp, "status", 200)
                if 200 <= code < 400:
                    return record, f"ok:{code}"
                if code in (403, 405) and method == "HEAD":
                    continue
                return record, f"http:{code}"
        except HTTPError as exc:
            if exc.code in (403, 405, 429) and method == "HEAD":
                continue
            # 403/429 often means bot-blocked but reachable; flag soft.
            if exc.code in (403, 429):
                return record, f"blocked:{exc.code}"
            return record, f"http:{exc.code}"
        except (URLError, TimeoutError, socket.timeout) as exc:
            if method == "HEAD":
                continue
            return record, f"error:{type(exc).__name__}"
        except Exception as exc:  # noqa: BLE001 - audit should report unexpected failures
            if method == "HEAD":
                continue
            return record, f"error:{type(exc).__name__}"
    return record, "error:unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-urls", action="store_true", help="Perform bounded network reachability checks")
    parser.add_argument("--high-risk-only", action="store_true", help="Restrict URL collection/checks to high-risk topic paths")
    parser.add_argument("--limit", type=int, default=0, help="Max unique URLs to check when --check-urls is set")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()

    errors, warnings, records = collect_urls(args.high_risk_only)
    # Deduplicate while preserving first file association.
    seen: set[str] = set()
    unique: list[UrlRecord] = []
    for rec in records:
        if rec.url in seen:
            continue
        seen.add(rec.url)
        unique.append(rec)
    if args.limit:
        unique = unique[: args.limit]

    print(f"Source-section errors: {len(errors)}")
    print(f"Source-quality warnings: {len(warnings)}")
    print(f"Unique URLs collected: {len(unique)}")
    if errors:
        print("\n## Errors")
        for item in errors[:200]:
            print(f"- {item}")
    if warnings:
        print("\n## Warnings")
        for item in warnings[:200]:
            print(f"- {item}")

    url_failures: list[str] = []
    url_soft: list[str] = []
    if args.check_urls and unique:
        with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
            futs = [pool.submit(check_url, rec, args.timeout) for rec in unique]
            for fut in futures.as_completed(futs):
                rec, status = fut.result()
                if status.startswith("ok:"):
                    continue
                line = f"{rec.file}: {status} {rec.url}"
                if status.startswith("blocked:"):
                    url_soft.append(line)
                else:
                    url_failures.append(line)
        print(f"URL hard failures: {len(url_failures)}")
        print(f"URL soft blocks: {len(url_soft)}")
        if url_failures:
            print("\n## URL hard failures")
            for item in url_failures[:200]:
                print(f"- {item}")
        if url_soft:
            print("\n## URL soft blocks")
            for item in url_soft[:100]:
                print(f"- {item}")

    return 1 if errors or url_failures else 0


if __name__ == "__main__":
    sys.exit(main())
