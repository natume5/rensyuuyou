# 配列に対して引き算、掛け算、割り算を行う
import numpy as np


A = np.array([10, 20, 30, 40]).reshape(2, 2)
print(A)
print(A - 5)    # 配列の全ての要素から5を引く
print(A * 2)    # 配列の全ての要素に2を掛ける
print(A / 2)    # 配列の全ての要素を2で割る
