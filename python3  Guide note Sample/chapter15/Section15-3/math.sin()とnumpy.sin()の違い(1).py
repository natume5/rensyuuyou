# math.sin()とnumpy.sin()の違い(1)
import math
import numpy as np


data = [0.0, 0.28, 0.57, 0.85, 1.14, 1.42, 1.71, 1.99, 2.38, 2.57, 2.85, 3.14]
print(math.sin(data)    # mathのsin()はリストの値を一度に計算できない
