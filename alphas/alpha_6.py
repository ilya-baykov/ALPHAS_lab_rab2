from total import all_alphas
from backtest import *
from search_alphs import *
import warnings

warnings.filterwarnings('ignore')


def alpha_6(_close: pd.DataFrame(), _returns: pd.DataFrame()) -> None:
    global all_alphas
    alpha = decay(
        alpha_SMB(_close, 2, 190),
        21
    )
    profits = profit(alpha, _returns)
    all_alphas.append([alpha, profits])
    print("После добавления альфы_6:")
    print(matrix(all_alphas))
