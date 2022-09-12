#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- NumPy入門   ユニバーサル関数とは---")


"""
ユニバーサル関数とは

NumPyの配列、ndarrayの全要素に対して、要素ごとに演算等の処理を行い、
結果をndarrayで返す関数をユニバーサル関数と呼びます。
組込みのmap関数を併用した場合と同じような作用をイメージしていただいてもかまいません。
ユニバーサル関数は省略してufuncと呼ぶこともあります。
予めNumPyライブラリで提供されているものに加え、独自実装することも可能です。


ユニバーサル関数の例

Numpyライブラリで提供されているユニバーサル関数の例をいくつか挙げてみましょう。


sin 正弦を返す

１つのndarrayの各値に対し、正弦を返す関数です。
"""

import numpy as np

x = np.arange(1, 10)
print(x)    # [1 2 3 4 5 6 7 8 9]


print(np.sin(x))
# [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.2794155
#   0.6569866   0.98935825  0.41211849]

"""
引数にndarrayを指定すると、それぞれの正弦の値が格納された
ndarrayが返されていることが確認できます。


add 足し算

一方で２つのndarrayを引数にそれぞれの演算結果を返すユニバーサル関数もあります。
基本的なものとしてaddが挙げられます。名前の通り、足し算の結果を返すユニバーサル関数です。
"""

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.add(x, y))    # [5 7 9]

"""
２つの配列x,yのそれぞれの加算した値が返されていることが確認できます。
"""


print("--- NumPy入門 代表的なユニバーサル関数---")


"""
このページではNumPyに予め組み込まれているユニバーサル関数のうち、代表的なものを紹介します。

代数演算、論理演算、比較演算、指数・対数、三角関数といった初等関数は全て用意されています。


演算などの基本的な関数

まずは基本的な代数演算系からです。
関数名 	                説明
add(x1, x2) 	        加算
subtract(x1, x2) 	    減算
multiply(x1, x2) 	    掛け算
divide(x1, x2) 	        割り算
mod(x1, x2) 	        剰余
remainder(x1, x2) 	    余り
square(x) 	            ２乗
power(x1, x2) 	        べき乗
sign(x) 	            符号
negative(x) 	        符号逆転
sqrt(x) 	            平方根
cbrt(x) 	            三乗根
reciprocal(x) 	        逆数
fabs(x) 	            絶対値
modf(x) 	            小数部分と整数部分

最後のmodfについて補足します。
この関数、小数部分と整数部分、戻り値が２つ返されます。
サンプルで確認してみましょう。
"""

# import numpy as np

x = np.array([1.0, 2.1, -3.2])
i, f = np.modf(x)

print(i)    # (小数部分)
# [ 0.   0.1 -0.2]

print(f)    # (整数部分)
# [ 1.  2. -3.]


"""
指数・対数関数

次に指数・対数関数です。

exp(x) 	      自然対数のべき乗
exp2(x) 	     2のべき乗
log(x) 	         自然対数
log2(x) 	     底が2の対数
log10(x) 	     常用対数
expm1(x) 	     exp(x) - 1
log1p(x) 	     log(1+x)


三角関数

三角関数です。

関数名 	             説明
sin(x) 	             正弦
cos(x) 	             余弦
tan(x) 	             正接
arcsin(x) 	         逆正弦
arccos(x) 	         逆余弦
arctan(x) 	         逆正接
sinh(x) 	         双曲線正弦
cosh(x) 	         双曲線余弦
tanh(x) 	         双曲線正接
arcsinh(x) 	         逆双曲線正弦
arccosh(x) 	         逆双曲線余弦
arctanh(x) 	         逆双曲線正接
deg2rad(x) 	         角度を度からラジアンに変換します。
rad2deg(x) 	         角度をラジアンから度に変換します。

単位としてラジアンを使用する点に注意してください。
弧度法からラジアンの変換は上記表の通り、deg2radで可能です。
試しに６０度を変換して確認してみましょう。円周率はnp.piを使用します。
"""

# import numpy as np

deg = 60

print(np.deg2rad(deg))    # 1.0471975511965976

# 60度 = 半円(180度)の3分の1
print(np.pi / 3)    # 1.0471975511965976

