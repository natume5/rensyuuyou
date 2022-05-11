#!/usr/bin/python
# -*- coding: UTF-8 -*-


# import math
# from decimal import Decimal
# from fractions import Fraction


print("--- Python学習講座---")
print("--- Python入門　基本的な数値の演算---")


"""
演算

数値型の場合、以下の演算を利用することができます。
以下の表は、演算の優先順位の低い順にソートされています。

演算の一覧
演算 	            結果
x + y 	        x と y の和
x - y 	        x と y の差
x * y 	        x と y の積
x / y 	        x と y の商
x // y 	        x と y の商を切り下げたもの
x % y 	        x / y の剰余
-x 	            x の符号反転
+x 	            x そのまま
abs(x) 	        x の絶対値または大きさ
int(x) 	        x の整数への変換
float(x) 	    x の浮動小数点数への変換
complex(re, im) 実部 re, 虚部 im の複素数。 im の既定値はゼロ。
c.conjugate() 	複素数 c の共役複素数
divmod(x, y) 	(x // y, x % y) からなるペア
pow(x, y) 	    x の y 乗
x ** y 	        x の y 乗

一般的なプログラム言語と変わりませんが、商は2種類あるので注意してください。
サンプルで確認してみましょう。
"""

# 四則演算
x = 16
y = 3
val = x + y
print(val)     # 19

val = x - y
print(val)    # 13

val = x * y
print(val)    # 48

val = x / y
print(val)    # 5.333333333333333

val = x // y
print(val)    # 5

val = x % y
print(val)    # 1

val = int(x / y)
print(val)    # 5

val = float(x)
print(val)    # 16.0

# 複素数
val = 3 + 5j
print(val.conjugate())    # (3-5j)

# 乗数
val = pow(2, 3)
print(val)    # 8

val = 2 ** 3
print(val)    # 8

"""
また、演算子以外にabs、int、float、divmod、powといった組込み関数で演算することができます。
"""

"""
数値と数値演算で使用するモジュール

数値クラスとデータ分析等の際に数値演算でよく利用するモジュールを簡単に紹介します。モジュールのインポートが必要となりますが、モジュールとimport文に関する説明は別項にて説明しますので、とりあえずこう書くのだな、と思って読んでください。
math, cmathモジュール

数値演算で利用する関数セットです。いくつか例を交えて紹介します。
"""

import math

# 指数関数
val = math.exp(2)
print(val)    # 7.38905609893065

# 対数関数
val = math.log(5)
print(val)    # 1.6094379124341003

# 三角関数
val = math.sin(math.pi / 2)
print(val)    # 1.0


"""
指数関数、対数関数、三角関数など一通り利用できます。
また、円周率やネイピア数なども定数として準備されています。
データ分析では非常に使用するモジュールです。
なお、mathモジュールは複素数型では利用できません。
複素数の場合はcmathを利用します。
実数と同様の演算が可能ですのでサンプルは省略します。
"""

"""
decimalモジュール

floatは内部的には2進数なので、簡単な計算で誤差が発生します。
例えば、float型の0.1に3を掛け算すると、以下のようになります。
これは、0.1が内部的には2進数の無限小数になっていることに起因します。
"""

x = 0.1 * 3
print(x)    # 0.30000000000000004

is_equal = (0.1 * 33 == 3.3)
print(is_equal)    # False

"""
もし金融や科学技術分野の処理で精緻な計算が必要な場合は、decimalを利用します。
上と同じ計算をdecimalで行ってみます。
"""

from decimal import Decimal


x = Decimal('0.1')
print(x)    # 0.1
print(x * 3)    # 0.3

Decimal('0.3')
is_equal = (x * 33 == Decimal('3.3'))
print(is_equal)    # True

"""
decimalを使用することで、想定通りの結果を得ることができました。


fractionsモジュール

有理数、つまり分数をサポートするモジュールです。
除算と積算が交互に行われるような計算をする場合、徐々に誤差が蓄積していきますが、
fractionsを利用するとその誤差を少なくすることができます。
また、約分も自動的に行われます。
"""

