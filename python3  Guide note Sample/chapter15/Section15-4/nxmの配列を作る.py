# nxmの配列を作る
import numpy as np


n = 3    # n行
m = 4    # m列
print(np.arange(n*m).reshape(n, m))    # 0~11の数値から3行4列の配列を作る
