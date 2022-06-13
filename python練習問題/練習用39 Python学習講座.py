#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　matplotlib 折れ線グラフ---")


"""
このページではmatplotlibを使用して折れ線グラフを描画する方法について解説します。
なお、連続な関数のグラフについては別頁で説明する予定です。

サンプルはOO形式と呼ばれる書き方となっています。
figure、axesについて知らない方は事前に以下を一読することをおすすめします。
matplotlib入門
matplotlibの基本 figureとaxes

折れ線グラフの基本
簡単なサンプル

まずは最低限、簡単なサンプルからです。
"""

import matplotlib.pyplot as plt

# 対象データ
x = [1, 2, 3, 4, 5]    # x軸の値
y = [100, 300, 200, 500, 0]    # y軸の値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y)

# 表示
plt.show()

"""
折れ線グラフを描画する場合、ax.plotを使用します。x, yにそれぞれ値の配列を指定するだけです。


オプション

最低限の表示ができたところで、折れ線グラフ向けのオプションについて紹介します。

線の種類

ax.plotの第3引数に先の種類を指定することができます。指定できる線の種類は以下の通りです。

      値 	      出力
      - 	      実線
      -- 	      点線
      : 	      細かい点線
      -. 	      複合点線


線の色

線の色は引数cで指定することができます。


先の太さ

linewidthで先の太さを指定することができます。


マーカー

マーカーの種類は、引数markerで指定することが可能です。散布図編に記述したものと同様なので、一覧は割愛します。


線の色、太さ、種類、マーカーの指定のサンプル

以下は先ほどのコードに線の色、太さ、種類、マーカーの指定を加えたものです。
"""

import matplotlib.pyplot as plt

# 対象データ
x = [1, 2, 3, 4, 5]    # x軸の値
y1 = [100, 400, 200, 650, 0]    # y軸の値
y2 = [150, 250, 650, 450, 50]    # y軸の値
y3 = [200, 450, 350, 500, 100]    # y軸の値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, '-', c='#ff0000', linewidth=1, marker='*')
ax.plot(x, y2, '--', c='#00ff00', linewidth=2, marker='o')
ax.plot(x, y3, ':', c='#0000ff', linewidth=4, marker='D')

# 表示
plt.show()


"""
凡例、タイトル等

散布図のときの説明と同様となりますが、
基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりです。
よくサイト内を検索されるため凡例、ラベルなどの各種グラフ要素を挿入したサンプルを掲載します。
詳しくはリンク先を参照してください。
"""

import matplotlib.pyplot as plt

# 対象データ
x = [1, 2, 3, 4, 5]    # x軸の値
y1 = [100, 300, 200, 500, 700]    # y軸の値
y2 = [150, 350, 250, 550, 750]    # y軸の値

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, '-', c='#ff0000', linewidth=1, marker='*')
ax.plot(x, y2, '--', c='#00ff00', linewidth=2, marker='o')

# 汎用要素を表示
plt.grid(True)    # grid表示ON
ax.set_xlim(left=-1, right=6)    # x範囲
ax.set_ylim(bottom=-100, top=1000)    # y範囲
plt.xlabel('X')    # x軸ラベル
plt.ylabel('Y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
plt.legend(['Line 1', 'Line 2'])    # 凡例を表示

# 表示
plt.show()

"""
範囲指定やグリッド、軸ラベル、凡例の表示がされていることが確認できます。
"""


print("--- Python入門　matplotlib 関数のグラフ---")


"""
このページではmatplotlibを使用して連続的な関数のグラフを描画する方法について解説します。
サンプルはOO形式と呼ばれる書き方となっています。

関数のグラフ

前回解説した折れ線グラフの離散的な点を十分多くすると関数のグラフを描画することができます。
（ですので、この記事はどちらかというとNumpyの説明になりますが）通常、
点の数を連続的に見えるほど多くするにはnumpyのlinspaceやarangeを使用します。

以下のコードでは[-5, 5]区間の2次関数のグラフを描画しています。プロットする点の数は100を指定しています。
"""

import numpy as np
import matplotlib.pyplot as plt


# 対象データ
x = np.linspace(-5, 5, 100)
y = x ** 2

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y)

# 表示
plt.show()

"""
十分滑らかに描画されていることが確認できます。

Numpy組み込みのユニバーサル関数を使用すると大抵の初等関数を使用することが可能です。

例えば、[-2π, 2π]区間のsin、cosの三角関数のグラフを描画する場合、以下のように記述します。
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ
x = np.linspace(-np.pi * 2, np.pi * 2, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, c='blue')
ax.plot(x, y2, c='red')

# 表示
plt.show()


"""
グラフを塗りつぶす

また、fill_betweenを利用すると第3引数で指定した高さのグラフに囲まれた領域が塗りつぶされます。
先程のplot部分の後ろに以下を追記してみます。

