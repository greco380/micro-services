from datetime import UTC, datetime

from trading_system.common.models import Position, Side, Signal
from trading_system.execution.engine import ExecutionService, PaperBroker, PortfolioTracker, RiskEngine, RiskLimits


def test_risk_engine_and_execution():
    risk = RiskEngine(RiskLimits(max_order_qty=10, max_position_qty=20))
    broker = PaperBroker()
    portfolio = PortfolioTracker(starting_cash=1000)
    service = ExecutionService(risk, broker, portfolio)

    signal = Signal("AAPL", datetime.now(UTC), Side.BUY, 5, "test")
    assert service.process_signal(signal, market_price=10)
    assert portfolio.positions["AAPL"].quantity == 5

    bad_signal = Signal("AAPL", datetime.now(UTC), Side.BUY, 50, "too_large")
    assert not risk.approve(bad_signal, Position("AAPL", quantity=5))
