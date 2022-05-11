# 仕事を内積dot()で計算する
import numpy as np


F = np.array([8.66, 5.0])    # ベクトルF
S = np.array([20,0])    # ベクトルS
W = np.dot(F, S)    # 仕事(内積)を求める
print(W)
