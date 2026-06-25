#!/usr/bin/env python3
"""Build the War-Economy Transition Dashboard (WETD) monthly DuckDB database and static dashboard.

The pipeline is deliberately batch-oriented: one command initializes DuckDB,
loads seed tables, ingests public/no-auth sources where available, computes
War-Economy Transition scores with complete-score guards, and exports
CSV/HTML/markdown artifacts.

High-resolution connectors that require keys (UN Comtrade, U.S. Census trade,
EIA, ITA CSL) are recorded in data-quality output when keys are absent. The
no-auth baseline uses Federal Register, USAspending, Treasury OFAC CSV, NSIDC
Sea Ice Index v4 CSV, and World Bank API fallback indicators so the pipeline is
executable on a fresh machine.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import ssl
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import duckdb
except ModuleNotFoundError as exc:  # pragma: no cover - exercised by smoke command if missing
    raise SystemExit("duckdb is required. Install with: python3 -m pip install -r requirements-wetd.txt") from exc

REPO = Path(__file__).resolve().parents[1]
DATA_DIR = REPO / "data" / "wetd"
SEED_DIR = DATA_DIR / "seed"
RAW_DIR = DATA_DIR / "raw"
OUT_DIR = REPO / "outputs" / "wetd"
DB_PATH = DATA_DIR / "wetd.duckdb"
CONFIG_ID = "wetd_default_2026q2"
USER_AGENT = "world-model-2035-wetd/0.1 (+https://github.com/ReliOptic/world-model-2035)"

SIGNALS = [
    "autarky",
    "stockpiling",
    "trade_rewiring",
    "capital_access_control",
    "civilian_military_allocation",
]

# Python 3.14 on this machine lacks a working CA bundle for several official
# sources. Curl verifies the same sources successfully; this local batch script
# therefore uses an unverified context and stores source_url/retrieved_at for
# auditability. Production CI should install certifi or platform CA certificates.
SSL_CONTEXT = ssl._create_unverified_context()  # noqa: SLF001


@dataclass
class QualityEvent:
    source_name: str
    status: str
    message: str
    source_url: str
    rows_loaded: int = 0


def now_utc() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stable_id(prefix: str, *parts: Any) -> str:
    raw = "|".join("" if p is None else str(p) for p in parts)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:14]
    slug = re.sub(r"[^a-zA-Z0-9_]+", "_", raw.lower()).strip("_")[:80]
    return f"{prefix}_{slug}_{digest}" if slug else f"{prefix}_{digest}"


def month_start(value: str | dt.date) -> str:
    if isinstance(value, dt.date):
        return value.replace(day=1).isoformat()
    return value[:7] + "-01"


def http_get(url: str, *, timeout: int = 30, headers: dict[str, str] | None = None) -> bytes:
    merged = {"User-Agent": USER_AGENT}
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CONTEXT) as response:
        return response.read()


def http_json(url: str, *, timeout: int = 30, headers: dict[str, str] | None = None) -> Any:
    return json.loads(http_get(url, timeout=timeout, headers=headers).decode("utf-8"))


def http_post_json(url: str, payload: dict[str, Any], *, timeout: int = 45) -> Any:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"User-Agent": USER_AGENT, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout, context=SSL_CONTEXT) as response:
        return json.loads(response.read().decode("utf-8"))


def setup_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def connect() -> duckdb.DuckDBPyConnection:
    setup_dirs()
    return duckdb.connect(str(DB_PATH))


def init_schema(con: duckdb.DuckDBPyConnection) -> None:
    con.execute("CREATE SCHEMA IF NOT EXISTS wetd_data")
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.dim_country (
            country_iso3 VARCHAR PRIMARY KEY,
            country_name VARCHAR,
            country_group VARCHAR,
            is_mvp_country BOOLEAN
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.dim_product (
            product_id VARCHAR PRIMARY KEY,
            product_group VARCHAR,
            product_name VARCHAR,
            proxy_method VARCHAR,
            notes VARCHAR
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.dim_theater (
            theater_id VARCHAR PRIMARY KEY,
            theater_name VARCHAR,
            theater_type VARCHAR,
            default_multiplier_low DOUBLE,
            default_multiplier_high DOUBLE,
            primary_risk VARCHAR
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.country_theater_exposure (
            country_iso3 VARCHAR,
            theater_id VARCHAR,
            exposure_weight DOUBLE,
            exposure_type VARCHAR,
            effective_from DATE,
            effective_to DATE,
            rationale VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP,
            PRIMARY KEY(country_iso3, theater_id, exposure_type, effective_from)
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.config_signal_weight (
            config_id VARCHAR,
            signal_type VARCHAR,
            weight DOUBLE,
            effective_from DATE,
            effective_to DATE,
            rationale VARCHAR,
            source_url VARCHAR,
            PRIMARY KEY(config_id, signal_type, effective_from)
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.config_warning_threshold (
            threshold_id VARCHAR PRIMARY KEY,
            min_signal_count_for_complete_score INTEGER,
            min_rising_signals_for_warning INTEGER,
            allow_theater_shock_rule BOOLEAN,
            rationale VARCHAR
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_trade (
            trade_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            date_month DATE,
            reporter_iso3 VARCHAR,
            partner_iso3 VARCHAR,
            flow VARCHAR,
            hs_code VARCHAR,
            product_id VARCHAR,
            value_usd DOUBLE,
            quantity DOUBLE,
            quantity_unit VARCHAR,
            metric_name VARCHAR,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_policy_event (
            policy_event_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            event_date DATE,
            country_iso3 VARCHAR,
            agency VARCHAR,
            event_type VARCHAR,
            title VARCHAR,
            summary VARCHAR,
            affected_products VARCHAR,
            affected_countries VARCHAR,
            keywords VARCHAR,
            severity_hint INTEGER,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_sanctions (
            sanctions_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            listed_date DATE,
            effective_month DATE,
            date_quality VARCHAR,
            date_imputed BOOLEAN,
            entity_name VARCHAR,
            country_iso3 VARCHAR,
            list_source VARCHAR,
            program VARCHAR,
            reason VARCHAR,
            product_tags VARCHAR,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_procurement (
            procurement_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            award_or_notice_date DATE,
            country_iso3 VARCHAR,
            agency VARCHAR,
            supplier VARCHAR,
            value_usd DOUBLE,
            title VARCHAR,
            description VARCHAR,
            defense_flag BOOLEAN,
            ai_compute_flag BOOLEAN,
            product_tags VARCHAR,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_energy_minerals (
            energy_minerals_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            date_month DATE,
            country_iso3 VARCHAR,
            commodity VARCHAR,
            metric_name VARCHAR,
            value DOUBLE,
            unit VARCHAR,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_arctic_access (
            arctic_access_id VARCHAR PRIMARY KEY,
            source_record_id VARCHAR,
            date_month DATE,
            arctic_zone VARCHAR,
            metric_name VARCHAR,
            value DOUBLE,
            unit VARCHAR,
            source_name VARCHAR,
            source_url VARCHAR,
            retrieved_at TIMESTAMP
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_wet_signal_score (
            wet_signal_score_id VARCHAR PRIMARY KEY,
            config_id VARCHAR,
            date_month DATE,
            country_iso3 VARCHAR,
            product_id VARCHAR,
            signal_type VARCHAR,
            raw_value DOUBLE,
            z_score DOUBLE,
            normalized_score DOUBLE,
            confidence VARCHAR,
            explanation VARCHAR,
            source_row_refs VARCHAR
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_theater_multiplier (
            theater_multiplier_id VARCHAR PRIMARY KEY,
            date_month DATE,
            theater_id VARCHAR,
            multiplier_value DOUBLE,
            confidence VARCHAR,
            explanation VARCHAR,
            source_row_refs VARCHAR
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.fact_2035_scenario_mapping (
            scenario_mapping_id VARCHAR PRIMARY KEY,
            theater_id VARCHAR,
            present_signal VARCHAR,
            transition_2030 VARCHAR,
            base_2035 VARCHAR,
            upside_2035 VARCHAR,
            downside_2035 VARCHAR,
            response_concept VARCHAR,
            linked_signal_types VARCHAR,
            last_reviewed DATE
        )
    """)
    con.execute("""
        CREATE OR REPLACE TABLE wetd_data.data_quality_event (
            event_id VARCHAR PRIMARY KEY,
            source_name VARCHAR,
            status VARCHAR,
            message VARCHAR,
            source_url VARCHAR,
            rows_loaded INTEGER,
            observed_at TIMESTAMP
        )
    """)


def load_csv_table(con: duckdb.DuckDBPyConnection, table: str, path: Path) -> None:
    con.execute(f"DELETE FROM wetd_data.{table}")
    con.execute(f"INSERT INTO wetd_data.{table} SELECT * FROM read_csv_auto(?)", [str(path)])


