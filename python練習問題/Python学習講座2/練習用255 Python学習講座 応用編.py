#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib 3次元散布図 ---")


print("--- 3次元散布図 ---")


"""
3次元の散布図を描画する場合、
mpl_toolkits.mplot3d.axes3dというライブラリを追加でインポートします。
通常axesはfigureのメソッド、例えばadd_subplotを使用しますが、
3次元散布図の場合はAxes3Dを使用します。サンプルを見てみましょう。
"""

from matplotlib import pyplot as plt
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

# 表示
plt.show()

"""
MatplotlibDeprecationWarning: Axes3D(fig) adding itself to the figure is deprecated since 3.4. Pass the keyword argument auto_add_to_figure=False and use fig.add_axes(ax) to suppress this warning. The default value of auto_add_to_figure will change to False in mpl3.5 and True values will no longer work in 3.6.  This is consistent with other Axes classes.

MatplotlibDeprecationWarning: Axes3D(fig) 自体を Figure に追加することは、3.4 以降非推奨です。 キーワード引数 auto_add_to_figure=False を渡し、 fig.add_axes(ax) を使用してこの警告を抑制します。 auto_add_to_figure のデフォルト値は mpl3.5 で False に変更され、True 値は 3.6 では機能しなくなります。 これは、他の Axes クラスと一致しています。


先程の説明の通り、axesはAxes3Dを使用して生成します。
引数で指定したfigireに対して3Dのaxesが設定されます。
なお、出力結果についてはマウスのドラッグ・アンド・ドロップで方向を動かすことも可能です。

描画する点が多くなると、環境によってはレンダリングに時間がかかります。
あと、奥の点ほど色が薄く描画されていますが、
点が持つ値が表現されているわけではないという点に留意してください。
点が持つ値や量を表す場合は次に説明するカラーバーを利用してください。
"""


print("--- 3次元でカラーバーを利用する場合 ---")


"""
先程の散布図では単純に3次元空間上の点の分布について表現していました。
カラーバーを使うと3次元上の点の分布に加え、
それぞれ持つ量を可視化することが可能です。
例えば観測施設内に設置したセンサーで得た気温等の
値の分布を表現することが可能です。
カラーマップを使用しますがそれについては前回の記事を参照してください。
"""

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D

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

# axに散布図を描画、戻り値にPAthcollectionを得る
mappable = ax.scatter(x, y, c=value, cmap=cm)
fig.colorbar(mappable, ax=ax)

# 表示
plt.show()

"""
上のサンプルコードでは3次元上の座標列x, y, zに加え、
valueがそれぞれの点がもつ値の配列を表しています。
"""



print("--- アヒルの豆知識より ---")


print("--- 3D散布図(scatter)の作り方【matplotlib】 ---")


"""
matplotlibで3D散布図(scatter)の作成のやり方を紹介したいと思います。


3D scatterを作ってみる

基本的には2Dグラフの場合と同じようにして作成することができます。
2Dグラフと違うところは

    3次元目のデータを用意する
    add_subplotにおいてprojection='3d'を指定する

ところだけです。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z)
plt.show()


print("--- 3D scatter をカスタマイズ ---")


"""
基本的に2dの場合と同じように色やサイズ等をカスタマイズすることができます。


全ての色を変更

color引数から色を指定します。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, color='purple')
plt.show()


"""
個別に色を設定

個別に散布図の点の色を変更することもできます。


カラーネームのリストから設定

リスト形式のカラーネームをcolor引数に与えることで、
それに対応した点の色を変更することができます。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(5)
y = np.random.rand(5)
z = np.random.rand(5)

colors = ['green', 'blue', 'yellow', 'purple', 'red']
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, color=colors)
plt.show()


"""
RGBから設定

カラーネームでなくRGB or RGBA でもOKです。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

colors = np.random.random_sample((100, 3))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, color=colors)
plt.show()


"""
透明度を設定

color引数にRGBAを与えることで、個別に透明度を設定できますが、
alpha引数を利用することで全ての点の透明度を一括で設定できます。
値は0.0~1.0までで、0.0が完全に透明を表し、1.0が完全に不透明を表します。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, alpha=0.2)
plt.show()


"""
sizeの変更

scatterのmarkerの大きさは s引数に数値を与えることで、変更することができます。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, s=100)
plt.show()


"""
markerの形を変更

3D scatterのmarkerの形はデフォルトで●ですが、色々な形に変更することができ、
変更に用いるのはmarker引数です。
具体的にどのような文字を引数に渡せばどのようなmarkerになるかは
下記のドキュメントを参照してください。
https://matplotlib.org/stable/api/markers_api.html
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, marker='|')
plt.show()


"""
枠線のカスタマイズ

3D scatterの点は塗りつぶし部と枠線によって構成されています。
この枠線部のみをカスタマイズすることが可能です。


枠線の色を変更

色の指定にはedgecolor引数を使いますが、
色の指定方法は前述したcolor引数と同様で、
カラーネームで一括設定もできれば、
点の数だけカラーネーム or RGBを用意して個別に指定することもできます。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, edgecolor='r')
plt.show()


"""
枠線の幅を調整

枠線の線幅はlinewidth引数によって調整ができます。
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, edgecolor='r', linewidth=5)
plt.show()
