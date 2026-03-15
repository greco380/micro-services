from trading_system.execution.broker import PaperBroker
from trading_system.execution.risk import RiskEngine
from trading_system.models import FeatureRow, PortfolioState, Signal


class ExecutionEngine:
    def __init__(self, broker: PaperBroker, risk: RiskEngine, qty_per_trade: int = 1) -> None:
        self.broker = broker
        self.risk = risk
        self.qty_per_trade = qty_per_trade

    def route_signal(self, signal: Signal, feature: FeatureRow, portfolio: PortfolioState):
        if signal == "HOLD":
            return None, None

        side = "BUY" if signal == "BUY" else "SELL"
        decision = self.risk.check_order(side, self.qty_per_trade, feature.close, portfolio)
        order, fill = self.broker.submit_order(
            symbol=feature.symbol,
            side=side,
            quantity=self.qty_per_trade,
            price=feature.close,
            approved=decision.approved,
            reason=decision.reason,
        )

        if fill:
            if fill.side == "BUY":
                portfolio.cash -= fill.quantity * fill.price
                portfolio.position_qty += fill.quantity
            else:
                portfolio.cash += fill.quantity * fill.price
                portfolio.position_qty -= fill.quantity
        return order, fill
