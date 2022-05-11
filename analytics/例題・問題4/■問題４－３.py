# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－３
キーボードから2つの数 x と y を入力し，y が x 以下なら x−y を表示し，
 y が x より大きければ '負になります' と表示するプログラムを作れ．
"""


counter = 0

try:
    while True:
        X = int(float(input("数を2回入力してください。1回目の数から2回目の数を引きます。")))
        Y = int(float(input("数を入力してください(2回目)")))
        if Y > X:
            print("負になります。")
            break
        elif Y < X:
            print(X - Y)
            break
        else:
            print("数を入れ直してください。")
            counter += 1
            if counter >= 2:
                print("終了します。")
                break
except KeyboardInterrupt:
    print('終了します。')
