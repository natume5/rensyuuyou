#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　matplotlib カラーバー付き散布図---")


"""
カラーバー付きの散布図を出力する

前回の説明で、点に色を付ける方法を説明しましたが、今回は連続的な量を持つ点に色付けしたい場合です。
先に出力結果を添付します。

ソースコードは以下のとおりです。scatterの出力でカラーマップを指定するのと、
カラーバーの出力を行う２点が通常の散布図の描画と異なる点です。
"""

import matplotlib.pyplot as plt


# x, yデータ
x = range(20)
y = range(20)

# 点(x, y)が持つ量
z = range(20)

# カラーマップ
cm = plt.cm.get_cmap('RdYlBu')

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axに散布図を描画、戻り値にPathCollectionを得る
mappable = ax.scatter(x, y, c=z, vmin=0, vmax=20, s=35, cmap=cm)

# カラーバーを付加
fig.colorbar(mappable, ax=ax)

# 表示
plt.show()

"""
matplotlibのカラーマップ

カラーマップとは値と色の対応関係を表す辞書を指します。
matploblitのグラフ描画関数の多くにcmapというパラメータがありますが、
ここでカラーマップオブジェクトを指定することで値に応じた色付けが可能となります。

カラーマップの生成

matploblibでカラーマップを生成する場合、以下のようにget_cmapを使用します。

cm = plt.cm.get_cmap('RdYlBu')

get_cmapで指定したパラメターでカラーマップの種類を指定します。
カラーマップは目的に応じて様々な種類があるのですが、
上のサンプルでは単調な増減に適したDivergingと呼ばれるものの一種で'RdYlBu'を使用しました。
これは赤〜青に変化するカラーマップです。

個人的には'RdYlBu'と'seismic'をよく使いますが、それ以外にも様々なものがあります。
詳しくは以下を参照してください。
https://matplotlib.org/3.1.3/tutorials/colors/colormaps.html

随分雰囲気が変わりますね。カラーマップの解説だけでかなり長くなりますので機会があれば
別途詳しく説明したいと思います。

カラーマップの範囲

次にパラメータで指定したvmaxとvminです。
カラーマップには色の度合いに対して0〜100の範囲が割り当てられています。先程の参考リンクから引用します。

ここから説明が難しくなるのですが、散布される値の範囲とカラーマップで定義された値の範囲を
vmaxとvminでマッピングすることにより色の範囲を表現します。
例えば、上の散布図は値の範囲が0〜20の間に収まっていますが、
この点に対して0〜100をマッピングさせると、カラーバーの中の0〜20までの範囲しか使われなくなり、
全体的に赤色に寄った散布図となります。

mappable = ax.scatter(x, y, c=z, vmin=0, vmax=100, s=35, cmap=cm)

通常vmin、vmaxを省略するとこの範囲が自動的に設定されますので1枚図できれいに見せたいときは
指定する必要はないと思います。
"""


print("--- Python入門　matplotlib 3次元散布図---")


"""
3次元散布図

3次元の散布図を描画する場合、mpl_toolkits.mplot3d.axes3dというライブラリを追加でインポートします。
通常axesはfigureのメソッド、例えばadd_subplotを使用しますが、3次元散布図の場合はAxes3Dを使用します。
サンプルを見てみましょう。
"""

# from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D


# ランダムな点を生成する(x, y, z座標)
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = Axes3D(fig)

# axesに散布図を設定する
ax.scatter(x, y, c='b')

# 表示する
plt.show()

"""
先程の説明の通り、axesはAxes3Dを使用して生成します。
引数で指定したfigireに対して3Dのaxesが設定されます。

なお、出力結果についてはマウスのドラッグ・アンド・ドロップで方向を動かすことも可能です。

描画する点が多くなると、環境によってはレンダリングに時間がかかります。
あと、奥の点ほど色が薄く描画されていますが、点が持つ値が表現されているわけではない
という点に留意してください。点が持つ値や量を表す場合は次に説明するカラーバーを利用してください。


3次元でカラーバーを利用する場合

先程の散布図では単純に3次元空間上の点の分布について表現していました。
カラーバーを使うと3次元上の点の分布に加え、それぞれ持つ量を可視化することが可能です。
例えば観測施設内に設置したセンサーで得た気温等の値の分布を表現することが可能です。
カラーマップを使用しますがそれについては前回の記事を参照してください。
matplotlib カラーバー付き散布図
"""

