# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－８
キーボードから数を入力し，その数が正ならその数を表示．
そうでなければ，もうひとつ数を入力し，最初の数との積を表示するプログラムを作れ．

表示結果例

x = -3
y = 2
product = -6
"""


Y = 0


try:
    while True:
        X = int(
                float(input(
                            "数値を入力してください。"
                            "入力した数が正の値でない時は、"
                            "もう一度入力して最初の数との積を表示します。")))
        if X > 0:
            print("正の値です。")
        elif X < 0:
            print("負の値だったのでもう一度入力して下さい。")
            Y = int(
                float(input(
                            "数値を入力してください。"
                            "入力した数が正の値でない時は、"
                            "もう一度入力して最初の数との積を表示します。")))
            print(X * Y, "でした。")
        if X or Y >= 3:
            print("終了です。")
            break

except KeyboardInterrupt:
    print('終了します。')
except BaseException as e:
    print(e, "終了します。")
    print(type(e))
