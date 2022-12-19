#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- matplotlib 関数のグラフ ---")


print("--- 関数のグラフ ---")


"""
前回解説した折れ線グラフの離散的な点を十分多くすると
関数のグラフを描画することができます。
（ですので、この記事はどちらかというとNumpyの説明になりますが）
通常、点の数を連続的に見えるほど多くするには
numpyのlinspaceやarangeを使用します。

以下のコードでは[-5, 5]区間の2次関数のグラフを描画しています。
プロットする点の数は100を指定しています。
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

Numpy組み込みのユニバーサル関数を使用すると
大抵の初等関数を使用することが可能です。


例えば、[-2π, 2π]区間のsin、cosの三角関数のグラフを描画する場合、
以下のように記述します。
"""

import numpy as np
import matplotlib.pyplot as plt

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


print("--- グラフを塗りつぶす ---")


"""
また、fill_betweenを利用すると
第3引数で指定した高さのグラフに囲まれた領域が塗りつぶされます。
先程のplot部分の後ろに以下を追記してみます。
"""

import numpy as np
import matplotlib.pyplot as plt

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
ax.fill_between(x, y1, y2, color='#30a0ff')

# 表示
plt.show()
