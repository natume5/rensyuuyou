# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題６－２
(1)　「入力した5個の数の最小」を表示するプログラムを作りなさい．
(2)　入力した5個の数の中で「10以下の数の中での最大」を表示するようなプログラムを作りなさい．
ただし，10以下の数は必ず1つは入力される，とみなして良いとします．
"""

# (1)
list = []


for num in range(5):
    y = int(input("数値を5回入力して下さい。:"))
    list.append(y)


print(min(list))


# (2)　入力した5個の数の中で「10以下の数の中での最大」を表示するようなプログラムを作りなさい．

list = []
A ＝ 10 > y


for num in range(5):
    list.append(int(input("数値を5回入力してください:")))
    list.append(y)



print(max(list))