# from matplotlib import pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d.axes3d import Axes3D


# ランダムな点を生成する(x, y, z座標)
x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

# 点(x, y, z)が持つ量
value = np.random.rand(50)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = Axes3D(fig)

# カラーマップを生成
cm = plt.cm.get_cmap('RdYlBu')

# axに散布図を描画、戻り値にPathCollectionを得る
mappable = ax.scatter(x, y, c=value, cmap=cm)

# 表示する
plt.show()

"""
上のサンプルコードでは3次元上の座標列x, y, zに加え、valueがそれぞれの点がもつ値の配列を表しています。
"""


print("--- Python入門　matplotlib 棒グラフ---")


"""
このページではmatplotlibを使用して棒グラフを描画する方法について解説します。
サンプルはOO形式と呼ばれる書き方となっています。
figure、axesについて知らない方は事前に以下を一読することをおすすめします。

matplotlib入門
matplotlibの基本 figureとaxes

棒グラフの基本
簡単なサンプル

まずは最低限、簡単なサンプルからです。
"""

# import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesに棒グラフを設定する
ax.bar(left, height)

# 表示する
plt.show()

"""
leftで横軸、heightで値を設定します。
leftはマイナスや、小数の指定が可能です。
また、幅のデフォルトは0.8となります。

オプション

最低限の表示ができたところで、オプションについて確認してみましょう。ax.barの引数は以下の通りです。

引数 	      必須 	  意味 	      指定する値
left 	       ○ 	  横座標 	  数値シーケンス
height 	       ○ 	  縦座標 	  数値シーケンス
width 		          棒の幅 	  数値。デフォルトは0.8
bottom 		          棒の下側の位置 	#RGB
color 		          棒の色 	    #RGB
edgecolor 		      棒の枠線の色 	数値
linewidth 		      棒の枠線の太さ 	数値
tick_label 		      横軸のラベル   文字列シーケンス
xerr 		          横軸のエラーバー 数値シーケンス
yerr 		          縦軸のエラーバー 数値シーケンス
ecolor 		          エラーバーの色 	#RGB
align 		          棒の位置 	   ‘edge’ 、‘center’ のどちらかを指定。
                                   デフォルトは’edge’
log 		          対数目盛り    TrueかFalseのどちらかを指定。
                                   デフォルトはFalse

それでは、上記オプションを踏まえて色んな棒グラフを作成してみましょう。

横軸ラベルを挿入する

tick_labelを指定すると横軸にラベルを打てます。
横軸が性別、血液型、都道府県といった質的データの場合に利用できます。
"""

# import matplotlib.pyplot as plt


# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 4, 5, 1, 2]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# 前後は先ほどと同じなので省略
labels = ['A', 'B', 'C', 'D', 'E']
plt.bar(left, height, tick_label=labels)

# 表示する
plt.show()

"""
枠線を設定する

バージョンによって挙動が異なるのですが、この記事の作成で使用している2.2.X系では枠線が表示されません。
枠線を表示するにはedgecolorとlinewidthを設定します。

# 前後は先ほどと同じなので省略
ax.bar(left, height, linewidth=1, edgecolor="#000000")

"""

# import matplotlib.pyplot as plt


# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# 前後は先ほどと同じなので省略
labels = ['A', 'B', 'C', 'D', 'E']
plt.bar(left, height, linewidth=1, edgecolor="#000000")

# 表示する
plt.show()

"""
linewidthは上のサンプルのように数値を指定する以外に配列で棒ごとのエッジを設定することも可能です。

ax.bar(left, height, linewidth=[1, 4, 6, 8, 10], edgecolor="#000000")
"""

