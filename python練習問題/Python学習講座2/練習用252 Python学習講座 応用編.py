#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- axesのカスタマイズ グラフの汎用要素 ---")


print("--- グラフの汎用要素 ---")


"""
グラフやチャートには散布図、棒グラフ、円グラフe.t.c.等、様々な種類があります。
これらのグラフは目的に応じて異なる形状をしていますが、
一方で種類によらず共通する要素も多々あります。
例えば以下のようなものが挙げられます。

    グラフのタイトル
    グリッド
    X軸、Y軸の範囲
    X軸、Y軸のラベル
    凡例

こういった要素についてはmatplotlibではaxesオブジェクトに対して設定を行います。
以下、axesに対するカスタマイズ方法について列挙します。
記事下部にサンプルを掲載していますが
人によってはそちらを先に読んだほうがわかりやすいかもしれません。


グラフのタイトル

グラフタイトルを設定する場合、set_titleで指定します。
グラフタイトル
ax.set_title('グラフタイトル')


グリッド

gridにTrueを設定するとグリッドが表示されます。
グリッドの設定
ax.grid(True)


X軸、Y軸の範囲

set_xlim、set_ylimでそれぞれx軸、y軸の範囲を指定することができます。

X軸の範囲
ax.set_xlim(left=-2, right=2)
Y軸の範囲
ax.set_ylim(bottom=-2, top=2)


X軸、Y軸のラベル

set_xlabel、set_ylabelでそれぞれx軸、y軸のラベルを設定することができます。

X軸のラベル
ax.set_xlabel('x')
Y軸のラベル
ax.set_ylabel('f(x)')


凡例

legendでグラフの凡例を設定することができます。
引数に系列ごとのリストを設定します。

凡例
ax.legend(説明リスト)
"""


print("--- axのカスタマイズ例 ---")


"""
それではサンプルです。
上で説明したaxesに設定する汎用要素を利用する場合のコード例です。
例として線グラフを使用していますが、細かい説明は別頁にて行う予定です。
"""

import matplotlib.pyplot as plt

# figureを生成
fig1 = plt.figure(1)

# グラフ描画設定
ax = fig1.add_subplot(1, 1, 1)
x1 = [-2, 0, 2]
y1 = [-2, 0, 2]
ax.plot(x1, y1)

x2 = [-2, 0, 2]
y2 = [-4, 0, 4]
ax.plot(x2, y2)

ax.grid(True)    # grid表示ON
ax.set_xlim(left=-2, right=2)    # x範囲
ax.set_ylim(bottom=-2, top=2)    # y範囲
ax.set_xlabel('x')    # x軸ラベル
ax.set_ylabel('y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
ax.legend(['f(x)=x', 'g(x)=2x'])    # 凡例を表示
plt.show()

"""
タイトルや凡例といった汎用要素が設定されたことが確認できます。
"""
