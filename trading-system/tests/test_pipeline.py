from trading_system.config import RiskLimits, SystemConfig
from trading_system.pipeline import run_trading_system


def test_pipeline_runs_end_to_end() -> None:
    result = run_trading_system()

    assert result["rows_loaded"] > 0
    assert len(result["features"]) == result["rows_loaded"]
    assert len(result["signals"]) == result["rows_loaded"]

    report = result["report"]
    assert "Trading System Report" in report
    assert "Filled/rejected events" in report


def test_risk_limits_can_force_rejections() -> None:
    cfg = SystemConfig(
        risk_limits=RiskLimits(
            max_position_units=1,
            max_notional_per_order=1.0,
            max_daily_loss=2_000.0,
        )
    )
    result = run_trading_system(cfg)
    assert result["execution"].rejected_orders > 0
