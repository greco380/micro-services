from dataclasses import dataclass


@dataclass(frozen=True)
class RiskLimits:
    max_position_units: int = 1
    max_notional_per_order: float = 25_000.0
    max_daily_loss: float = 2_000.0


@dataclass(frozen=True)
class SystemConfig:
    symbol: str = "DEMO"
    starting_cash: float = 100_000.0
    short_window: int = 5
    long_window: int = 20
    history_bars: int = 250
    use_ml_assist: bool = True
    db_path: str = ":memory:"
    risk_limits: RiskLimits = RiskLimits()
    paper_trading: bool = True
