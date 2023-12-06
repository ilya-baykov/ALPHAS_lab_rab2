from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_5(_open: pd.DataFrame(), _close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = decay(
        alpha_open_close(_open, _close).apply(lambda x: CutOutliers(x, 120)).apply(lambda x: CutMiddle(x, 2050)),
        6
    )
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_5:")
    print(matrix(all_alphas))
