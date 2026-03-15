from trading_system.models import FeatureRow, OHLCVBar


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


class FeatureEngineer:
    def __init__(self, fast_window: int = 5, slow_window: int = 20) -> None:
        self.fast_window = fast_window
        self.slow_window = slow_window

    def build(self, bars: list[OHLCVBar]) -> list[FeatureRow]:
        closes = [b.close for b in bars]
        features: list[FeatureRow] = []

        for i, bar in enumerate(bars):
            fast = _mean(closes[max(0, i - self.fast_window + 1) : i + 1])
            slow = _mean(closes[max(0, i - self.slow_window + 1) : i + 1])
            prev_close = closes[i - 1] if i > 0 else closes[i]
            momentum = (bar.close - prev_close) / prev_close if prev_close else 0.0

            features.append(
                FeatureRow(
                    symbol=bar.symbol,
                    timestamp=bar.timestamp,
                    close=bar.close,
                    sma_fast=fast,
                    sma_slow=slow,
                    momentum=momentum,
                )
            )
        return features
