# -*- coding: utf-8 -*-
# リストdataの数値をグラフ化する

import matplotlib.pyplot as plt    # matplotlib.pyplotモジュールを読み込む
import matplotlib as mpl


data = [2, 2.3, 4.1, 2.4, 5.3, 3.2, 4.6]    # グラフ化するデータ
plt.plot(data)    # グラフを描く
plt.show()    # 表示する  show()を実行するとグラフが表示される
