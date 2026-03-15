from dataclasses import dataclass, field


@dataclass(slots=True)
class DataConfig:
    symbol: str = "DEMO"
    bar_count: int = 200


@dataclass(slots=True)
class RiskConfig:
    max_position_size: int = 100
    max_daily_loss: float = 500.0


@dataclass(slots=True)
class ExecutionConfig:
    starting_cash: float = 100_000.0
    mode: str = "paper"


@dataclass(slots=True)
class AppConfig:
    database_path: str = "trading_system.db"
    data: DataConfig = field(default_factory=DataConfig)
    risk: RiskConfig = field(default_factory=RiskConfig)
    execution: ExecutionConfig = field(default_factory=ExecutionConfig)
