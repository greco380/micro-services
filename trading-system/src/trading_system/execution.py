from __future__ import annotations

from dataclasses import dataclass, field

from .broker import OrderEvent, PaperBrokerAdapter
from .config import RiskLimits
from .risk import evaluate_order


@dataclass
class PortfolioState:
    cash: float
    units: int = 0
    realized_pnl_today: float = 0.0
    events: list[OrderEvent] = field(default_factory=list)
    rejected_orders: int = 0


def run_execution(
    *,
    timestamps: list[str],
    closes: list[float],
    signals: list[int],
    symbol: str,
    starting_cash: float,
    limits: RiskLimits,
) -> PortfolioState:
    broker = PaperBrokerAdapter(symbol)
    state = PortfolioState(cash=starting_cash)
    prior_price = closes[0] if closes else 0.0

    for ts, close, signal in zip(timestamps, closes, signals):
        state.realized_pnl_today += state.units * (close - prior_price)

        decision = evaluate_order(
            target_units=signal,
            current_units=state.units,
            price=close,
            realized_pnl_today=state.realized_pnl_today,
            limits=limits,
        )

        if not decision.allowed:
            state.rejected_orders += 1
            state.events.append(
                OrderEvent(
                    ts=ts,
                    symbol=symbol,
                    target_units=state.units,
                    fill_price=close,
                    status="rejected",
                    reason=decision.reason,
                )
            )
            prior_price = close
            continue

        delta = signal - state.units
        state.cash -= delta * close
        state.units = signal
        state.events.append(broker.execute_target(ts=ts, target_units=signal, fill_price=close))
        prior_price = close

    return state
