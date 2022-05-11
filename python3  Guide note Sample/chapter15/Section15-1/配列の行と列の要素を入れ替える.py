# 配列の行と列の要素を入れ替える
import numpy as np


a = np.array([[0, 1], [2, 3], [4, 5]])
print(a)

print(np.transpose(a))    # trancepose()で転置する

print(a.T)
# np.trancepose(a)もprint(a.T)も結果は同じ
