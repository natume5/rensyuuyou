#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　文字列操作の基本---")


"""
基本操作(strメソッド)
文字列の結合

すでに何度か出てきていますが、Pythonの文字列は+で結合することができます。
続けて複数使用することができます。以下のコードでは3つの文字列を+で結合しています。
"""

text1 = 'aaa'
text2 = 'iii'
text3 = 'tohaaa'

text = text1 + text2 + text3
print(text)

"""
また、数値などとは直接結合できずTypeErrorが発生するため組込みのstr関数を使用します。
"""

label = 'pi='
val = 3.14
text = label + str(val)    # strで文字に変換する
print(text)


"""
文字列リストの連結

リストに格納された文字列を特定の文字列で連結する場合、joinメソッドを使用します。
join
結合文字.join(リスト)

例えば、文字列リストをカンマ区切りの文字列に変換したい場合は以下のようにします。
"""

data = ['aaaaa', 'bul', 'cat', 'ddt', 'eeee!']
csv = ','.join(data)
print(csv)    # aaaaa,bul,cat,ddt,eeee!


"""
文字列の分割

区切り文字で分割したい場合はsplitメソッドを使用します。
引数で区切り文字を指定します。戻り値に分割された文字列のリストが返されます。
以下のサンプルではスペースを区切り文字とした文字列を分割してリストを得ています。
"""

data = "aaa bbb ccc ddt eee!"
data_list = data.split(' ')
print(data_list)    # ['aaa', 'bbb', 'ccc', 'ddt', 'eee!']


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

print(text)    # xxxbbbccc(変更されない)
print(new_text)    # aaabbbccc


"""
シーケンスとしての操作

Pythonの文字列はシーケンスです。したがって、
リスト等で利用できたインデックスの指定等が文字列でも同様に利用することができます。


N番目の文字の取得

N番目の文字を取得する場合は最初の文字を0番目としたインデックスを指定します。
例えば、先頭、3番目、最後の文字を取得する場合、以下のようにします。
"""

text = 'abcdefghijklmn'

print(text[0])    # a 先頭(0番目)
print(text[3])    # d 3番目
print(text[-1])    # n 末尾


"""
部分文字列の取得

スライスを使用することで部分文字列を取得することができます。
"""

text = 'abcdefghijklmn'
print(text[0:3])    # abc


"""
文字列が含まれるかどうかを判定する

inを使用することで文字列の包含を判定することができます。
以下のサンプルでは、文字列型の変数textに文字列cdeが含まれるかどうかを判定しています。
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


"""
文字列の検索

findメソッドを使用すると、文字列内を検索することができます。
対象文字列が見つかれば最初の文字列インデックスを返します。
ない場合は-1を返します。末尾から検索したい場合はrfindを使用します。
以下のサンプルでは文字列「bc」が含まれる場所を検索しています。
"""

text = 'abcabcdcfhytrdxfcse'

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
(スペース・タブ文字・改行(\r, \n))を除去する場合はstripメソッドを使用します。
また、前か後ろだけ除去する場合はそれぞれlstrip, rstripを使用します。
"""

text = ' abcabc '
print(text.strip())    # abcabc
print(text.lstrip())    # abcabc 左側だけstrip
print(text.rstrip())    #  abcabc 右側だけstrip


"""
大文字/小文字変換

文字列を大文字、小文字に変換する場合はそれぞれupperメソッド、lowerメソッドを使用します。
また、先頭だけ大文字にする場合は、capitalizeメソッドを使用します。
いずれも戻り値に新たな文字列が返されます。
"""

text = 'abcDEFG'

print(text.upper())    # ABCDEFG
print(text.lower())    # abcdefg
print(text.capitalize())    # Abcdefg



print("--- Python入門　文字列の判定系メソッド---")


"""
判定メソッド

Pythonの文字列には以下のような文字列の種別の判定用メソッドが用意されています。
1文字以上でなおかつすべての文字が条件を満たしている場合、Trueが返されます。

    isalnum：英字or数字
    isalpha：英字
    isascii：ASCII文字
    isdigit：ASCII文字の数字
    isdecimal：10進数の数字
    isnumeric：数を表す文字
    islower：子文字
    isupper：大文字

isalnumとisalpha

ただし、注意が必要なのがisalnumとisalphaです。
ここで記述されている英字とは「Unicode 文字データベースで "Letter" として定義されているもの」
であるため、いわゆる全角文字等でも英字として扱われています。
このため、純粋な英字であるかどうかの判別はisasciiと合わせて使用するなどの工夫が必要となります。
以下のサンプルはisalnum、isalphaの使用して挙動を比較しています。
"""

# 半角英数字
print("la".isalnum())    # True
print("la".isalpha())    # True

# 半角英字
print("a".isalnum())    # True
print("a".isalpha())    # True

# 半角記号
print("!".isalnum())    # False
print("!".isalpha())    # False

# 全角
print("あ".isalnum())    # True
print("あ".isalpha())    # True


"""
isdigit/isdecimal/isnumeric

また、数字文字の判定としてisdecimal()、isdigit()、isnumeric()の
3つの数値判定メソッドが用意されていますが、取り扱う文字に依っては微妙に挙動が異なります。
小数点を含む文字はいずれも数値として判定されないため、注意が必要です。
また符号付きの場合も数値とは判定されません。このため、数値への変換可否に使用することはおすすめしません。

以下のサンプルはisdigit、isdecimal、isnumericを使用して挙動を比較しています。
"""

# 半角数字
print("1".isdigit())    # True
print("1".isdecimal())    # True
print("1".isnumeric())    # True

# 半角数値(符号付き)
print("0.01".isdigit())    # False
print("0.01".isdecimal())    # False
print("0.01".isnumeric())    # False

# 半角数値(小数)
print("0.01".isdigit())    # False
print("0.01".isdecimal())    # False
print("0.01".isnumeric())    # False

# U+0660を含む場合
print("0.01".isdigit())    # False
print("0.01".isdecimal())    # False
print("0.01".isnumeric())    # False

# 全角数字
print("1".isdigit())    # True
print("1".isdecimal())    # True
print("1".isnumeric())    # True

# 全角漢数字
print("百".isdigit())    # False
print("百".isdecimal())    # False
print("百".isnumeric())    # True

# 全角ローマ数字
print("Ⅳ".isdigit())    # False
print("Ⅳ".isdecimal())    # False
print("Ⅳ".isnumeric())    # True


"""

"""









