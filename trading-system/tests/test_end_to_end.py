from pathlib import Path
import tempfile
import unittest

from trading_system.cli import run
from trading_system.config import AppConfig, DataConfig, ExecutionConfig, RiskConfig


class TradingSystemE2ETest(unittest.TestCase):
    def test_run_creates_expected_outputs(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            cwd = Path(tmp_dir)
            db_path = cwd / "test.db"
            reports = cwd / "reports"

            prev = Path.cwd()
            try:
                import os

                os.chdir(cwd)
                outputs = run(
                    AppConfig(
                        database_path=str(db_path),
                        data=DataConfig(symbol="demo", bar_count=120),
                        risk=RiskConfig(max_position_size=5, max_daily_loss=1_000),
                        execution=ExecutionConfig(starting_cash=10_000),
                    )
                )
            finally:
                os.chdir(prev)

            self.assertTrue(db_path.exists())
            self.assertTrue((reports / "ma_backtest.md").exists())
            self.assertTrue((reports / "ml_backtest.md").exists())
            self.assertTrue((reports / "portfolio_snapshot.json").exists())
            self.assertEqual(outputs["database"], str(db_path))


if __name__ == "__main__":
    unittest.main()
