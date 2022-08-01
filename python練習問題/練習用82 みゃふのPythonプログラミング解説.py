#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- matplotlibで折れ線グラフを描く方法 ---")


"""
pythonでグラフを描画するには、専用のライブラリmatplotlibを使います。
matplotlibを使うことで簡単に折れ線グラフや棒グラフのような代表的なグラフを作成できます。
ここでは「matplotlibの基本的な使い方は？」「どんな種類のグラフを描けるの？」
といった疑問を持つPython初心者の方へ、matplotlibを使って折れ線グラフや棒グラフ、
2つ以上のグラフなどの基本的な描き方を解説します。
なお、matplotlibをインストールしていない場合、まずはpip等でmatplotlibをインストールしましょう。
"""


print("--- matplotlibでグラフを描いてみる ---")


"""
では早速、matplotlibを使って簡単なグラフを描いてみましょう。


シンプルな折れ線グラフ

まずは最も単純な折れ線グラフを描画します。
"""

import matplotlib.pyplot as plt

data = [3.0, 2.1, 4.5, 3.3, 3.4, 8.9]
plt.plot(data)
plt.show()

"""
グラフが作成されました。１行ずつプログラムを追ってみましょう。
始めに1行目でmatplotlibのpyplotモジュールをインポートしています。
ここでは慣習としてpltという略名をつけています。
2行目はグラフのデータ です。ここではリストを使っていますが、
numpyで作成できるndarrayでも同じことが可能です。
続いて3行目ではplot()を呼び出します。
2行目のデータを引数に渡すことでグラフを描画します。
最後にshow()を呼び出します。これで3行目で描画したグラフを表示させています。
show()を忘れるとグラフが表示されないので注意しましょう。
これでグラフが表示されました。縦軸（Y軸）はリストの値、横軸（X軸）はリストのインデックス番号です。


2つのリストからグラフを描画する

今度は2つのリストからグラフを描画してみましょう。
1つは縦軸、もう1つは横軸として使います。
例として、今回は「2019年の東京の月別平均気温」を折れ線グラフで描画するプログラムを作ってみました。
"""

# import matplotlib.pyplot as plt

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature_avg = [5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5]
plt.title("2019 Tokyo Avg Temperature")
plt.xlabel('Month')
plt.ylabel('Temperature Avg')
plt.plot(month, temperature_avg)
plt.show()

"""
変数monthが横軸のラベルで、実際のデータは変数temperature_avgに格納しています。
plt.title()はグラフのタイトル、plt.xlabel()は横軸のラベル、
plt.ylabel()は縦軸のラベルを付けています。あとは先ほどと同じく、
plot()で描画してshow()で表示しています。
"""


print("--- 2つのグラフを同時に描画し、凡例も追加する ---")


"""
次は2つの折れ線を同じグラフに表示してみましょう。
先ほどの東京の各月平均気温のグラフに、
札幌の平均気温を追加して両都市を比較するようなグラフを作ってみました。
"""

# import matplotlib.pyplot as plt

month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature_avg = [5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5]
temperature_avg_s = [-3.0, -2.6, 2.5, 8.0, 15.7, 17.4, 21.7, 22.5, 19.3, 13.3, 3.9, -0.8]
plt.title("2019 Tokyo Avg Temperature")
plt.xlabel('Month')
plt.ylabel('Temperature Avg')
plt.plot(month, temperature_avg, label='Tokyo')
plt.plot(month, temperature_avg_s, label='Sapporo')
plt.legend(loc='upper left')
plt.show()

"""
2つのグラフを表示させたい場合は、plot()を2回呼び出し、
縦軸のみ別々のデータを入れる必要があります。
また、今回は左上に凡例を追加しました。
plot()の引数labelに各グラフの凡例の名前を指定し、
legend()で実際に凡例を作成しています。
legend()の第一引数には凡例をどこに作るかのロケーションを設定しています。
"""


print("--- 棒グラフの作成とラベルの付与 ---")


"""
次は棒グラフを作成してみましょう。棒グラフはbar()を使って作成します。
"""

# import matplotlib.pyplot as plt

subjects = ["Japanese", "Math", "Science", "Social", "English"]
score_avg = [61.2, 59.9, 72.4, 51.3, 77.6]
plt.xlabel('Subjects')
plt.ylabel('Score Avg')
x = [0, 1, 2, 3, 4]
plt.bar(x, score_avg, tick_label=subjects)
plt.show()

"""
棒グラフを使って、各教科の平均点を可視化しました。
bar()の第一引数は横軸の数値の配列です。
今回はtick_labelに横軸のラベルを指定しましたが、
指定しない場合は第一引数の配列の値がラベルになります。
第二引数は縦軸の数値です。これで棒グラフの高さが決まります。
次のtick_labelは横軸のラベルを指定しています。
"""


print("--- 散布図を作成する ---")


"""
今度は散布図を描画してみましょう。
"""

# import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.show()

"""
今回はnumpyのrandomモジュールからランダムな数値の配列を、
x軸とy軸でそれぞれ100個ずつ作っています。
ちなみに、np.random.rand()はnp.rondom.random()と同じですが、
それらを散布図を描画するscatter()に渡し、show()で表示しています。
"""


print("--- タイトル、マーカー、線の太さまで設定できる ---")


"""
以上、今回はmatplotlibを使っていくつかのパターングラフの描き方を解説しました。
グラフだけでなく凡例やラベルの付け方も紹介しましたが、matplotlibでは他にもグラフタイトル、
マーカー（各数値に付く●印）、グラフの線の太さまで自在に変えることができ、
PowerPoint並みに表示をカスタマイズすることが可能です。
Pythonはデータの出力や加工が多いプログラミング言語です。matplotlibを使いこなして、
是非理想のデータ表示を実現してください！
"""
