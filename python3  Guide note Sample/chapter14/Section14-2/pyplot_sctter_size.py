# 第３の値をマーカーの大きさで表現する
import matplotlib.pyplot as plt
import numpy as np


X, Y = np.random.rand(100), np.random.rand(100)    # ランダムな配列を作る
V = np.random.rand(100) * 1000 + 50    # サイズを決めるデータの配列
plt.scatter(X, Y, s=V, c="b", alpha=0.3, linewidths=1, edgecolors="b")
# グラフを描く  s=V  Vの値をマーカーのサイズで表す
plt.show()