from fractions import Fraction

# 分数の定義
x = Fraction(3, 7)
print(x)    # 3/7

# 約分の確認
y = x * 7
print(y)    # 3

# 小数との演算
z = x + 0.1
print(z)    # 0.5285714285714286

"""
上のサンプルでは、3/7に7を掛け算し約分がサれていることが確認できます。
また、小数型との演算も可能であることも確認できます。


その他

上記に上げた基本的なモジュール以外に、擬似乱数を生成するrandomモジュール、
統計計算をサポートするstatisticsモジュールといったものがあります。
専門的な内容となるため、詳細は別記事に記述する予定です。
"""


print("--- Python入門　bool(真理値)型---")


"""
Pythonのbool(論理)型

bool型とは真理値、つまり真偽を表す変数の型です。
Pythonのbool型は一般的なプログラミング言語と同様、以下の真偽2値が用意されています。
値 	        意味
True 	    真
False 	    偽


論理演算

Pythonのbool型はor、and、notというキーワードで論理演算することが可能です。
それぞれ、論理和、論理積、否定となります。
（論理演算についてご存知でない方はページ下の補足を参照してください。）

ではサンプルです。
"""

b1 = True
b2 = False
b3 = True

b3 = b1 or b2    # 論理和
print(b3)    # Trueが出力される

b4 = b1 and b2    # 論理積
print(b4)    # Falseが出力される

b5 = not b1    # 否定
print(b5)    # Falseが出力される

"""
それぞれ論理演算された結果が出力されます。

また、Pythonは複数の変数に対して論理演算を並べて記述することが可能です。
"""

b1 = True
b2 = False
# b3 = True

b = b1 and b2 and b3
print(b)    # False

b = b1 or b2 and b3
print(b)    # True

"""
複数の論理演算を行う場合、演算子の優先順位は高い順にnot、and、orとなります。
ただし、可読性の観点から以下のように括弧をつけることをおすすめします。
"""

b = b1 or (b2 and b3)
print(b)    # True


"""
比較演算子とbool型

数値の比較演算子の演算結果はbool型となります。サンプルを見てみましょう。
"""

x = 100
y = 200
b1 = (x < y)    # 100 < 200は正しいので真
print(b1)    # Trueが出力される

b2 = (y < x)    # 200 < 100は誤りなので偽
print(b2)    # Falseが出力される

"""
比較演算子を括弧でくくっていますが、なくても正常に動作します。
ただし可読性が落ちますのでやはりこちらも演算の優先順位を表すために括弧をつけることをおすすめします。


TIPS

Pythonのbool型はint型のサブクラスとして定義されています。
このため、int型に変換することが可能です。
また、int型で用意されている各種メソッドも利用することができます。
"""
b1 = True
b2 = False

print(int(b1))    # 1が出力される
print(int(b2))    # 0が出力される

"""
補足　論理演算とは

プログラミング初学者向けに論理演算の初歩に関する補足をします。
真と偽を表す論理値に対し、否定、論理和、論理積３種類の演算が定義されています。
今後学習する、条件分岐（条件によって処理を変化させる制御のこと）等で活躍します。


否定

否定とは、変数が真の場合は偽に、偽の場合は真に変換する演算です。
bool値 	not演算結果
True 	False
False 	True


論理和

論理和は２つの論理変数に対し、一方でもTrueであれば結果をTrueとして返す演算です。
変数1 	変数2 	or演算結果
True 	True 	True
True 	False 	True
False 	True 	True
False 	False 	False

「２つ条件があり、そのうちひとつでも条件を満たしている場合」を表したい場合に使用します。


論理積

論理和は２つの論理変数に対し、両方ともTrueであれば結果をTrueとして返す演算です。
変数1 	変数2 	and演算結果
True 	True 	True
True 	False 	False
False 	True 	False
False 	False 	False

「２つ条件があり、両方条件を満たしている場合」を表したい場合に使用します。
"""


