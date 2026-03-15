from dataclasses import dataclass
from datetime import datetime
from typing import Literal


Signal = Literal["BUY", "SELL", "HOLD"]
OrderSide = Literal["BUY", "SELL"]
OrderStatus = Literal["NEW", "REJECTED", "FILLED"]


@dataclass(slots=True)
class OHLCVBar:
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass(slots=True)
class FeatureRow:
    symbol: str
    timestamp: datetime
    close: float
    sma_fast: float
    sma_slow: float
    momentum: float


@dataclass(slots=True)
class Order:
    id: str
    symbol: str
    side: OrderSide
    quantity: int
    price: float
    status: OrderStatus
    reason: str = ""


@dataclass(slots=True)
class Fill:
    order_id: str
    symbol: str
    side: OrderSide
    quantity: int
    price: float
    timestamp: datetime


@dataclass(slots=True)
class PortfolioState:
    cash: float
    position_qty: int = 0
    avg_entry_price: float = 0.0
