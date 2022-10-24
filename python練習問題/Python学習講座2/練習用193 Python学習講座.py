#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 文字列の判定系メソッド ---")


print("--- 判定メソッド ---")


"""
Pythonの文字列には以下のような文字列の種別の
判定用メソッドが用意されています。
1文字以上でなおかつすべての文字が条件を満たしている場合、
Trueが返されます。

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
ここで記述されている英字とは
「Unicode 文字データベースで "Letter" として定義されているもの」であるため、
いわゆる全角文字等でも英字として扱われています。
このため、純粋な英字であるかどうかの判別は
isasciiと合わせて使用するなどの工夫が必要となります。
以下のサンプルはisalnum、isalphaの使用して挙動を比較しています。
"""

# 半角英数字
print('1a'.isalnum())    # True
print('1a'.isalpha())    # False

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

また、数字文字の判定としてisdecimal()、isdigit()、isnumeric()
の3つの数値判定メソッドが用意されていますが、
取り扱う文字に依っては微妙に挙動が異なります。
小数点を含む文字はいずれも数値として判定されないため、注意が必要です。
また符号付きの場合も数値とは判定されません。
このため、数値への変換可否に使用することはおすすめしません。
以下のサンプルはisdigit、isdecimal、isnumeric
を使用して挙動を比較しています。
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
print("0٠01".isdigit()) # True 
print("0٠01".isdecimal()) # True 
print("0٠01".isnumeric()) # True 

# 全角数字
print("１".isdigit())    # True
print("１".isdecimal())    # True
print("１".isnumeric())    # True

# 全角漢数字
print("百".isdigit())    # False
print("百".isdecimal())    # False
print("百".isnumeric())    # True

# 全角ローマ数字
print("Ⅳ".isdigit())    # False
print("Ⅳ".isdecimal())    # False 
print("Ⅳ".isnumeric())    # True


print("--- 補足 文字列の数字変換可否の判定 ---")


"""
文字列を整数に変換する場合は組込みのint関数を、
小数に変換する場合は組込みのfloat関数を使用します。
"""

# 整数
integer_str = '100'
integer_num = int(integer_str)
print(integer_num)    # 100

# 小数
decimal_str = '1.55'
decimal_num = float(decimal_str)
print(decimal_num)    # 1.55

"""
数値に変換できない不正な文字列の場合はValueErrorが送出されます。
前述のとおり、符号や小数点ではstrに実装されているメソッドでは判別できません。
自前で正規表現を使用しても良いのですが、
厳密には符号と小数点以外に指数表記等も考慮する必要があります。
ですが、まず変換処理を行い変換に失敗すればValueErrorが起きるため、
これを利用すれば符号付きや指数表記にも
対応して判定と変換を行うことができます。
"""

def is_float_str(num_str, default=0):
    try:
        return {'is_float': True, 'val': float(num_str)}
    except ValueError:
        return {'is_float': False, 'val': default}

print(is_float_str('-1.5'))
# {'is_float': True, 'val': -1.5}

print(is_float_str('1E16'))
# {'is_float': True, 'val': 1e+16}

print(is_float_str('1.5x'))
# {'is_float': False, 'val': 0}

"""
上のサンプルでは文字列に対し、数値への変換可否と変換に成功した場合は
その値を返しています。
また、defaultを指定することで
変換に失敗した場合のデフォルト値を設定することができます。
"""
