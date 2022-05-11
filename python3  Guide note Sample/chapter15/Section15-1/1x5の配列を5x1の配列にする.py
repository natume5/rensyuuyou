# 1x5の配列を5x1の配列にする
import numpy as np


a = np.array([0, 1, 2, 3, 4])    # 1次元配列
b = a[:, np.newaxis]
print(b)
