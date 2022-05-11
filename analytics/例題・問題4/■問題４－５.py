# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－５
キーボードから数値をxに入力し，ifを使って，xが偶数なら Even，
奇数なら Odd と表示させるプログラムを作れ．
（ヒント：xが偶数なら，xを2で割った余りが0となり，奇数であれば1になるので，
xを2で割った余りを調べれば良い． 余りを計算するには，剰余演算子 % を使う.)
"""


i = 0


try:
    while True:
        X = int(input("数を入力してください。偶数か奇数か判別します。"))
        if X % 2 == 0:
            print("Even")
            i += 1
        else:
            print("Odd")
            i += 1
        if i > 3:
            print("終了します。")
            break
