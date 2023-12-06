from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_4(_high: pd.DataFrame(), _low: pd.DataFrame(), _close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = decay(
        alpha_high_low_2close_close(_high, _low, _close).apply(lambda x: CutOutliers(x, 120)).apply(
            lambda x: CutMiddle(x, 2150)),
        4
    )
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_4:")
    print(matrix(all_alphas))