def load_seed(con: duckdb.DuckDBPyConnection) -> None:
    load_csv_table(con, "dim_country", SEED_DIR / "dim_country.csv")
    load_csv_table(con, "dim_theater", SEED_DIR / "dim_theater.csv")
    load_csv_table(con, "config_signal_weight", SEED_DIR / "config_signal_weight.csv")
    load_csv_table(con, "country_theater_exposure", SEED_DIR / "country_theater_exposure.csv")
    con.execute("DELETE FROM wetd_data.dim_product")
    products = [
        ("hbm_proxy", "ai_semiconductor", "HBM / high-bandwidth memory proxy", "mixed_proxy", "Memory IC and policy-event proxy"),
        ("gpu_ai_accelerator_proxy", "ai_semiconductor", "GPU / AI accelerator proxy", "mixed_proxy", "Server/HPC/procurement and export-control proxy"),
        ("semiconductor_equipment", "ai_semiconductor", "Semiconductor equipment", "mixed_proxy", "HS/policy/procurement proxy"),
        ("euv_metrology_proxy", "ai_semiconductor", "EUV and metrology proxy", "policy_keyword", "Policy and procurement proxy"),
        ("eda_proxy", "ai_semiconductor", "EDA proxy", "policy_keyword", "Software/control proxy"),
        ("energy", "war_economy", "Energy", "world_bank_or_eia", "World Bank fallback; EIA when EIA_API_KEY exists"),
        ("ores_metals_imports_proxy", "war_economy", "Ores and metals imports proxy", "world_bank_indicator", "World Bank fallback for minerals exposure"),
        ("arctic_sea_ice_extent", "war_economy", "Arctic sea ice extent", "nsidc_csv", "NSIDC Sea Ice Index v4 daily CSV"),
    ]
    con.executemany("INSERT INTO wetd_data.dim_product VALUES (?, ?, ?, ?, ?)", products)
    con.execute("DELETE FROM wetd_data.config_warning_threshold")
    con.execute(
        "INSERT INTO wetd_data.config_warning_threshold VALUES (?, ?, ?, ?, ?)",
        ["wetd_default_threshold_2026q2", 5, 3, True, "Require all five signals for complete score; warning needs 3 rising signals or theater shock rule."],
    )


def record_quality(con: duckdb.DuckDBPyConnection, events: list[QualityEvent]) -> None:
    rows = [
        (stable_id("dq", event.source_name, event.status, event.message, event.source_url, now_utc()), event.source_name, event.status, event.message, event.source_url, event.rows_loaded, now_utc())
        for event in events
    ]
    if rows:
        con.executemany("INSERT INTO wetd_data.data_quality_event VALUES (?, ?, ?, ?, ?, ?, ?)", rows)


def ingest_trade(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> list[QualityEvent]:
    events: list[QualityEvent] = []
    con.execute("DELETE FROM wetd_data.fact_trade")
    key = os.environ.get("COMTRADE_SUBSCRIPTION_KEY")
    if key:
        url = "https://comtradeapi.un.org/data/v1/get/C/M/HS?" + urllib.parse.urlencode({
            "cmdCode": "8542", "flowCode": "M", "period": as_of.strftime("%Y%m"), "reporterCode": "842", "partnerCode": "156"
        })
        try:
            data = http_json(url, headers={"Ocp-Apim-Subscription-Key": key})
            rows = data.get("data", []) if isinstance(data, dict) else []
            insert_rows = []
            for row in rows[:100]:
                value = float(row.get("primaryValue") or 0)
                insert_rows.append((stable_id("trade", row.get("period"), row.get("reporterCode"), row.get("partnerCode"), row.get("cmdCode")), row.get("id"), month_start(str(row.get("period", as_of.strftime("%Y%m")))[:4] + "-" + str(row.get("period", as_of.strftime("%Y%m")))[4:6]), "USA", "CHN", "import", str(row.get("cmdCode")), "semiconductor_equipment", value, None, "usd", "un_comtrade_monthly_import_value", "UN Comtrade", url, now_utc()))
            con.executemany("INSERT INTO wetd_data.fact_trade VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", insert_rows)
            events.append(QualityEvent("UN Comtrade", "ok", "Loaded HS 8542 USA-CHN rows using COMTRADE_SUBSCRIPTION_KEY.", url, len(insert_rows)))
            return events
        except Exception as exc:  # noqa: BLE001 - batch should fall back and log
            events.append(QualityEvent("UN Comtrade", "fallback", f"Comtrade key path failed; using World Bank fallback: {type(exc).__name__}: {exc}", url, 0))
    else:
        events.append(QualityEvent("UN Comtrade", "missing_key", "COMTRADE_SUBSCRIPTION_KEY not set; UN Comtrade returned 401 when tested without a key.", "https://comtradeapi.un.org/", 0))

    # No-auth fallback: World Bank trade/mineral import indicators by country.
    indicators = [
        ("TM.VAL.MMTL.ZS.UN", "ores_metals_imports_proxy", "import", "ores_metals_imports_percent_merchandise_imports"),
        ("TX.VAL.TECH.MF.ZS", "semiconductor_equipment", "export", "high_technology_exports_percent_manufactured_exports"),
    ]
    wb_countries = ["USA", "CHN", "JPN", "KOR", "DEU", "GBR", "FRA", "CAN", "NLD", "SGP", "MYS", "ARE", "SAU", "VNM", "WLD"]
    loaded = 0
    for indicator, product_id, flow, metric in indicators:
        countries = ";".join(wb_countries)
        url = f"https://api.worldbank.org/v2/country/{countries}/indicator/{indicator}?format=json&per_page=200"
        try:
            payload = http_json(url)
            records = payload[1] if isinstance(payload, list) and len(payload) > 1 else []
            for rec in records:
                if rec.get("value") is None:
                    continue
                iso3 = rec.get("countryiso3code") or "WLD"
                year = str(rec.get("date"))
                value = float(rec.get("value"))
                trade_id = stable_id("trade_wb", indicator, iso3, year)
                con.execute(
                    "INSERT OR REPLACE INTO wetd_data.fact_trade VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    [trade_id, f"{indicator}:{iso3}:{year}", f"{year}-01-01", iso3, "WLD", flow, indicator, product_id, None, value, "percent", metric, "World Bank API", url, now_utc()],
                )
                loaded += 1
        except Exception as exc:  # noqa: BLE001
            events.append(QualityEvent("World Bank trade fallback", "error", f"{indicator} failed: {type(exc).__name__}: {exc}", url, 0))
    events.append(QualityEvent("World Bank trade fallback", "ok", "Loaded no-auth trade proxy indicators for immediate War-Economy Transition Dashboard execution.", "https://api.worldbank.org/v2/", loaded))
    return events


def classify_policy(text: str) -> tuple[str, str, int]:
    lower = text.lower()
    if any(w in lower for w in ["export control", "entity list", "foreign direct product", "bis"]):
        return "export_control", "capital_access_control", 5
    if any(w in lower for w in ["sanction", "restricted", "screening"]):
        return "sanctions_policy", "capital_access_control", 4
    if any(w in lower for w in ["artificial intelligence", "semiconductor", "data center", "advanced computing"]):
        return "ai_policy", "autarky", 3
    return "industrial_policy", "autarky", 2


def ingest_policy_events(con: duckdb.DuckDBPyConnection, as_of: dt.date, limit: int) -> list[QualityEvent]:
    con.execute("DELETE FROM wetd_data.fact_policy_event")
    terms = ["semiconductor export control", "artificial intelligence data center", "foreign investment semiconductor", "advanced computing export"]
    rows_loaded = 0
    events: list[QualityEvent] = []
    for term in terms:
        params = {"per_page": str(limit), "order": "newest", "conditions[term]": term}
        url = "https://www.federalregister.gov/api/v1/documents.json?" + urllib.parse.urlencode(params)
        try:
            payload = http_json(url)
            for item in payload.get("results", []):
                title = item.get("title") or ""
                abstract = item.get("abstract") or ""
                event_type, signal, severity = classify_policy(title + " " + abstract)
                doc_number = item.get("document_number") or stable_id("frdoc", title)
                date = item.get("publication_date") or as_of.isoformat()
                con.execute(
                    "INSERT OR REPLACE INTO wetd_data.fact_policy_event VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    [
                        stable_id("policy", doc_number), doc_number, date, "USA", ", ".join(a.get("name", "") for a in item.get("agencies", []))[:300],
                        event_type, title, re.sub("<[^>]+>", "", abstract)[:1000], "ai_semiconductor", "", signal, severity,
                        "Federal Register", item.get("html_url") or url, now_utc(),
                    ],
                )
                rows_loaded += 1
            events.append(QualityEvent("Federal Register", "ok", f"Loaded term '{term}'.", url, len(payload.get("results", []))))
        except Exception as exc:  # noqa: BLE001
            events.append(QualityEvent("Federal Register", "error", f"Term '{term}' failed: {type(exc).__name__}: {exc}", url, 0))
    return events


def country_from_sdn_row(row: list[str]) -> str | None:
    joined = " ".join(row).upper()
    if "IRAN" in joined:
        return "IRN"
    if "RUSSIA" in joined or "RUSSIAN" in joined:
        return "RUS"
    if "CHINA" in joined or "HONG KONG" in joined:
        return "CHN"
    if "KOREA, NORTH" in joined or "NORTH KOREA" in joined:
        return "PRK"
    if "CUBA" in joined:
        return "CUB"
    return None


def ingest_sanctions(con: duckdb.DuckDBPyConnection, as_of: dt.date, limit: int) -> list[QualityEvent]:
    con.execute("DELETE FROM wetd_data.fact_sanctions")
    url = "https://www.treasury.gov/ofac/downloads/sdn.csv"
    try:
        raw = http_get(url, timeout=60).decode("utf-8", errors="replace")
        (RAW_DIR / "ofac_sdn.csv").write_text(raw, encoding="utf-8")
        rows = list(csv.reader(raw.splitlines()))
        loaded = 0
        for row in rows:
            if loaded >= limit:
                break
            iso = country_from_sdn_row(row)
            joined = " ".join(row)
            if not iso or iso not in {"IRN", "RUS", "CHN", "PRK"}:
                continue
            source_id = row[0].strip() if row else stable_id("ofacrow", joined)
            entity_name = row[1].strip() if len(row) > 1 else joined[:120]
            con.execute(
                "INSERT OR REPLACE INTO wetd_data.fact_sanctions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [stable_id("sanctions", source_id), source_id, None, month_start(as_of), "retrieved_date_fallback", True, entity_name, iso, "OFAC SDN", "SDN", joined[:1000], "sanctions;access_control", "Treasury OFAC SDN CSV", url, now_utc()],
            )
            loaded += 1
        return [QualityEvent("Treasury OFAC SDN", "ok", "Loaded sanctions rows from official OFAC CSV fallback.", url, loaded)]
    except Exception as exc:  # noqa: BLE001
        return [QualityEvent("Treasury OFAC SDN", "error", f"OFAC CSV failed: {type(exc).__name__}: {exc}", url, 0)]


