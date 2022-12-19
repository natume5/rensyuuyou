#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib 棒グラフ ---")


print("--- 棒グラフの基本 ---")


"""
簡単なサンプル

まずは最低限、簡単なサンプルからです。
"""

import matplotlib.pyplot as plt

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
上記リストをleft = [-1, 2.5, 3, 4, 7]と指定した場合、
以下のようになります。
left = [-1, 2.5, 3, 4, 7]の場合
"""

import matplotlib.pyplot as plt

# 対象データ
left = [-1, 2.5, 3, 4, 7]    # 横軸(棒の左端の位置)
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
オプション

最低限の表示ができたところで、オプションについて確認してみましょう。
ax.barの引数は以下の通りです。


引数 	  必須 	  意味 	        指定する値
left 	   ○ 	  横座標 	    数値シーケンス
height 	   ○ 	  縦座標 	    数値シーケンス
width 		      棒の幅 	    数値。デフォルトは0.8
bottom 		    棒の下側の位置 	#RGB
color 		      棒の色 	    #RGB
edgecolor 		棒の枠線の色 	    数値
linewidth 		棒の枠線の太さ 	数値
tick_label 		横軸のラベル 	    文字列シーケンス
xerr 		    横軸のエラーバー 	数値シーケンス
yerr 		    縦軸のエラーバー 	数値シーケンス
ecolor 		    エラーバーの色 	    #RGB
align 		    棒の位置 	        ‘edge’ 、‘center’ のどちらかを指定。
                                デフォルトは’edge’
log 		    対数目盛り 	    TrueかFalseのどちらかを指定。
                                デフォルトはFalse

それでは、上記オプションを踏まえて色んな棒グラフを作成してみましょう。


横軸ラベルを挿入する

tick_labelを指定すると横軸にラベルを打てます。
横軸が性別、血液型、都道府県といった質的データの場合に利用できます。
"""

import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

labels = ['A', 'B', 'C', 'D', 'E']
ax.bar(left, height, tick_label=labels)

# axesに棒グラフを設定する
ax.bar(left, height)

# 表示する
plt.show()


"""
枠線を設定する

バージョンによって挙動が異なるのですが、
この記事の作成で使用している2.2.X系では枠線が表示されません。
枠線を表示するにはedgecolorとlinewidthを設定します。
"""

import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

ax.bar(left, height, linewidth=1, edgecolor='#000000')

# axesに棒グラフを設定する
ax.bar(left, height)

# 表示する
plt.show()

"""
linewidthは上のサンプルのように数値を指定する以外に
配列で棒ごとのエッジを設定することも可能です。
"""

import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

ax.bar(left, height, linewidth=[1, 4, 6, 8, 10], edgecolor='#000000')

# axesに棒グラフを設定する
ax.bar(left, height)

# 表示する
plt.show()

"""
強調したい系列に対して有効な表現手段の1つとして知っておくと役に立つと思います。


棒の間隔を調整する

widthを指定すると棒の間隔を調整することができます。
デフォルト値は0.8となっています。
例えば棒と棒の間隔を開けたくない場合、
leftの間隔と棒の幅を同じにすると隙間がなくなります。
上のサンプルのleftの間隔は1となっているので、widthに1を指定してみます。
"""

import matplotlib.pyplot as plt

# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height = [3, 5, 1, 2, 3]    # 値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

ax.bar(left, height, width=1, linewidth=1, edgecolor='#000000')

# axesに棒グラフを設定する
ax.bar(left, height)

# 表示する
plt.show()


"""
凡例、タイトル、最大/最小を指定等

基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりですが、
よくサイト内を検索されるため凡例、ラベルなどの各種グラフ要素を挿入した
サンプルを掲載します。詳しくはリンク先を参照してください。
"""

import matplotlib.pyplot as plt
import numpy as np



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
ax.bar(left, height, width=1, linewidth=1, edgecolor='#000000')
# 凡例要素を表示
ax.grid(True)    # grid表示ON
ax.set_xlim(left=0, right=7)    # x範囲
ax.set_ylim(bottom=0, top=10)    # y範囲
ax.set_xlabel('X')    # x軸ラベル
ax.set_ylabel('Y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
ax.legend(['legend'])    # 凡例を表示

plt.show()


print("--- 複数系列の棒グラフ ---")


"""
積み上げ棒グラフ

積み上げ棒グラフで複数の系列を表示する場合は簡単で、
2番目以降の系列に対し、bottomオプションで１番目の系列の値分、底上げします。
"""

import matplotlib.pyplot as plt


# 対象データ
left = [1, 2, 3, 4, 5]    # 横軸(棒の左端の位置)
height1 = [3, 5, 1, 2, 3]
height2 = [6, 10, 2, 4, 6]

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesに棒グラフを設定する
ax.bar(left, height1)
ax.bar(left, height2, bottom=height1)

# 表示する
plt.show()


"""
複数系列を並べる

複数の系列を横に並べて描画する場合は少し工夫が必要になります。
2系列目以降はleftに棒の幅分ずらした値を指定する必要があります。
要素毎の計算が必要であるためnumpy.ndarrayを使用することをおすすめします。
"""

import matplotlib.pyplot as plt
import numpy as np

left = np.arange(5)
height1 = [20, 34, 30, 35, 27]
height2 = [25, 32, 34, 20, 25]

width = 0.3

fig, ax = plt.subplots()
ax.bar(left - width / 2, height1, width=width, linewidth=1, edgecolor='#000000')
ax.bar(left + width / 2, height2, width=width, linewidth=1, edgecolor='#000000')

plt.show()

"""
さらにラベルを打つ場合も位置の考慮が必要なのですが、
公式ドキュメントで非常にわかりやすいサンプルがあったため紹介します。

Grouped bar chart with labels

リンク先のコードを実行すると以下のように
複数系列の棒グラフにラベルをつけることが可能です。
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))    # the label locations
width = 0.35    # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, men_means, width, label='Men')
rects2 = ax.bar(x + width / 2, women_means, width, label='Women')

# Add same text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label abave  each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),     # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()







