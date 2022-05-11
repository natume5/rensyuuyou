# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題6－2 （最大値）
10個の数を入力して，その中で最大のものを表示する，というプログラムを作成する．
    最大値を表す補助変数 mmm を準備して，十分に小さな数を代入しておく．
    次にfor文による反復の中で，入力した数が mmm より大きいならば，
    その数を mmm に代入する．
    反復から抜けたときの mmm の値が最大値になる．

m = -9999
for i in range(10):
    j = int(input("Please enter an integer:"))
    if m < j:
        m = j
print(m)

10

参考　一覧
　　　
"""


m = -9999


for i in range(10):
    j = int(input("数を10回入力して下さい。最も大きい数を表示します。:"))
    if m < j:
        m = j
print(m)
