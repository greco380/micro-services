# Trading System

A modular Python trading research and execution system for disciplined experimentation.

## Scope

This microproject provides:

1. **Historical market data ingestion** from pluggable providers
2. **Strategy research and backtesting** with rule-based and ML-assisted signals
3. **Paper-trading execution and monitoring** with strict risk controls

> The system defaults to **paper trading only** and does **not** promise profitability.

## Architecture

```text
Market Data Providers
    ↓
Data Fetchers / Normalizers / Validators
    ↓
Local Storage (SQLite)
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

## Project Layout

```text
trading-system/
  trading_system/
    data/
      providers.py      # Market data provider interfaces + synthetic provider
      ingestion.py      # Validation + normalization pipeline
      storage.py        # SQLite storage adapter
      features.py       # Feature engineering
    research/
      strategies.py     # Rule-based + ML-assisted strategies
      backtest.py       # Historical simulation engine
      reporting.py      # Backtest report generation
    execution/
      risk.py           # Risk engine and checks
      broker.py         # Paper broker adapter
      engine.py         # Signal → risk → order routing
      monitor.py        # Portfolio/equity monitoring
    config.py           # Configuration dataclasses
    models.py           # Core domain models
    cli.py              # End-to-end runnable workflow
  tests/
    test_end_to_end.py
```

## Quickstart

```bash
cd trading-system
python -m trading_system.cli
```

Run tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```
