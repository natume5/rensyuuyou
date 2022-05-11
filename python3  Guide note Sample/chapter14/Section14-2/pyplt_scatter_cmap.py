# 第３の値をマーカーの色で表現する
import matplotlib.pyplot as plt
import numpy as np


X, Y = np.random.rand(100), np.random.rand(100)    # ランダムな配列を作る
V = np.random.rand(100)    # 色の濃淡を決めるデータの配列
plt.scatter(X, Y, s=200, c=V, cmap="Blues", edgecolors="b")    # グラフを描く
plt.grid(True)    # グリッド
plt.show()
"""
cmapで指定するカラーマップはcolorで指定する色とは異なる。
定義済みのカラーマップには次のようなものがある。
Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBuGn,PuRd,Purples,
RdPu,Reds,YlGn,YlOrBr,YlOrRd,afmhot,autum,bone,cool,copper,gist_heat,
grey,hot,pink,spring,summer,winter
"""
