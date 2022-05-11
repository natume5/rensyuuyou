# 行数A、Bを比較して要素が異なる個数を数える
import numpy as np


A = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
B = np.array([1, 2, 9, 4, 8, 6]).reshape(2, 3)
n = (A != B).sum()    # 要素が異なる数を数える
# 異なっている位置にTrueが入る。Trueは1、Falseは0で合計する。
print(n)
