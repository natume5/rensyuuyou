# グラフを画像ファイルに保存する
import matplotlib.pyplot as plt
import math


X = range(0, 360)    # x軸の値
Y = [math.sin(math.radians(d)) for d in X]    # y軸の値
plt.plot(X, Y)    # グラフを描く
plt.savefig("sin.png")    # 画像ファイルに保存する
# 画面に表示する前に画像として保存
plt.show()    # 画面表示するならば最後で実行する
