from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from random import Random
from typing import Iterable


@dataclass(frozen=True)
class OHLCVRecord:
    ts: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


class SyntheticMarketDataProvider:
    """Deterministic provider for repeatable local research and tests."""

    def __init__(self, seed: int = 7) -> None:
        self._rng = Random(seed)

    def fetch_ohlcv(self, bars: int = 250, start_price: float = 100.0) -> list[OHLCVRecord]:
        rows: list[OHLCVRecord] = []
        ts = datetime(2024, 1, 1)
        price = start_price

        for _ in range(bars):
            drift = self._rng.uniform(-1.2, 1.4)
            open_px = price
            close_px = max(1.0, open_px + drift)
            high_px = max(open_px, close_px) + self._rng.uniform(0.0, 0.6)
            low_px = min(open_px, close_px) - self._rng.uniform(0.0, 0.6)
            volume = self._rng.uniform(8_000, 60_000)
            rows.append(
                OHLCVRecord(
                    ts=ts,
                    open=round(open_px, 4),
                    high=round(high_px, 4),
                    low=round(max(0.5, low_px), 4),
                    close=round(close_px, 4),
                    volume=round(volume, 2),
                )
            )
            ts += timedelta(days=1)
            price = close_px
        return rows


def validate_ohlcv(records: Iterable[OHLCVRecord]) -> list[OHLCVRecord]:
    validated: list[OHLCVRecord] = []
    for rec in records:
        if rec.high < rec.low:
            continue
        if rec.volume < 0:
            continue
        if not (rec.low <= rec.open <= rec.high):
            continue
        if not (rec.low <= rec.close <= rec.high):
            continue
        validated.append(rec)
    return validated


def normalize_ohlcv(records: Iterable[OHLCVRecord]) -> list[OHLCVRecord]:
    """Sort rows and clamp malformed values into a consistent canonical form."""

    sorted_rows = sorted(records, key=lambda r: r.ts)
    normalized: list[OHLCVRecord] = []

    for rec in sorted_rows:
        high = max(rec.open, rec.close, rec.high, rec.low)
        low = min(rec.open, rec.close, rec.high, rec.low)
        normalized.append(
            OHLCVRecord(
                ts=rec.ts,
                open=float(rec.open),
                high=float(high),
                low=float(low),
                close=float(rec.close),
                volume=max(0.0, float(rec.volume)),
            )
        )

    return normalized
