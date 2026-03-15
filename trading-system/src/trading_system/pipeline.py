from __future__ import annotations

from .backtest import BacktestResult, run_backtest
from .config import SystemConfig
from .data_ingestion import SyntheticMarketDataProvider, normalize_ohlcv, validate_ohlcv
from .execution import PortfolioState, run_execution
from .features import build_feature_frame
from .reporting import build_report
from .storage import SQLiteMarketStore
from .strategy import generate_signals


def run_trading_system(config: SystemConfig | None = None) -> dict:
    cfg = config or SystemConfig()

    provider = SyntheticMarketDataProvider()
    raw = provider.fetch_ohlcv(bars=cfg.history_bars)
    clean = normalize_ohlcv(validate_ohlcv(raw))

    store = SQLiteMarketStore(db_path=cfg.db_path)
    store.save_ohlcv(clean)
    ts_and_closes = store.load_closes()

    timestamps = [ts for ts, _ in ts_and_closes]
    closes = [close for _, close in ts_and_closes]

    features = build_feature_frame(closes, cfg.short_window, cfg.long_window)
    signals = generate_signals(features, use_ml_assist=cfg.use_ml_assist)

    backtest: BacktestResult = run_backtest(closes, signals, cfg.starting_cash)
    execution: PortfolioState = run_execution(
        timestamps=timestamps,
        closes=closes,
        signals=signals,
        symbol=cfg.symbol,
        starting_cash=cfg.starting_cash,
        limits=cfg.risk_limits,
    )
    report = build_report(backtest=backtest, execution=execution, last_close=closes[-1])

    return {
        "config": cfg,
        "rows_loaded": len(clean),
        "features": features,
        "signals": signals,
        "backtest": backtest,
        "execution": execution,
        "report": report,
    }
