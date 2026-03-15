from datetime import datetime, timedelta

from trading_system.common.models import Candle
from trading_system.research.backtest import Backtester, MovingAverageCrossStrategy


def _candles():
    start = datetime(2024, 1, 1)
    closes = [10, 11, 12, 11, 10, 12]
    return [
        Candle("AAPL", start + timedelta(days=i), c - 1, c + 1, c - 2, c, 1000)
        for i, c in enumerate(closes)
    ]


def test_strategy_and_backtester():
    candles = _candles()
    strategy = MovingAverageCrossStrategy(fast_window=2, slow_window=3, qty=5)
    signals = strategy.generate_signals(candles)
    assert signals

    result = Backtester().run(candles, signals, initial_cash=1000)
    assert isinstance(result.total_return, float)
    assert len(result.equity_curve) == len(candles)
