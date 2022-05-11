# 配列にリストの要素を挿入する
import numpy as np


a = np.array([0, 1, 2])
b = np.insert(a, 1, [88, 99])
print(b)