"""
ビット演算

ビット演算です。
関数名 	                          説明
bitwise_and(x1, x2) 	         ビットごとのAND演算
bitwise_or(x1, x2) 	             ビットごとのOR演算
bitwise_xor(x1, x2) 	         ビットごとのXOR演算
invert(x) 	                     ビットごとのNOT演算
left_shift(x1, x2) 	             整数ビットを左シフト演算
right_shift(x1, x2) 	         整数ビットを右シフト演算


比較演算

比較演算です。
関数名 	                      説明
greater(x1, x2) 	         （x1> x2）を判定
greater_equal(x1, x2) 	     （x1> = x2）を判定
less(x1, x2) 	             （x1 < x2 ）を判定
less_equal(x1, x2) 	         （x1 =< x2）を判定
not_equal(x1, x2) 	         （x1！= x2）を判定
equal(x1, x2) 	             （x1 == x2）を判定
logical_and(x1, x2) 	        AND演算
logical_or(x1, x2) 	            OR演算
logical_xor(x1, x2) 	        XOR演算
logical_not(x) 	                NOT演算
maximum(x1, x2) 	          配列要素の要素単位の最大値。
minimum(x1, x2) 	          配列要素の要素単位の最小値。
fmax(x1, x2) 	              配列要素の要素単位の最大値。
fmin(x1, x2) 	              配列要素の要素単位の最小値。

量が多いですが、最初はどういったものがあるのかを知っておく程度でよいかと思います。

実際に使用する際や詳細が知りたい場合は以下公式ドキュメントを参照してください。

Available ufuncs
"""


print("--- NumPy入門 通常の関数をユニバーサル関数に変換する frompyfunc---")


"""
前回はnumpyが提供する代表的なユニバーサル関数を紹介しましたが、
実はnpには様々な関数をユニバーサル関数に変換する関数、
frompyfuncが用意されています。このページではfrompyfuncを使用して
ユニバーサル関数を自前で作ってみましょう。
（関数オブジェクトについて理解していると理解がスムーズになると思います。）


frompyfunc

冒頭で紹介したとおり、frompyfuncというNumPyの関数を使用すると、
通常の関数をユニバーサル関数に変換することができます。
引数に対象となる関数オブジェクト、引数の数と出力の数を指定します。
戻り値としてユニバーサル関数オブジェクトが返されます。


サンプルその1

まずはPythonの組込み関数strをfrompyfuncでユニバーサル関数化してみましょう。
strは1つの引数に対し、文字列表現を1つ返す関数です。
"""

# frompyfuncで新たな関数を作る
new_str = np.frompyfunc(str, 1, 1)

# ndarrayを生成
a = np.array([1, 2, 3])

# frompyfuncで作った関数を使用
print(new_str(a))    # ['1' '2' '3']
# array(['1', '2', '3'], dtype=object) 文字列になっていることが確認できる

"""
frompyfuncから新たに作った関数を使用すると、
ndarrayそれぞれの要素に対して文字列表現が取得できていることが確認できます。


サンプルその2

もちろん、同様の方法で自前の関数をユニバーサル関数化することも可能です。
2つの引数に対し、和と差の2つを返す関数をユニバーサル関数化してみましょう。
"""

# import numpy as np

def sumsub(x, y):
	return x + y, x - y

# frompyfuncで新たな関数を作成
new_func = np.frompyfunc(sumsub, 2, 2)

# ndarrayを２つ生成
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

# frompyfuncで作った関数を使用
sum, sub = new_func(x, y)

print(sum)    # [4 4 4]

print(sub)    # [-2 0 2]

"""
frompyfuncの引数には元の関数sumsubの引数、戻り値の数を指定しますので、
上のサンプルでは2, 2を指定しています。

結果として、それぞれの要素に対して足し算、引き算が実行されていることが確認できます。
"""


print("--- NumPy入門 メッシュグリッドと可視化---")


"""
このページではデータを可視化する際によく使用するメッシュグリッドと呼ばれる
配列生成関数について学習します。


meshgridとは

配列X=[1, 2, 3]、Y=[-1, 0, 1]が与えられていたとします。
これらの格子点、つまりXとYの組み合わせは
(1, 0)、(2, 0)、(3, 0)、(1, 1)、(2, 1)、(3, 1)、(1, -1)、(2, -1)、(3, -1)
の9つとなりますが、meshgridを使用するとそれらをプログラム上で扱いやすい形で出力された
X, Yの組を得ることができます。

サンプルで具体的に確認してみましょう。
"""

X = [1, 2, 3]
Y = [-1, 0, 1]

