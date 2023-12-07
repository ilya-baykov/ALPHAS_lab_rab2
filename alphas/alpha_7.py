from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_7(_high: pd.DataFrame(), _volume: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = (-_high.rank(pct=True).shift(11, axis=1) / _volume.rank(pct=True)).apply(neutralization).apply(
        normalization)
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_7:")
    print(table_result(all_alphas))
