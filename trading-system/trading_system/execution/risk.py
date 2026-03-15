from dataclasses import dataclass

from trading_system.models import PortfolioState


@dataclass(slots=True)
class RiskDecision:
    approved: bool
    reason: str = ""


class RiskEngine:
    def __init__(self, max_position_size: int, max_daily_loss: float, starting_cash: float) -> None:
        self.max_position_size = max_position_size
        self.max_daily_loss = max_daily_loss
        self.starting_cash = starting_cash

    def check_order(self, side: str, qty: int, price: float, portfolio: PortfolioState) -> RiskDecision:
        projected_position = portfolio.position_qty + qty if side == "BUY" else portfolio.position_qty - qty
        if abs(projected_position) > self.max_position_size:
            return RiskDecision(False, "max_position_size_exceeded")

        equity = portfolio.cash + portfolio.position_qty * price
        loss = max(0.0, self.starting_cash - equity)
        if loss > self.max_daily_loss:
            return RiskDecision(False, "max_daily_loss_exceeded")

        return RiskDecision(True, "approved")
