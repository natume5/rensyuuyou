# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題４－２
もう少し難しい条件を判定しよう． if の後ろの式が成り立たない（偽: False）
のときに実行されるのが else: のブロックである．

if 条件文 :
    条件文が成立する(真：True)のときに実行される文のブロック
else:
    条件文が成立しない(偽: False)のときに実行される文のブロック

キーボードから入力した数に 250002500025000 を足したものが，
3500∗9 と等しいかどうかを判定するプログラムを作りたい．

それには，以下の順で命令を実行する．

1.　変数xに数値を入力する．

2.　ifで x+25000と 3500∗9が等しいかどうか判定する．

3.　等しいならOKを，そうでなければBooを表示する．

条件式では，等号に == を使う．

x = int(input("Please enter an integer:"))
if x+25000 == 3500*9 :    # 3500*9=31500,6500+25000=31500
    print("OK")
else:
    print ("Boo")

Boo
"""

X = 0


while True:
    try:
        A = int(float(input("整数を入力して下さい。3500×9と等しい数を25000と足して作ってください。:")))
        X = X + 1
        if (A + 25000) == (3500 * 9.0):
            print("OK")
        if X == 5:
            print("終了します。")
            break
    except ValueError:
        print("もう一度やり直してください。")
    except KeyboardInterrupt:
        print("終了します。")
        break
else:
    print("Boo!")
