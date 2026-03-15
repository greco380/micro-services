from __future__ import annotations

from datetime import datetime
import uuid

from trading_system.models import Fill, Order


class PaperBroker:
    def submit_order(self, symbol: str, side: str, quantity: int, price: float, approved: bool, reason: str) -> tuple[Order, Fill | None]:
        order = Order(
            id=str(uuid.uuid4()),
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
            status="FILLED" if approved else "REJECTED",
            reason=reason,
        )
        if not approved:
            return order, None

        fill = Fill(
            order_id=order.id,
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
            timestamp=datetime.utcnow(),
        )
        return order, fill
