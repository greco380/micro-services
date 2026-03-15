from __future__ import annotations

from dataclasses import dataclass

from .features import FeatureRow


def ma_crossover_signal(feature_row: FeatureRow) -> int:
    short_ma = feature_row["short_ma"]
    long_ma = feature_row["long_ma"]

    if short_ma is None or long_ma is None:
        return 0
    if short_ma > long_ma:
        return 1
    if short_ma < long_ma:
        return -1
    return 0


@dataclass
class NearestCentroidDirectionModel:
    """Minimal ML-assisted direction model using feature centroids."""

    up_centroid: tuple[float, float] = (0.0, 0.0)
    down_centroid: tuple[float, float] = (0.0, 0.0)

    def fit(self, features: list[FeatureRow]) -> None:
        up: list[tuple[float, float]] = []
        down: list[tuple[float, float]] = []

        for row in features:
            spread = row["ma_spread"]
            ret = row["return_1"]
            if spread is None:
                continue
            point = (float(spread), float(ret))
            if ret >= 0:
                up.append(point)
            else:
                down.append(point)

        self.up_centroid = _mean_point(up) if up else (0.0, 0.0)
        self.down_centroid = _mean_point(down) if down else (0.0, 0.0)

    def predict_signal(self, row: FeatureRow) -> int:
        spread = row["ma_spread"]
        ret = row["return_1"]
        if spread is None:
            return 0
        point = (float(spread), float(ret))

        up_dist = _distance(point, self.up_centroid)
        down_dist = _distance(point, self.down_centroid)
        if up_dist < down_dist:
            return 1
        if down_dist < up_dist:
            return -1
        return 0


def _mean_point(points: list[tuple[float, float]]) -> tuple[float, float]:
    x = sum(p[0] for p in points) / len(points)
    y = sum(p[1] for p in points) / len(points)
    return (x, y)


def _distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def generate_signals(features: list[FeatureRow], use_ml_assist: bool = True) -> list[int]:
    base = [ma_crossover_signal(row) for row in features]
    if not use_ml_assist:
        return base

    model = NearestCentroidDirectionModel()
    model.fit(features)

    merged: list[int] = []
    for row, base_signal in zip(features, base):
        ml_signal = model.predict_signal(row)
        if base_signal == 0:
            merged.append(ml_signal)
        elif ml_signal == 0:
            merged.append(base_signal)
        else:
            merged.append(base_signal if base_signal == ml_signal else 0)
    return merged
