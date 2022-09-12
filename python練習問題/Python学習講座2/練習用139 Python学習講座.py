#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 基本的な数値の演算 ---")


print("--- 演算 ---")


"""
数値型の場合、以下の演算を利用することができます。
以下の表は、演算の優先順位の低い順にソートされています。

演算の一覧
演算 	            結果
x + y 	            x と y の和
x - y 	            x と y の差
x * y 	            x と y の積
x / y 	            x と y の商
x // y 	            x と y の商を切り下げたもの
x % y 	            x / y の剰余
-x 	                x の符号反転
+x 	                x そのまま
abs(x)  	        x の絶対値または大きさ
int(x) 	            x の整数への変換
float(x) 	        x の浮動小数点数への変換
complex(re, im) 	実部 re, 虚部 im の複素数。 im の既定値はゼロ。
c.conjugate() 	    複素数 c の共役複素数
divmod(x, y) 	    (x // y, x % y) からなるペア
pow(x, y) 	        x の y 乗
x ** y 	            x の y 乗


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
また、演算子以外にabs、int、float、divmod、pow
といった組込み関数で演算することができます。
"""


print("--- 数値と数値演算で使用するモジュール ---")


"""
数値クラスとデータ分析等の際に数値演算でよく利用するモジュールを簡単に紹介します。
モジュールのインポートが必要となりますが、
モジュールとimport文に関する説明は別項にて説明しますので、
とりあえずこう書くのだな、と思って読んでください。

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
除算と積算が交互に行われるような計算をする場合、
徐々に誤差が蓄積していきますが、
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
