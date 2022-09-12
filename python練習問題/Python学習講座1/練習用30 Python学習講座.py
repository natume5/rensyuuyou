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
補足 文字列の数字変換可否の判定

文字列を整数に変換する場合は組込みのint関数を、
小数に変換する場合は組込みのfloat関数を使用します。
"""

# 整数
integer_str = "100"
integer_num = int(integer_str)
print(integer_num)

# 小数
decimal_str = '1.55'
decimal_num = float(decimal_str)
print(decimal_num)


"""
数値に変換できない不正な文字列の場合はValueErrorが送出されます。
前述のとおり、符号や小数点ではstrに実装されているメソッドでは判別できません。
自前で正規表現を使用しても良いのですが、
厳密には符号と小数点以外に指数表記等も考慮する必要があります。
ですが、まず変換処理を行い変換に失敗すればValueErrorが起きるため、
これを利用すれば符号付きや指数表記にも対応して判定と変換を行うことができます。
"""

def is_float_str(num_str, default=0):
	try:
		return {"is_float": True, "val": float(num_str)}
	except ValueError:
		return {"is_float": False, "val": default}

print(is_float_str('1.5x'))    # 変換に失敗{'is_float': False, 'val': 0}
print(is_float_str('-1.5'))    # 変換に成功{'is_float': True, 'val': -1.5}
print(is_float_str('1E16'))    # 変換に成功{'is_float': True, 'val': 1E+16}

"""
上のサンプルでは文字列に対し、数値への変換可否と変換に成功した場合はその値を返しています。
また、defaultを指定することで変換に失敗した場合のデフォルト値を設定することができます。
"""


print("--- Python入門　文字列への埋め込み---")


"""
文字列への変数埋め込み

Pythonで文字列に対して値を埋め込む方法はいくつかあるのですが、
このページでは以下3つの方法について解説します。

    f文字列
    formatメソッド
    printf 形式

f文字列

Python3.6以降、フォーマット済み文字列リテラルと呼ばれる記法が使用できます。
f文字列と呼ばれることもあります。リテラルの先頭にfを記述し、埋め込みたい変数を中括弧でくくります。
ただし、変数は予め定義する必要があります。
"""

item = 'apple'
text = f"There is an {item}."
print(text)    # There is an apple.


"""
formatメソッド

文字列のformatメソッドを使用すると中括弧で置換フィールドを設定することができます。
フィールドの設定方法は3つあり、中括弧単体、中括弧内に順序 or キーを指定する方法があります。
"""

item1 = 'apple'
item2 = 'banana'

# 中括弧単体
text1 = "There are {} and {}."
print(text1.format(item1, item2))

# 順序指定
text2 = "There are {0} and {1}."
print(text2.format(item1, item2))

# キー指定
text3 = "There are {item1} and {item2}."
print(text3.format(**{"item1": item1, "item2": item2}))

# いずれも以下の通り出力される
# There are apple and banana.


"""
printf形式

C言語のprintf形式と同様に%演算子に対しフォーマットすることができます。
順番にタプルで指定する方法と、辞書でキーを指定する方法があります。
ただし2021年現在、公式でも「よくある問題を引き起こす」といった記述があり、
上で紹介した2つの方法と比較して廃れつつある印象があります。
ただし、古いライブラリでは使用されているため知識として知っておくとコードを読み解く際に役に立つかと思います。

    printf-style String Formatting
    Note The formatting operations described here exhibit a variety of 
    quirks that lead to a number of common errors (such as failing to 
    display tuples and dictionaries correctly). Using the newer formatted 
    string literals, the str.format() interface, 
    or template strings may help avoid these errors. 
    Each of these alternatives provides their own trade-offs and benefits of 
    simplicity, flexibility, and/or extensibility. 


タプル

%sを列挙し、%演算子の後にタプルを指定します。
"""

text = "There are %s, %s and %s."
f_text = text % ("apple", "banana", "oranges",)
print(f_text)    # There are apple, banana and oranges.


"""
辞書