# import matplotlib.pyplot as plt


# 対象データ
left = [3, 1, 5, 4, 6]    # 横軸(棒の左端の位置)
height = [1, 2, 3, 4, 5]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# 前後は先ほどと同じなので省略
labels = ['A', 'B', 'C', 'D', 'E']
plt.bar(left, height, linewidth=[1, 4, 6, 8, 10], edgecolor="#000000")

# 表示する
plt.show()

"""
強調したい系列に対して有効な表現手段の1つとして知っておくと役に立つと思います。

棒の間隔を調整する

widthを指定すると棒の間隔を調整することができます。デフォルト値は0.8となっています。
例えば棒と棒の間隔を開けたくない場合、leftの間隔と棒の幅を同じにすると隙間がなくなります。
上のサンプルのleftの間隔は1となっているので、widthに1を指定してみます。

# 前後は先ほどと同じなので省略
ax.bar(left, height, width=1, linewidth=1, edgecolor="#000000")
"""

# import matplotlib.pyplot as plt


# 対象データ
left = [-1, 2, 5, 4, 7]    # 横軸(棒の左端の位置)
height = [1, 2, 3, 4, 5]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesに棒グラフを設定する
ax.bar(left, height)

# 前後は先ほどと同じなので省略
labels = ['A', 'B', 'C', 'D', 'E']
plt.bar(left, height, width=1, linewidth=1, edgecolor="#000000")

# 表示する
plt.show()

"""
凡例、タイトル、最大/最小を指定等

基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりですが、
よくサイト内を検索されるため凡例、ラベルなどの各種グラフ要素を挿入したサンプルを掲載します。
詳しくはリンク先を参照してください。
"""

# from matplotlib import pyplot as plt
# import numpy as np

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値
# 横軸のラベル
labels = ['A', 'B', 'C', 'D', 'E']

# axesに棒グラフを設定する
plt.bar(left, height, width=1, linewidth=1, edgecolor='#000000')

# 汎用要素を表示
plt.grid(True)     # grid表示ON
plt.xlim(left=0, right=7)    # x範囲
plt.ylim(bottom=0, top=10)    # y範囲
plt.xlabel('X')    # x軸ラベル
plt.ylabel('Y')    # y軸ラベル
plt.title('plt.title')    # グラフタイトル
plt.legend(['legend'])    # 凡例を表示

plt.show()


"""
複数系列の棒グラフ
積み上げ棒グラフ

積み上げ棒グラフで複数の系列を表示する場合は簡単で、
2番目以降の系列に対し、bottomオプションで１番目の系列の値分、底上げします。
"""

# from matplotlib import pyplot as plt


# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height1 = [3, 5, 1, 2, 3]    # 値
height2 = [6, 10, 2, 4, 6]

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)


# axesに棒グラフを設定する
plt.bar(left, height)
plt.bar(left, height, bottom=height1)

# 表示する
plt.show()


"""
複数系列を並べる

複数の系列を横に並べて描画する場合は少し工夫が必要になります。
2系列目以降はleftに棒の幅分ずらした値を指定する必要があります。
要素毎の計算が必要であるためnumpy.ndarrayを使用することをおすすめします。
"""

# from matplotlib import pyplot as plt
# import numpy as np



# 対象データ
left = np.arange(5)
height1 = [20, 34, 30, 35, 27]   
height2 = [25, 32, 34, 20, 25]

width = 0.3

fig, ax = plt.subplots()
plt.bar(left - width / 2, height1, width=-0.3, linewidth=1, edgecolor='#000000')
plt.bar(left - width / 2, height2, width=0.3, linewidth=1, edgecolor='#FFaaaa', align='edge')


plt.show()

"""
さらにラベルを打つ場合も位置の考慮が必要なのですが、公式ドキュメントで非常にわかりやすいサンプルがあったため紹介します。
Grouped bar chart with labels

リンク先のコードを実行すると以下のように複数系列の棒グラフにラベルをつけることが可能です。
"""