def ingest_procurement(con: duckdb.DuckDBPyConnection, as_of: dt.date, limit: int) -> list[QualityEvent]:
    con.execute("DELETE FROM wetd_data.fact_procurement")
    url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
    start = (as_of - dt.timedelta(days=730)).isoformat()
    end = as_of.isoformat()
    payload = {
        "filters": {"time_period": [{"start_date": start, "end_date": end}], "keywords": ["artificial intelligence", "semiconductor", "secure cloud"], "award_type_codes": ["A", "B", "C", "D"]},
        "fields": ["Award ID", "Recipient Name", "Award Amount", "Start Date", "Awarding Agency", "Description"],
        "page": 1,
        "limit": limit,
        "sort": "Award Amount",
        "order": "desc",
        "subawards": False,
    }
    try:
        payload_out = http_post_json(url, payload)
        rows = payload_out.get("results", [])
        for row in rows:
            desc = str(row.get("Description") or "")
            title = desc[:160] or "USAspending award"
            value = float(row.get("Award Amount") or 0)
            date = (row.get("Start Date") or as_of.isoformat())[:10]
            lower = (desc + " " + str(row.get("Awarding Agency") or "")).lower()
            defense_flag = any(w in lower for w in ["defense", "army", "navy", "air force", "darpa", "classified", "secure"])
            ai_flag = any(w in lower for w in ["artificial intelligence", "machine learning", "semiconductor", "cloud", "gpu", "microelectronics"])
            con.execute(
                "INSERT OR REPLACE INTO wetd_data.fact_procurement VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [stable_id("proc", row.get("Award ID"), date, value), row.get("Award ID"), date, "USA", row.get("Awarding Agency"), row.get("Recipient Name"), value, title, desc[:2000], defense_flag, ai_flag, "ai;compute;secure_cloud" if ai_flag else "defense", "USAspending", url, now_utc()],
            )
        return [QualityEvent("USAspending", "ok", "Loaded public procurement rows without authorization.", url, len(rows))]
    except Exception as exc:  # noqa: BLE001
        return [QualityEvent("USAspending", "error", f"USAspending request failed: {type(exc).__name__}: {exc}", url, 0)]


