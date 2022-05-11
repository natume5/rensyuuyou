# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題４－６
キーボードから入力した数が10以上20以下であればOKと表示するプログラムを作れ
"""
i = 0


try:
    while True:
        X = int(float(input("数を入力してください。10以上20以下であればOKの表示が出ます。")))
        if 20 >= X >= 10:
            print("OK")
            i += 1
        elif i > 3:
            break
        else:
            print("もう一度入力し直してください。")
            X = int(float(input("数を入力してください。10以上20以下であればOKの表示が出ます。")))
            i + 1
except KeyboardInterrupt:
    print('終了します。')
except BaseException as e:
    print(e, "終了します。")
    print(type(e))
