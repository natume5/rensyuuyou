# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題５－１
（１）「入力した数を表示する」という作業を，3回繰り返すプログラムを作れ．

（２）「入力した2つの整数の和を表示する」という作業を，3回繰り返すプログラムを作れ．

（３）「入力した定価の税込価格（消費税は8%で半端は切り捨てとする）を表示する」
という作業を3回繰り返すプログラムを作成せよ．

（４）０を入力したら，次の反復に移らず，終了するプログラムにせよ．

（５）負の数を入力したら，次の反復に移らず，終了するプログラムにせよ．
"""


# (1)入力した数を表示する」という作業を，3回繰り返すプログラムを作れ．


print("入力した数を3回表示します。")


for i in range(3):
    x = int(input("数値を入力して下さい。:"))
    print(x)
