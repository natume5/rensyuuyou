#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 メッシュグリッドと可視化 ---")


"""
このページではデータを可視化する際によく使用する
メッシュグリッドと呼ばれる配列生成関数について学習します。
"""


print("--- meshgridとは ---")


"""
配列X=[1, 2, 3]、Y=[-1, 0, 1]が与えられていたとします。
これらの格子点、つまりXとYの組み合わせは
(1, 0)、(2, 0)、(3, 0)、(1, 1)、(2, 1)、(3, 1)、(1, -1)、
(2, -1)、(3, -1)の9つとなりますが、
meshgridを使用するとそれらをプログラム上で扱いやすい形で出力された
X, Yの組を得ることができます。
サンプルで具体的に確認してみましょう。
"""

import numpy as np

X = [1, 2, 3]
Y = [-1, 0, 1]
xv, yv = np.meshgrid(X, Y)

print(xv)

print(yv)

"""
[[1 2 3]
 [1 2 3]
 [1 2 3]]

[[-1 -1 -1]
 [ 0  0  0]
 [ 1  1  1]]

少しわかりづらい構造ですが、以下のように2回ループで順番に要素を取り出すと
前述の直積、9つの要素が得られることが確認できます。
"""

for xx, yy in zip(xv, yv):
	for x, y in zip(xx, yy):
		print(x, y)

"""
1 -1
2 -1
3 -1
1 0
2 0
3 0
1 1
2 1
3 1
"""


print("--- meshgridを利用した可視化 ---")


"""
とっつきづらい構造ですが、ユニバーサル関数と相性がよく、
グリッド上の関数の評価する際に非常に便利です。
（公式より「meshgrid is very useful to evaluate 
functions on a grid.」）
また、評価結果をそのままmatplotlibに指定して出力することが可能です。
サンプルです。教養課程の微積の鞍点の説明でよく使用される関数
\( z = x^2 - y^2 \)について、
定義域\( [-1, 1] \times [-1, 1] \)
の様子を可視化して確認してみましょう。
ユニバーサル関数np.subtractに
そのまま値を指定することができている点に注目してください。
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d    # 警告が出ないように変更
import matplotlib as mpl    # 警告が出ないように変更


# 定義域[-1, 1]のx,yを50個区切りで生成
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)

# メッシュグリッドを生成
xv, yv = np.meshgrid(x, y)

# 関数x^2 - y^2の値をzに代入
z = np.subtract(xv ** 2, yv ** 2)

# x, y, zをワイヤフレームで表示
fig = plt.figure()    # 警告が出ないように変更
ax = mplot3d.Axes3D(fig, auto_add_to_figure=False)    # 警告が出ないように変更
fig.add_axes(ax)    # 警告が出ないように変更
ax.plot_wireframe(xv, yv, z)
plt.show()

"""
以下のようにグラフが出力され、各点におけるzの値
（＝高さ）を確認することができます。

Axes3D(fig)のMatplotlibDeprecationWarning より
mpl_toolkitsのmplot3d.Axes3Dの警告を消す方法について
書いてあったので試してみた。
修正箇所は　# 警告が出ないように変更　と追記されている個所
"""
