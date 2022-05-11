# 乱数の配列を散布図で表示する
import matplotlib.pyplot as plt
import numpy as np


X = np.random.rand(100)    # 乱数のはいい列を作る
Y = np.random.rand(100)    # 乱数のはいい列を作る
plt.scatter(X, Y)    # グラフを描く
plt.show()    # 表示する
