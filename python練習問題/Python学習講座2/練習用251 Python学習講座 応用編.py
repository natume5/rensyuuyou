#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlibの基本 figureとaxes ---")


"""
前回matplotlibとはどういったものなのか？について解説しました。
さっそく使ってみましょう、といきたいところなのですが
基本的な概念を抑えたほうが理解が進むかと思いますので、
先にmatplotlibの基礎となるオブジェクト、
figureとaxesについて解説したいと思います
"""


print("--- グラフ描画の基本フロー ---")


"""
matplotlibでグラフ等の可視化をする際、
以下2つの構成要素を意識する必要があります。

    figure
    axes

この2つがmatplotlibを使用する際の土台となります。


figureとは

まずは起点となるオブジェクト、figureから解説します。
公式の解説では
「The top level container for all the plot elements.
（すべてのプロット要素の最上位コンテナ）」と書かれていますが、
最初のうちはfigureとはウィンドウのことだと考えて差し支えないかと思います。
また、グラフを画像として保存する場合はfigure単位となります。
大抵の場合はfigureは1つで事足りると思います。


axesとは

次に、グラフをカスタマイズする上で最も重要なオブジェクト、axesについてです。
axesとは一般的に軸を指しますが、matplotlibでは1つのグラフのことだと思ってください。
figureの中に複数のaxesを設定することができます。
axと略すことがあります。先程のfigureに対してaxesを設置することになります。


利用の基本フロー

ここでグラフ描画時の基本的なフローについて解説します。
おそらく人によって使い方や考え方は様々だとは思いますが、
初学者の方は以下のフローで記述すると理解しやすいかと思います。

    figureを生成する
    生成したfigureにaxesを生成、配置する
    axesに描画データやグラフの情報を設定する
    表示したり画像として保存したりする
"""


print("--- figureとaxes ---")


"""
それではここからは実際に手を動かして
matplotlibでグラフの土台を描画してfigureとaxesを理解しましょう。


1つのグラフを表示する

まず1つのfigureに1つのaxesを表示してみましょう。
"""

import matplotlib.pyplot as plt

# 1.figureを生成する
fig = plt.figure()

# 2.生成したfigureにaxesを生成、配置する
ax1 = fig.add_subplot(1, 1, 1)

# 3.axesに描画データを設定する
X = [0, 1, 2]
Y = [0, 1, 2]
ax1.plot(X, Y)

# 4.表示する
plt.show()

"""
1つのfigureつまりウィンドウに1つのaxes、つまりグラフが描画されました。
次回説明しますがグラフのタイトルや凡例といったカスタマイズ要素については
axesに対して設定をすることが可能です。
また、実は1つのfigureには複数のaxesを並べることが可能です。
さきほど記述したfig.add_subplot(1, 1, 1)の引数ですが、
これは1x1の分割領域の1番目にaxesを配置してね、という意味となります。
多くのグラフを並べて分析することが簡単に可能になります。


複数つのグラフを表示する add_subplot

次に1つのfigureに複数のaxis、つまりグラフを表示しましょう。
figureをN行 x M列に分割してn番目にaxesを配置する場合、
以下のように記述します。（グラフの中身は今回省略します。）

add_subplot
ax_n = fig.add_subplot(N, M, n)

1つのfigureに複数のaxesを配置した場合のサンプルです。
"""

import matplotlib.pyplot as plt

# figureを生成する
fig = plt.figure()

# 2x3の1番目
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title('1')    # グラフタイトル

# 2x3の2番目
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_title('2')    # グラフタイトル

# 2x3の3番目
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_title('3')    # グラフタイトル

# 2x3の4番目
ax3 = fig.add_subplot(2, 3, 4)
ax3.set_title('4')    # グラフタイトル

# 2x3の5番目
ax3 = fig.add_subplot(2, 3, 5)
ax3.set_title('5')    # グラフタイトル

# 2x3の6番目
ax3 = fig.add_subplot(2, 3, 6)
ax3.set_title('6')    # グラフタイトル

# 表示する
plt.show()

"""
実行すると2行x3列のグラフが描画されます。

分析業務では複数のグラフを並べて観察することが多いので非常に便利な機能です。


複数つのfigureを表示する

次は複数のfigureを表示してみましょう。
"""

import matplotlib.pyplot as plt

# 1.figureを生成する
fig1 = plt.figure()

# 2.生成したfigureにaxesを生成、配置する
ax1 = fig1.add_subplot(1, 1, 1)

# 3.axesに描画データを設定する
X = [0, 1, 2]
Y = [0, 1, 2]
ax1.plot(X, Y)


# 1.figureを生成する
fig2 = plt.figure()

# 2.生成したfigure2にaxesを生成、配置する
ax2 = fig2.add_subplot(1, 1, 1)

# 3.axesに描画データを設定する
X = [0, 1, 2]
Y = [2, 1, 2]
ax2.plot(X, Y)

# 4.表示する
plt.show()

"""
以下のように2つのウィンドウが表示されるはずです。
（実務上は使う機会が少ないかと思います）
"""


print("--- 補足 add_subplotとadd_axes ---")


"""
上の説明ではfigureにaxesを追加する際にadd_subplotを使用しましたが、
もう１つ方法が提供されています。それがadd_axesです。
add_axesは引数に矩形を表すリスト[x0, y0, width, height]を指定します。
それぞれ軸の左下座標(x0, y0)と幅と高さを表します。
また、幅と高さはそれぞれ1を全体とした比率で表します。
例えば、左下1/4にグラフを描画したい場合、以下のようにaxesを設定します。
少しむずかしいですね。

ax = fig.add_axes([0, 0, 0.5, 0.5])

add_subplotではできない分割で表したい場合には
add_axesを使用することになります。
この講座では管理人の好みで以降はadd_subplotを主に使用します。


いかがだったでしょうか？
いくつかの例でfigureとaxesがどういったものなのか理解できたかと思います。
次回はaxesについてもう少し詳しく解説します。
"""
