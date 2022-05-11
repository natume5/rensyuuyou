# 各行の値が同じ配列を作る
import numpy as np


data = np.array([1, 2, 3])
print(data.repeat(3).reshape(3, 3))
