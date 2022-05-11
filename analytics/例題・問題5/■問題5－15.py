# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題５－１５
3×3×3のかけ算の表を表示するプログラムを作れ．
1×1×1，1×1×2，1×1×3，1×2×1，．．．の順で表示するようにせよ．

参考　　より
"""


def multiplicationTable():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                print('{}*{}*{}={} '.format(a, b, c, a * b * c), end=" ")
                ans = str(a * b * c)
                result = ans.rjust(4)
                print(result, end=" ")
            print('')


if __name__ == "__main__":
    multiplicationTable()

# rjsutメソッドでインデントを揃えています。
