from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Side(str, Enum):
    BUY = "buy"
    SELL = "sell"


@dataclass(frozen=True)
class Candle:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(frozen=True)
class Signal:
    symbol: str
    timestamp: datetime
    side: Side
    quantity: int
    reason: str


@dataclass(frozen=True)
class Order:
    id: str
    symbol: str
    timestamp: datetime
    side: Side
    quantity: int
    limit_price: float | None = None


@dataclass(frozen=True)
class Fill:
    order_id: str
    symbol: str
    timestamp: datetime
    side: Side
    quantity: int
    price: float


@dataclass
class Position:
    symbol: str
    quantity: int = 0
    avg_price: float = 0.0
