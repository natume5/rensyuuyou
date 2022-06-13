#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　matplotlib入門---")


"""
matplotlibとは？

matplotlibとはPythonのプロットライブラリの一つで、わずか数行のコードで、
ヒストグラム、パワースペクトル、棒グラフ、 errorcharts 、散布図などを生成することができます。

インストールについて、anacondaに予め入っているためそちらを使うことをおすすめします。
pyenvを利用している場合以下のコマンドでインストールできます。

pyenv install anaconda3-5.3.1

anacondaについては以下も参照してください。


matplotlibの2つの書き方

まず、matplotlibを学習する前に注意すべき点があります。それは書き方が2種類あるという点です。
もともとmatplotlibはMathWorks社が開発している数値解析ソフトウェア有償ソフト、
MATLAB（マトラボ）のグラフィックコマンドをエミュレートしていました。
ですが、時代が下るに従いPythonのオブジェクト指向のインターフェースが拡充されるようになりました。

というわけでmatplotlibには伝統的なMATLAB形式の書き方と、
オブジェクト指向形式のインターフェースを利用した書き方（以降、当サイトではOO形式と記述します）の2つがあります。

MATLAB形式の書き方は記述量が少なくて済むのですが、カスタマイズで難儀することが多いと言われており、
この記事を書いている2020年ではOO形式の書き方が推奨されています。

https://matplotlib.org/tutorials/introductory/lifecycle.html

今後のサンプルはOO形式で解説をすすめますが、サンプルで簡単に両者の違いを解説します。
すでにmatplotlibを使っているけど2つの書き方を混同している方は是非読んでみてください。
一方で構造的な部分に興味がない方は次のページへ読み飛ばしても問題ありません。

MATLAB形式の書き方

まず、MATLAB形式のサンプルです。散布図で3点プロットしてみます。
"""

from matplotlib import pyplot


# プロットする点
X = [1, 2, 3]
Y = [1, 1, 1]

# 関数を呼び出してプロット
pyplot.scatter(X, Y, c='b', label='test_data')

# 関数を呼び出して凡例設定
pyplot.legend(['test1'])

# 関数を呼び出してタイトルを設定
pyplot.title('sample3')

# 表示
pyplot.show()

"""
pyplotというモジュールの関数を順に呼び出して処理を行います。
比較的とっつきやすく感じるかもしれません。
一方でscatter、legend、titleはそれぞれ関数なのですが、
何に対して処理を行っているのかというのがわかりづらいという点があります。
実際、細かいカスタマイズをするととたんに面倒になる、というかできないことが多々あります。


OO形式

次にOO形式のサンプルを示します。
"""

import matplotlib.pyplot as plt


# プロットする点
X = [1, 2, 3]
Y = [1, 1, 1]

# figureオブジェクトを生成する
fig = plt.figure()

# axesオブジェクトをfigureオブジェクトに設定する
ax = fig.add_subplot(1, 1, 1)

# axesオブジェクトに対して散布図を設定する
ax.scatter(X, Y, color='b', label='test_data')

# axesオブジェクトに対して凡例設定
ax.legend(['test1'])

# axesオブジェクトに対してタイトルを設定
ax.set_title('sample4')

# 表示する
plt.show()

"""
出力は先程と同じなので省略します。figure、axというオブジェクトの属性に対して操作を行います。
MATLAB形式と比較して記述量は増えますが、グラフを構成するモノ（=オブジェクト）に対して
情報を付加していくだけなのでカスタマイズしやすさや考え方としてはこちらの方が優れていると思います。

次回、上のサンプルのfigure、axesについて詳しく解説します。
"""


print("--- Python入門　matplotlibの基本 figureとaxes---")


"""
前回matplotlibとはどういったものなのか？について解説しました。
さっそく使ってみましょう、といきたいところなのですが基本的な概念を抑えたほうが理解が進むかと思いますので、
先にmatplotlibの基礎となるオブジェクト、figureとaxesについて解説したいと思います。


グラフ描画の基本フロー

matplotlibでグラフ等の可視化をする際、以下2つの構成要素を意識する必要があります。

    figure
    axes

この2つがmatplotlibを使用する際の土台となります。


figureとは

まずは起点となるオブジェクト、figureから解説します。
公式の解説では「The top level container for all the plot elements.
（すべてのプロット要素の最上位コンテナ）」と書かれていますが、
最初のうちはfigureとはウィンドウのことだと考えて差し支えないかと思います。
また、グラフを画像として保存する場合はfigure単位となります。
大抵の場合はfigureは1つで事足りると思います。

axesとは

次に、グラフをカスタマイズする上で最も重要なオブジェク、axesについてです。
axesとは一般的に軸を指しますが、matplotlibでは1つのグラフのことだと思ってください。
figureの中に複数のaxesを設定することができます。axと略すことがあります。
先程のfigureに対してaxesを設置することになります。

利用の基本フロー

ここでグラフ描画時の基本的なフローについて解説します。
おそらく人によって使い方や考え方は様々だとは思いますが、
初学者の方は以下のフローで記述すると理解しやすいかと思います。

    figureを生成する
    生成したfigureにaxesを生成、配置する
    axesに描画データやグラフの情報を設定する
    表示したり画像として保存したりする

figureとaxes

それではここからは実際に手を動かしてmatplotlibでグラフの土台を描画してfigureとaxesを理解しましょう。

1つのグラフを表示する

まず1つのfigureに1つのaxesを表示してみましょう。
"""

