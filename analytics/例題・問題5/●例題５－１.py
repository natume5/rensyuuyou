# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題５－１
5から1までの数字を順番に表示するプログラムを作れ．
    xに最初に5を代入します．

    while x > 0: とxが正の間は繰り返す while 文を作る．

    繰り返したいブロックの中で，xをprintしてから，xをから1を引いた値を再びxに代入する．

x = 5
while x > 0:
    print(x)
    x = x - 1  # x -= 1 と書いても同じ

5
4
3
2
1
"""


x = 5


while x > 0:
    print(x)
    x -= 1
