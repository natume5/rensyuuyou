# 配列をリストに変換する
import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array([[0, 1], [2, 3], [4, 5]])
print(a.tolist())
# 配列がリストに変換される
print(b.tolist())
# 多次元配列は多次元リストになる
