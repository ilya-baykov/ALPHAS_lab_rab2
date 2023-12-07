from backtest import cumprofit
import matplotlib.pyplot as plt

all_alphas = []


def total_result() -> None:
    for i in all_alphas:
        cumprofit(i[1]).plot(figsize=(25, 11))
    plt.legend(
        [
            'alpha1',
            'alpha2',
            'alpha3',
            'alpha4',
            'alpha5',
            'alpha6',
            'alpha7',
            'alpha8',
            'alpha9',
            'alpha10',
        ]
    )
    plt.show()
