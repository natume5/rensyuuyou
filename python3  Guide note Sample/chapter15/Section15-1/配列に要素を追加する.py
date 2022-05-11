# 配列に要素を追加する
import numpy as np


a = np.array([0, 1, 2])
b = np.append(a, 3)    # 3を追加
print(a)    # 元の配列aは変化しない
print(b)    # 新しい配列bが作られる
