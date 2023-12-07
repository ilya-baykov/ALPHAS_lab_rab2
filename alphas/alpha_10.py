from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_10(_high: pd.DataFrame(), _open: pd.DataFrame(), _low: pd.DataFrame(), _volume: pd.DataFrame(),
             _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = (
        (((_high ** 3 + _low ** 3) / (_open ** 3 * _low ** 2) / _volume) ** 2)
        .ewm(5, axis=1)
        .mean()
        .shift(6, axis=1)
        .dropna(axis=1)
        .apply(lambda x: CutOutliers(x, 6))
        .apply(neutralization)
        .apply(normalization)
    )
    profits = profit(alpha, _returns)

    all_alphas.append([alpha, profits])
    print("После добавления альфы_10:")
    print(table_result(all_alphas))
