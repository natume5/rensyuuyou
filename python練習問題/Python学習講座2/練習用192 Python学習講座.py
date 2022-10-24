#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 文字列操作の基本 ---")


print("--- 基本操作(strメソッド) ---")


"""
文字列の結合

すでに何度か出てきていますが、Pythonの文字列は+で結合することができます。
続けて複数使用することができます。
以下のコードでは3つの文字列を+で結合しています。
"""

text1 = 'aaa'
text2 = 'bbb'
text3 = 'ccc'

text = text1 + text2 + text3    # +で文字列結合
print(text)    # aaabbbccc

"""
また、数値などとは直接結合できずTypeErrorが発生するため
組込みのstr関数を使用します。
"""

label = 'pi='
val = 3.14
text = label + str(val)    # strで文字列に変換する
print(text)    # pi=3.14

"""
文字列リストの連結

リストに格納された文字列を特定の文字列で連結する場合、
joinメソッドを使用します。

join
結合文字.join(リスト)

例えば、文字列リストをカンマ区切りの文字列に変換したい場合は
以下のようにします。
"""

data = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
csv = ','.join(data)
print(csv)    # aaa,bbb,ccc,ddd,eee

"""
文字列の分割

区切り文字で分割したい場合はsplitメソッドを使用します。
引数で区切り文字を指定します。
戻り値に分割された文字列のリストが返されます。
以下のサンプルではスペースを区切り文字とした
文字列を分割してリストを得ています。
"""

data = 'aaa bbb ccc ddd eee'
data_list = data.split(' ')
print(data_list)    # ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

"""
文字列の置換

文字列を置換する場合は、replaceメソッドを使用します。

文字列置換
元の文字列.replace(置換前, 置換後)

元の文字列はそのままで、新たに作成された文字列が戻り値で返されます。
以下のサンプルでは文字列を格納した変数textに対し、xをaに置換しています。
"""

text = 'xxxbbbccc'
new_text = text.replace('x', 'a')    # 置換して新たな文字列を取得する

print(text)    # xxxbbbccc (変更されない)
print(new_text)    # aaabbbccc

"""
シーケンスとしての操作

Pythonの文字列はシーケンスです。
したがって、リスト等で利用できたインデックスの指定等が
文字列でも同様に利用することができます。

N番目の文字の取得

N番目の文字を取得する場合は最初の文字を
0番目としたインデックスを指定します。
例えば、先頭、3番目、最後の文字を取得する場合、以下のようにします。
"""

text = 'abcdefghijklmn'

print(text[0])    # 先頭(0番目) a
print(text[2])    # 3番目 c
print(text[-1])    # 末尾 n

"""
部分文字列の取得

スライスを使用することで部分文字列を取得することができます。
"""

text = 'abcdefghijklmn'
print(text[0:3])    # abc

"""
文字列が含まれるかどうかを判定する

inを使用することで文字列の包含を判定することができます。
以下のサンプルでは、文字列型の変数textに
文字列cdeが含まれるかどうかを判定しています。
"""

text = 'abcdefg'
print('cde' in text)    # True

"""
ループ(１文字ずつ処理)

シーケンスなので、ループで一文字ずつ処理をすることもできます。
以下のサンプルでは文字列型の変数の内容を1文字ずつprintで出力しています。
"""

text = 'abcdefghijklmn'
for s in text:
	print(s)
# a
# b
# c
# d
# e
# f
# g
# h
# i
# j
# k
# l
# m
# n

"""
文字列の検索

findメソッドを使用すると、文字列内を検索することができます。
対象文字列が見つかれば最初の文字列インデックスを返します。
ない場合は-1を返します。末尾から検索したい場合はrfindを使用します。
以下のサンプルでは文字列「bc」が含まれる場所を検索しています。
"""

text = 'abcabc'

print(text.find('bc'))    # 1
print(text.rfind('bc'))    # 4

"""
また、countを使用するといくつ含まれているかを取得することができます。
"""

text = 'abcdabcd'
print(text.count('bc'))    # 2

"""
文字列のトリミング

文字列のトリミング、つまり前後にある不要な空白
(スペース・タブ文字・改行(\r, \n))を除去する場合は
stripメソッドを使用します。
また、前か後ろだけ除去する場合はそれぞれlstrip, rstripを使用します。
"""

text = ' abcabc '
print(text.strip())    # abcabc
print(text.lstrip())    # abcabc
print(text.rstrip())    #  abcabc

"""
大文字/小文字変換

文字列を大文字、小文字に変換する場合はそれぞれ
upperメソッド、lowerメソッドを使用します。
また、先頭だけ大文字にする場合は、capitalizeメソッドを使用します。
いずれも戻り値に新たな文字列が返されます。
"""

text = 'abcDEFG'

print(text.upper())    # ABCDEFG
print(text.lower())    # abcdefg
print(text.capitalize())    # Abcdefg
