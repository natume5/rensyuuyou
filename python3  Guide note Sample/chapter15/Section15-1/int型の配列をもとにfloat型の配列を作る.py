# int型の配列をもとにfloat型の配列を作る
import numpy as np


a_int = np.array([0, 1, 2, 3, 4, 5])
a_float = np.array(a_int, dtype=float)    # 要素の型を変換する
print(a_float)
