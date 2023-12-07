from alphas.alpha_1 import alpha_1
from alphas.alpha_2 import alpha_2
from alphas.alpha_3 import alpha_3
from alphas.alpha_4 import alpha_4
from alphas.alpha_5 import alpha_5
from alphas.alpha_6 import alpha_6
from alphas.alpha_7 import alpha_7
from alphas.alpha_8 import alpha_8
from alphas.alpha_9 import alpha_9
from alphas.alpha_10 import alpha_10
from search_alphs import *
from total import total_result

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
alpha_5(open, close, returns)
print()
alpha_6(close, returns)
print()
alpha_7(high, volume, returns)
print()
alpha_8(close, returns)
print()
alpha_9(_open=open, _high=high, _low=low, _volume=volume, _returns=returns)
print()
alpha_10(_open=open, _high=high, _low=low, _volume=volume, _returns=returns)
print()
total_result()
