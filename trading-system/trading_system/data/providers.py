from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import random

from trading_system.models import OHLCVBar


class MarketDataProvider(ABC):
    @abstractmethod
    def fetch_ohlcv(self, symbol: str, limit: int) -> list[OHLCVBar]:
        raise NotImplementedError


class SyntheticMarketDataProvider(MarketDataProvider):
    """Deterministic random-walk data source for local research/testing."""

    def __init__(self, seed: int = 7) -> None:
        self._seed = seed

    def fetch_ohlcv(self, symbol: str, limit: int) -> list[OHLCVBar]:
        rng = random.Random(self._seed)
        now = datetime.utcnow().replace(microsecond=0)
        price = 100.0
        bars: list[OHLCVBar] = []

        for i in range(limit):
            drift = rng.uniform(-1.2, 1.2)
            open_price = price
            close = max(1.0, open_price + drift)
            high = max(open_price, close) + abs(rng.uniform(0, 0.6))
            low = min(open_price, close) - abs(rng.uniform(0, 0.6))
            volume = 1_000 + rng.randint(0, 2_000)
            bars.append(
                OHLCVBar(
                    symbol=symbol,
                    timestamp=now - timedelta(minutes=(limit - i)),
                    open=round(open_price, 4),
                    high=round(high, 4),
                    low=round(low, 4),
                    close=round(close, 4),
                    volume=float(volume),
                )
            )
            price = close
        return bars
