# math.sin()とnumpy.sin()の違い(2)
import numpy as np


data = [0.0, 0.28, 0.57, 0.85, 1.14, 1.42, 1.71, 1.99, 2.28, 2.57, 2.85, 3.14]
print(np.sin(data))    # numpyのsin()はリストの値を一度に計算できる
