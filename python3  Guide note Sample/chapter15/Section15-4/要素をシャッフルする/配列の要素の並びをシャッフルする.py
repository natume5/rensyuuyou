# 配列の要素の並びをシャッフルする
import numpy as np


data = np.arange(9).reshape(3, 3)    # 0~8の配列を作る
np.random.shuffle(data)
print(data)    # 並びがシャッフルされる
