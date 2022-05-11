# 3問目と同じバブルソート

"""バブルソートのアルゴリズム

単純に隣り合った要素を比較交換しながら、
小さい(あるいは大きい)値を手前の方に持ってきます。
比較も交換も多くて時間がかかります。入れ子になっているループの走査範囲を
きっちり無駄なくしておく必要があります。"""


# !/usr/bin/env python
# -*- coding: utf-8 -*-


# バブルソート
def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if array[j] < array[j - 1]:
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp

# デバッグ
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 0]
    print("befor", array)
    bubble_sort(array)
    print("after", array)
