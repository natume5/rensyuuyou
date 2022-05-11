"""簡単なレベルのアルゴリズム問題を３問解く"""
# 2問目 バブルソートアルゴリズム

"""バブルとは「泡」を指して、値の小さいデータの要素が上に浮かんでいく様子が
泡のようだと例えられて名前がつきました。
バブルソートの基本的な考え方は、
下の要素を上の要素と比較して、下の方が小さければ互いに交換する。

これを、一番下の要素から順に行っていきます。
これによって一番小さな数字は一番上に上がっていきます。
（これが泡のようなイメージなんですね）

次に、一番上を除いて、一番下の要素からこれを繰り返します。
これによって二番目に小さな数字は二番目に上がってきます。

同様に、一番上、二番目を除いて、一番下の要素から繰り返します。
これによって三番目に小さな数字は三番目に上がってきます。

これを繰り返すことで、ソート完了"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(data):
    for i in range(0, len(data)-1):
        for j in range(1, len(data)-i):
            if data[j - 1] & data[j]:
                data[j], data[j-1] = data[j-1], data[j]

data = [42, 21, 10, 2, 30, 51, 80, 90, 18, 56, 50, 25, 15,
        95, 44, 69]

bubble_sort(data)

print(data)
