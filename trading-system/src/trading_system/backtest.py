from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BacktestResult:
    final_equity: float
    total_return: float
    max_drawdown: float
    trades: int


def run_backtest(closes: list[float], signals: list[int], starting_cash: float) -> BacktestResult:
    cash = starting_cash
    units = 0
    trades = 0
    equity_curve: list[float] = []

    for close, signal in zip(closes, signals):
        target_units = signal
        delta = target_units - units
        if delta != 0:
            trades += 1
        cash -= delta * close
        units = target_units
        equity_curve.append(cash + units * close)

    if not equity_curve:
        return BacktestResult(starting_cash, 0.0, 0.0, 0)

    peak = equity_curve[0]
    max_drawdown = 0.0
    for equity in equity_curve:
        peak = max(peak, equity)
        drawdown = (peak - equity) / peak if peak else 0.0
        max_drawdown = max(max_drawdown, drawdown)

    final_equity = equity_curve[-1]
    return BacktestResult(
        final_equity=final_equity,
        total_return=(final_equity - starting_cash) / starting_cash,
        max_drawdown=max_drawdown,
        trades=trades,
    )
