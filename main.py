from alphas.alpha_1 import alpha_1
from alphas.alpha_2 import alpha_2
from alphas.alpha_3 import alpha_3
from alphas.alpha_4 import alpha_4
from search_alphs import *

close = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Close.csv')
open = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Open.csv')
high = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\High.csv')
low = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Low.csv')
volume = data_reader(r'C:\Users\ilyab\PycharmProjects\lab2\df\Volume.csv')
returns = returns_calculator(close)

alpha_1(close, returns)
print()
alpha_2(close, returns)
print()
alpha_3(high, close, returns)
print()
alpha_4(high, low, close, returns)
print()
