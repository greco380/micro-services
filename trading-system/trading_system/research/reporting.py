from trading_system.research.backtest import BacktestResult


class BacktestReporter:
    @staticmethod
    def to_markdown(result: BacktestResult, strategy_name: str) -> str:
        return "\n".join(
            [
                f"# Backtest Report: {strategy_name}",
                "",
                f"- Trades: **{result.trades}**",
                f"- Final Equity: **{result.final_equity:.2f}**",
                f"- Return: **{result.return_pct:.2f}%**",
                f"- Max Drawdown: **{result.max_drawdown_pct:.2f}%**",
            ]
        )