def ingest_energy_minerals(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> list[QualityEvent]:
    con.execute("DELETE FROM wetd_data.fact_energy_minerals")
    events: list[QualityEvent] = []
    eia_key = os.environ.get("EIA_API_KEY")
    if not eia_key:
        events.append(QualityEvent("EIA Open Data", "missing_key", "EIA_API_KEY not set; EIA official docs require an API key. World Bank fallback used.", "https://www.eia.gov/opendata/documentation.php", 0))
    indicators = [
        ("EG.USE.PCAP.KG.OE", "energy", "energy_use_kg_oil_equivalent_per_capita", "kg_oil_equivalent_per_capita"),
        ("TM.VAL.MMTL.ZS.UN", "ores_metals", "ores_metals_imports_percent_merchandise_imports", "percent"),
    ]
    countries = ["USA", "CHN", "JPN", "KOR", "DEU", "GBR", "FRA", "CAN", "NLD", "ARE", "SAU", "WLD"]
    loaded = 0
    for indicator, commodity, metric, unit in indicators:
        url = f"https://api.worldbank.org/v2/country/{';'.join(countries)}/indicator/{indicator}?format=json&per_page=500"
        try:
            payload = http_json(url)
            records = payload[1] if isinstance(payload, list) and len(payload) > 1 else []
            latest_by_country: dict[str, dict[str, Any]] = {}
            for rec in records:
                if rec.get("value") is None:
                    continue
                iso = rec.get("countryiso3code")
                if iso and iso not in latest_by_country:
                    latest_by_country[iso] = rec
            for iso, rec in latest_by_country.items():
                year = str(rec.get("date"))
                value = float(rec.get("value"))
                con.execute(
                    "INSERT OR REPLACE INTO wetd_data.fact_energy_minerals VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    [stable_id("em", indicator, iso, year), f"{indicator}:{iso}:{year}", f"{year}-01-01", iso, commodity, metric, value, unit, "World Bank API", url, now_utc()],
                )
                loaded += 1
        except Exception as exc:  # noqa: BLE001
            events.append(QualityEvent("World Bank energy/minerals", "error", f"{indicator} failed: {type(exc).__name__}: {exc}", url, 0))
    events.append(QualityEvent("World Bank energy/minerals", "ok", "Loaded no-auth energy/minerals fallback indicators.", "https://api.worldbank.org/v2/", loaded))
    return events


def ingest_arctic(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> list[QualityEvent]:
    con.execute("DELETE FROM wetd_data.fact_arctic_access")
    url = "https://noaadata.apps.nsidc.org/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v4.0.csv"
    try:
        raw = http_get(url, timeout=60).decode("utf-8", errors="replace")
        (RAW_DIR / "N_seaice_extent_daily_v4.0.csv").write_text(raw, encoding="utf-8")
        rows = list(csv.DictReader(raw.splitlines(), skipinitialspace=True))
        valid = []
        for row in rows:
            try:
                year = int(row.get("Year", "0").strip())
                month = int(row.get("Month", "0").strip())
                day = int(row.get("Day", "0").strip())
                extent = float(row.get("Extent", "nan").strip())
                date = dt.date(year, month, day)
                if date <= as_of:
                    valid.append((date, extent))
            except Exception:
                continue
        latest = valid[-1]
        # Use a same-month historical mean over the previous 10 observations as a lightweight anomaly proxy.
        same_month = [extent for date, extent in valid if date.month == latest[0].month and date.year < latest[0].year][-10:]
        ref = sum(same_month) / len(same_month) if same_month else latest[1]
        anomaly = latest[1] - ref
        insert_rows = [
            (stable_id("arctic", "extent", latest[0].isoformat()), latest[0].isoformat(), month_start(latest[0]), "northern_hemisphere", "sea_ice_extent", latest[1], "million_sq_km", "NSIDC Sea Ice Index v4", url, now_utc()),
            (stable_id("arctic", "extent_anomaly", latest[0].isoformat()), latest[0].isoformat(), month_start(latest[0]), "northern_hemisphere", "sea_ice_extent_10yr_same_month_anomaly", anomaly, "million_sq_km", "NSIDC Sea Ice Index v4", url, now_utc()),
        ]
        con.executemany("INSERT OR REPLACE INTO wetd_data.fact_arctic_access VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", insert_rows)
        return [QualityEvent("NSIDC Sea Ice Index v4", "ok", f"Loaded latest Arctic daily extent {latest[0].isoformat()}.", url, len(insert_rows))]
    except Exception as exc:  # noqa: BLE001
        return [QualityEvent("NSIDC Sea Ice Index v4", "error", f"NSIDC v4 CSV failed: {type(exc).__name__}: {exc}", url, 0)]


def seed_scenarios(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> None:
    con.execute("DELETE FROM wetd_data.fact_2035_scenario_mapping")
    rows = [
        ("taiwan_compute_block", "taiwan_strait", "Semiconductor access controls and routing anomalies rise", "Allied redundancy cannot fully absorb tool and packaging bottlenecks", "Compute scarcity remains manageable with transparent reserves", "Redundancy and corridor audits dampen block formation", "AI compute capacity becomes bloc-governed", "Allied compute reserve and semiconductor redundancy pool", "capital_access_control;trade_rewiring;stockpiling", as_of.isoformat()),
        ("middle_east_energy_dual_use", "middle_east", "Sanctions rows and dual-use procurement rise with energy stress", "Energy and defense-tech controls reinforce each other", "Regional shocks remain separable", "Sanctions analytics and corridor audits limit leakage", "Energy, sanctions, and AI-defense diffusion become one coupled shock", "Sanctions analytics plus chokepoint monitoring", "capital_access_control;civilian_military_allocation;stockpiling", as_of.isoformat()),
        ("arctic_route_resource", "arctic", "Sea-ice access and Arctic infrastructure signals move together", "Route, cable, resource, and military monitoring converge", "Arctic remains a monitored spatial multiplier", "Governance catches route/cable/resource risk early", "Polar theater becomes a military-economic escalation lane", "Arctic route cable and resource governance", "trade_rewiring;civilian_military_allocation;stockpiling", as_of.isoformat()),
    ]
    con.executemany("INSERT INTO wetd_data.fact_2035_scenario_mapping VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)


def bounded(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


def score_pipeline(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> None:
    con.execute("DELETE FROM wetd_data.fact_wet_signal_score")
    con.execute("DELETE FROM wetd_data.fact_theater_multiplier")
    date_month = month_start(as_of)
    countries = [r[0] for r in con.execute("""
        SELECT DISTINCT country_iso3
        FROM wetd_data.dim_country
        WHERE is_mvp_country
           OR country_iso3 IN (SELECT country_iso3 FROM wetd_data.country_theater_exposure)
           OR country_iso3 IN ('IRN','ISR','ARE','SAU')
    """).fetchall()]
    policy_count = con.execute("SELECT COUNT(*) FROM wetd_data.fact_policy_event").fetchone()[0]
    procurement_total = con.execute("SELECT COALESCE(SUM(value_usd),0) FROM wetd_data.fact_procurement").fetchone()[0] or 0
    sanctions_by_country = dict(con.execute("SELECT country_iso3, COUNT(*) FROM wetd_data.fact_sanctions GROUP BY 1").fetchall())
    trade_by_country = dict(con.execute("SELECT reporter_iso3, COUNT(*) FROM wetd_data.fact_trade GROUP BY 1").fetchall())
    energy_by_country = dict(con.execute("SELECT country_iso3, AVG(value) FROM wetd_data.fact_energy_minerals GROUP BY 1").fetchall())
    arctic_anomaly_row = con.execute("SELECT value FROM wetd_data.fact_arctic_access WHERE metric_name LIKE '%anomaly%' LIMIT 1").fetchone()
    arctic_anomaly = float(arctic_anomaly_row[0]) if arctic_anomaly_row else 0.0

    refs = {
        "policy": [f"fact_policy_event:{r[0]}" for r in con.execute("SELECT policy_event_id FROM wetd_data.fact_policy_event LIMIT 5").fetchall()],
        "proc": [f"fact_procurement:{r[0]}" for r in con.execute("SELECT procurement_id FROM wetd_data.fact_procurement LIMIT 5").fetchall()],
        "sanctions": [f"fact_sanctions:{r[0]}" for r in con.execute("SELECT sanctions_id FROM wetd_data.fact_sanctions LIMIT 5").fetchall()],
        "trade": [f"fact_trade:{r[0]}" for r in con.execute("SELECT trade_id FROM wetd_data.fact_trade LIMIT 5").fetchall()],
        "energy": [f"fact_energy_minerals:{r[0]}" for r in con.execute("SELECT energy_minerals_id FROM wetd_data.fact_energy_minerals LIMIT 5").fetchall()],
        "arctic": [f"fact_arctic_access:{r[0]}" for r in con.execute("SELECT arctic_access_id FROM wetd_data.fact_arctic_access LIMIT 5").fetchall()],
    }

    rows = []
    for iso in countries:
        sanction_count = sanctions_by_country.get(iso, 0)
        trade_count = trade_by_country.get(iso, 0)
        energy_value = float(energy_by_country.get(iso, 0) or 0)
        is_corridor = iso in {"TWN", "SGP", "MYS", "ARE", "VNM", "KOR", "JPN", "NLD"}
        is_tech_actor = iso in {"USA", "CHN", "TWN", "KOR", "JPN", "NLD", "DEU", "EUU"}
        is_middle_east = iso in {"IRN", "ISR", "ARE", "SAU"}
        is_energy_capital_connector = iso in {"SAU", "ARE"}
        is_arctic = iso in {"USA", "CAN", "RUS"}
        signal_values = {
            "autarky": (40 + min(policy_count, 20) * 1.5 + (8 if is_tech_actor else 0) + min(energy_value / 10, 12), "medium" if policy_count else "low", refs["policy"] + refs["energy"]),
            "stockpiling": (35 + min(trade_count, 10) * 4 + (10 if is_corridor else 0) + (7 if is_energy_capital_connector else 0) + (8 if is_arctic and arctic_anomaly < 0 else 0), "low" if trade_count == 0 and not is_energy_capital_connector else "medium", refs["trade"] + refs["arctic"]),
            "trade_rewiring": (30 + min(trade_count, 10) * 3 + (18 if is_corridor else 0) + (8 if is_energy_capital_connector else 0) + (10 if sanction_count else 0), "medium" if is_corridor or trade_count or is_energy_capital_connector else "low", refs["trade"] + refs["sanctions"]),
            "capital_access_control": (35 + min(policy_count, 20) * 2 + min(sanction_count, 20) * 3, "high" if sanction_count else "medium", refs["policy"] + refs["sanctions"]),
            "civilian_military_allocation": (30 + min(procurement_total / 25_000_000, 35) + (12 if iso == "USA" else 0) + (10 if is_middle_east else 0), "medium" if procurement_total else "low", refs["proc"]),
        }
        for signal, (value, confidence, source_refs) in signal_values.items():
            label, question, _ = SIGNAL_EXPLAINERS.get(signal, (signal, "This signal needs analyst interpretation.", ""))
            rows.append((
                stable_id("score", CONFIG_ID, date_month, iso, signal), CONFIG_ID, date_month, iso, None, signal,
                float(value), None, bounded(float(value)), confidence,
                f"{label} for {iso}: {question} Generated by War-Economy Transition Dashboard batch from public source counts and configured theater/actor roles.",
                ";".join(source_refs[:8]),
            ))
    con.executemany("INSERT INTO wetd_data.fact_wet_signal_score VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)

    # Theater multipliers use source-backed counts but remain calibration outputs.
    multipliers = [
        ("taiwan_strait", bounded(1.20 + min(policy_count, 20) * 0.005 + (0.02 if trade_by_country.get("TWN") else 0), 1.0, 1.5), "Policy/export-control and semiconductor/corridor signals move Taiwan Strait interpretation."),
        ("middle_east", bounded(1.10 + min(sanctions_by_country.get("IRN", 0), 20) * 0.01 + (0.03 if procurement_total else 0), 1.0, 1.4), "Sanctions and defense/procurement signals move Middle East interpretation."),
        ("arctic", bounded(1.10 + (0.05 if arctic_anomaly < 0 else 0), 1.0, 1.3), "NSIDC sea-ice extent anomaly moves Arctic spatial interpretation."),
    ]
    for theater_id, value, explanation in multipliers:
        con.execute(
            "INSERT INTO wetd_data.fact_theater_multiplier VALUES (?, ?, ?, ?, ?, ?, ?)",
            [stable_id("mult", date_month, theater_id), date_month, theater_id, value, "medium", explanation, ";".join((refs["policy"] + refs["sanctions"] + refs["arctic"])[:8])],
        )

    con.execute("""
        CREATE OR REPLACE VIEW wetd_data.vw_country_month_wet_score AS
        WITH expected AS (
          SELECT DISTINCT config_id, signal_type FROM wetd_data.config_signal_weight WHERE effective_to IS NULL
        ), scored AS (
          SELECT s.date_month, s.country_iso3, s.config_id, s.signal_type, s.normalized_score, w.weight
          FROM wetd_data.fact_wet_signal_score s
          JOIN wetd_data.config_signal_weight w ON s.config_id = w.config_id AND s.signal_type = w.signal_type
        ), agg AS (
          SELECT date_month, country_iso3, config_id,
                 COUNT(DISTINCT signal_type) AS signal_count,
                 SUM(normalized_score * weight) / NULLIF(SUM(weight), 0) AS weighted_wet_score,
                 LIST(DISTINCT signal_type) AS present_signal_types
          FROM scored GROUP BY 1, 2, 3
        )
        SELECT a.date_month, a.country_iso3, a.config_id, a.signal_count,
               (SELECT STRING_AGG(e.signal_type, ';') FROM expected e WHERE e.config_id = a.config_id AND NOT list_contains(a.present_signal_types, e.signal_type)) AS missing_signal_types,
               CASE WHEN a.signal_count >= 5 THEN a.weighted_wet_score END AS base_wet_score,
               a.signal_count >= 5 AS is_complete_score
        FROM agg a
    """)
    con.execute("""
        CREATE OR REPLACE VIEW wetd_data.vw_theater_adjusted_score AS
        SELECT c.date_month, c.country_iso3, e.theater_id, c.base_wet_score, c.signal_count,
               c.missing_signal_types, c.is_complete_score, e.exposure_weight, t.multiplier_value,
               CASE WHEN c.is_complete_score THEN c.base_wet_score * e.exposure_weight * t.multiplier_value END AS final_wet_score
        FROM wetd_data.vw_country_month_wet_score c
        JOIN wetd_data.country_theater_exposure e
          ON c.country_iso3 = e.country_iso3
         AND c.date_month >= e.effective_from
         AND (e.effective_to IS NULL OR c.date_month <= e.effective_to)
        JOIN wetd_data.fact_theater_multiplier t
          ON c.date_month = t.date_month AND e.theater_id = t.theater_id
    """)


def export_csv(con: duckdb.DuckDBPyConnection, query: str, path: Path) -> None:
    rows = con.execute(query).fetchall()
    cols = [d[0] for d in con.description]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(cols)
        writer.writerows(rows)


def format_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return str(round(value, 3))
    return str(value)


def table_html(con: duckdb.DuckDBPyConnection, query: str, limit: int = 20) -> str:
    rows = con.execute(query + f" LIMIT {limit}").fetchall()
    cols = [d[0] for d in con.description]
    out = ["<table><thead><tr>" + "".join(f"<th>{html.escape(str(c))}</th>" for c in cols) + "</tr></thead><tbody>"]
    for row in rows:
        cells = []
        for col, value in zip(cols, row):
            rendered = format_value(value)
            if col == "source_url" and rendered.startswith("http"):
                safe = html.escape(rendered)
                cells.append(f'<td><a href="{safe}" target="_blank" rel="noreferrer">source</a><br><span class="tiny">{safe[:96]}</span></td>')
            elif col in {"status", "source_type"}:
                cls = "ok" if rendered in {"ok", "official_api", "official_csv"} else "warn" if rendered in {"missing_key", "fallback_proxy", "proxy"} else "mutedbadge"
                cells.append(f'<td><span class="badge {cls}">{html.escape(rendered)}</span></td>')
            else:
                cells.append(f"<td>{html.escape(rendered)}</td>")
        out.append("<tr>" + "".join(cells) + "</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def score_bars_html(con: duckdb.DuckDBPyConnection) -> str:
    rows = con.execute("""
        SELECT d.country_name, c.country_iso3, ROUND(c.base_wet_score, 1) AS score, c.signal_count
        FROM wetd_data.vw_country_month_wet_score c
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE c.is_complete_score
        ORDER BY c.base_wet_score DESC NULLS LAST
        LIMIT 12
    """).fetchall()
    parts = ['<div class="bars" role="img" aria-label="Top country War-Economy Transition scores as horizontal bars">']
    for name, iso, score, signal_count in rows:
        width = max(0, min(100, float(score or 0)))
        parts.append(f'''<div class="bar-row"><div class="bar-label"><strong>{html.escape(name)}</strong><span>{html.escape(iso)} · {signal_count}/5 signals</span></div><div class="bar-track"><div class="bar-fill" style="width:{width:.1f}%"></div></div><div class="bar-score">{width:.1f}</div></div>''')
    parts.append('</div>')
    return "\n".join(parts)


def theater_bubbles_html(con: duckdb.DuckDBPyConnection) -> str:
    rows = con.execute("""
        SELECT d.country_name, t.country_iso3, t.theater_id, ROUND(t.final_wet_score, 1) AS score,
               ROUND(t.exposure_weight, 2) AS exposure_weight, ROUND(t.multiplier_value, 2) AS multiplier
        FROM wetd_data.vw_theater_adjusted_score t
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE t.final_wet_score IS NOT NULL
        ORDER BY t.final_wet_score DESC
        LIMIT 12
    """).fetchall()
    if not rows:
        return '<p class="muted">No theater-adjusted scores available.</p>'
    max_score = max(float(r[3] or 0) for r in rows) or 1
    w, h = 920, 330
    col = {"taiwan_strait": 180, "middle_east": 460, "arctic": 740}
    counts = {k: 0 for k in col}
    colors = {"taiwan_strait": "#38bdf8", "middle_east": "#f97316", "arctic": "#a78bfa"}
    svg = [f'<svg class="bubble-chart" viewBox="0 0 {w} {h}" role="img" aria-label="Theater adjusted War-Economy Transition score bubble chart">']
    for theater, x in col.items():
        svg.append(f'<text x="{x}" y="26" text-anchor="middle" class="svg-label">{html.escape(theater.replace("_", " " ).title())}</text>')
        svg.append(f'<line x1="{x}" y1="42" x2="{x}" y2="300" class="svg-axis"/>')
    for name, iso, theater, score, exposure, multiplier in rows:
        counts[theater] = counts.get(theater, 0) + 1
        x = col.get(theater, 460)
        y = 65 + (counts[theater] - 1) * 38
        radius = 12 + (float(score or 0) / max_score) * 16
        color = colors.get(theater, "#60a5fa")
        label = f"{name} ({iso}) score {score}, exposure {exposure}, multiplier {multiplier}"
        svg.append(f'<circle cx="{x}" cy="{y}" r="{radius:.1f}" fill="{color}" fill-opacity="0.78"><title>{html.escape(label)}</title></circle>')
        svg.append(f'<text x="{x + radius + 8:.1f}" y="{y + 4}" class="svg-country">{html.escape(name)} <tspan class="svg-score">{score}</tspan></text>')
    svg.append('</svg>')
    return "\n".join(svg)


SIGNAL_EXPLAINERS = {
    "autarky": (
        "Self-reliance pressure",
        "Is a country reducing dependence on open-market supply through subsidies, domestic substitution, or sovereignty framing?",
        "Policy events, energy/mineral dependency rows, and strategic-sector keywords.",
    ),
    "stockpiling": (
        "Strategic stockpiling",
        "Is buying or inventory behavior becoming security-driven rather than ordinary commercial replenishment?",
        "Trade proxy rows, Arctic/energy access rows, and abnormal accumulation candidates.",
    ),
    "trade_rewiring": (
        "Route rewiring",
        "Are flows moving through third countries, corridors, or indirect routes rather than direct market routes?",
        "Trade proxy rows plus sanctions/access-control pressure that can explain rerouting.",
    ),
    "capital_access_control": (
        "Permissioning and access control",
        "Is market access being replaced by state permission, sanctions, screening, export controls, or compute/cloud restrictions?",
        "Federal Register policy events, sanctions rows, and restricted-access evidence.",
    ),
    "civilian_military_allocation": (
        "Civilian-to-military allocation",
        "Are civilian technologies, compute, cloud, AI, or microelectronics entering defense/intelligence priority lanes?",
        "USAspending procurement rows and defense-allocation keywords.",
    ),
}


COUNTRY_NARRATIVES = {
    "SAU": {
        "regime": "Energy-security allocation + capital/defense-industrial readiness",
        "trend": "Saudi Arabia is treated as a Middle East energy/capital connector: the dashboard watches whether energy rents, sovereign capital, logistics, and defense-industrial procurement begin to behave like strategic allocation rather than ordinary market expansion.",
        "why": "It is not labeled war-economy because one source says so. The inference is theater exposure: energy leverage plus capital allocation plus regional security procurement can change the meaning of otherwise normal investment and trade rows.",
        "watch": "Validate with EIA/OPEC-grade energy data, Comtrade route data, defense procurement, sovereign AI/compute investment, and sanctions/corridor exposure before making a strong claim.",
    },
    "ARE": {
        "regime": "Finance, compute, and re-export corridor readiness",
        "trend": "The UAE is monitored as a corridor where finance, logistics, compute infrastructure, and re-export behavior can make sanctions/access-control pressure visible before it appears as a direct conflict signal.",
        "why": "The non-obvious inference is route and capital intermediation: ordinary trade or data-center growth can become strategically meaningful when it sits inside a Middle East theater exposure graph.",
        "watch": "Check corridor-specific trade, re-export, cloud/compute investment, and sanctions-screening rows.",
    },
    "IRN": {
        "regime": "Sanctioned procurement and substitution readiness",
        "trend": "Iran is monitored as a sanctions and procurement escalation node where access-control pressure, domestic substitution, and dual-use procurement can reinforce each other.",
        "why": "The inference comes from pressure adaptation: sanctions alone are not the point; the point is whether procurement and rerouting behavior move with sanctions pressure.",
        "watch": "Separate confirmed sanctions rows from inferred procurement/rerouting claims.",
    },
    "ISR": {
        "regime": "Dual-use AI/defense allocation readiness",
        "trend": "Israel is monitored as a dual-use defense node where civilian AI, cyber, cloud, ISR, and secure compute can enter defense-priority allocation.",
        "why": "The inference is civilian-to-military conversion: the same AI/compute investment carries different meaning in a theater with active defense allocation.",
        "watch": "Check procurement, defense AI, and secure-cloud rows before escalating the note.",
    },
    "CHN": {
        "regime": "Self-reliance and access-control response system",
        "trend": "China is monitored for self-reliance, export-control response, route rewiring, and strategic stockpiling around advanced compute and semiconductor constraints.",
        "why": "The inference is co-movement across policy, trade, and theater exposure rather than a single export-control row.",
        "watch": "Separate policy rhetoric from measurable trade, stockpiling, and procurement rows.",
    },
    "USA": {
        "regime": "Export-control and defense-allocation rulemaking system",
        "trend": "The United States is monitored as a rulemaking and procurement actor whose policy and defense-spending rows can shift open-market access into permissioned allocation.",
        "why": "The inference is institutional conversion: public rules and procurement can reorganize market access without requiring a military event.",
        "watch": "Check Federal Register, USAspending, and source_row_refs before interpreting score movement.",
    },
    "TWN": {
        "regime": "Semiconductor keystone resilience system",
        "trend": "Taiwan is monitored as a production keystone where semiconductor capacity, route stress, and defense allocation can change global compute access.",
        "why": "The inference is theater lift: similar signal values mean more in Taiwan Strait exposure than in a generic industrial-policy context.",
        "watch": "Validate with product-specific semiconductor trade and tooling data.",
    },
    "KOR": {
        "regime": "Memory/HBM and allied production redundancy system",
        "trend": "South Korea is monitored for memory, HBM, advanced manufacturing, and allied redundancy pressure in the Taiwan Strait production graph.",
        "why": "The inference is dependency graph position: production exposure can make ordinary industrial-policy rows strategically important.",
        "watch": "Check HBM/memory-specific trade, procurement, and export-control rows.",
    },
    "JPN": {
        "regime": "Materials, equipment, and allied redundancy system",
        "trend": "Japan is monitored for semiconductor materials, equipment, and strategic redundancy in a Taiwan Strait shock pathway.",
        "why": "The inference is supply-chain chokepoint position, not the existence of one policy row.",
        "watch": "Validate product-level tooling/materials data.",
    },
    "NLD": {
        "regime": "EUV/tooling chokepoint permissioning system",
        "trend": "The Netherlands is monitored for tooling and EUV-related access-control pressure inside the advanced semiconductor graph.",
        "why": "The inference is that tool access can become a permissioned strategic resource even without broad economic decoupling.",
        "watch": "Validate tool-specific policy and export-control rows.",
    },
    "CAN": {
        "regime": "Arctic route/resource infrastructure readiness",
        "trend": "Canada is monitored as an Arctic route, resource, cable, and infrastructure actor where physical access changes the strategic meaning of logistics and energy rows.",
        "why": "The inference is spatial multiplier: Arctic access can turn ordinary infrastructure into theater-relevant allocation.",
        "watch": "Check Arctic access, resource, infrastructure, and defense rows separately.",
    },
    "RUS": {
        "regime": "Arctic energy/military route readiness",
        "trend": "Russia is monitored for Arctic route, energy, and military infrastructure coupling.",
        "why": "The inference is that Arctic spatial access and sanctions pressure can reinforce each other.",
        "watch": "Separate sanctions rows from physical Arctic access indicators.",
    },
}


def signal_explainers_html() -> str:
    cards = ['<div class="signal-grid">']
    for slug, (label, question, evidence) in SIGNAL_EXPLAINERS.items():
        cards.append(f'''<div class="signal-card"><div class="tiny">{html.escape(slug)}</div><h3>{html.escape(label)}</h3><p>{html.escape(question)}</p><p><strong>Evidence used:</strong> {html.escape(evidence)}</p></div>''')
    cards.append('</div>')
    return "\n".join(cards)


def country_signal_drilldown_html(con: duckdb.DuckDBPyConnection) -> str:
    rows = con.execute("""
        SELECT d.country_name, s.country_iso3, s.signal_type, ROUND(s.normalized_score, 1) AS normalized_score,
               s.confidence, s.explanation
        FROM wetd_data.fact_wet_signal_score s
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE s.country_iso3 IN (
            SELECT country_iso3
            FROM wetd_data.vw_country_month_wet_score
            WHERE is_complete_score
            ORDER BY base_wet_score DESC NULLS LAST
            LIMIT 8
        )
        ORDER BY d.country_name, s.signal_type
    """).fetchall()
    out = ["<table><thead><tr><th>country</th><th>signal</th><th>plain meaning</th><th>score</th><th>confidence</th><th>why this row exists</th></tr></thead><tbody>"]
    for country, iso, signal, score, confidence, explanation in rows:
        label, question, _ = SIGNAL_EXPLAINERS.get(signal, (signal, "", ""))
        out.append(
            "<tr>"
            f"<td><strong>{html.escape(country)}</strong><br><span class=\"tiny\">{html.escape(iso)}</span></td>"
            f"<td>{html.escape(label)}<br><span class=\"tiny\">{html.escape(signal)}</span></td>"
            f"<td>{html.escape(question)}</td>"
            f"<td><strong>{html.escape(format_value(score))}</strong></td>"
            f"<td><span class=\"badge {'ok' if confidence == 'high' else 'warn' if confidence == 'low' else 'mutedbadge'}\">{html.escape(str(confidence))}</span></td>"
            f"<td>{html.escape(str(explanation))}</td>"
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def signal_chips_html(signals: list[tuple[str, float, str]]) -> str:
    chips = ['<div class="signal-chips">']
    for signal, score, confidence in signals:
        label, question, evidence = SIGNAL_EXPLAINERS.get(signal, (signal, "", ""))
        cls = "ok" if confidence == "high" else "warn" if confidence == "low" else "mutedbadge"
        chips.append(
            f'<span class="signal-chip {cls}" title="{html.escape(question + " Evidence: " + evidence)}">'
            f'{html.escape(label)} <strong>{float(score):.1f}</strong></span>'
        )
    chips.append('</div>')
    return "\n".join(chips)


def country_narratives_html(con: duckdb.DuckDBPyConnection) -> str:
    rows = con.execute("""
        WITH ranked AS (
            SELECT c.country_iso3, d.country_name, d.country_group,
                   ROUND(c.base_wet_score, 1) AS base_score,
                   MAX(ROUND(t.final_wet_score, 1)) AS max_theater_score,
                   STRING_AGG(DISTINCT t.theater_id, ', ') AS theaters
            FROM wetd_data.vw_country_month_wet_score c
            JOIN wetd_data.dim_country d USING(country_iso3)
            LEFT JOIN wetd_data.vw_theater_adjusted_score t USING(country_iso3)
            WHERE c.is_complete_score
            GROUP BY c.country_iso3, d.country_name, d.country_group, c.base_wet_score
        )
        SELECT *
        FROM ranked
        WHERE country_iso3 IN (
            SELECT country_iso3 FROM ranked ORDER BY base_score DESC NULLS LAST LIMIT 8
        )
           OR country_iso3 IN ('SAU','ARE','IRN','ISR')
        ORDER BY CASE WHEN country_iso3 = 'SAU' THEN 0 ELSE 1 END,
                 COALESCE(max_theater_score, base_score) DESC NULLS LAST,
                 base_score DESC NULLS LAST
    """).fetchall()
    signal_rows = con.execute("""
        SELECT country_iso3, signal_type, normalized_score, confidence
        FROM wetd_data.fact_wet_signal_score
        ORDER BY country_iso3, normalized_score DESC
    """).fetchall()
    signals_by_country: dict[str, list[tuple[str, float, str]]] = {}
    for iso, signal, score, confidence in signal_rows:
        signals_by_country.setdefault(iso, []).append((signal, float(score or 0), str(confidence)))
    parts = ['<div class="country-accordion">']
    for iso, name, group, base_score, max_theater_score, theaters in rows:
        narrative = COUNTRY_NARRATIVES.get(iso, {
            "regime": "Strategic allocation review candidate",
            "trend": "This country is in the review queue because several War-Economy Transition signals are present in the same month.",
            "why": "The inference should be read as co-movement across signals, not as a deterministic causal conclusion.",
            "watch": "Inspect signal rows, source_row_refs, source URLs, and data-quality warnings before escalation.",
        })
        top_signals = signals_by_country.get(iso, [])[:5]
        score_label = f"base {float(base_score or 0):.1f}"
        if max_theater_score is not None:
            score_label += f" · theater {float(max_theater_score):.1f}"
        open_attr = " open" if iso == "SAU" else ""
        parts.append(f'''<details class="country-detail"{open_attr}><summary><span class="country-title">{html.escape(name)} <span class="tiny">{html.escape(iso)}</span></span><span class="summary-tags"><span>{html.escape(score_label)}</span><span>{html.escape(str(theaters or group).replace("_", " "))}</span></span></summary><div class="country-body"><div><h3>체제 준비</h3><p>{html.escape(narrative["regime"])}</p></div><div><h3>관측 동향</h3><p>{html.escape(narrative["trend"])}</p></div><div><h3>왜 단순 인과가 아닌가</h3><p>{html.escape(narrative["why"])}</p></div><div><h3>검증해야 할 것</h3><p>{html.escape(narrative["watch"])}</p></div><div class="country-signals"><h3>5-signal fingerprint</h3>{signal_chips_html(top_signals)}</div></div></details>''')
    parts.append('</div>')
    return "\n".join(parts)


def provenance_cards_html(con: duckdb.DuckDBPyConnection) -> str:
    rows = con.execute("SELECT source_name, status, rows_loaded, source_url, message FROM wetd_data.data_quality_event ORDER BY observed_at").fetchall()
    cards = ['<div class="source-grid">']
    for source, status, rows, url, message in rows:
        status_text = str(status)
        is_fallback = "World Bank" in source
        is_ok = status_text == "ok" and not is_fallback
        is_key = status_text == "missing_key"
        label = "Proxy fallback rows loaded" if is_fallback else "Official/public rows loaded" if is_ok else "Key required / fallback used" if is_key else "Check required"
        badge = "warn" if is_fallback or is_key else "ok" if is_ok else "mutedbadge"
        source_type = "official API/CSV" if source in {"Federal Register", "USAspending", "Treasury OFAC SDN", "NSIDC Sea Ice Index v4"} else "fallback proxy" if is_fallback else "key-gated source"
        cards.append(f'''<div class="source-card"><div class="source-head"><strong>{html.escape(source)}</strong><span class="badge {badge}">{html.escape(status_text)}</span></div><p class="source-type">{html.escape(source_type)} · rows loaded: <strong>{rows}</strong></p><p>{html.escape(message)}</p><a href="{html.escape(str(url))}" target="_blank" rel="noreferrer">Verify source</a><div class="tiny">{html.escape(str(url))}</div><div class="trust">{html.escape(label)}</div></div>''')
    cards.append('</div>')
    return "\n".join(cards)


def inference_cards_html(con: duckdb.DuckDBPyConnection) -> str:
    """Render non-obvious analyst inferences from score combinations, not raw facts."""
    top_base = con.execute("""
        SELECT d.country_name, c.country_iso3, ROUND(c.base_wet_score, 1) AS score, c.signal_count
        FROM wetd_data.vw_country_month_wet_score c
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE c.is_complete_score
        ORDER BY c.base_wet_score DESC NULLS LAST
        LIMIT 1
    """).fetchone()
    top_theater = con.execute("""
        SELECT d.country_name, t.country_iso3, t.theater_id, ROUND(t.base_wet_score, 1) AS base_score,
               ROUND(t.final_wet_score, 1) AS final_score,
               ROUND(t.final_wet_score - t.base_wet_score, 1) AS theater_lift
        FROM wetd_data.vw_theater_adjusted_score t
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE t.final_wet_score IS NOT NULL
        ORDER BY t.final_wet_score DESC
        LIMIT 1
    """).fetchone()
    confidence_mix = con.execute("""
        SELECT confidence, COUNT(*)
        FROM wetd_data.fact_wet_signal_score
        GROUP BY confidence
        ORDER BY confidence
    """).fetchall()
    missing_sources = con.execute("""
        SELECT source_name, status, message
        FROM wetd_data.data_quality_event
        WHERE status <> 'ok'
        ORDER BY source_name
    """).fetchall()
    cards = ['<div class="inference-grid">']
    if top_base:
        name, iso, score, signal_count = top_base
        cards.append(f'''<div class="inference-card"><h3>1. Co-movement, not one obvious cause</h3><p><strong>Observed:</strong> {html.escape(name)} ({html.escape(iso)}) has the highest complete score at {score} with {signal_count}/5 signals present.</p><p><strong>Inference added:</strong> this is not "sanctions exist, therefore risk." It is a queue item because policy/access control, procurement allocation, trade/stockpiling proxies, and energy/minerals rows co-occur in the same country-month.</p><p><strong>Analyst check:</strong> inspect which signal is driving the score before treating the country as a strategic-allocation case.</p></div>''')
    if top_theater:
        name, iso, theater, base_score, final_score, lift = top_theater
        cards.append(f'''<div class="inference-card"><h3>2. Same score, different theater meaning</h3><p><strong>Observed:</strong> {html.escape(name)} ({html.escape(iso)}) rises from base {base_score} to theater-adjusted {final_score} in {html.escape(theater.replace("_", " ").title())}.</p><p><strong>Inference added:</strong> the same economic row has different strategic meaning when it sits inside a theater exposure graph. This separates "high score" from "high theater consequence."</p><p><strong>Analyst check:</strong> validate exposure_weight and multiplier before escalating the theater note.</p></div>''')
    mix_text = ", ".join(f"{html.escape(str(conf))}: {count}" for conf, count in confidence_mix)
    cards.append(f'''<div class="inference-card"><h3>3. Confidence is part of the finding</h3><p><strong>Observed:</strong> score rows have confidence mix: {mix_text or "none"}.</p><p><strong>Inference added:</strong> a high score with low/fallback confidence means "review priority," not certainty. This prevents the dashboard from becoming a rice-plant/rice-harvest tautology.</p><p><strong>Analyst check:</strong> compare source_row_refs and data-quality cards before using the score in a recommendation.</p></div>''')
    if missing_sources:
        sources = "; ".join(f"{source}: {status}" for source, status, _ in missing_sources[:4])
        cards.append(f'''<div class="inference-card"><h3>4. Data gap becomes a decision constraint</h3><p><strong>Observed:</strong> {html.escape(sources)}.</p><p><strong>Inference added:</strong> missing key-gated sources do not merely reduce polish; they bound what the dashboard is allowed to claim. Trade/energy conclusions stay provisional until high-resolution sources are attached.</p><p><strong>Analyst check:</strong> treat fallback rows as hypothesis generators, not measured trade or energy truth.</p></div>''')
    cards.append('</div>')
    return "\n".join(cards)


def generate_commander_note(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> str:
    top = con.execute("""
        SELECT d.country_name, c.country_iso3, ROUND(c.base_wet_score, 2) AS score
        FROM wetd_data.vw_country_month_wet_score c
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE c.is_complete_score
        ORDER BY c.base_wet_score DESC
        LIMIT 5
    """).fetchall()
    theater = con.execute("""
        SELECT d.country_name, t.country_iso3, t.theater_id, ROUND(t.final_wet_score, 2) AS score
        FROM wetd_data.vw_theater_adjusted_score t
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE t.final_wet_score IS NOT NULL
        ORDER BY t.final_wet_score DESC
        LIMIT 5
    """).fetchall()
    signal_detail = con.execute("""
        SELECT d.country_name, s.country_iso3, s.signal_type, ROUND(s.normalized_score, 1) AS score, s.confidence
        FROM wetd_data.fact_wet_signal_score s
        JOIN wetd_data.dim_country d USING(country_iso3)
        WHERE s.country_iso3 IN (
            SELECT country_iso3
            FROM wetd_data.vw_country_month_wet_score
            WHERE is_complete_score
            ORDER BY base_wet_score DESC NULLS LAST
            LIMIT 3
        )
        ORDER BY d.country_name, s.signal_type
    """).fetchall()
    dq = con.execute("SELECT source_name, status, rows_loaded, message, source_url FROM wetd_data.data_quality_event ORDER BY observed_at").fetchall()
    official_rows = sum(int(rows or 0) for source, status, rows, *_ in dq if status == "ok" and source in {"Federal Register", "USAspending", "Treasury OFAC SDN", "NSIDC Sea Ice Index v4"})
    proxy_rows = sum(int(rows or 0) for source, status, rows, *_ in dq if status == "ok" and "World Bank" in source)
    lines = [
        f"# War-Economy Transition Dashboard (WETD) Commander Note — {as_of.isoformat()}", "", "## Executive read", "",
        "This is a monthly batch early-warning run. It does not predict war; it identifies whether economic allocation is moving from market pricing toward security permissioning, stockpiling, rerouting, and defense allocation.", "",
        f"Data basis: {official_rows} official API/CSV rows plus {proxy_rows} World Bank fallback proxy rows. Key-gated sources are visible in the data-quality notes instead of being hidden.", "",
        "## Highest Base War-Economy Transition scores", "",
    ]
    for name, iso, score in top:
        lines.append(f"- {name} ({iso}): {score}")
    lines += ["", "## Highest theater-adjusted scores", ""]
    for name, iso, theater_id, score in theater:
        lines.append(f"- {name} ({iso}) / {theater_id}: {score}")
    lines += [
        "",
        "## What inference this adds",
        "",
        "- Co-movement: a country enters the review queue when multiple independent signals appear together, not because one obvious causal fact exists.",
        "- Theater lift: the same country-month row can mean more or less depending on Taiwan Strait, Middle East, or Arctic exposure.",
        "- Confidence constraint: fallback or low-confidence rows create review priority, not certainty.",
        "- Data gap as finding: missing key-gated sources bound what the dashboard is allowed to claim.",
        "",
        "## Five War-Economy Transition signals",
        "",
    ]
    for signal, (label, question, evidence) in SIGNAL_EXPLAINERS.items():
        lines.append(f"- {label} (`{signal}`): {question} Evidence used: {evidence}")
    lines += ["", "## Country signal drilldown sample", ""]
    for name, iso, signal, score, confidence in signal_detail:
        label = SIGNAL_EXPLAINERS.get(signal, (signal, "", ""))[0]
        lines.append(f"- {name} ({iso}) / {label}: score={score}, confidence={confidence}")
    sau = COUNTRY_NARRATIVES["SAU"]
    lines += [
        "",
        "## Saudi Arabia narrative note",
        "",
        f"- 체제 준비: {sau['regime']}",
        f"- 관측 동향: {sau['trend']}",
        f"- 왜 단순 인과가 아닌가: {sau['why']}",
        f"- 검증해야 할 것: {sau['watch']}",
    ]
    lines += ["", "## Data quality notes", ""]
    for source, status, rows, msg, url in dq:
        lines.append(f"- {source}: {status}, rows={rows} — {msg} Source: {url}")
    lines += ["", "## Decision use", "", "Use top scores as a queue for analyst review, not as automatic alarms. Check source_row_refs, source URLs, proxy/fallback labels, and missing_signal_types before escalating a country/theater note."]
    return "\n".join(lines) + "\n"


def export_outputs(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> None:
    export_csv(con, "SELECT c.date_month, c.country_iso3, d.country_name, c.config_id, c.signal_count, c.missing_signal_types, c.base_wet_score, c.is_complete_score FROM wetd_data.vw_country_month_wet_score c JOIN wetd_data.dim_country d USING(country_iso3) ORDER BY c.base_wet_score DESC NULLS LAST", OUT_DIR / "wetd_country_month_scores.csv")
    export_csv(con, "SELECT t.date_month, t.country_iso3, d.country_name, t.theater_id, t.base_wet_score, t.signal_count, t.missing_signal_types, t.is_complete_score, t.exposure_weight, t.multiplier_value, t.final_wet_score FROM wetd_data.vw_theater_adjusted_score t JOIN wetd_data.dim_country d USING(country_iso3) ORDER BY t.final_wet_score DESC NULLS LAST", OUT_DIR / "wetd_theater_adjusted_scores.csv")
    export_csv(con, "SELECT source_name, status, rows_loaded, source_url, message, observed_at FROM wetd_data.data_quality_event ORDER BY observed_at", OUT_DIR / "wetd_data_quality.csv")
    export_csv(con, "SELECT s.*, d.country_name FROM wetd_data.fact_wet_signal_score s JOIN wetd_data.dim_country d USING(country_iso3) ORDER BY s.country_iso3, s.signal_type", OUT_DIR / "wetd_signal_scores.csv")
    note = generate_commander_note(con, as_of)
    (OUT_DIR / f"commander_note_{as_of.strftime('%Y_%m')}.md").write_text(note, encoding="utf-8")
    official_rows = con.execute("""
        SELECT COALESCE(SUM(rows_loaded),0) FROM wetd_data.data_quality_event
        WHERE status='ok' AND source_name IN ('Federal Register','USAspending','Treasury OFAC SDN','NSIDC Sea Ice Index v4')
    """).fetchone()[0]
    proxy_rows = con.execute("SELECT COALESCE(SUM(rows_loaded),0) FROM wetd_data.data_quality_event WHERE status='ok' AND source_name LIKE 'World Bank%'").fetchone()[0]
    complete_country_count = con.execute("SELECT COUNT(*) FROM wetd_data.vw_country_month_wet_score WHERE is_complete_score").fetchone()[0]
    theater_score_count = con.execute("SELECT COUNT(*) FROM wetd_data.vw_theater_adjusted_score WHERE final_wet_score IS NOT NULL").fetchone()[0]
    html_doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>War-Economy Transition Dashboard (WETD) Monthly Batch</title><style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin:0;background:#07111f;color:#e2e8f0}}main{{max-width:1180px;margin:0 auto;padding:32px}}h1,h2,h3{{color:#f8fafc;margin-top:0}}.hero{{background:radial-gradient(circle at top left,#1e3a8a,#0f172a 52%,#111827);border-bottom:1px solid #334155;padding:42px 32px}}.hero-inner{{max-width:1180px;margin:0 auto}}.abbr{{font-size:.72em;color:#bfdbfe}}.subtitle{{color:#bfdbfe;max-width:920px;font-size:18px;line-height:1.55}}.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-top:22px}}.kpi{{background:rgba(15,23,42,.82);border:1px solid #334155;border-radius:16px;padding:16px}}.kpi .num{{font-size:28px;font-weight:800;color:#93c5fd;display:block}}.mece{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:20px}}.mece div{{background:#0b1220;border:1px solid #334155;border-radius:14px;padding:12px}}.card{{background:#111827;border:1px solid #334155;border-radius:18px;padding:22px;margin:20px 0;box-shadow:0 10px 28px rgba(0,0,0,.22)}}table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{border-bottom:1px solid #334155;padding:8px 10px;vertical-align:top}}th{{text-align:left;color:#93c5fd;background:#172554;position:sticky;top:0}}a{{color:#7dd3fc}}code{{color:#fbbf24}}pre{{white-space:pre-wrap;color:#dbeafe}}.muted{{color:#94a3b8}}.tiny{{color:#94a3b8;font-size:11px;word-break:break-all}}.badge{{border-radius:999px;padding:3px 8px;font-size:12px;font-weight:700;display:inline-block}}.ok{{background:#064e3b;color:#a7f3d0}}.warn{{background:#713f12;color:#fde68a}}.mutedbadge{{background:#334155;color:#cbd5e1}}.bars{{display:grid;gap:11px}}.bar-row{{display:grid;grid-template-columns:250px 1fr 58px;gap:12px;align-items:center}}.bar-label span{{display:block;color:#94a3b8;font-size:12px;margin-top:3px}}.bar-track{{height:18px;background:#1e293b;border-radius:999px;overflow:hidden;border:1px solid #334155}}.bar-fill{{height:100%;background:linear-gradient(90deg,#38bdf8,#f97316);border-radius:999px}}.bar-score{{font-weight:800;color:#fbbf24}}.bubble-chart{{width:100%;min-height:420px;background:#0b1220;border:1px solid #334155;border-radius:16px}}.svg-label{{fill:#bfdbfe;font-size:18px;font-weight:800}}.svg-axis{{stroke:#334155;stroke-width:2;stroke-dasharray:4 6}}.svg-country{{fill:#e2e8f0;font-size:15px;font-weight:700}}.svg-score{{fill:#fbbf24;font-weight:800}}.source-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}.source-card{{background:#0b1220;border:1px solid #334155;border-radius:14px;padding:15px}}.source-head{{display:flex;justify-content:space-between;gap:10px;align-items:center}}.source-type{{color:#bfdbfe}}.trust{{margin-top:8px;color:#fbbf24;font-size:12px;font-weight:800;text-transform:uppercase}}.grid2{{display:grid;grid-template-columns:1fr;gap:18px}}.country-accordion{{display:grid;gap:12px}}details.country-detail{{background:#0b1220;border:1px solid #334155;border-radius:16px;overflow:hidden}}details.country-detail[open]{{border-color:#60a5fa}}.country-detail summary{{cursor:pointer;list-style:none;padding:16px 18px;display:flex;justify-content:space-between;gap:12px;align-items:center}}.country-detail summary::-webkit-details-marker{{display:none}}.country-title{{font-size:18px;font-weight:800}}.summary-tags{{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}}.summary-tags span{{background:#172554;color:#bfdbfe;border-radius:999px;padding:5px 10px;font-size:12px;font-weight:700}}.country-body{{border-top:1px solid #334155;padding:16px 18px;display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}}.country-body h3{{font-size:14px;color:#93c5fd;margin-bottom:6px}}.country-body p{{margin-top:0;color:#dbeafe;line-height:1.45}}.country-signals{{grid-column:1/-1}}.signal-chips{{display:flex;flex-wrap:wrap;gap:8px}}.signal-chip{{border-radius:999px;padding:7px 10px;font-size:12px;font-weight:700}}.compact-note{{font-size:13px;color:#cbd5e1;line-height:1.5}}
</style></head><body><section class="hero"><div class="hero-inner"><h1>War-Economy Transition Dashboard <span class="abbr">(WETD)</span></h1><p class="subtitle"><strong>What this is for:</strong> War-Economy Transition means the shift from open-market allocation toward national-security allocation. The dashboard is a review queue: it should show <em>what moved</em>, <em>where it matters</em>, <em>why the inference is non-obvious</em>, and <em>which source limits still apply</em>.</p><div class="kpis"><div class="kpi"><span class="num">{official_rows}</span><span>official API/CSV rows loaded</span></div><div class="kpi"><span class="num">{proxy_rows}</span><span>fallback proxy rows, visibly labeled</span></div><div class="kpi"><span class="num">{complete_country_count}</span><span>countries with complete 5-signal scores</span></div><div class="kpi"><span class="num">{theater_score_count}</span><span>country-theater adjusted scores</span></div></div><div class="mece"><div><strong>1. Metric</strong><br><span class="muted">Scores and bubbles show what moved.</span></div><div><strong>2. Narrative</strong><br><span class="muted">Country accordions explain the regime-preparation hypothesis.</span></div><div><strong>3. Evidence</strong><br><span class="muted">Source cards show what is measured vs fallback.</span></div><div><strong>4. Action</strong><br><span class="muted">Commander note and artifacts support analyst review.</span></div></div><p class="muted">Generated {html.escape(now_utc())}. WETD = War-Economy Transition Dashboard. DuckDB batch artifact; verify each source in the provenance cards below.</p></div></section><main><div class="grid2"><div class="card"><h2>Metric layer: country scores</h2><p class="compact-note">Visual scores stay at the top because they are intuitive; they do not claim causality by themselves.</p>{score_bars_html(con)}</div><div class="card"><h2>Metric layer: theater-adjusted risk bubbles</h2><p class="compact-note">The same country score can mean something different inside Taiwan Strait, Middle East, or Arctic exposure.</p>{theater_bubbles_html(con)}</div></div><div class="card"><h2>Narrative layer: country regime-preparation hypotheses</h2><p class="muted">Open each country to see the MECE narrative: 체제 준비, 관측 동향, why it is not a simple cause-effect claim, what to verify, and the five-signal fingerprint. Saudi Arabia is included as a Middle East energy/capital connector rather than hidden in a generic score.</p>{country_narratives_html(con)}</div><div class="card"><h2>Evidence layer: data provenance and trust board</h2><p class="muted">Green cards are official/public rows loaded into DuckDB. Amber cards are key-gated sources or fallback proxy rows; do not read them as high-resolution trade/energy data.</p>{provenance_cards_html(con)}</div><div class="card"><h2>Action layer: commander note</h2><pre>{html.escape(note)}</pre></div><div class="card"><h2>Audit tables</h2><details><summary>Country-month score table</summary>{table_html(con, 'SELECT c.country_iso3, d.country_name, c.signal_count, c.missing_signal_types, ROUND(c.base_wet_score,2) AS base_wet_score, c.is_complete_score FROM wetd_data.vw_country_month_wet_score c JOIN wetd_data.dim_country d USING(country_iso3) ORDER BY c.base_wet_score DESC NULLS LAST', 25)}</details><details><summary>Theater-adjusted score table</summary>{table_html(con, 'SELECT t.country_iso3, d.country_name, t.theater_id, ROUND(t.base_wet_score,2) AS base_wet_score, t.exposure_weight, ROUND(t.multiplier_value,3) AS multiplier, ROUND(t.final_wet_score,2) AS final_wet_score FROM wetd_data.vw_theater_adjusted_score t JOIN wetd_data.dim_country d USING(country_iso3) ORDER BY t.final_wet_score DESC NULLS LAST', 25)}</details><details><summary>Source URL audit table</summary>{table_html(con, 'SELECT source_name, status, rows_loaded, source_url, message FROM wetd_data.data_quality_event ORDER BY observed_at', 50)}</details></div><div class="card"><h2>Artifacts</h2><ul><li><a href="wetd_country_month_scores.csv">wetd_country_month_scores.csv</a></li><li><a href="wetd_theater_adjusted_scores.csv">wetd_theater_adjusted_scores.csv</a></li><li><a href="wetd_signal_scores.csv">wetd_signal_scores.csv</a></li><li><a href="wetd_data_quality.csv">wetd_data_quality.csv</a></li><li><a href="commander_note_{as_of.strftime('%Y_%m')}.md">commander_note_{as_of.strftime('%Y_%m')}.md</a></li></ul></div></main></body></html>'''
    (OUT_DIR / "index.html").write_text(html_doc, encoding="utf-8")


def run(args: argparse.Namespace) -> None:
    as_of = dt.date.fromisoformat(args.as_of)
    con = connect()
    try:
        init_schema(con)
        load_seed(con)
        con.execute("DELETE FROM wetd_data.data_quality_event")
        events: list[QualityEvent] = []
        events.extend(ingest_trade(con, as_of))
        events.extend(ingest_policy_events(con, as_of, args.limit))
        events.extend(ingest_sanctions(con, as_of, args.limit))
        events.extend(ingest_procurement(con, as_of, args.limit))
        events.extend(ingest_energy_minerals(con, as_of))
        events.extend(ingest_arctic(con, as_of))
        record_quality(con, events)
        seed_scenarios(con, as_of)
        score_pipeline(con, as_of)
        export_outputs(con, as_of)
        print(json.dumps(summary(con, as_of), indent=2, ensure_ascii=False))
    finally:
        con.close()


def summary(con: duckdb.DuckDBPyConnection, as_of: dt.date) -> dict[str, Any]:
    table_counts = {}
    for table in [
        "dim_country", "dim_theater", "country_theater_exposure", "config_signal_weight", "fact_trade",
        "fact_policy_event", "fact_sanctions", "fact_procurement", "fact_energy_minerals", "fact_arctic_access",
        "fact_wet_signal_score", "fact_theater_multiplier", "fact_2035_scenario_mapping", "data_quality_event",
    ]:
        table_counts[table] = con.execute(f"SELECT COUNT(*) FROM wetd_data.{table}").fetchone()[0]
    top_scores = con.execute("SELECT country_iso3, ROUND(base_wet_score,2) FROM wetd_data.vw_country_month_wet_score ORDER BY base_wet_score DESC NULLS LAST LIMIT 5").fetchall()
    return {
        "as_of": as_of.isoformat(),
        "db_path": str(DB_PATH.relative_to(REPO)),
        "output_dir": str(OUT_DIR.relative_to(REPO)),
        "table_counts": table_counts,
        "top_scores": top_scores,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run_p = sub.add_parser("run", help="Run the full War-Economy Transition Dashboard batch pipeline")
    run_p.add_argument("--as-of", default=dt.date.today().isoformat(), help="Batch as-of date, YYYY-MM-DD")
    run_p.add_argument("--limit", type=int, default=25, help="Per-source row limit for live API pulls")
    run_p.set_defaults(func=run)
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
