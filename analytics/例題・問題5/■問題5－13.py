# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－13
２つの整数a,bをキーボードから入力し，
 縦がa文字，横がb文字の∗*∗で出来た四角を描くプログラムを作りなさい．
たとえば，a=2,b=5なら，

*****
*****

と表示される．

参考　Python3練習問題01　練習14 棒グラフ　より
"""


a = int(input("数値を入力して下さい。(一回目):"))
b = int(input("数値を入力して下さい。(二回目):"))

for i in range(0, a):
    for j in range(0, b):
        print('■', end='')
    print()
