from __future__ import annotations

import sqlite3
from pathlib import Path

from .data_ingestion import OHLCVRecord


class SQLiteMarketStore:
    def __init__(self, db_path: str | Path = ":memory:") -> None:
        self.conn = sqlite3.connect(str(db_path))
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS ohlcv (
                ts TEXT PRIMARY KEY,
                open REAL NOT NULL,
                high REAL NOT NULL,
                low REAL NOT NULL,
                close REAL NOT NULL,
                volume REAL NOT NULL
            )
            """
        )
        self.conn.commit()

    def save_ohlcv(self, records: list[OHLCVRecord]) -> None:
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO ohlcv(ts, open, high, low, close, volume)
            VALUES(?, ?, ?, ?, ?, ?)
            """,
            [(r.ts.isoformat(), r.open, r.high, r.low, r.close, r.volume) for r in records],
        )
        self.conn.commit()

    def load_ohlcv(self) -> list[tuple[str, float, float, float, float, float]]:
        cur = self.conn.execute("SELECT ts, open, high, low, close, volume FROM ohlcv ORDER BY ts")
        return [(str(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5])) for r in cur.fetchall()]

    def load_closes(self) -> list[tuple[str, float]]:
        cur = self.conn.execute("SELECT ts, close FROM ohlcv ORDER BY ts")
        return [(str(row[0]), float(row[1])) for row in cur.fetchall()]
