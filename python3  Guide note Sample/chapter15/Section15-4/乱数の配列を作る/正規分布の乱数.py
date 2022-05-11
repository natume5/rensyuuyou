# 正規分布の乱数
import matplotlib.pyplot as plt
import numpy as np


sigma = 2.5    # 分数
mu = 50    # 平均
data = sigma * np.random.randn(2, 3) + mu    # 正規分布の乱数
print(data)
