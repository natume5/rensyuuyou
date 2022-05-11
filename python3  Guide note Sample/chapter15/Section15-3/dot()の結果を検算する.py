# dot()の結果を検算する
import numpy as np


F = np.array([8.66, 5.0])    # ベクトルF
S = np.array([20,0])    # ベクトルS
W = np.dot(F, S)    # 仕事(内積)を求める
f = np.linalg.norm(F)    # ベクトルFの長さ
s = np.linalg.norm(S)    # ベクトルSの長さ
rad = np.radians(30)     # 30度をラジアンに換算
w = f * s * np.cos(rad)    # 仕事を計算
print(w)
