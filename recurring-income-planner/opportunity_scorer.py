#!/usr/bin/env python3
"""Score and rank legal micro-SaaS opportunities by risk-adjusted ROI assumptions."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Opportunity:
    name: str
    setup_cost_eur: float
    monthly_operating_cost_eur: float
    estimated_price_eur: float
    estimated_customers: int
    estimated_hours_per_month: float
    reliability_score: float
    legal_complexity_score: float
    competition_score: float

    @property
    def estimated_revenue(self) -> float:
        return self.estimated_price_eur * self.estimated_customers

    @property
    def estimated_profit(self) -> float:
        return self.estimated_revenue - self.monthly_operating_cost_eur

    @property
    def payback_months(self) -> float:
        profit = self.estimated_profit
        return self.setup_cost_eur / profit if profit > 0 else float("inf")

    @property
    def risk_adjusted_score(self) -> float:
        if self.estimated_profit <= 0:
            return -999.0

        # Higher reliability and lower complexity/competition improve confidence.
        confidence = (
            (self.reliability_score * 0.5)
            + ((10 - self.legal_complexity_score) * 0.3)
            + ((10 - self.competition_score) * 0.2)
        ) / 10

        automation_bonus = max(0.1, 1 - (self.estimated_hours_per_month / 40))
        payback_penalty = min(2.0, self.payback_months / 12)

        return (self.estimated_profit * confidence * automation_bonus) - (payback_penalty * 100)


def load_opportunities(path: Path) -> List[Opportunity]:
    data = json.loads(path.read_text())
    return [Opportunity(**item) for item in data]


def recommend(opportunities: List[Opportunity], target_profit: float) -> List[Opportunity]:
    candidates = [o for o in opportunities if o.estimated_profit >= target_profit]
    if not candidates:
        candidates = opportunities
    return sorted(candidates, key=lambda o: o.risk_adjusted_score, reverse=True)


def format_row(rank: int, opp: Opportunity) -> str:
    payback = "never" if opp.payback_months == float("inf") else f"{opp.payback_months:.1f} mo"
    return (
        f"{rank:>2}. {opp.name:<38} "
        f"profit €{opp.estimated_profit:>7.2f} | "
        f"payback {payback:<8} | "
        f"score {opp.risk_adjusted_score:>7.2f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank microservice business ideas by assumptions.")
    parser.add_argument("--input", type=Path, default=Path("opportunities.sample.json"))
    parser.add_argument("--target-profit", type=float, default=400.0)
    args = parser.parse_args()

    opportunities = load_opportunities(args.input)
    ranking = recommend(opportunities, args.target_profit)

    print("Top opportunities (assumption-based, not guaranteed):")
    for idx, opp in enumerate(ranking, start=1):
        print(format_row(idx, opp))

    best = ranking[0]
    print("\nRecommended first project:")
    print(f"- {best.name}")
    print(f"- Estimated monthly revenue: €{best.estimated_revenue:.2f}")
    print(f"- Estimated monthly profit: €{best.estimated_profit:.2f}")
    print(f"- Estimated payback period: {best.payback_months:.1f} months")


if __name__ == "__main__":
    main()
