#!/usr/bin/env python3
"""Audit issue-backed sector vertical slices for the 2035 model."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

ISSUE_FILES = {
    2: [
        "16_industrial_base/manufacturing_capacity.md",
        "16_industrial_base/electrical_equipment.md",
        "16_industrial_base/machine_tools.md",
        "16_industrial_base/industrial_automation.md",
    ],
    3: [
        "17_materials_and_mining/copper.md",
        "17_materials_and_mining/lithium.md",
        "17_materials_and_mining/rare_earths.md",
        "17_materials_and_mining/steel_cement_chemicals.md",
    ],
    4: [
        "18_built_environment/construction_capacity.md",
        "18_built_environment/data_center_construction.md",
        "18_built_environment/permitting_labor_bottlenecks.md",
        "18_built_environment/housing_real_estate.md",
    ],
    5: [
        "19_logistics_and_trade/shipping.md",
        "19_logistics_and_trade/ports.md",
        "19_logistics_and_trade/rail_trucking.md",
        "19_logistics_and_trade/supply_chain_fragmentation.md",
    ],
    6: [
        "20_food_water_agriculture/food_security.md",
        "20_food_water_agriculture/water_stress.md",
        "20_food_water_agriculture/fertilizer.md",
        "20_food_water_agriculture/agricultural_automation.md",
    ],
    7: [
        "21_healthcare_systems/aging_capacity.md",
        "21_healthcare_systems/hospital_capacity.md",
        "21_healthcare_systems/insurance_costs.md",
        "21_healthcare_systems/ai_care_delivery.md",
    ],
    8: [
        "22_financial_markets/credit_spreads.md",
        "22_financial_markets/private_credit.md",
        "22_financial_markets/insurance_reinsurance.md",
        "22_financial_markets/asset_price_divergence.md",
    ],
    9: [
        "23_connectivity_infrastructure/fiber_backbone.md",
        "23_connectivity_infrastructure/subsea_cables.md",
        "23_connectivity_infrastructure/6g.md",
        "23_connectivity_infrastructure/satellite_backhaul.md",
    ],
    10: [
        "24_human_capital/skilled_trades.md",
        "24_human_capital/engineers.md",
        "24_human_capital/healthcare_workforce.md",
        "24_human_capital/education_reskilling.md",
    ],
    11: [
        "25_circular_economy/battery_recycling.md",
        "25_circular_economy/e_waste.md",
        "25_circular_economy/secondary_metals.md",
        "25_circular_economy/plastics_waste.md",
    ],
    12: [
        "00_foundations/fundamental_line_prediction.md",
        "13_scenarios/fundamental_line_pilot_ai_infra.md",
    ],
}

REQUIRED_TOKENS = [
    "**정보 신선도:**",
    "## 2026년 4월 현재 상태",
    "## 1년 단위 전망",
    "## 2035 전망 요약",
    "## 연결 문서",
    "## 정보 출처",
    "Base",
    "Upside",
    "Downside",
]
YEAR_ROW_RE = re.compile(r"\|\s*(20[2-3][0-9])\s*\|")
URL_RE = re.compile(r"https?://\S+")


def main() -> int:
    errors: list[str] = []
    checked = 0
    for issue, rels in ISSUE_FILES.items():
        for rel in rels:
            path = REPO_ROOT / rel
            if not path.exists():
                errors.append(f"#{issue} missing {rel}")
                continue
            checked += 1
            text = path.read_text(encoding="utf-8", errors="ignore")
            for token in REQUIRED_TOKENS:
                if token not in text:
                    errors.append(f"#{issue} {rel}: missing `{token}`")
            years = set(YEAR_ROW_RE.findall(text))
            missing_years = [str(y) for y in range(2026, 2036) if str(y) not in years]
            if missing_years:
                errors.append(f"#{issue} {rel}: missing annual rows {', '.join(missing_years)}")
            if "## 정보 출처" in text and not URL_RE.search(text.split("## 정보 출처", 1)[1]):
                errors.append(f"#{issue} {rel}: source section has no URL")
            if issue == 12 and "deterministic" not in text.lower():
                errors.append(f"#{issue} {rel}: missing deterministic calculation language")
    print(f"Issue-backed files checked: {checked}")
    print(f"Issue-backed errors: {len(errors)}")
    if errors:
        print("\n## Errors")
        for err in errors[:300]:
            print(f"- {err}")
        if len(errors) > 300:
            print(f"- ... {len(errors) - 300} more")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
