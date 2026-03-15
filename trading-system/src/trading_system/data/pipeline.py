from __future__ import annotations

import sqlite3
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Iterable

from trading_system.common.models import Candle


class InMemoryProvider:
    """Simple provider for deterministic research and tests."""

    def __init__(self, candles: Iterable[Candle]):
        self._candles = list(candles)

    def fetch(self, symbol: str) -> list[Candle]:
        return [c for c in self._candles if c.symbol == symbol]


class DataValidator:
    def validate(self, candles: Iterable[Candle]) -> list[Candle]:
        clean: list[Candle] = []
        for candle in candles:
            if not (candle.low <= candle.open <= candle.high):
                continue
            if not (candle.low <= candle.close <= candle.high):
                continue
            if candle.volume < 0:
                continue
            clean.append(candle)
        return clean


class DataNormalizer:
    def normalize(self, candles: Iterable[Candle]) -> list[Candle]:
        return sorted(candles, key=lambda c: c.timestamp)


class SQLiteCandleStore:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._ensure_schema()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _ensure_schema(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS candles (
                    symbol TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    open REAL NOT NULL,
                    high REAL NOT NULL,
                    low REAL NOT NULL,
                    close REAL NOT NULL,
                    volume REAL NOT NULL,
                    PRIMARY KEY(symbol, timestamp)
                )
                """
            )

    def write(self, candles: Iterable[Candle]) -> None:
        rows = [asdict(c) for c in candles]
        with self._connect() as conn:
            conn.executemany(
                """
                INSERT OR REPLACE INTO candles(symbol, timestamp, open, high, low, close, volume)
                VALUES(:symbol, :timestamp, :open, :high, :low, :close, :volume)
                """,
                [{**r, "timestamp": r["timestamp"].isoformat()} for r in rows],
            )

    def load(self, symbol: str) -> list[Candle]:
        with self._connect() as conn:
            cursor = conn.execute(
                """
                SELECT symbol, timestamp, open, high, low, close, volume
                FROM candles WHERE symbol = ? ORDER BY timestamp
                """,
                (symbol,),
            )
            rows = cursor.fetchall()
        return [
            Candle(
                symbol=row[0],
                timestamp=datetime.fromisoformat(row[1]),
                open=row[2],
                high=row[3],
                low=row[4],
                close=row[5],
                volume=row[6],
            )
            for row in rows
        ]


class FeatureEngineer:
    def add_sma(self, candles: list[Candle], window: int = 3) -> list[dict]:
        output: list[dict] = []
        closes = [c.close for c in candles]
        for idx, candle in enumerate(candles):
            start = max(0, idx - window + 1)
            sub = closes[start : idx + 1]
            sma = sum(sub) / len(sub)
            output.append({"candle": candle, "sma": sma})
        return output
