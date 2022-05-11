"""円を表すCircleクラスを定義する。
そのクラスに面積を計算して返すメゾットareaを持たせる。
面積の計算には、pythonの組み込みモジュールmathのpi定数が使える。
次に、Circleオブジェクトを使ってareaメゾットを呼び出し、結果を出力させる。"""

import math


class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius * self.radius * math.pi
        # 半径×半径×3.14


circle = Circle(4)   # 円の直径を4cmにした
print(circle.area())
"""データの演算

    基本 : + - * % /
    切り捨て除算 ://
    べき乗 : **

x = 10

#割り算
 print (x/3)

# 除算
print (x //3)

# 余り
print (x % 3)

#べき乗
print (3 ** 2)

result
3.3333333333333335
3
1
9
"""
