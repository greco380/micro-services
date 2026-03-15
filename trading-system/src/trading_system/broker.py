from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OrderEvent:
    ts: str
    symbol: str
    target_units: int
    fill_price: float
    status: str
    reason: str = ""


class PaperBrokerAdapter:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def execute_target(self, ts: str, target_units: int, fill_price: float) -> OrderEvent:
        return OrderEvent(
            ts=ts,
            symbol=self.symbol,
            target_units=target_units,
            fill_price=fill_price,
            status="filled",
        )
