#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- set型と集合演算 ---")


"""
setのメリットは何でしょうか？
set型はリストと比較して順序を保てないというデメリットを感じますが、
要素がユニークであるため集合演算を行うことができるという特徴があります。
このページではset型の集合演算について学びます。
"""


print("--- setの集合演算 ---")


"""
それではset型の集合演算について見ていきましょう。
基本となるUnion、Intersection、
Differenceと包含関係の判定について説明します。

Union(和集合)
2つの集合の和を取ります。
setオブジェクトがもつunionメソッドを利用します。
戻り値にunionした新たなsetが返されます。
もとのsetには変更ありません。

union
setオブジェクト1.union(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.union(s2)    # s1とs2をunionする
print(s)    # {'D', 'C', 'E', 'A', 'B'}
print(s1)    # {'A', 'B', 'C'}


"""
Intersection(積集合)
2つの集合の積、つまり共通要素を取り出します。
setオブジェクトがもつintersectionメソッドを利用します。

intersection
setオブジェクト1.intersection(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.intersection(s2)
print(s)    # {'C'}


"""
Difference(差集合)
2つの集合の差、つまり元の集合に存在し、
比較対象の集合に存在しない要素を取得します。
setオブジェクトがもつdifferenceメソッドを利用します。

difference
setオブジェクト1.difference(setオブジェクト2)

uniot、intersectionと異なり、演算順序で違いがあるので注意してください。
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

# s1 - s2
s = s1.difference(s2)
print(s)    # {'B', 'A'}

# s2 - s1
s = s2.difference(s1)
print(s)    # {'E', 'D'}

"""
以下の計算となり、演算順序で違いが出ていることが確認できます。注意してください。
s1 - s2 = s1にあってs2にないもの = A, B
s2 - s1 = s2にあってs1にないもの = D, E


包含判定
ある集合が別の集合を含むかどうか、
または含まれるかどうかを判定するメソッドがsetオブジェクトに用意されています。

含まれているかどうかを判定
ある集合s1が別の集合s2に含まれている場合、
s1はs2のsubset(サブセット=部分集合)であるといいます。
setオブジェクトのissubsetメソッドを利用して判定することができます。

issubset
setオブジェクト1.issubset(setオブジェクト2)
"""

s1 = {'A', 'B'}
s2 = {'A', 'B', 'C'}
print(s1.issubset(s2))    # True

"""
s1はs2の部分集合なので、Trueが返されています。

含んでいるかどうかを判定
ある集合s1が別の集合s2に含まれている場合、
s1はs2のsuperset(スーパーセット)であるといいます。
スーパーセットを上位集合と訳すこともありますが、
和訳を見かけることは少ないですね。
少し話がそれましたが、
setオブジェクトのissupersetメソッドを利用して判定することができます。

issuperset
setオブジェクト1.issuperset(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'A', 'B'}
print(s1.issuperset(s2))    # True

"""
s2はs1の部分集合なので、Trueとなります。
"""
