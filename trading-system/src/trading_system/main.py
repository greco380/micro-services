from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

from trading_system.common.models import Candle
from trading_system.data.pipeline import DataNormalizer, DataValidator, FeatureEngineer, InMemoryProvider, SQLiteCandleStore
from trading_system.execution.engine import ExecutionService, PaperBroker, PortfolioTracker, RiskEngine, RiskLimits
from trading_system.research.backtest import Backtester, MovingAverageCrossStrategy


def sample_candles(symbol: str = "AAPL") -> list[Candle]:
    start = datetime(2024, 1, 1)
    closes = [100, 101, 103, 102, 104, 107, 105, 106]
    return [
        Candle(
            symbol=symbol,
            timestamp=start + timedelta(days=i),
            open=close - 0.5,
            high=close + 1,
            low=close - 1,
            close=close,
            volume=10_000 + i * 100,
        )
        for i, close in enumerate(closes)
    ]


def run_pipeline() -> dict:
    provider = InMemoryProvider(sample_candles())
    candles = provider.fetch("AAPL")
    candles = DataNormalizer().normalize(DataValidator().validate(candles))

    store = SQLiteCandleStore(Path("trading_system.db"))
    store.write(candles)
    loaded = store.load("AAPL")

    features = FeatureEngineer().add_sma(loaded)

    strategy = MovingAverageCrossStrategy(fast_window=2, slow_window=4, qty=10)
    signals = strategy.generate_signals(loaded)
    backtest = Backtester().run(loaded, signals)

    execution = ExecutionService(RiskEngine(RiskLimits()), PaperBroker(), PortfolioTracker())
    for signal in signals:
        matching = [c for c in loaded if c.timestamp == signal.timestamp]
        if matching:
            execution.process_signal(signal, market_price=matching[0].close)

    last_price = loaded[-1].close if loaded else 0.0
    equity = execution.portfolio.equity({"AAPL": last_price})

    return {
        "candles": len(loaded),
        "features": len(features),
        "signals": len(signals),
        "backtest_return": backtest.total_return,
        "executed_orders": len(execution.portfolio.order_log),
        "equity": equity,
    }


if __name__ == "__main__":
    result = run_pipeline()
    print("Trading system run complete:")
    for k, v in result.items():
        print(f"- {k}: {v}")
