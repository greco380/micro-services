from trading_system.models import FeatureRow, Signal


class Strategy:
    def generate(self, feature: FeatureRow) -> Signal:
        raise NotImplementedError


class MovingAverageCrossStrategy(Strategy):
    def generate(self, feature: FeatureRow) -> Signal:
        if feature.sma_fast > feature.sma_slow:
            return "BUY"
        if feature.sma_fast < feature.sma_slow:
            return "SELL"
        return "HOLD"


class MLAssistedStrategy(Strategy):
    """Lightweight proxy for ML scoring over engineered features."""

    def __init__(self, threshold: float = 0.001) -> None:
        self.threshold = threshold

    def _score(self, feature: FeatureRow) -> float:
        return 0.7 * feature.momentum + 0.3 * ((feature.sma_fast - feature.sma_slow) / max(feature.close, 1e-9))

    def generate(self, feature: FeatureRow) -> Signal:
        score = self._score(feature)
        if score > self.threshold:
            return "BUY"
        if score < -self.threshold:
            return "SELL"
        return "HOLD"
