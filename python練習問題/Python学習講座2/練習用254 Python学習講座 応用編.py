#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib カラーバー付き散布図 ---")


print("--- カラーバー付きの散布図を出力する ---")


"""
前回の説明で、点に色を付ける方法を説明しましたが、
今回は連続的な量を持つ点に色付けしたい場合です。
先に出力結果を添付します。

ソースコードは以下のとおりです。
scatterの出力でカラーマップを指定するのと、
カラーバーの出力を行う２点が通常の散布図の描画と異なる点です。
"""

import matplotlib.pyplot as plt

# x,yデータ
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

# axに散布図を描画、戻り値にPathcollectionを得る
mappable = ax.scatter(x, y, c=z, vmin=0, vmax=20, s=35, cmap=cm)

# カラーバーを付加
fig.colorbar(mappable, ax=ax)

# 表示
plt.show()


print("--- matplotlibのカラーマップ ---")


"""
カラーマップとは値と色の対応関係を表す辞書を指します。
matploblitのグラフ描画関数の多くにcmapというパラメータがありますが、
ここでカラーマップオブジェクトを指定することで値に応じた色付けが可能となります。


カラーマップの生成

matploblibでカラーマップを生成する場合、以下のようにget_cmapを使用します。

cm = plt.cm.get_cmap('RdYlBu')

get_cmapで指定したパラメターでカラーマップの種類を指定します。
カラーマップは目的に応じて様々な種類があるのですが、
上のサンプルでは単調な増減に適したDiverging
と呼ばれるものの一種で'RdYlBu'を使用しました。
これは赤〜青に変化するカラーマップです。

個人的には'RdYlBu'と'seismic'をよく使いますが、
それ以外にも様々なものがあります。詳しくは以下を参照してください。

https://matplotlib.org/3.1.3/tutorials/colors/colormaps.html

同じくDivergingの一種、'PRGn'を指定すると以下のようになります。
"""

import matplotlib.pyplot as plt

# x,yデータ
x = range(20)
y = range(20)

# 点(x, y)が持つ量
z = range(20)

# カラーマップ
cm = plt.cm.get_cmap('PRGn')

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axに散布図を描画、戻り値にPathcollectionを得る
mappable = ax.scatter(x, y, c=z, vmin=0, vmax=20, s=35, cmap=cm)

# カラーバーを付加
fig.colorbar(mappable, ax=ax)

# 表示
plt.show()

"""
随分雰囲気が変わりますね。
カラーマップの解説だけでかなり長くなりますので機会があれば
別途詳しく説明したいと思います。


カラーマップの範囲

次にパラメータで指定したvmaxとvminです。
カラーマップには色の度合いに対して0〜100の範囲が割り当てられています。
先程の参考リンクから引用します。

ここから説明が難しくなるのですが、
散布される値の範囲とカラーマップで定義された値の範囲を
vmaxとvminでマッピングすることにより色の範囲を表現します。
例えば、上の散布図は値の範囲が0〜20の間に収まっていますが、
この点に対して0〜100をマッピングさせると、
カラーバーの中の0〜20までの範囲しか使われなくなり、
全体的に赤色に寄った散布図となります。
"""

import matplotlib.pyplot as plt

# x,yデータ
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

# axに散布図を描画、戻り値にPathcollectionを得る
mappable = ax.scatter(x, y, c=z, vmin=0, vmax=100, s=35, cmap=cm)

# カラーバーを付加
fig.colorbar(mappable, ax=ax)

# 表示
plt.show()

"""
通常vmin、vmaxを省略すると
この範囲が自動的に設定されますので
1枚図できれいに見せたいときは指定する必要はないと思います。
"""
