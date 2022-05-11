# ポアゾン分布の乱数
import matplotlib.pyplot as plt
import numpy as np


print(np.random.poisson(lam=10, size=(10)))
"""
lamは平均値(中央値)、sizeは作成する行列サイズか個数を指定する。
"""
