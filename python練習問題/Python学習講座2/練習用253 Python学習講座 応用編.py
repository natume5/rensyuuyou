#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib入門 散布図の作成 ---")


print("--- 簡単な散布図 ---")


"""
散布図とは２次元のデータ配列の散らばり具合を可視化した図です。
Pythonで散布図を描画する場合、matplotlibのaxes.scatterを使用します。
（MATLAB形式のpyplot.scatterを使用する方法もありますが、
OO形式の記述が推奨されているためそちらの説明は割愛します。参考:2つの書き方）

まずは適当に３点をプロットしてみましょう。
pyplotはx、yそれぞれの座標のリストやnumpyの配列等のシーケンスを指定します。
例えば、(1, 2)、(2, 4)、(3, 6)の３点をプロットしたい場合、
X = [1, 2, 3]、Y = [2, 4, 6]と２つリストを指定することになります。
"""

import matplotlib.pyplot as plt

# 対象データ
x = [1, 2, 3]
y = [2, 4, 6]

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesに散布図を設定する
ax.scatter(x, y, c='b')

# 表示する
plt.show()

"""
簡単に散布図を作成することができました。
"""


print("--- axes.scatterの使い方 ---")


"""
次にaxes.scatterについて詳しいパラメータを紹介します。よく使われるパラメータは以下の通りとなります。
axes.scatter
Axes.scatter(self, x, y,
s=None,
c=None,
marker=None,
cmap=None,
norm=None,
vmin=None,
vmax=None,
alpha=None,
linewidths=None,
verts=None,
edgecolors=None,
plotnonfinite=False,
data=None)

パラメータ                  	説明
x, y 	                    x軸、y軸ごとのデータ配列
s 	                        マーカーサイズ
c 	                        色
marker 	                    マーカーの形
alpha 	                    マーカーの透明度（0〜1を指定、0：完全透明、1：不透明）
linewidths 	                マーカーのエッジ線の太さ
edgecolors 	                マーカーのエッジ線の色

上記以外にカラーマップ、カラーバーを表すことができるパラメータも存在します。
以下を参照してください。
matplotlib カラーバー付き散布図
"""


print("--- プロットマーカーの大きさ、色、透明度を変更 ---")


"""
ここからはマーカーの大きさ等の散布図のカスタマイズについて解説します。
sでマーカーの大きさ、alphaで透明度、
cもしくはcolorでマーカー内の色、
edgecolorsでマーカーのエッジの色を指定することができます。
今度は要素数をnp.random.randで生成してみます。
"""

import matplotlib.pyplot as plt
import numpy as np

# ランダムな点を生成する
x = np.random.rand(50)
y = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# プロットマーカーの大きさ、色、透明度を変更
ax.scatter(x, y, s=300, alpha=0.5, linewidths=2, c = '#aaaaFF', edgecolors='b')
plt.show()

"""
見せ方のテクニックなのですが、サンプルのようにエッジの色と中の色は同系統にし、
エッジの方を濃い目の色にすると綺麗に見えます。
"""


print("--- 複数の系列を色分けしてプロットする ---")


"""
scatterを系列ごとに呼び出すだけで複数の系列を色分けしてプロットすることができます。
青、赤2色で2系列を分けてみましょう。
"""

import matplotlib.pyplot as plt
import numpy as np

# ランダムな点を生成する
x1 = np.random.rand(30)
y1 = np.random.rand(30)
x2 = np.random.rand(30)
y2 = np.random.rand(30)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# x1, y1を青色でプロット
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c = '#aaaaFF', edgecolors='b')

# x2, y2を赤色でプロット
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c = '#FFaaaa', edgecolors='r')

plt.show()


print("--- マーカーの形を指定 ---")


"""
markerを指定すると、マーカーの形を変えることができます。
よく見かけるものを挙げます。

    o:円
    D:菱型
    s:四角
    p:五角形
    h:六角形
    *:星形

$記号で挟むと任意の文字列のマーカーも利用できます。

サンプルコード
"""

import matplotlib.pyplot as plt
import numpy as np

# ランダムな点を生成する
x1 = np.random.rand(20)
y1 = np.random.rand(20)
x2 = np.random.rand(20)
y2 = np.random.rand(20)
x3 = np.random.rand(20)
y3 = np.random.rand(20)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# スター
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c = '#FFFF00', edgecolors='#F0B325', marker='*', label='*')

# 菱形
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c = '#aaaaFF', edgecolors='b', marker='D', label='D')

# 文字
ax.scatter(x3, y3, s=300, alpha=0.5, linewidths=2, c = '#DDDDDD', edgecolors='k', marker='$--->$', label='D')

plt.show()


print("--- 凡例、タイトル等 ---")


"""
基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりですが、
よくサイト内を検索されるため凡例、
ラベルなどの各種グラフ要素を挿入したサンプルを掲載します。
詳しくはリンク先を参照してください。
"""

import matplotlib.pyplot as plt
import numpy as np

# ランダムな点を生成する
x1 = np.random.rand(30)
y1 = np.random.rand(30)
x2 = np.random.rand(30)
y2 = np.random.rand(30)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# x1, y1を青色でプロット
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c = '#aaaaFF', edgecolors='b')

# x2, y2を赤色でプロット
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c = '#FFaaaa', edgecolors='r')

# 凡例要素を表示
ax.grid(True)    # grid表示ON
ax.set_xlim(left=-2, right=2)    # x範囲
ax.set_ylim(bottom=-2, top=2)    # y範囲
ax.set_xlabel('x')    # x軸ラベル
ax.set_ylabel('y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
ax.legend(['x1, y1', 'x2, y2'])    # 凡例を表示

plt.show()

"""
範囲指定やグリッド、軸ラベル、凡例の表示がされていることが確認できます。
"""


print("--- 蛇足 かわいいグラフを描いてみる ---")


"""
マーカーに$\heartsuit$とかを指定すると、
ハート記号とかを表示することができますので
以下のようなかわいい散布図を作成することも可能です。
サンプルコード
"""

import matplotlib.pyplot as plt
import numpy as np

# ランダムな点を生成する
x1 = np.random.rand(10)
y1 = np.random.rand(10)
x2 = np.random.rand(10)
y2 = np.random.rand(10)

# figureを生成する
fig = plt.figure(facecolor='#FFE0E0')

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1, facecolor='#FFFAFF')
ax.axvspan(0, 0.05, color='#A0A0FF', alpha=0.5)
ax.axvspan(0, 0.05, color='#D0D0FF', alpha=0.5)

ax.scatter(x1, y1, s=600, alpha=0.5, linewidths=2, c = '#FFFF00', edgecolors='#F0B325', marker='*')

ax.scatter(x2, y2, s=1000, alpha=0.5, linewidths=1, c = '#FFAAAA', edgecolors='#FFAAAA', marker='$\heartsuit$')

plt.show()

"""
真面目なプレゼンで使用すると顰蹙を買うこと請け合いです。
"""
