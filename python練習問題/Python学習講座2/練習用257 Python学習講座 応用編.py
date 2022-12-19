#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib 折れ線グラフ ---")


print("--- 折れ線グラフの基本 ---")


"""
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
折れ線グラフを描画する場合、ax.plotを使用します。
x, yにそれぞれ値の配列を指定するだけです。
"""


print("--- オプション ---")


"""
最低限の表示ができたところで、折れ線グラフ向けのオプションについて紹介します。
線の種類

ax.plotの第3引数に先の種類を指定することができます。
指定できる線の種類は以下の通りです。


値 	出力
- 	実線
-- 	点線
: 	細かい点線
-. 	複合点線


線の色

線の色は引数cで指定することができます。


先の太さ

linewidthで先の太さを指定することができます。


マーカー

マーカーの種類は、引数markerで指定することが可能です。
散布図編に記述したものと同様なので、一覧は割愛します。


線の色、太さ、種類、マーカーの指定のサンプル

以下は先ほどのコードに線の色、太さ、種類、マーカーの指定を加えたものです。
"""

import matplotlib.pyplot as plt

# 対象データ
x = [1, 2, 3, 4, 5]    # x軸の値
y1 = [100, 300, 200, 500, 0]    # y軸の値
y2 = [150, 350, 250, 550, 50]    # y軸の値
y3 = [200, 400, 300, 600, 100]    # y軸の値


# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y1, "-", c="#ff0000", linewidth=1, marker='*')
ax.plot(x, y2, "--", c="#00ff00", linewidth=2, marker='o')
ax.plot(x, y3, ":", c="#0000ff", linewidth=4, marker='D')

# 表示
plt.show()


print("--- 凡例、タイトル等 ---")


"""
散布図のときの説明と同様となりますが、
基本的にはaxesのカスタマイズ グラフの汎用要素で説明したとおりです。
よくサイト内を検索されるため凡例、
ラベルなどの各種グラフ要素を挿入したサンプルを掲載します。
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
ax.plot(x, y1, "-", c="#ff0000", linewidth=1, marker='*')
ax.plot(x, y2, "--", c="#00ff00", linewidth=2, marker='o')

# 凡例要素を表示
ax.grid(True)    # grid表示ON
ax.set_xlim(left=-1, right=6)    # x範囲
ax.set_ylim(bottom=-100, top=1000)    # y範囲
ax.set_xlabel('X')    # x軸ラベル
ax.set_ylabel('Y')    # y軸ラベル
ax.set_title('ax title')    # グラフタイトル
ax.legend(['Line 1', 'Line 2'])    # 凡例を表示

plt.show()

"""
範囲指定やグリッド、軸ラベル、凡例の表示がされていることが確認できます。
"""