xv, yv = np.meshgrid(X, Y)

print(xv)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

print(yv)
# [[-1 -1 -1]
#  [ 0  0  0]
#  [ 1  1  1]]

"""
少しわかりづらい構造ですが、以下のように2回ループで順番に要素を取り出すと前述の直積、
9つの要素が得られることが確認できます。
"""

for xx, yy in zip(xv, yv):
	for x, y in zip(xx, yy):
		print(x, y)
# 1 -1
# 2 -1
# 3 -1
# 1 0
# 2 0
# 3 0
# 1 1
# 2 1
# 3 1


"""
meshgridを利用した可視化

とっつきづらい構造ですが、ユニバーサル関数と相性がよく、
グリッド上の関数の評価する際に非常に便利です。
（公式より「meshgrid is very useful to evaluate functions on a grid.」）

また、評価結果をそのままmatplotlibに指定して出力することが可能です。

サンプルです。教養課程の微積の鞍点の説明でよく使用される関数
\( z = x^2 - y^2 \)について、定義域\( [-1, 1] \times [-1, 1] \)
の様子を可視化して確認してみましょう。
ユニバーサル関数np.subtractにそのまま値を指定することができている点に注目してください。
"""

# import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定義域[-1, 1]のx, yを50個区切りで生成
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)

# メッシュグリッドを生成
xv, yv = np.meshgrid(x, y)

# 関数x^2 - y^2の値をzに代入
z = np.subtract(xv**2, yv**2)

# x, y, zをワイヤフレームで表示
ax = Axes3D(plt.figure())
ax.plot_wireframe(xv, yv, z)
plt.show()

"""
以下のようにグラフが出力され、各点におけるzの値（＝高さ）を確認することができます。
"""


print("--- NumPy入門 乱数---")


"""
今回はシミュレーションやテストデータを作成する際によく使う乱数についてです。

randomモジュールとrand

NumPyのrandomモジュールには様々な乱数を生成するメソッドが用意されています。
まずは基本的なrandメソッドについて学習しましょう。


rand

randメソッドを使用すると、最も基本的な乱数である[0, 1)区間（0.0以上、1.0未満）
の一様乱数を生成することができます。

引数で生成する要素数を指定します。

10000個の乱数を生成し、階級数が20のヒストグラムで可視化するサンプルを見てみましょう。
"""

# import numpy as np
# import matplotlib.pyplot as plt


rand_array = np.random.rand(10000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(rand_array, bins=20, ec='b')
plt.show()


"""
多次元の乱数

第二引数以降を指定すると、その次元の乱数行列が返されます。
2x20の行列を生成してプロットしてみましょう。

2次元でランダムにプロットされていることが確認できます。
"""

# import numpy as np
# import matplotlib.pyplot as plt

rand_x, rand_y = np.random.rand(2, 20)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(rand_x, rand_y)
plt.show()


"""
さまざまな分布の乱数
さまざまな分布の乱数

randomモジュールには様々な分布の乱数を生成するメソッドが用意されています。
代表的なものを紹介します。

メソッド 	                   分布
beta 	                   ベータ分布
binomial 	               二項分布
chisquare 	               カイ二乗分布
dirichlet 	               ディリクレ分布
exponential 	           指数分布
f 	                       F分布
gamma 	                   ガンマ分布
geometric 	               幾何分布
gumbel 	                   ガンベル分布
hypergeometric 	           超幾何分布
logistic 	               ロジスティック分布
lognormal 	               対数正規分布
logseries 	               対数級数分布
multinomial 	           多項分布
multivariate_normal 	   多変量正規分布
negative_binomial 	       負の二項分布
noncentral_chisquare 	   非中心カイ二乗分布
noncentral_f 	           非中心F分布から
normal 	                   正規分布
poisson 	               ポアソン分布
standard_cauchy 	       標準コーシー分布
standard_exponential 	   標準指数分布
standard_gamma 	           標準ガンマ分布
standard_normal 	       標準正規分布
standard_t 	               標準t分布
uniform 	               一様分布
weibull 	               ワイブル分布

その他の分布の乱数や、引数については以下を参照してください。
Random sampling


サンプル

例として標準正規分布をヒストグラムで可視化してみましょう。
"""

# import numpy as np
# import matplotlib.pyplot as plt

rand_array = np.random.standard_normal(10000)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(rand_array, bins=50, ec = 'b')
plt.show()
