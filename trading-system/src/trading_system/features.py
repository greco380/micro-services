from __future__ import annotations


FeatureRow = dict[str, float | int | None]


def simple_moving_average(values: list[float], window: int) -> list[float | None]:
    if window <= 0:
        raise ValueError("window must be positive")

    out: list[float | None] = []
    running_sum = 0.0
    for index, value in enumerate(values):
        running_sum += value
        if index >= window:
            running_sum -= values[index - window]
        if index + 1 < window:
            out.append(None)
        else:
            out.append(running_sum / window)
    return out


def _rolling_std(values: list[float], window: int) -> list[float | None]:
    if window <= 1:
        return [0.0 for _ in values]

    out: list[float | None] = []
    for i in range(len(values)):
        if i + 1 < window:
            out.append(None)
            continue
        chunk = values[i + 1 - window : i + 1]
        mean = sum(chunk) / window
        variance = sum((x - mean) ** 2 for x in chunk) / (window - 1)
        out.append(variance**0.5)
    return out


def build_feature_frame(closes: list[float], short_window: int, long_window: int) -> list[FeatureRow]:
    short_ma = simple_moving_average(closes, short_window)
    long_ma = simple_moving_average(closes, long_window)
    vol = _rolling_std(closes, short_window)

    rows: list[FeatureRow] = []
    for i, close in enumerate(closes):
        prev_close = closes[i - 1] if i else close
        ret = 0.0 if i == 0 else (close - prev_close) / prev_close
        rows.append(
            {
                "close": close,
                "return_1": ret,
                "short_ma": short_ma[i],
                "long_ma": long_ma[i],
                "ma_spread": None if short_ma[i] is None or long_ma[i] is None else short_ma[i] - long_ma[i],
                "volatility": vol[i],
            }
        )
    return rows
