# 二項分布の乱数
import matplotlib.pyplot as plt
import numpy as np


print(np.random.binomial(n=100, p=0.1, size=(2, 3)))
# nは試行回数、pは確率、sizeを省略すると乱数が1個返る
