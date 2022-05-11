# 多次元配列を1次元配列にする
import numpy as np


a = np.array([[0, 1], [2, 3], [4, 5]])
print(a.ravel())    # 1次元配列になる
print(a.flatten())
