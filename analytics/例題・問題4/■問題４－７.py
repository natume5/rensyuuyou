# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－７
文字で作った絵を2つ作ってみよう．
そして，キーボードから入力した数が10 以上20 以下なら1つ目の絵を，
50以上60以下なら2つ目の絵を表示するプログラムを作れ
"""


wrong1 = 0
stage1 = ["^_^"]
stage2 = ["*o*"]


try:
    while True:
        X = int(float(input("数値を入力してください。ある数を入力すると絵が表示されます。")))
        if 10 < X < 20:
            print(stage1)
        elif 50 < X < 60:
            print(stage2)
        else:
            wrong1 += 1
        if wrong1 >= 3:
            print("終了です。")
            break

except KeyboardInterrupt:
    print('終了します。')
except BaseException as e:
    print(e, "終了します。")
    print(type(e))
