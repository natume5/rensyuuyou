# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－12（for，whileの使い分け）
２つの整数aとbをキーボードから入力させ，
a以上b以下の整数をすべて表示させるプログラムを作れ

（１） for文を使って作れ（whileは使わない）

（２） while文を使って作れ（forは使わない）
"""

# （１） for文を使って作れ（whileは使わない）

print("for文の場合")
val_1 = int(input(
                  "数値を入力して下さい。1回目に入力した数値と2回目の数値の間にある数値を表示します。 1回目:"))
val_2 = int(input("数値を入力して下さい。 2回目:"))

for i in range(val_1, val_2):
    print(i)


# （２） while文を使って作れ（forは使わない）

print("while文の場合")
val_1 = int(input(
                  "数値を入力して下さい。1回目に入力した数値と2回目の数値の間にある数値を表示します。 1回目:"))
val_2 = int(input("数値を入力して下さい。 2回目:"))


while True:
    if (val_1 < val_2):
        print(val_1)
        val_1 = val_1 + 1
    elif (val_2 < val_1):
        print(val_2)
        val_2 = val_2 + 1
