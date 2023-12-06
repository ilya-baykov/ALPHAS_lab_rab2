from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_3(_high: pd.DataFrame(), _close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = decay(alpha_high_close(_high, _close).apply(lambda x: CutMiddle(x, 100)), 6).apply(neutralization).apply(
        normalization)
    profits = profit(alpha, _returns)

    all_alphas.append([alpha, profits])
    print("После добавления альфы_3:")
    print(matrix(all_alphas))
