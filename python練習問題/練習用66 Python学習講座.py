#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- 初めてのプログラミング編 グラフを作成してみよう---")


"""
今回でプログラミング基礎編が最後となります。
初めてのプログラミング編の最後はサードパーティ製ライブラリを使用してグラフを描いてみましょう。


pipとサードパーティ製ライブラリ

Pythonはインストールするだけで様々な処理ができるようになるのが大きなメリットです。
また、サードパーティ製ライブラリも充実しており、それらを使用するとさらにできることが広がります。

サードパーティ製ライブラリとは、公式のライブラリではなく有志が作成したライブラリのことで、
Pythonの場合はPyPIというサーバで公開されています。Pythonをインストールするとpip
というコマンドが使用できるようになりますが、
このpipでPyPIから様々なライブラリを追加でインストールすることができます。

pipを使ってmatplotlibをインストールしてみよう

それでは実際に試してみましょう。PyPIにはmatplotlibと呼ばれるグラフ描画ライブラリが公開されています。
以下のコマンドでインストールすることができます。

pip install matplotlib

インストールされたものを確認する場合、以下のコマンドを入力してください。

pip freeze

matplotlibと動作に必要となる関連するライブラリがズラリと表示されます。
グラフを作成してみよう

では、せっかくインストールしたので練習がてら使ってみましょう。以下のコードを入力してみてください。
"""

import numpy as np
import matplotlib.pyplot as plt


# 対象データ
x = np.linspace(-np.pi * 2, np.pi * 2, 100)
y = np.sin(x)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y, c='blue')

# 表示
plt.show()

"""
もう1つ試してみましょう。以下のコードを入力して実行してみてください。
"""

# import numpy as np
from matplotlib import pyplot as plt
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
数行のコードで綺麗なグラフが描画できることがご理解いただけたかと思います。
細かいコードの説明はここではしませんが、興味がある方は入門編を学習した上、
以下の記事を参照してください。
"""


"""
補足 ライブラリの完全アンインストール

演習後、学習を終えてクリーンな状態に戻したい場合は以下のコマンドを実行してください。

pip freeze > requirements.txt
pip uninstall -r requirements.txt

1つ目のコマンド、pip freezeでインストール済みライブラリの一覧をrequirements.txtに出力し、
requirements.txtに記述されたライブラリをすべてアンインストールしています。
1つ目のコマンドのように出力結果をファイルに出力することをリダイレクトと呼びます。
重要な単語なので覚えておいてください。


演習

それでは最後の演習です。上のプログラムを観察して、内容を書き換えてみてください。
（ライブラリを完全アンインストールしてしまった方は、再度pipでインストールしてください。）

以前にも書きましたが、既存のコードを書き換えてみてみる、
というのはプログラミングの上達のテクニックとして有効です。
今回もコードの書き換えにチャレンジしてみましょう。

演習

上で実行した三角関数のグラフは\(\sin(x)\)を\( [-2\pi, 2\pi] \)
の範囲で青色で作成しました。このグラフを\(\cos(x)\)、
範囲を\( [-4\pi, 4\pi] \)、色を赤色に修正してみてください。
"""

# import numpy as np
# import matplotlib.pyplot as plt

# 対象データ
x = np.linspace(-np.pi * 4, np.pi * 4, 100)
y = np.cos(x)

# figureを生成する
fig = plt.figure()

# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)

# axesにplot
ax.plot(x, y, c='red')

# 表示
plt.show()


