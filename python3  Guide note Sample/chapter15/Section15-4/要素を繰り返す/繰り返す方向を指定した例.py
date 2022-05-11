# 繰り返す方向を指定した例
import numpy as np


data = np.arange(6).reshape(2, 3)
print(data)
print(data.repeat(2, axis=0))    # 行を2回繰り返す
print(data.repeat(2, axis=1))    # 列を2回繰り返す
