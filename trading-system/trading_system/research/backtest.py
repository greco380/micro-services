from dataclasses import dataclass

from trading_system.models import FeatureRow
from trading_system.research.strategies import Strategy


@dataclass(slots=True)
class BacktestResult:
    trades: int
    final_equity: float
    return_pct: float
    max_drawdown_pct: float


class Backtester:
    def __init__(self, starting_cash: float = 100_000.0) -> None:
        self.starting_cash = starting_cash

    def run(self, features: list[FeatureRow], strategy: Strategy) -> BacktestResult:
        cash = self.starting_cash
        position = 0
        peak_equity = self.starting_cash
        max_drawdown = 0.0
        trades = 0

        for feature in features:
            signal = strategy.generate(feature)
            price = feature.close

            if signal == "BUY" and position <= 0:
                cash -= price
                position += 1
                trades += 1
            elif signal == "SELL" and position >= 1:
                cash += price
                position -= 1
                trades += 1

            equity = cash + position * price
            peak_equity = max(peak_equity, equity)
            dd = (peak_equity - equity) / peak_equity if peak_equity else 0.0
            max_drawdown = max(max_drawdown, dd)

        last_price = features[-1].close if features else 0.0
        final_equity = cash + position * last_price
        return BacktestResult(
            trades=trades,
            final_equity=final_equity,
            return_pct=((final_equity - self.starting_cash) / self.starting_cash) * 100,
            max_drawdown_pct=max_drawdown * 100,
        )
