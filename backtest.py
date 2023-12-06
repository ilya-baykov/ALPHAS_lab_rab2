import numpy as np
import pandas as pd


def data_reader(name):
    return pd.read_csv(name, index_col='Unnamed: 0')


def returns_calculator(close):
    return (close / close.shift(axis=1) - 1).dropna(axis=1)


def neutralization(alpha):
    return alpha - alpha.mean()


def normalization(alpha):
    return alpha / alpha.abs().sum()


def profit(alpha, returns):
    return (alpha.shift(axis=1) * returns).dropna(axis=1).sum()


def cumprofit(profit):
    return profit.cumsum()


def turnover(alpha):
    return (alpha.shift(axis=1) - alpha).dropna(axis=1).abs().sum()


def sharpe(profit):
    return np.sqrt(len(profit)) * profit.mean() / profit.std()


def drawdorn(cumprofit):
    drawDown = 0
    maxValue = cumprofit[0]
    for i in cumprofit:
        if i > maxValue:
            maxValue = i
        else:
            if maxValue - i > drawDown:
                drawDown = maxValue - i
    return drawDown


def truncate(alpha, threshold):
    alpha[alpha > threshold] = threshold
    alpha[alpha < -threshold] = -threshold
    alpha[alpha >= 0] /= (2 * np.sum(alpha[alpha >= 0]))
    alpha[alpha < 0] /= (2 * np.sum(alpha[alpha < 0]))
    return alpha


def CutOutliers(alpha, number):
    if number % 2 == 0:
        return alpha.where(
            alpha >= alpha.sort_values()[number // 2 - 1],
            0
        ).where(
            alpha <= alpha.sort_values()[-(number // 2)],
            0
        )

    else:
        return alpha.where(
            alpha >= alpha.sort_values()[number // 2],
            0
        ).where(
            alpha <= alpha.sort_values()[-(number // 2)],
            0
        )


def CutMiddle(alpha, number):
    if number % 2 == 0:
        return alpha.mask(
            (alpha >= alpha.sort_values()[len(alpha) // 2 - number // 2]) & (
                    alpha <= alpha.sort_values()[len(alpha) // 2 + number // 2]),
            0
        )

    else:
        return alpha.mask(
            (alpha >= alpha.sort_values()[len(alpha) // 2 - number // 2 + 1]) & (
                    alpha <= alpha.sort_values()[len(alpha) // 2 + number // 2]),
            0
        )


def truncate(alpha, threshold):
    return alpha.where(
        alpha <= threshold,
        threshold
    ).where(
        alpha >= -threshold,
        -threshold
    )


def rank(vector):
    a = list(enumerate(vector))
    a.sort(key=lambda x: x[1])

    for i in range(len(a)):
        a[i] = list(a[i])

    for i in range(len(a)):
        a[i].append((i + 1) / len(a))

    a.sort(key=lambda x: x[0])
    b = [i[2] for i in a]

    return b


def decay(alpha, n):
    s = []

    for i in range(n):
        s.append(i)

    s = np.array(rank(s))

    d_alpha = pd.DataFrame(alpha[alpha.columns[n - 1:]])
    for i in range(len(alpha.columns) - n):
        d_alpha[alpha.columns[i + n - 1]] = np.sum(pd.DataFrame(alpha[alpha.columns[i: n + i]]) * s, axis=1)

    for i in range(len(d_alpha.columns)):
        d_alpha[d_alpha.columns[i]] = normalization(neutralization(d_alpha[d_alpha.columns[i]]))

    return d_alpha


def sharpe_per_year(alpha, profits):
    s = set()
    dates = []

    for i in profits.index:
        s.add(i[:4])
    s = list(s)
    s.sort()

    for i in s:
        dates.append([])

    for i in range(len(s)):
        for j in profits.index:
            if j[:4] == s[i]:
                dates[i].append(j)

    year_sharpes = []
    for i in dates:
        year_sharpes.append(sharpe(profits[i]))

    return year_sharpes


def matrix(alpha: list) -> pd.DataFrame:
    pnl = pd.DataFrame()
    pnl_sum = []
    mean_turnover = []
    good_sharp_years = []
    index = []
    for i in range(len(alpha)):
        pnl['alpha' + str(i + 1)] = alpha[i][1]
        pnl_sum.append(
            np.sum(
                alpha[i][1]
            )
        )
        mean_turnover.append(
            np.mean(
                turnover(alpha[i][0])
            )
        )
        good_sharp_years.append(
            np.sum(
                np.array(sharpe_per_year(alpha[i][0], alpha[i][1])) > 1
            )
        )
        corr_matrix = pnl.dropna().corr()
        index.append('alpha' + str(i + 1))
    return pd.concat(
        [
            pd.DataFrame(
                {
                    'pnl': pnl_sum,
                    'mean_turnover': mean_turnover,
                    'good_sharp_years': good_sharp_years
                },
                index=index
            ),
            corr_matrix
        ],
        axis=1
    )
