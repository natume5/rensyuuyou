# 配列の構造を調べる
import numpy as np


a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)
print(a.shape)    # 何行何列か出る  (3, 2)なら3行2列
print(a.ndim)    # 何次元配列か出る  2なら2次元配列
