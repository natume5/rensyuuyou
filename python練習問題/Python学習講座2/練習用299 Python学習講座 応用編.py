#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 代表的なユニバーサル関数 ---")


"""
このページではNumPyに予め組み込まれているユニバーサル関数のうち、
代表的なものを紹介します。

代数演算、論理演算、比較演算、指数・対数、
三角関数といった初等関数は全て用意されています。
"""


print("--- 演算などの基本的な関数 ---")


"""
まずは基本的な代数演算系からです。

関数名 	             説明
add(x1, x2) 	    加算
subtract(x1, x2) 	減算
multiply(x1, x2) 	掛け算
divide(x1, x2) 	    割り算
mod(x1, x2) 	    剰余
remainder(x1, x2) 	余り
square(x) 	        ２乗
power(x1, x2) 	    べき乗
sign(x) 	        符号
negative(x) 	    符号逆転
sqrt(x) 	        平方根
cbrt(x) 	        三乗根
reciprocal(x) 	    逆数
fabs(x) 	        絶対値
modf(x) 	        小数部分と整数部分

最後のmodfについて補足します。
この関数、小数部分と整数部分、戻り値が２つ返されます。
サンプルで確認してみましょう。
"""

import numpy as np

x = np.array([1.0, 2.1, -3.2])

i, f = np.modf(x)

print(i)    # (整数部分)

print(f)    # (小数部分)


print("--- 指数・対数関数 ---")


"""
次に指数・対数関数です。

exp(x) 	    自然対数のべき乗
exp2(x) 	2のべき乗
log(x) 	    自然対数
log2(x) 	底が2の対数
log10(x) 	常用対数
expm1(x) 	exp(x) - 1
log1p(x) 	log(1+x)
"""


print("--- 三角関数 ---")


"""
三角関数です。

関数名 	     説明
sin(x) 	    正弦
cos(x) 	    余弦
tan(x) 	    正接
arcsin(x) 	逆正弦
arccos(x) 	逆余弦
arctan(x) 	逆正接
sinh(x) 	双曲線正弦
cosh(x) 	双曲線余弦
tanh(x) 	双曲線正接
arcsinh(x) 	逆双曲線正弦
arccosh(x) 	逆双曲線余弦
arctanh(x) 	逆双曲線正接
deg2rad(x) 	角度を度からラジアンに変換します。
rad2deg(x) 	角度をラジアンから度に変換します。

単位としてラジアンを使用する点に注意してください。
弧度法からラジアンの変換は上記表の通り、deg2radで可能です。
試しに６０度を変換して確認してみましょう。
円周率はnp.piを使用します。
"""

import numpy as np

deg = 60

print(np.deg2rad(deg))

# 60度 = 半円(180度)の3分の1
print(np.pi / 3)

"""
1.0471975511965976
1.0471975511965976
"""


print("--- ビット演算 ---")


"""
ビット演算です。

関数名 	                     説明
bitwise_and(x1, x2) 	ビットごとのAND演算
bitwise_or(x1, x2) 	    ビットごとのOR演算
bitwise_xor(x1, x2) 	ビットごとのXOR演算
invert(x) 	            ビットごとのNOT演算
left_shift(x1, x2) 	    整数ビットを左シフト演算
right_shift(x1, x2) 	整数ビットを右シフト演算
"""


print("--- 比較演算 ---")


"""
比較演算です。

関数名 	説明
greater(x1, x2) 	    （x1> x2）を判定
greater_equal(x1, x2) 	（x1> = x2）を判定
less(x1, x2) 	        （x1 < x2 ）を判定
less_equal(x1, x2) 	    （x1 =< x2）を判定
not_equal(x1, x2) 	    （x1！= x2）を判定
equal(x1, x2) 	        （x1 == x2）を判定
logical_and(x1, x2) 	  AND演算
logical_or(x1, x2) 	      OR演算
logical_xor(x1, x2) 	  XOR演算
logical_not(x) 	          NOT演算
maximum(x1, x2) 	      配列要素の要素単位の最大値。
minimum(x1, x2) 	      配列要素の要素単位の最小値。
fmax(x1, x2) 	          配列要素の要素単位の最大値。
fmin(x1, x2) 	          配列要素の要素単位の最小値。

量が多いですが、最初はどういったものがあるのかを知っておく程度でよいかと思います。
実際に使用する際や詳細が知りたい場合は以下公式ドキュメントを参照してください。
"""
