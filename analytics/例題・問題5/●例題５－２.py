# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題５－２
while の中で break文を入れると，whileの反復（ループ）から出ることができる．
10から1までの数字の2乗を順に出力するプログラムを作成せよ．
    xに最初に10を代入しておく．

    while の後に True（もしくは1）と常に真になる式を入れて whileループを作ります．
    繰り返しブロックの中でxの2乗を出力してから，１を引く．

    その後に，if文を入れて，xが0以下になったら breakするようにする．

x = 10
while True:
    print(x**2)
    x = x-1
    if x <= 0:
        break

100
81
64
49
36
25
16
9
4
1
"""


x = 10


while 1:
    print(x ** 2)
    x -= 1
    if x <= 0:
        break
