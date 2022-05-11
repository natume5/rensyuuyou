# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題6－6 (continue）
breakを使うと反復から強制的に抜けることを上で学びました。
代わりに continue文を使うと、反復から抜けるのではなく、次の反復に移ることができます。
以下の例では、入力された数字をprintで出力しますが、
反復のカウンタが3のときだけprintしないようにしています。

for i in range(5):
    if i == 3 :
        continue
    print("入力値は",i)

入力値は 0
入力値は 1
入力値は 2
入力値は 4
"""


for i in range(5):
    if i == 3:
        continue
    print("入力値は", i)
