import json
from dataclasses import dataclass, asdict

from trading_system.models import PortfolioState


@dataclass(slots=True)
class PortfolioSnapshot:
    cash: float
    position_qty: int
    mark_price: float
    equity: float


class Monitor:
    @staticmethod
    def snapshot(portfolio: PortfolioState, mark_price: float) -> PortfolioSnapshot:
        equity = portfolio.cash + portfolio.position_qty * mark_price
        return PortfolioSnapshot(
            cash=portfolio.cash,
            position_qty=portfolio.position_qty,
            mark_price=mark_price,
            equity=equity,
        )

    @staticmethod
    def to_json(snapshot: PortfolioSnapshot) -> str:
        return json.dumps(asdict(snapshot), indent=2)
