# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題２－２
例題２－３のサンプルコードを用いて，
(1) 各行の式に出てくる10や20などの数値を，自分の好きな数，例えば30や5に変更し，
実行結果がどう変わるか調べよ．

(2) 4行目と5行目を入れ替えると，実行結果がどう代わるか，予測せよ．
また，7行目と8行目を入れ替えるとどのようになるかも予測せよ 予測したら，
実際に入れ替えて実行し，予測があっているか確認せよ．

100 100
30 20
20 -10
"""

# (1)
x = 10.09
y = 34 - x
print("x = 10.09, y = 34 - x ", " x = {}, y = {}".format(x, y))

x = y + 68.073
y = 18
print("x = y + 68.073, y = 18 ", " x = {}, y = {}".format(x, y))

x = x - 81
y = y - x * 2
print("x = x - 81, y = y - x * 2 ", " x = {}, y = {}".format(x, y))
