# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""

参考　Qiita　pythonで九九表を表示する方法　より
"""


def multiplicationTable():
    for a in range(1, 10):
        for b in range(1, 10):
            ans = str(a * b)
            result = ans.rjust(4)
            print(result, end=" ")
        print('')


if __name__ == "__main__":
    multiplicationTable()

# rjsutメソッドでインデントを揃えています。