ax.fill_between(x, y1, y2, color="#30a0ff")

sin(x)とcos(x)に囲まれた部分が塗りつぶされます。
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ
x = np.linspace(-np.pi * 2, np.pi * 2, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, c='green')
ax.plot(x, y2, c='red')
ax.fill_between(x, y1, y2, color="#30a0ff")


# 表示
plt.show()


print("--- Python入門　matplotlib ヒストグラム---")


"""
このページではmatplotlibを使用してヒストグラムを描画する方法について解説します。
サンプルはOO形式と呼ばれる書き方となっています

ヒストグラムの基本
簡単なサンプル

まずは最低限、簡単なサンプルからです。以下のサンプルでは平均0、標準偏差10の正規乱数を1000個生成し、
ヒストグラムで表示しています。
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ(平均0、標準偏差10の正規乱数を1000個生成)
x = np.random.normal(0, 10, 1000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, bins=10)

# 表示
plt.show()

"""
オプション

最低限の表示ができたところで、オプションについて解説します。以下、hist()の代表的なオプションです。

axes.hist
axes.hist(x, binx, range, density, cumulative, color, ec)

パラメータ                     説明
x(必須)                     データ配列
bins                        階級数(デフォルト値: 10)
range                       表示する階級の範囲（最大と最小を指定）
density                     Trueを指定すると面積が1となるように正規化(デフォルト値：False)
cumulative                  Trueを指定すると累積化(デフォルト値：False)
color                       色
ec                          境界色
alpha                       透明度（0〜1を指定、0：完全透明、1：不透明）

それでは、上記オプションを踏まえて様々なヒストグラムを作成してみましょう。


bins 階級数

binsを指定すると階級数を指定することができます。
また、リストなどの配列を指定するとその配列を階級とすることができます。
スタージェスの公式で自動的に階級分けすることもできます。
上のコードのbinsの値を以下の通り変更してみます。
つまり、階級数を20にするわけですね。

ax.hist(x, bins=20)
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ(平均0、標準偏差10の正規乱数を1000個生成)
x = np.random.normal(0, 10, 1000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, bins=20)

# 表示
plt.show()

"""
このように階級幅が細かくなったことが確認できます。
また、文字列autoを指定するとスタージェスの公式若しくはフリードマン＝ダイアコニスの法則の公式が適用されます。

density 正規化

densityにTrueを指定すると、面積1に調整してくれるため、
十分大きいサンプルで階級数を増やすと確率密度関数に近づけることができます。
実際、density=Trueのヒストグラムと平均0、標準偏差10の正規分布の確率密度関数を重ねて表示すると、
以下の通り十分近いかたちが得られます。
"""

# import numpy as np
# import matplotlib.pyplot as plt
from scipy.stats import norm


# 対象データ(平均0、標準偏差10の正規乱数)
x = np.random.normal(0, 10, 10000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, bins=30, density=True)

# 対象データ(平均0、標準偏差10の正規分布の確率密度関数のグラフ)
X = np.linspace(-50, 50, 100)
Y = norm.pdf(X, loc=0, scale=10)
ax.plot(X, Y, c='red')

# 表示
plt.show()

"""
このようにdensityを指定するとヒストグラムで確率的に可視化することができます。


cumulative 累積ヒストグラム

cumulative=Trueを指定すると、累積ヒストグラムを作成することができます。
最初のサンプルから以下の通り修正してみます。

ax.hist(x, cumulative=True)
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ(平均0、標準偏差10の正規乱数)
x = np.random.normal(0, 10, 10000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, cumulative=True)

# 表示
plt.show()


"""
色と境界線

color、ecを指定すると、色・境界色を指定することができます。最初のサンプルから以下の通り修正してみます。

ax.hist(x, color="#FF8888")
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ(平均0、標準偏差10の正規乱数を1000個生成)
x = np.random.normal(0, 10, 1000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x, bins=10, color='#FF8888')

# 表示
plt.show()


"""
重ね合わせと透明度

また、複数系列を重ねることもできますが、この際、alphaを指定して透明度を調整すると重複範囲が見やすくなります。
以下のサンプルは2種類の正規乱数のヒストグラムを重ねて表示しています。
"""

# import numpy as np
# import matplotlib.pyplot as plt


# 対象データ(平均0、標準偏差10の正規乱数を1000個生成)
x1 = np.random.normal(0, 10, 1000)

# 対象データ(平均10、標準偏差10の正規乱数を1000個生成)
x2 = np.random.normal(10, 10, 1000)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.hist(x1, color='#00AAFF', ec='#0000FF', alpha=0.5)
ax.hist(x2, color='#FF8888', ec='#FF0000', alpha=0.5)

# 表示
plt.show()