%とsの間に丸括弧でキーを挟むと、辞書を指定することができます。
以下のサンプルは、"first", "second", "third"がそれぞれキーになります。
複雑なフォーマットを指定する場合はこちらを使用したほうがよいでしょう。
"""

text = "There are %(first)s, %(second)s and %(third)s."

f_text = text % {'first': 'apple', 'second': 'bananas', 'third': 'oranges'}
print(f_text)    # There are apple, bananas and oranges


print("--- Python入門　モジュール---")


"""
外部モジュールのimport
外部モジュールのimport

これまで既に何度か登場しましたが、標準ライブラリなどのモジュールを使用する際はimport文を使用します。
例えば、標準ライブラリのmathモジュールを使用する場合、以下のようにimportします。
"""

import math

print(math.pi)    # 3.141592653589793

"""
mathモジュールの一部、例えば円周率の定数piだけ使用したい場合はfrom文と合わせて
以下のように記述することもできます。
また、この場合はmath.を書かずに使用することができます。
"""

from math import pi

print(pi)


"""
asによる別名

さらに、importしたモジュールが長い場合、asで別名を付けることができます。
例えばnumpyという数値計算モジュールでランダムな点を生成する場合、以下のように記述します。
"""

import numpy

x = numpy.random.rand(50)
y = numpy.random.rand(50)

print(x, y)
"""
モジュールを利用するたびにnumpyと書かなければなりませんが、
これにasで以下のように短い名前をつけることができます。
"""

import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

print(x, y)



"""
モジュールと同名のクラス

Pythonのモジュールimportで初学者が少し混乱するのが
モジュール名と同じ名前のクラスや関数がある場合です。
たとえば、標準ライブラリのdatetimeモジュールにはdatetimeという型が存在します。
利用する場合、以下のようにimportします。
"""

import datetime
# datetimeモジュールのdatetimeをインポート

dt_obj = datetime.datetime(2017, 12, 22)    # datetime型のオブジェクトを生成する

"""
また、fromを使うと以下のように書き換えることができます。
"""

from datetime import datetime
#  datetimeモジュールのdatetimeをインポート

dt_obj = datetime(2017, 12, 22)    # datetime型のオブジェクトを生成する


"""
独自モジュールの作成

次に独自にモジュールを作成して使用みましょう。
拡張子がpyとなるPythonスクリプトを作成し、別のスクリプトから呼び出します。


単一モジュールのimport

まずはmod1.pyという名前の簡単なモジュールを作成します。

# mod1.py
def func1():
    print('func1')

同じディレクトリにrun.pyという実行スクリプトを作成します。

# run.py
import mod1
mod1.func1() # mod1.pyのfunc1関数が呼び出される。


パッケージ化

もう少しモジュールの数を増やしてそれらをまとめたパッケージを作ってみましょう。
先ほど作ったrun.pyと同じディレクトリ内にmypkgというパッケージディレクトリを作成します。
mypkgの中に、mod2.py、mod3.pyというモジュールを作成してみましょう。

# ./mypkg/mod2.py
def func2():
    print('func2')

# ./mypkg/mod3.py
class MyClass():
    def method3(self):
        print('method3')

さらに、パッケージには_init__.pyという空ファイルを配置します。
これはディレクトリがパッケージであることを示す目印となります。

階層は以下のようになります。

$ tree
.
├── mod1.py
├── mypkg
│   ├── __init__.py
│   ├── mod2.py
│   └── mod3.py
└── run.py

最後にモジュール伸び出しのrun.pyを以下のように記述します。

import mod1
from mypkg import mod2, mod3  

mod1.func1()
mod2.func2()
mod3.MyClass().method3()

実行してみると、それぞれのモジュールを呼び出すことが確認できます。


__init__.pyの活用

さて、先ほど空のファイルだった__init__.pyですが、以下のように修正してみましょう。

# ./mypkg/__init__.py
from . import mod2
from . import mod3   

すると、run.py側では、以下のように呼び出すこともできます。

import mod1
import mypkg

mod1.func1()
mypkg.mod2.func2()
mypkg.mod3.MyClass().method3()

mypkgをimportすると、配下のものもimportされていることが確認できますね。
"""