print("--- Python入門　None型---")


"""
値が存在しないことを表すNone

変数に値が存在しない場合、PythonではNoneを利用します。CやJava、C#のnullに相当します。

ある変数valにNoneを代入する場合は以下のように記述します。
"""

val = None

"""
変数をとりあえず初期化する際に使用できます。


Noneかどうかを判定する

変数がNoneかどうかを判定する際はisを使います。
（if文についてはまだ説明していませんが、別途説明します。わからない方は一旦飛ばして構いません。）
"""

val = None
if val is None:
	print('val is None')    # この行が出力される


"""
Noneの評価と空文字

また、None自体はif文でFalseと評価されます。
"""

val = None

if val:
	print('True')
else:
	print('False')    # この行が出力される


"""
Noneの文字列表現

Noneを使用する際にもう１点、注意が必要なのが文字列表現です。
Noneをprint関数などで出力してみましょう。
"""

var = None
print(var)    # Noneが出力される

"""
Noneという文字列が出力されるため、ログなどで空文字を期待した実装をする際には注意が必要です。
"""


print("--- Python入門　シーケンス---")


"""
シーケンス

これまで学習した数値や真理値などは変数にただ1つの値を格納していましたが、
変数の基本で解説したとおり、Pythonには複数の値を格納する型がいくつか用意されています。
これから学習するシーケンスも複数の値を格納することが可能です。

シーケンスとは複数の値を順番に並べたものをひとかたまりとして格納するための型です。
例えば、第1回から第10回までのテストの点数データがあり、順番に出力する場合を考えてみましょう。
以下のように10個の配列を用意することは少々面倒臭そうですね。また、数を追加するとさらに大変です。

# テストの点数
num1 = 97
num2 = 78
num3 = 88
# :
# :
num9 = 92
num10 = 75

# 出力
print(num1)
print(num2)
# :
# :
print(num9)
print(num10)

そこでシーケンスの一種であるリストを使用すると、以下のように記述することができます。
"""

# テストの点数
num_list = [97, 78, 88, 76, 100, 85, 72, 85, 92, 75]

# 出力する
for num in num_list:
	print(num)

"""
後ほど説明しますが、for文と呼ばれるループを活用し、順番に処理を行うことが可能となります。

シーケンス型には様々な種類がありますが、基本的なシーケンス型として、

    リスト
    タプル
    range
    文字列

が挙げられます。それぞれに学習する前に、簡単に概要を説明しましょう。
用語の補足

概要の説明の前に用語の補足です。
先程、シーケンスは「複数の値を順番に並べたものをひとかたまりとして」と書きました。
複数の値のなかで、それぞれの値を要素と呼びます。
また、要素には何番目、という番号がつけられており、その番号のことをインデックス、若しくは添字と呼びます。


リスト

リストはシーケンスでもっとも基本的かつ重要といえます。
上のサンプルのようにデータをまとめて取り扱うことができ、
またデータの要素を書き換えたり順序を変更したりすることができます。


タプル

タプルはリストとは異なり、後から値や順序を変更することができないシーケンスです。
最初に定めた値が保証されるため、安全にプログラミングを行う際に活躍します。
（タプルのような後から値を変更できない性質のことイミュータブルといいます。）


range

range関数を使用すると引数で指定した整数の数の要素をもった
rangeと呼ばれるシーケンスを得ることができます。
所定の回数分ループする際に使用できます。
また、リストと比較してメモリの使用量が少ないのも特徴の1つです。


文字列

ダブルクォート、もしくはシングルクォートでくくった文字列を変数に格納することができます。

text = 'abce'

この変数の型を文字列型(str)と呼びます。

いずれも重要ですのでこれから順番に学習していきましょう。
"""
