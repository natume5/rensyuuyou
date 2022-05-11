# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題6－5（break）
Pythonの機能を使うと、上と同じ問題をフラグを用いずに解くことができます。
Pythonでは、for文による反復の中で、break文を入れることによって、
反復を強制的に抜けることができます。
以下の例では、5があったら反復を抜けるようにしてあります。
また、for文を抜けた直後に、elseによるブロックを入れると、
breakで終了しなかったときだけ実行されます。
ここでは、「５がなかった」と表示するようにしてあります。

for i in range(5) :
    j = int(input("Please enter an integer:"))
    if j == 5 :
        print ("5があった")
        break
else:
    print("5がなかった")

5がなかった

参考　一覧
"""


for i in range(5):
    j = int(input("数を入力して下さい。5があるかカウントします:"))
    if j == 5:
        print("5がありました")
        break
else:
    print("5はありませんでした。")
