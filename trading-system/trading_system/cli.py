from __future__ import annotations

from pathlib import Path

from trading_system.config import AppConfig
from trading_system.data.features import FeatureEngineer
from trading_system.data.ingestion import IngestionPipeline
from trading_system.data.providers import SyntheticMarketDataProvider
from trading_system.data.storage import Storage
from trading_system.execution.broker import PaperBroker
from trading_system.execution.engine import ExecutionEngine
from trading_system.execution.monitor import Monitor
from trading_system.execution.risk import RiskEngine
from trading_system.models import PortfolioState
from trading_system.research.backtest import Backtester
from trading_system.research.reporting import BacktestReporter
from trading_system.research.strategies import MLAssistedStrategy, MovingAverageCrossStrategy


def run(config: AppConfig | None = None) -> dict[str, str]:
    config = config or AppConfig()
    storage = Storage(config.database_path)

    provider = SyntheticMarketDataProvider()
    bars = provider.fetch_ohlcv(config.data.symbol, config.data.bar_count)
    clean_bars = IngestionPipeline().process(bars)
    storage.write_bars(clean_bars)

    features = FeatureEngineer().build(clean_bars)
    storage.write_features(features)

    ma_strategy = MovingAverageCrossStrategy()
    ml_strategy = MLAssistedStrategy()

    backtester = Backtester(starting_cash=config.execution.starting_cash)
    ma_result = backtester.run(features, ma_strategy)
    ml_result = backtester.run(features, ml_strategy)

    report_dir = Path("reports")
    report_dir.mkdir(exist_ok=True)
    ma_report = BacktestReporter.to_markdown(ma_result, "MovingAverageCross")
    ml_report = BacktestReporter.to_markdown(ml_result, "MLAssisted")

    ma_path = report_dir / "ma_backtest.md"
    ml_path = report_dir / "ml_backtest.md"
    ma_path.write_text(ma_report, encoding="utf-8")
    ml_path.write_text(ml_report, encoding="utf-8")

    risk = RiskEngine(
        max_position_size=config.risk.max_position_size,
        max_daily_loss=config.risk.max_daily_loss,
        starting_cash=config.execution.starting_cash,
    )
    exec_engine = ExecutionEngine(PaperBroker(), risk)
    portfolio = PortfolioState(cash=config.execution.starting_cash)

    for feature in features[-20:]:
        signal = ml_strategy.generate(feature)
        order, fill = exec_engine.route_signal(signal, feature, portfolio)
        if order:
            storage.write_order(order)
        if fill:
            storage.write_fill(fill)

    snapshot = Monitor.snapshot(portfolio, features[-1].close)
    snapshot_json = Monitor.to_json(snapshot)
    snapshot_path = report_dir / "portfolio_snapshot.json"
    snapshot_path.write_text(snapshot_json, encoding="utf-8")

    return {
        "database": config.database_path,
        "ma_report": str(ma_path),
        "ml_report": str(ml_path),
        "snapshot": str(snapshot_path),
    }


if __name__ == "__main__":
    outputs = run()
    for name, path in outputs.items():
        print(f"{name}: {path}")
