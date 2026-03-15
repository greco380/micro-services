from __future__ import annotations

from .backtest import BacktestResult
from .execution import PortfolioState


def build_report(*, backtest: BacktestResult, execution: PortfolioState, last_close: float) -> str:
    equity = execution.cash + execution.units * last_close
    lines = [
        "=== Trading System Report ===",
        f"Backtest final equity: {backtest.final_equity:.2f}",
        f"Backtest total return: {backtest.total_return:.2%}",
        f"Backtest max drawdown: {backtest.max_drawdown:.2%}",
        f"Backtest trades: {backtest.trades}",
        f"Paper execution cash: {execution.cash:.2f}",
        f"Paper execution units: {execution.units}",
        f"Paper execution equity: {equity:.2f}",
        f"Filled/rejected events: {sum(e.status == 'filled' for e in execution.events)}/{execution.rejected_orders}",
    ]
    return "\n".join(lines)