# import matplotlib.pyplot as plt

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
次回説明しますがグラフのタイトルや凡例といったカスタマイズ要素についてはaxesに対して設定をすることが可能です。

また、実は1つのfigureには複数のaxesを並べることが可能です。
さきほど記述したfig.add_subplot(1, 1, 1)の引数ですが、
これは1x1の分割領域の1番目にaxesを配置してね、という意味となります。
多くのグラフを並べて分析することが簡単に可能になります。

複数つのグラフを表示する add_subplot

次に1つのfigureに複数のaxis、つまりグラフを表示しましょう。
figureをN行 x M列に分割してn番目にaxesを配置する場合、以下のように記述します。
（グラフの中身は今回省略します。）

add_subplot
ax_n = fig.add_subplot(N, M, n)

1つのfigureに複数のaxesを配置した場合のサンプルです。
"""

# import matplotlib.pyplot as plt

# 1.figureを生成する
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
ax4 = fig.add_subplot(2, 3, 4)
ax4.set_title('4')    # グラフタイトル

# 2x3の5番目
ax5 = fig.add_subplot(2, 3, 5)
ax5.set_title('5')    # グラフタイトル

# 2x3の6番目
ax6 = fig.add_subplot(2, 3, 6)
ax6.set_title('6')    # グラフタイトル

# 表示する
plt.show()

"""
実行すると以下のグラフが描画されます。2行x3列のグラフが描画されます。
分析業務では複数のグラフを並べて観察することが多いので非常に便利な機能です。

複数のfigureを表示する

次は複数のfigureを表示してみましょう。
"""

# import matplotlib.pyplot as plt

# 1.figureを生成する
fig = plt.figure()

# 2.生成したfigureにaxesを生成、配置する
ax1 = fig.add_subplot(1, 1, 1)

# 3.axesに描画データを設定する
X = [0, 1, 2]
Y = [0, 1, 2]
ax1.plot(X, Y)

# 1.figure2を生成する
fig2 = plt.figure()

# 2.生成したfigure2にaxesを生成、配置する
ax2 = fig2.add_subplot(1, 1, 1)

# 3.axesに描画データを設定する
X = [0, 1, 2]
Y = [2, 1, 0]
ax2.plot(X, Y)


# 4.表示する
plt.show()

"""
以下のように2つのウィンドウが表示されるはずです。（実務上は使う機会が少ないかと思います）


補足 add_subplotとadd_axes

上の説明ではfigureにaxesを追加する際にadd_subplotを使用しましたが、
もう１つ方法が提供されています。それがadd_axesです。
add_axesは引数に矩形を表すリスト[x0, y0, width, height]を指定します。
それぞれ軸の左下座標(x0, y0)と幅と高さを表します。
また、幅と高さはそれぞれ1を全体とした比率で表します。
例えば、左下1/4にグラフを描画したい場合、以下のようにaxesを設定します。少しむずかしいですね。

ax = fig.add_axes([0, 0, 0.5, 0.5])

add_subplotではできない分割で表したい場合にはadd_axesを使用することになります。
この講座では管理人の好みで以降はadd_subplotを主に使用します。

  
いかがだったでしょうか？いくつかの例でfigureとaxesがどういったものなのか理解できたかと思います。
次回はaxesについてもう少し詳しく解説します。
"""


print("--- Python入門　axesのカスタマイズ グラフの汎用要素---")


"""
グラフの汎用要素

グラフやチャートには散布図、棒グラフ、円グラフe.t.c.等、様々な種類があります。
これらのグラフは目的に応じて異なる形状をしていますが、一方で種類によらず共通する要素も多々あります。
例えば以下のようなものが挙げられます。

    グラフのタイトル
    グリッド
    X軸、Y軸の範囲
    X軸、Y軸のラベル
    凡例

こういった要素についてはmatplotlibではaxesオブジェクトに対して設定を行います。

以下、axesに対するカスタマイズ方法について列挙します。
記事下部にサンプルを掲載していますが人によってはそちらを先に読んだほうがわかりやすいかもしれません。

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

legendでグラフの凡例を設定することができます。引数に系列ごとのリストを設定します。

凡例
ax.legend(説明リスト)


axのカスタマイズ例

それではサンプルです。上で説明したaxesに設定する汎用要素を利用する場合のコード例です。
例として線グラフを使用していますが、細かい説明は別頁にて行う予定です。
"""

# import matplotlib.pyplot as plt

# 1.figureを生成する
fig1 = plt.figure(1)

# グラフ描画設定
ax = fig1.add_subplot(111)
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


print("--- Python入門　matplotlib入門 散布図の作成---")


"""
簡単な散布図

