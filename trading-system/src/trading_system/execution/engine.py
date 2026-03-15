from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from trading_system.common.models import Fill, Order, Position, Side, Signal


@dataclass
class RiskLimits:
    max_order_qty: int = 100
    max_position_qty: int = 500


class RiskEngine:
    def __init__(self, limits: RiskLimits):
        self.limits = limits

    def approve(self, signal: Signal, current_position: Position) -> bool:
        if signal.quantity <= 0 or signal.quantity > self.limits.max_order_qty:
            return False
        projected = current_position.quantity + signal.quantity if signal.side == Side.BUY else current_position.quantity - signal.quantity
        return abs(projected) <= self.limits.max_position_qty


class PaperBroker:
    """Always paper mode; executes at provided market price."""

    def submit(self, signal: Signal, market_price: float) -> tuple[Order, Fill]:
        order = Order(
            id=str(uuid4()),
            symbol=signal.symbol,
            timestamp=signal.timestamp,
            side=signal.side,
            quantity=signal.quantity,
        )
        fill = Fill(
            order_id=order.id,
            symbol=order.symbol,
            timestamp=datetime.now(UTC),
            side=order.side,
            quantity=order.quantity,
            price=market_price,
        )
        return order, fill


class PortfolioTracker:
    def __init__(self, starting_cash: float = 50_000):
        self.cash = starting_cash
        self.positions: dict[str, Position] = {}
        self.order_log: list[Order] = []
        self.fill_log: list[Fill] = []

    def _position(self, symbol: str) -> Position:
        if symbol not in self.positions:
            self.positions[symbol] = Position(symbol=symbol)
        return self.positions[symbol]

    def apply_fill(self, fill: Fill) -> None:
        pos = self._position(fill.symbol)
        if fill.side == Side.BUY:
            total_cost = pos.avg_price * pos.quantity + fill.price * fill.quantity
            pos.quantity += fill.quantity
            pos.avg_price = total_cost / pos.quantity
            self.cash -= fill.price * fill.quantity
        else:
            pos.quantity -= fill.quantity
            self.cash += fill.price * fill.quantity
            if pos.quantity == 0:
                pos.avg_price = 0.0
        self.fill_log.append(fill)

    def equity(self, last_prices: dict[str, float]) -> float:
        holdings = sum(p.quantity * last_prices.get(sym, p.avg_price) for sym, p in self.positions.items())
        return self.cash + holdings


class ExecutionService:
    def __init__(self, risk_engine: RiskEngine, broker: PaperBroker, portfolio: PortfolioTracker):
        self.risk_engine = risk_engine
        self.broker = broker
        self.portfolio = portfolio

    def process_signal(self, signal: Signal, market_price: float) -> bool:
        position = self.portfolio.positions.get(signal.symbol, Position(signal.symbol))
        if not self.risk_engine.approve(signal, position):
            return False

        order, fill = self.broker.submit(signal, market_price)
        self.portfolio.order_log.append(order)
        self.portfolio.apply_fill(fill)
        return True
