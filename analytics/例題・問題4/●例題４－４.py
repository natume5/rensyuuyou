# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題４－４
入力した整数が負か100以上なら"範囲外"と出力し，
それ以外なら"OK"と出力するプログラムを作成せよ．

x =int( input("数を入力してください "))
if x < 0 or x >= 100:
    print("範囲外")
else:
    print("OK")


範囲外
"""


x = int(input("数を入力してください "))
if x < 0 or x >= 100:
    print("範囲外です。")
else:
    print("OK!")
