# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－１
（1）　入力した数が0ならzeroと表示するプログラムを作れ．

（2）　入力した数が100以上ならOKと表示するプログラムを作れ．

（3）　入力した数が0以上ならpositive，そうでなければnegativeと表示するプログラムを作れ．

（4）　入力した2つの数が等しいならequalと表示するプログラムを作れ．

"""


# (1)入力した数が0ならzeroと表示するプログラムを作れ．

X = int(input("数を入力してください "))
if X == 0:
    print("ZERO")
else:
    None


# (2)入力した数が100以上ならOKと表示するプログラムを作れ．

X = int(float(input("数を入力してください ")))
if X > 100:
    print("OK!")
else:
    None


# (3)入力した数が0以上ならpositive,そうでなければnegativeと表示するプログラムを作れ

X = int(float(input("数を入力してください ")))
if X > 0:
    print("positive")
else:
    print("negative")


# (4)入力した2つの数が等しいならequalと表示するプログラムを作れ

X = int(float(input("数を2回入力してください、2つの数が等しいならequalと表示します。")))
Y = int(float(input("数を入力してください(2回目)")))
if X == Y:
    print("equal")
else:
    None
