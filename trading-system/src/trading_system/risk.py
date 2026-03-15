from __future__ import annotations

from dataclasses import dataclass

from .config import RiskLimits


@dataclass
class RiskDecision:
    allowed: bool
    reason: str


def evaluate_order(
    *,
    target_units: int,
    current_units: int,
    price: float,
    realized_pnl_today: float,
    limits: RiskLimits,
) -> RiskDecision:
    if abs(target_units) > limits.max_position_units:
        return RiskDecision(False, "position limit exceeded")

    delta_units = abs(target_units - current_units)
    if (delta_units * price) > limits.max_notional_per_order:
        return RiskDecision(False, "order notional limit exceeded")

    if realized_pnl_today <= -abs(limits.max_daily_loss):
        return RiskDecision(False, "daily loss limit hit")

    return RiskDecision(True, "approved")
