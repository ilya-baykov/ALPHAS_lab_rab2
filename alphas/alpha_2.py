from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_2(_close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = alpha_one_delta(_close, 15).apply(lambda x: CutMiddle(x, 1800)).apply(neutralization).apply(normalization)
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_2:")
    print(table_result(all_alphas))
