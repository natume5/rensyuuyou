# ベクトルaの2倍の長さのベクトル
import numpy as np


p0 = np.array((1, 1))    # 点p0の座標
p1 = np.array((6, 4))    # 点p1の座標
A = p1 - p0    # ベクトルaを示す配列になる
A2 = A * 2    # ベクトルaの長さを2倍にする
print(A2)    # ベクトルaを2倍にしたベクトルA2の値
a2_norm = np.linalg.norm(A * 2)
print(a2_norm)    # ベクトルaの2倍の長さになる
