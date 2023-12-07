from backtest import *


def alpha_one_delta(data, delta):
    return (
        (
                -data / data.shift(delta, axis=1) + 1
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_high_low_close(high, low, close):
    return (
        (
                (high - low) / close
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_high_low(high, low):
    return (
        (
                high / low
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_high_low_2close_close(high, low, close):
    return (
        (
                (high + low - 2 * close) / close
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_high_low_close2(high, low, close):
    return (
        (
                high * low / close ** 2
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_open_close(open, close):
    return (
        (
                open / close
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_high_close(high, close):
    return (
        (
                high / close
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_close_low_high(close, low, high):
    return (
        (
                -(close - low) / (high - low)
        )
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1).drop('2010-01-04', axis=1)
    )


def alpha_if_high_low_close(high, low, close):
    return (
        ((high + low) / 2 < close).replace([False, True], [1, -1])
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
    )


def alpha_if_close_low_high(close, low, high):
    return (
        (
            ((close - low) / (high - low) < 0.5).replace([False, True], [-1, 1])
        )
        .dropna(axis=1)
        .apply(neutralization)
        .apply(normalization)
        .shift(1, axis=1)
        .dropna(axis=1)
    )


def alpha_SMB(close, delta, n):
    alpha = pd.DataFrame()
    profit = pd.DataFrame()

    num = int(len(close) / n)

    for i in range(len(close.columns) - 1):
        profit[close.columns[i + 1]] = close[close.columns[i + 1]] / close[close.columns[i]] - 1
    profit.index = close.index

    # Если доходность принадлежит к верхнему квантилю, присваивается положительное значение.
    # Если доходность принадлежит к нижнему квантилю, присваивается отрицательное значение.
    # В противном случае, присваивается 0

    for i in range(len(profit.columns) - delta):
        alpha[profit.columns[i + delta]] = np.where(
            profit[profit.columns[i]] <= profit[profit.columns[i]].sort_values()[num],
            0.4 / (num + 1),
            np.where(
                profit[profit.columns[i]] >= profit[profit.columns[i]].sort_values()[len(profit[profit.columns]) - num],
                -0.4 / (num + 1),
                0
            )
        )
    alpha.index = close.index

    return alpha.apply(neutralization).apply(normalization)
