# 同じ行列数の配列の掛け算、割り算
import numpy as np


A = np.array([1, 2, 3, 4]).reshape(2, 2)
B = np.array([10, 20, 30, 40]).reshape(2, 2)
D = A * B    # 要素同士の掛け算をする
E = A / B    # 要素同士の割り算をする
print(D)
print(E)
