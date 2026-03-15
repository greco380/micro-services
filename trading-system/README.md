# Trading System

A modular Python microproject for trading research and execution with a strict **paper-trading default**.

> This project is for disciplined experimentation only. It does **not** assume profitability and does **not** guarantee returns.

## Overview

This system is built for:

1. Historical market data ingestion
2. Strategy research and backtesting
3. Paper-trading execution with strict risk controls

## Core Components

### 1) Data Ingestion
- Deterministic/synthetic market data provider for reproducible experiments
- OHLCV validation and normalization
- Local persistence in SQLite
- Feature engineering inputs emitted for research and execution

### 2) Strategy Research + Backtesting
- Rule-based strategy: moving-average crossover
- ML-assisted overlay: nearest-centroid direction model over engineered features
- Historical replay backtest with equity, returns, drawdown, and trade counts

### 3) Execution + Monitoring
- Risk checks before each target-position order
- Paper broker adapter (default mode)
- Order event log with filled/rejected statuses
- Portfolio tracking and human-readable operational report

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
├── pyproject.toml
├── README.md
├── src/trading_system/
│   ├── __init__.py
│   ├── backtest.py
│   ├── broker.py
│   ├── cli.py
│   ├── config.py
│   ├── data_ingestion.py
│   ├── execution.py
│   ├── features.py
│   ├── pipeline.py
│   ├── reporting.py
│   ├── risk.py
│   ├── storage.py
│   └── strategy.py
└── tests/
    └── test_pipeline.py
```

## Quickstart

```bash
cd trading-system
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest -q
trading-system
```

## Test readiness

Yes — you can start testing now.

- Package import path for tests is configured in `pyproject.toml`.
- End-to-end pipeline test is included.
- CLI runs the full ingestion → research/backtest → execution/report flow.
