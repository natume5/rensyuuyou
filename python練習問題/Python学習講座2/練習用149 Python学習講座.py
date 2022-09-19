#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- シーケンスの共通処理 ---")


print("--- シーケンスの共通処理 ---")


"""
リスト、タプル、文字列等、どのシーケンス型にも使用できる共通的の演算や関数があります。
すでに説明したものも含まれますが、復習も兼ねてまとめて整理してみましょう。
以下の演算や関数を使用することができます。

演算 	           説明
x in s 	            シーケンスsに要素xが含まれている場合にTrueを返します
x not in s 	        シーケンスsに要素xが含まれていない場合にTrueを返します
s + t 	            2つのシーケンスsとtを結合します。
s * n または n * s 	シーケンスs同士をn回結合します。
s[i] 	            0始まりのインデックスを指定してシーケンスsのi番目の要素を
                    取得します。
s[i:j] 	            シーケンスsのi番目からj番目までのスライスを返します。
s[i:j:k] 	        シーケンスsのi番目からj番目までのk毎のスライスを返します。
len(s) 	            シーケンスsの長さ(=要素数)を返します。
min(s) 	            シーケンスsの最小の要素を返します。
max(s) 	            シーケンスsの最大の要素を返します。
s.index(x) 	        シーケンスsの中で要素xが最初に出現する
                    インデックスを返します。
s.count(x) 	シーケンスsの中で要素xが出現する回数を返します。
"""


print("--- 共通処理の解説 ---")


"""
以下、よく使うものを中心に解説していきます。

包含判定(in、not in)

シーケンスsとオブジェクトxが要素に含まれているかどうかを判定するにはx in sと書きます。
また、含まれていないかどうかを判定するにはx not in xと書きます。
"""

list_data = ['a', 'b', 'c', 'd']

# 含まれているかどうかを判定する
b1 = 'a' in list_data
# 文字列'a'がリストに含まれているかどうかを判定
print(b1)    # True

b2 = 'x' in list_data
#  文字列'x'がリストに含まれているかどうかを判定
print(b2)    # False

b3 = 'a' not in list_data
# 文字列'a'がリストに含まれていないかどうかを判定
print(b3)    # False

b4 = 'x' not in list_data
# 文字列'x'がリストに含まれていないかどうかを判定
print(b4)    # True


"""
結合(+、*)

+演算子でシーケンス同士を結合することができます。
また、*演算子で指定回数分結合を繰り返すことができます。
"""

list_data1 = ['a', 'b', 'c']
list_data2 = ['d', 'e', 'f']

# リストの結合
new_list = list_data1 + list_data2
print(new_list)    # ['a', 'b', 'c', 'd', 'e', 'f']

new_list = list_data1 * 3
# list_data1 + list_data1 + list_data1と同じ
print(new_list)    # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

"""
スライス文

リスト型のスライス文は既に説明しましたが、
文字列もシーケンス型なので同様の操作が可能です。
文字列でのスライス文を見てみましょう。
"""

text = "ABCDEFG"

# 0番目から2番目の手前まで
print(text[0:2])    # AB

# 開始インデックスの省略
print(text[:2])    # AB

# 2番目から最後まで
print(text[2:7])    # CDEFG

# 最後を省略
print(text[2:])    # CDEFG

# 1つ飛ばしで
print(text[0:7:2])    # ACEG

"""
リストの時と同様にスライスが使用できます。


要素数

len関数で要素数を確認することができます。
リスト、タプル、文字列で確認してみましょう。
"""

# リストの場合
l = [1, 2, 3]
print(len(l))    # 3

# タプルの場合
t = ('a', 'b', 'c', 'd')
print(len(t))    # 4

# 文字列の場合
text = "abcdefg"
print(len(text))    # 7

"""
最初に出現するインデックス

indexメソッドで指定した要素が何番目のインデックスに存在するのか、
出現する最初のインデックスを取得することができます。
なお、見つからない場合はValueErrorが発生します。
"""

l = ['a', 'b', 'c', 'd']

print(l.index('c'))    # 2

"""
print(l.index('x')) # ValueError: 'x' is not in list

以下、文字列の場合です。
含まれる文字のインデックスを取得することができます。
部分文字列を指定することも可能です。
"""

text = "abcdefg"

print(text.index('b'))    # 1
print(text.index('ef'))    # 4

"""
print(text.index('x')) # ValueError: substring not found

出現する回数

countメソッドで出現する回数をカウントすることができます。
"""

text = "abcdefg abcdefg"

print(text.count('b'))    # 2
print(text.count('ef'))    # 2
print(text.count('x'))    # 0
