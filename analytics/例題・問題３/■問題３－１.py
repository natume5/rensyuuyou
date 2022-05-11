# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題３－１
inputが入力した数値を変数に代入している，
ということを，プログラムを作って確認せよ．
代入された変数の値を表示すれば確認できるので，
プログラムの基本的な構造は以下のようになる．

    input関数で変数xに整数を入力する．

    print関数で変数xの値を表示する．

（１）上の構造どおりのプログラムを作れ

（２）変数xの名前を自分の好きな名前に変えてみよ．

（３）数値を入力して表示する，という作業を2回するように変更せよ．

（４）入力する前に Integer = ?と表示するようにせよ．

（５）小数（正確には浮動小数点数）を入力し，それを表示させるように変えよ．
(文字列を浮動小数点数に変換するにはfloat()関数を用いる．）
"""

# (1)上の構造どおりのプログラムを作れ
x = input("文字を入力して下さい。10回繰返します。")
print(x * 10)


# (2)変数xの名前を自分の好きな名前に変えてみよ．
Hage = input("文字を入力して下さい。:")
print(Hage * 10)


# (3)数値を入力して表示する，という作業を2回するように変更せよ．
X = int(input("数値を入力して下さい。:"))
Y = int(input("もう一度数値を入力して下さい。:"))
print("{}と{}を掛けた数は".format(X, Y))
print((X * Y), "です。")


# (4)入力する前に Integer = ?と表示するようにせよ．
Z = int(input("Integer = ?:"))
print(Z, "は整数です。")


# （５）小数（正確には浮動小数点数）を入力し，それを表示させるように変えよ．
# (文字列を浮動小数点数に変換するにはfloat()関数を用いる．）
F = int(float(input("浮動小数点まで数値を入力して下さい。:")))