散布図とは２次元のデータ配列の散らばり具合を可視化した図です。
Pythonで散布図を描画する場合、matplotlibのaxes.scatterを使用します。
（MATLAB形式のpyplot.scatterを使用する方法もありますが、
OO形式の記述が推奨されているためそちらの説明は割愛します。参考:2つの書き方）

まずは適当に３点をプロットしてみましょう。pyplotはx、yそれぞれの座標のリストや
numpyの配列等のシーケンスを指定します。例えば、(1, 2)、(2, 4)、(3, 6)の３点をプロットしたい場合、
X = [1, 2, 3]、Y = [2, 4, 6]と２つリストを指定することになります。
"""

# import matplotlib.pyplot as plt

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
axes.scatterの使い方

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

パラメータ 	             説明
x, y 	             x軸、y軸ごとのデータ配列
s 	                 マーカーサイズ
c 	                 色
marker 	             マーカーの形
alpha 	             マーカーの透明度（0〜1を指定、0：完全透明、1：不透明）
linewidths 	         マーカーのエッジ線の太さ
edgecolors 	         マーカーのエッジ線の色

上記以外にカラーマップ、カラーバーを表すことができるパラメータも存在します。以下を参照してください。
matplotlib カラーバー付き散布図


プロットマーカーの大きさ、色、透明度を変更

ここからはマーカーの大きさ等の散布図のカスタマイズについて解説します。
sでマーカーの大きさ、alphaで透明度、cもしくはcolorでマーカー内の色、
edgecolorsでマーカーのエッジの色を指定することができます。
今度は要素数をnp.random.randで生成してみます。
"""

# import matplotlib.pyplot as plt
import numpy as np


# ランダムな点を生成する
x = np.random.rand(50)
y = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# プロットマーカーの大きさ、色、透明度を変更
ax.scatter(x, y, s=300, alpha=0.5, linewidths=2, c='#aaaaFF', edgecolors='b')
plt.show()

"""
見せ方のテクニックなのですが、サンプルのようにエッジの色と中の色は同系統にし、
エッジの方を濃い目の色にすると綺麗に見えます。


複数の系列を色分けしてプロットする

scatterを系列ごとに呼び出すだけで複数の系列を色分けしてプロットすることができます。
青、赤2色で2系列を分けてみましょう。
"""

# import matplotlib.pyplot as plt
# import numpy as np


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
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c='#aaaaFF', edgecolors='b')

# x1, y1を赤色でプロット
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c='#FFaaaa', edgecolors='r')

plt.show()


"""
マーカーの形を指定

markerを指定すると、マーカーの形を変えることができます。よく見かけるものを挙げます。

    o:円
    D:菱型
    s:四角
    p:五角形
    h:六角形
    *:星形

$記号で挟むと任意の文字列のマーカーも利用できます。

サンプルコード
"""

# import matplotlib.pyplot as plt
# import numpy as np


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
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c='#FFFF00', 
	edgecolors='#F0B325', marker='*', label='*')

# 菱形
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c='#aaaaFF', edgecolors='b',
	marker='D', label='D')

# 文字
ax.scatter(x3, y3, s=300, alpha=0.5, linewidths=2, c='#DDDDDD', edgecolors='k',
	marker='$--->$', label='D')

plt.show()


"""
凡例、タイトル等

基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりですが、
よくサイト内を検索されるため凡例、ラベルなどの各種グラフ要素を挿入したサンプルを掲載します。
詳しくはリンク先を参照してください。
"""

# import matplotlib.pyplot as plt
# import numpy as np


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
ax.scatter(x1, y1, s=300, alpha=0.5, linewidths=2, c='#aaaaFF', 
	edgecolors='b')

# x2, y2を赤色でプロット
ax.scatter(x2, y2, s=300, alpha=0.5, linewidths=2, c='#FFaaaa', 
	edgecolors='r')

# 汎用要素を表示
ax.grid(True)    # grid表示ON
ax.set_xlim(left=-2, right=2)    # x範囲
ax.set_ylim(bottom=-2, top=2)    # y範囲
ax.set_xlabel('X')    # x軸ラベル
ax.set_ylabel('Y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
ax.legend(['x1, y1', 'x2, y2'])    # 凡例を表示

plt.show()

"""
範囲指定やグリッド、軸ラベル、凡例の表示がされていることが確認できます。


蛇足 かわいいグラフを描いてみる

マーカーに$\heartsuit$とかを指定すると、
ハート記号とかを表示することができますので以下のようなかわいい散布図を作成することも可能です。
サンプルコード
"""

# import matplotlib.pyplot as plt
# import numpy as np


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
ax.axhspan(0, 0.05, color='#D0D0FF', alpha=0.5)

# x1, y1を青色でプロット
ax.scatter(x1, y1, s=600, alpha=0.5, linewidths=2, c='#FFFF00', 
	edgecolors='#F0B325', marker='*')

# x2, y2を赤色でプロット
ax.scatter(x2, y2, s=1000, alpha=0.5, linewidths=1, c='#FFAAAA', 
	edgecolors='#FFAAAA', marker='$\heartsuit$')

plt.show()

"""
真面目なプレゼンで使用すると顰蹙を買うこと請け合いです。
"""
