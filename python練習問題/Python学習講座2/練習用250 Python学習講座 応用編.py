#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib入門 ---")


print("--- matplotlibとは？ ---")


"""
matplotlibとはPythonのプロットライブラリの一つで、
わずか数行のコードで、ヒストグラム、パワースペクトル、棒グラフ、
 errorcharts 、散布図などを生成することができます。

インストールについて、anacondaに予め入っているためそちらを使うことをおすすめします。
pyenvを利用している場合以下のコマンドでインストールできます。

pyenv install anaconda3-5.3.1

anacondaについては以下も参照してください。
"""


print("--- matplotlibの2つの書き方 ---")


"""
まず、matplotlibを学習する前に注意すべき点があります。
それは書き方が2種類あるという点です。
もともとmatplotlibはMathWorks社が開発している数値解析ソフトウェア有償ソフト、
MATLAB（マトラボ）のグラフィックコマンドをエミュレートしていました。
ですが、時代が下るに従いPythonの
オブジェクト指向のインターフェースが拡充されるようになりました。
というわけでmatplotlibには伝統的なMATLAB形式の書き方と、
オブジェクト指向形式のインターフェースを利用した書き方
（以降、当サイトではOO形式と記述します）の2つがあります。
MATLAB形式の書き方は記述量が少なくて済むのですが、
カスタマイズで難儀することが多いと言われており、
この記事を書いている2020年ではOO形式の書き方が推奨されています。

https://matplotlib.org/tutorials/introductory/lifecycle.html

今後のサンプルはOO形式で解説をすすめますが、
サンプルで簡単に両者の違いを解説します。
すでにmatplotlibを使っているけど
2つの書き方を混同している方は是非読んでみてください。
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
pyplot.title('sample_1')

# 表示
pyplot.show()

"""
pyplotというモジュールの関数を順に呼び出して処理を行います。
比較的とっつきやすく感じるかもしれません。
一方でscatter、legend、titleはそれぞれ関数なのですが、
何に対して処理を行っているのかというのがわかりづらいという点があります。
実際、細かいカスタマイズをするととたんに面倒になる、
というかできないことが多々あります。


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
ax.set_title('sample1')

# 表示する
plt.show()

"""
出力は先程と同じなので省略します。
figure、axというオブジェクトの属性に対して操作を行います。
MATLAB形式と比較して記述量は増えますが、
グラフを構成するモノ（=オブジェクト）に対して情報を
付加していくだけなのでカスタマイズしやすさや考え方としては
こちらの方が優れていると思います。
次回、上のサンプルのfigure、axesについて詳しく解説します。
"""
