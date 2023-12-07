from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_8(_close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = (_close - _close.ewm(35, axis=1).mean()) / _close
    alpha = (
        (alpha - alpha.mean())
        .shift(35, axis=1)
        .apply(lambda x: CutMiddle(x, 2022))
        .apply(lambda x: CutOutliers(x, 93))
        .apply(lambda x: truncate(x, 0.008))
        .apply(neutralization)
        .apply(normalization)
    )
    profits = profit(alpha, _returns)

    all_alphas.append([alpha, profits])
    print("После добавления альфы_8:")
    print(table_result(all_alphas))
