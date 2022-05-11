# 多次元配列の要素を順に取り出す
import numpy as np


data = np.array([10, 20, 30, 40, 50, 60]).reshape(2, 3)
print(data)
for i, item in np.ndenumerate(data):
    # np.ndenumerate(data)  多次元配列から位置と要素を取り出す
    print(i, item)
    # i  iには(行、列)のタプルが入る
