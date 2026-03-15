from __future__ import annotations

import sqlite3

from trading_system.models import FeatureRow, Fill, OHLCVBar, Order


class Storage:
    def __init__(self, path: str) -> None:
        self.path = path
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS bars (
                    symbol TEXT,
                    timestamp TEXT,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    volume REAL
                );
                CREATE TABLE IF NOT EXISTS features (
                    symbol TEXT,
                    timestamp TEXT,
                    close REAL,
                    sma_fast REAL,
                    sma_slow REAL,
                    momentum REAL
                );
                CREATE TABLE IF NOT EXISTS orders (
                    id TEXT,
                    symbol TEXT,
                    side TEXT,
                    quantity INTEGER,
                    price REAL,
                    status TEXT,
                    reason TEXT
                );
                CREATE TABLE IF NOT EXISTS fills (
                    order_id TEXT,
                    symbol TEXT,
                    side TEXT,
                    quantity INTEGER,
                    price REAL,
                    timestamp TEXT
                );
                """
            )

    def write_bars(self, bars: list[OHLCVBar]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT INTO bars VALUES (?, ?, ?, ?, ?, ?, ?)",
                [
                    (
                        b.symbol,
                        b.timestamp.isoformat(),
                        b.open,
                        b.high,
                        b.low,
                        b.close,
                        b.volume,
                    )
                    for b in bars
                ],
            )

    def write_features(self, features: list[FeatureRow]) -> None:
        with self._connect() as conn:
            conn.executemany(
                "INSERT INTO features VALUES (?, ?, ?, ?, ?, ?)",
                [
                    (
                        f.symbol,
                        f.timestamp.isoformat(),
                        f.close,
                        f.sma_fast,
                        f.sma_slow,
                        f.momentum,
                    )
                    for f in features
                ],
            )

    def write_order(self, order: Order) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)",
                (order.id, order.symbol, order.side, order.quantity, order.price, order.status, order.reason),
            )

    def write_fill(self, fill: Fill) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO fills VALUES (?, ?, ?, ?, ?, ?)",
                (fill.order_id, fill.symbol, fill.side, fill.quantity, fill.price, fill.timestamp.isoformat()),
            )
