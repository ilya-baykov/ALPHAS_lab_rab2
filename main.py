from alphas.alpha_1 import alpha_1
from backtest import *
from search_alphs import *
from total import all_alphas

close = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Close.csv')
open = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Open.csv')
high = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\High.csv')
low = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Low.csv')
volume = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Volume.csv')
returns = returns_calculator(close)

alpha_1(close, returns)
