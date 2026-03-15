from trading_system.models import OHLCVBar


class DataValidator:
    @staticmethod
    def validate_bar(bar: OHLCVBar) -> bool:
        if any(v <= 0 for v in (bar.open, bar.high, bar.low, bar.close, bar.volume)):
            return False
        if bar.high < max(bar.open, bar.close):
            return False
        if bar.low > min(bar.open, bar.close):
            return False
        return True


class DataNormalizer:
    @staticmethod
    def normalize_bar(bar: OHLCVBar) -> OHLCVBar:
        return OHLCVBar(
            symbol=bar.symbol.upper(),
            timestamp=bar.timestamp,
            open=round(bar.open, 4),
            high=round(bar.high, 4),
            low=round(bar.low, 4),
            close=round(bar.close, 4),
            volume=float(round(bar.volume, 2)),
        )


class IngestionPipeline:
    def __init__(self, validator: DataValidator | None = None, normalizer: DataNormalizer | None = None) -> None:
        self.validator = validator or DataValidator()
        self.normalizer = normalizer or DataNormalizer()

    def process(self, bars: list[OHLCVBar]) -> list[OHLCVBar]:
        processed: list[OHLCVBar] = []
        for bar in bars:
            if self.validator.validate_bar(bar):
                processed.append(self.normalizer.normalize_bar(bar))
        return processed
