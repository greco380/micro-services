from __future__ import annotations

from dataclasses import dataclass

from trading_system.common.models import Candle, Side, Signal


class MovingAverageCrossStrategy:
    """Generates buy/sell signals using fast and slow SMA crossover."""

    def __init__(self, fast_window: int = 3, slow_window: int = 5, qty: int = 1):
        if fast_window >= slow_window:
            raise ValueError("fast_window must be less than slow_window")
        self.fast_window = fast_window
        self.slow_window = slow_window
        self.qty = qty

    def _sma(self, candles: list[Candle], idx: int, window: int) -> float:
        start = max(0, idx - window + 1)
        subset = candles[start : idx + 1]
        return sum(c.close for c in subset) / len(subset)

    def generate_signals(self, candles: list[Candle]) -> list[Signal]:
        signals: list[Signal] = []
        if not candles:
            return signals

        last_state: str | None = None
        for idx in range(len(candles)):
            fast = self._sma(candles, idx, self.fast_window)
            slow = self._sma(candles, idx, self.slow_window)
            state = "above" if fast > slow else "below"
            if last_state and state != last_state:
                side = Side.BUY if state == "above" else Side.SELL
                signals.append(
                    Signal(
                        symbol=candles[idx].symbol,
                        timestamp=candles[idx].timestamp,
                        side=side,
                        quantity=self.qty,
                        reason=f"ma_cross:{last_state}->{state}",
                    )
                )
            last_state = state
        return signals


@dataclass
class BacktestResult:
    total_return: float
    trades: int
    win_rate: float
    equity_curve: list[float]


class Backtester:
    def run(self, candles: list[Candle], signals: list[Signal], initial_cash: float = 10_000) -> BacktestResult:
        if not candles:
            return BacktestResult(0.0, 0, 0.0, [initial_cash])

        by_ts = {s.timestamp: s for s in signals}
        cash = initial_cash
        position = 0
        entry_price = 0.0
        wins = 0
        closed = 0
        equity_curve: list[float] = []

        for candle in candles:
            signal = by_ts.get(candle.timestamp)
            if signal:
                if signal.side == Side.BUY:
                    cost = signal.quantity * candle.close
                    if cash >= cost:
                        cash -= cost
                        position += signal.quantity
                        entry_price = candle.close
                else:
                    qty = min(position, signal.quantity)
                    if qty > 0:
                        cash += qty * candle.close
                        if candle.close > entry_price:
                            wins += 1
                        position -= qty
                        closed += 1
            equity_curve.append(cash + position * candle.close)

        total_return = (equity_curve[-1] - initial_cash) / initial_cash
        win_rate = (wins / closed) if closed else 0.0
        return BacktestResult(total_return, closed, win_rate, equity_curve)
