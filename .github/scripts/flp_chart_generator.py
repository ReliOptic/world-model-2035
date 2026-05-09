#!/usr/bin/env python3
"""Generate deterministic Fundamental Line Prediction outputs and SVG chart."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

GROUPS = ("demand", "capacity", "finance")
SCENARIOS = ("base", "upside", "downside", "current")


@dataclass(frozen=True)
class InputRow:
    year: int
    scenario: str
    group: str
    variable_id: str
    source_value: float
    normalization_min: float
    normalization_base: float
    normalization_max: float
    direction: str
    weight: float
    confidence: float
    source_url: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def normalize(row: InputRow) -> float:
    denom = row.normalization_max - row.normalization_min
    if denom == 0:
        return 0.0
    raw = clamp((row.source_value - row.normalization_min) / denom)
    if row.direction == "higher_is_capacity":
        return raw
    if row.direction == "higher_is_constraint":
        return 1 - raw
    raise ValueError(f"Invalid direction: {row.direction}")


def weighted_score(rows: list[InputRow]) -> float:
    denom = sum(row.weight * row.confidence for row in rows)
    if denom == 0:
        return 0.0
    return sum(normalize(row) * row.weight * row.confidence for row in rows) / denom


def read_inputs(path: Path) -> list[InputRow]:
    rows: list[InputRow] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            rows.append(
                InputRow(
                    year=int(raw["year"]),
                    scenario=raw["scenario"],
                    group=raw["group"],
                    variable_id=raw["variable_id"],
                    source_value=float(raw["source_value"]),
                    normalization_min=float(raw["normalization_min"]),
                    normalization_base=float(raw["normalization_base"]),
                    normalization_max=float(raw["normalization_max"]),
                    direction=raw["direction"],
                    weight=float(raw["weight"]),
                    confidence=float(raw["confidence"]),
                    source_url=raw["source_url"],
                )
            )
    return rows


def calculate(rows: list[InputRow]) -> list[dict[str, str]]:
    grouped: dict[tuple[int, str, str], list[InputRow]] = defaultdict(list)
    for row in rows:
        grouped[(row.year, row.scenario, row.group)].append(row)

    years = sorted({row.year for row in rows})
    out: list[dict[str, str]] = []
    for year in years:
        scenario_scores: dict[str, dict[str, float]] = {}
        for scenario in SCENARIOS:
            scores = {group: weighted_score(grouped[(year, scenario, group)]) for group in GROUPS}
            fundamental_score = min(scores["demand"], scores["capacity"], scores["finance"])
            unconstrained = 100 + (year - years[0]) * 7.5
            value = unconstrained * fundamental_score
            scenario_scores[scenario] = {**scores, "fundamental_score": fundamental_score, "value": value}

        base_value = scenario_scores["base"]["value"]
        current_value = scenario_scores["current"]["value"]
        if base_value == 0:
            divergence = 0.0
            signal = "unscorable"
        else:
            divergence = (current_value - base_value) / base_value
            if divergence >= 0.30:
                signal = "overheated"
            elif divergence <= -0.30:
                signal = "undervalued"
            else:
                signal = "neutral"

        out.append(
            {
                "year": str(year),
                "demand_score": f'{scenario_scores["base"]["demand"]:.6f}',
                "capacity_score": f'{scenario_scores["base"]["capacity"]:.6f}',
                "finance_score": f'{scenario_scores["base"]["finance"]:.6f}',
                "fundamental_score": f'{scenario_scores["base"]["fundamental_score"]:.6f}',
                "base_value": f"{base_value:.3f}",
                "upside_value": f'{scenario_scores["upside"]["value"]:.3f}',
                "downside_value": f'{scenario_scores["downside"]["value"]:.3f}',
                "current_implied_value": f"{current_value:.3f}",
                "divergence_pct": f"{divergence:.6f}",
                "signal": signal,
            }
        )
    return out


def write_output(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "year",
        "demand_score",
        "capacity_score",
        "finance_score",
        "fundamental_score",
        "base_value",
        "upside_value",
        "downside_value",
        "current_implied_value",
        "divergence_pct",
        "signal",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def write_chart(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    width, height = 960, 540
    left, right, top, bottom = 80, 40, 45, 80
    plot_w = width - left - right
    plot_h = height - top - bottom
    years = [int(row["year"]) for row in rows]
    series = {
        "Base": [float(row["base_value"]) for row in rows],
        "Upside": [float(row["upside_value"]) for row in rows],
        "Downside": [float(row["downside_value"]) for row in rows],
        "Current implied": [float(row["current_implied_value"]) for row in rows],
    }
    max_v = max(max(vals) for vals in series.values()) * 1.12
    min_v = 0.0

    def x(year: int) -> float:
        return left + (year - years[0]) / (years[-1] - years[0]) * plot_w

    def y(value: float) -> float:
        return top + (max_v - value) / (max_v - min_v) * plot_h

    colors = {
        "Base": "#2563eb",
        "Upside": "#16a34a",
        "Downside": "#dc2626",
        "Current implied": "#111827",
    }
    dash = {"Base": "", "Upside": "4 4", "Downside": "4 4", "Current implied": "8 4"}
    lines = []
    for name, vals in series.items():
        pts = [(x(year), y(value)) for year, value in zip(years, vals)]
        dash_attr = f' stroke-dasharray="{dash[name]}"' if dash[name] else ""
        lines.append(f'<polyline fill="none" stroke="{colors[name]}" stroke-width="3"{dash_attr} points="{polyline(pts)}" />')

    x_ticks = "\n".join(
        f'<text x="{x(year):.1f}" y="{height-45}" text-anchor="middle" font-size="12">{year}</text>'
        for year in years
    )
    y_ticks = []
    for frac in (0, 0.25, 0.5, 0.75, 1.0):
        val = min_v + (max_v - min_v) * frac
        yy = y(val)
        y_ticks.append(f'<line x1="{left}" x2="{width-right}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="#e5e7eb" />')
        y_ticks.append(f'<text x="{left-10}" y="{yy+4:.1f}" text-anchor="end" font-size="12">{val:.0f}</text>')
    legend = []
    lx, ly = left + 20, top + 10
    for i, name in enumerate(series):
        yy = ly + i * 24
        legend.append(f'<line x1="{lx}" x2="{lx+28}" y1="{yy}" y2="{yy}" stroke="{colors[name]}" stroke-width="3" />')
        legend.append(f'<text x="{lx+36}" y="{yy+5}" font-size="13">{name}</text>')
    last = rows[-1]
    subtitle = f"2035 divergence: {float(last['divergence_pct'])*100:.1f}% · signal: {last['signal']}"
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Fundamental Line Prediction chart 2026 to 2035">
  <rect width="100%" height="100%" fill="#ffffff" />
  <text x="{left}" y="26" font-size="20" font-weight="700">AI Infrastructure Fundamental Line Prediction</text>
  <text x="{left}" y="48" font-size="13" fill="#4b5563">{subtitle}</text>
  <line x1="{left}" x2="{left}" y1="{top}" y2="{height-bottom}" stroke="#374151" />
  <line x1="{left}" x2="{width-right}" y1="{height-bottom}" y2="{height-bottom}" stroke="#374151" />
  {''.join(y_ticks)}
  {''.join(lines)}
  {x_ticks}
  <text x="{width/2}" y="{height-12}" text-anchor="middle" font-size="13">Year</text>
  <text transform="translate(20 {height/2}) rotate(-90)" text-anchor="middle" font-size="13">Index value</text>
  {''.join(legend)}
  <text x="{left}" y="{height-25}" font-size="11" fill="#6b7280">Generated deterministically from FLP-0.1 input table.</text>
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--chart", required=True, type=Path)
    args = parser.parse_args()
    rows = calculate(read_inputs(args.input))
    write_output(args.output, rows)
    write_chart(args.chart, rows)
    print(f"Wrote {args.output}")
    print(f"Wrote {args.chart}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
