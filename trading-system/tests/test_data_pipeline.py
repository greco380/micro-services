from datetime import datetime

from trading_system.common.models import Candle
from trading_system.data.pipeline import DataNormalizer, DataValidator, FeatureEngineer, SQLiteCandleStore


def test_validate_normalize_and_features(tmp_path):
    candles = [
        Candle("AAPL", datetime(2024, 1, 2), 10, 12, 9, 11, 100),
        Candle("AAPL", datetime(2024, 1, 1), 10, 12, 9, 11, 100),
        Candle("AAPL", datetime(2024, 1, 3), 15, 14, 9, 11, 100),
    ]
    valid = DataValidator().validate(candles)
    assert len(valid) == 2

    normalized = DataNormalizer().normalize(valid)
    assert normalized[0].timestamp < normalized[1].timestamp

    feats = FeatureEngineer().add_sma(normalized, window=2)
    assert len(feats) == 2
    assert "sma" in feats[0]

    store = SQLiteCandleStore(tmp_path / "candles.db")
    store.write(normalized)
    loaded = store.load("AAPL")
    assert len(loaded) == 2
