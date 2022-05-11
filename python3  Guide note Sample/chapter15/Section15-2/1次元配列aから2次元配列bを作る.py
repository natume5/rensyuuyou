# 1次元配列aから2次元配列bを作る
import numpy as np


a = np.array([10, 20, 30, 40])
b = a.reshape(2, 2)    # 配列aからbを作る
print(a)
print(b)
