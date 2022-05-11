# 3次元ベクトルa,bの外積となるベクトルcを求める
import numpy as np


a = np.array([1, 2, 0])
b = np.array([0, 1, -1])
c = np.cross(a, b)    # 外積
print(c)
