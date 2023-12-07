from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_1(_close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = decay(
        alpha_one_delta(_close, 3).apply(lambda x: CutMiddle(x, 100)).apply(lambda x: CutOutliers(x, 12)).apply(
            lambda x: truncate(x, 0.003)),
        2
    )
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_1:")
    print(table_result(all_alphas))
