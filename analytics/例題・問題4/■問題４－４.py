# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
まず，文字で絵を3種類作れ （例えば '(>_<)'や '⌒▽⌒"'のような絵）．
そして，キーボードから数を入力し，その数が1なら1番目の絵を，2なら2番目の絵を，
3なら3番目の絵を表示するプログラムを作れ．
 それ以外の数が入力された場合は，何もしなくて良い．
"""
i = 0


try:
    while True:
        X = int(input("数を入力してください。ある数を入力すると絵文字が出ます。"))
        if X == 1:
            print(':__;')
            i += 1
        elif X == 2:
            print("^o^")
            i += 1
        elif X == 3:
            print(";_;")
            i += 1
        elif i == 3:
            print("終了します。")
            break
except BaseException as e:
    print(e, "終了します。")
    print(type(e))
else:
    pass
