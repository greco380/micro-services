# Trading System

A modular Python trading research and execution system for disciplined experimentation.

## Safety principles
- Paper trading by default.
- Explicit risk controls before order routing.
- No guarantee of profitability or returns.

## Architecture

```text
Market Data Providers
    ↓
Data Fetchers / Normalizers / Validators
    ↓
Local Storage (SQLite or DuckDB)
    ↓
Feature Engineering
    ↓
Strategies / Model Training / Backtests
    ↓
Signals
    ↓
Risk Engine
    ↓
Broker Adapter (Paper by default)
    ↓
Orders / Fills / Positions / Equity Tracking
    ↓
Reports / Logs / Alerts
```

## Quick start
```bash
cd trading-system
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m trading_system.main
pytest -q
```

## Project layout
- `src/trading_system/data`: ingestion, validation, normalization, storage, features.
- `src/trading_system/research`: strategy and backtesting engine.
- `src/trading_system/execution`: risk engine, broker adapter, portfolio tracking.
- `src/trading_system/main.py`: example end-to-end pipeline.
- `tests/`: unit tests for all core components.
