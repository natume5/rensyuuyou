# ベクトルaの長さ
import numpy as np


p0 = np.array((1, 1))    # 点p0の座標
p1 = np.array((6, 4))    # 点p1の座標
A = p1 - p0    # ベクトルaを示す配列になる
a_norm = np.linalg.norm(A)    # ベクトルの長さを求める
print(a_norm)
