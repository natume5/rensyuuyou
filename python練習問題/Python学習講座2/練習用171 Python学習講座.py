#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- デコレータ ---")


print("--- まえがき(アノテーションではないので注意) ---")


"""
PythonにはJavaのアノテーションのように関数宣言の前に@から始まる文を書きますが、
これを関数デコレータまたは単にデコレータと呼びます。
アノテーションとはまったく別物なので注意してください。
"""


print("--- デコレータとは ---")


"""
デコレータとは高階関数を使用して既存の関数に対して
機能を追加・変更するための機能です。
元の関数の処理内部に手を加えずに機能を
追加・変更できるという点が大きなメリットです。
別ページで解説しますが、クラスにもデコレータを使用することができ、
それらと区別する際は関数デコレータと呼びます。
ただし、いきなりデコレータの説明から入ると大抵理解できません。
（実際、デコレータを苦手とする方は多いようです。）
このため、復習を兼ねて順に説明していきましょう。


関数オブジェクトと高階関数の復習

Pythonの関数はオブジェクトとして取り扱いが可能である、という説明を以前しました。
また、引数や戻り値に関数オブジェクトを含むようなものを高階関数と呼びました。
ピンとこない方は以下を復習してください。

関数オブジェクト
内部関数とnonlocal宣言
lambda式

まず、内部関数と組み合わせた高階関数のサンプルを以下に示します。
"""

def deco_func(f):
	def new_func():
		print('start')
		val = f()
		print('end')
		return val

	return new_func


def my_func():
	""" 1から10までの合計を返す関数 """
	ret = 0
	for i in range(1, 11):
		ret += i
	print('my_func実装中')
	return ret


f = deco_func(my_func)    # 新たに機能を追加した関数オブジェクトを作成
x = f()    # 新たに作成した関数を実行する
# start
# my_func実装中
# end
print(x)    # 55

"""
deco_funcは引数で指定された関数に対して処理の前後にstart、
endという文字列の3つを出力するように機能の改変を行ったものを
関数オブジェクトとして返しています。
deco_func内をもう少し詳しくみてみましょう。
内部でnew_funcという内部関数を定義しています。
このnew_funcは、deco_funcが引数で受け取った関数を実行していますが、
その処理に加え、startという文字列、処理結果、
endという文字列の3つを出力しています。
deco_funcはこの内部関数を新たな関数オブジェクトとして返却しているわけです。
新たな関数new_funcを実行すると、処理前後にstart、endが出力され、
処理結果が出力されます。


デコレータ

上の高階関数では、元の関数に手を加えずに
処理の追加ができている点に注意してください。
さて、この高階関数を常に適用したい場合、どうすればよいでしょうか？
そこでいよいよデコレータの出番です。
以下のように処理を追加したい関数の上に@をつけて高階関数を記述します。
デコレータ
@高階関数
def 関数名(引数):
    ：
    ：

デコレータがつけられた関数は
常に@以降で指定した高階関数が適用された状態に変化します。
さきほどの関数をデコレータを利用したものに書き換えてみましょう。
"""

def deco_func(f):
	def new_func():
		print('start')
		val = f()
		print('end')
		return val

	return new_func


@deco_func
def my_func():
	""" 1から10までの合計を返す関数 """
	ret = 0
	for i in range(1, 11):
		ret += i
	print('my_func実装中')
	return ret


x = my_func()    
# 普通にmy_funcを実行すると、deco_funcが適用された関数が実行される。
# start
# my_func実装中
# end
print(x)    # 55

"""
デコレータと可変長引数

上のサンプルでは引数なしの関数だけしか使えません。
入門編を通して読まれている方はすぐにピンときたと思いますが、
そう、可変長引数を利用するとこの問題が解決できます。
さらに書きなおしてみましょう。
"""

def deco_func(f):
	def new_func(*args, **kwargs):
		print('start')
		val = f(*args, **kwargs)
		print('end')
		return val

	return new_func


@deco_func
def my_func(n, m):
	""" nからmまでの合計を返す関数 """
	ret = 0
	for i in range(n, m + 1):
		ret += i

	print('my_func実装中')
	return ret


x = my_func(1, 10)
# start
# my_func実装中
# end
print(x)    # 55

"""
いかがでしょうか？少し難しいですが、
前述の通り元の関数に手を加えずに機能追加ができますので、
積極的に活用したいですね。
"""



print("--- SAMURAIENGINEER Blog ---")
print("--- 【Python入門】デコレータの使い方をわかりやすく解説！ ---")


"""
今回はPythonで使われるデコレータの基本的な使い方を、
やさしく解説していきたいと思います。
デコレータの仕組みや使用方法を理解していると、
Pythonプログラミングの幅がとても広がります。
"""


print("--- デコレータとは ---")


"""
デコレータとは、すでにある関数に処理の追加や変更を行う為の機能です。
デコレータを使うことによって、既存の関数の中身を直接変更することなく、
それらに機能を追加したり変更したりすることが出来るようになります。
たとえば、ある関数があって処理によって関数の動作を変更させていときに
デコレータを定義しておけば、わざわざ処理ごとに似たような関数を作る手間が省けます。
"""


print("--- デコレータの基本的な使い方 ---")


"""
では、基本的な使い方からご紹介したいと思います。
デコレータには関数の知識も必要になります。
こちらのコードをご覧ください。
"""

def sample_decorator(myfunc):
	print('I am the decorator!')
	return 0

@sample_decorator
def myfunc():
	pass

# I am the decorator!

"""
こちらのコードでは、sample_decoratorというデコレータを作成しました。
「＠」の後にデコレータの名前を記述し、その下に新たな関数myfuncを定義しました。
デコレータの基本構文は以下のようになります。

＠デコレータ名

このサンプルコード内では関数を実行したわけでもないのに、
「I am the decorator!」という文字列が出力されました。
ではどうして、実行していないのに文字列が表示されたのでしょうか。
それは、先程のコードに出てきたような構文は、
以下のようなコードのシンタックスシュガー
（＝糖衣構文。よりシンプルでわかりやすい書き方）だからです。
実際、先ほどのコードは以下のようにも書けます。
"""

def myfunc():
	pass

myfunc = sample_decorator(myfunc)
# I am the decorator!

"""
上のコードでは、sample_decorator関数が呼び出されていることが分かります。
先ほどお伝えしたように、デコレータには既存の関数に機能を追加する働きがあります。
つまり、その名の通りデコレート（decorate＝装飾）するのです。
このサンプルコードでは、sample_decoratorによりmyfuncが装飾されました。
実際、myfuncは関数ではなく数値0を格納している変数になりましたね。
"""

print('myfunc:{}'.format(x))
# myfunc:0

"""
先ほどのコードでは、デコレータを使用して関数を定数に変換するという操作を行いました。
しかしもちろん、関数を変化させて別の関数にする事も出来ます。
以下のコードをご覧ください。
"""

def sample_decorator(myfunc):
	def inner_func(text):
		return 'I am the decorator!'
	return inner_func

@sample_decorator
def myfunc(text):
	return text

print(myfunc("Blabla"))
# I am the decorator!

"""
上のコードでは、myfuncを実行したにも関わらず「Blabla」とは表示されず、
反対に「I am the decorator!」という文字列が出力されました。
このサンプルコードでは関数を返すデコレータを使用しました。
その為、先ほどのサンプルコードでは装飾後myfuncはint型の0を格納しましたが、
今回myfuncの値は関数からまた別の関数に差し替えられたのです。
また，myfuncの結果をそのままデコレータ内で使用することもできます。
以下のコードをご覧ください。
"""

def sample_decorator(myfunc):
	def inner_func(*args):
		print('I am the decorator!')
		myfunc(*args)
	return inner_func

@sample_decorator
def myfunc(text):
	print(text)

myfunc('Blabla')
# I am the decorator!
# Blabla

"""
このように、myfuncに与えられた引数を使用するときは、
inner_funcに*arg(可変長引数)として渡してあげます。
"""


print("--- Python標準のデコレータ ---")


"""
Pythonには便利なデコレータが標準で用意されています。
最も一般的なデコレータは

@classmethod
@staticmethod
@property

になります。
では早速、ご紹介したいと思います。
"""


print("--- @classmethodの使い方 ---")


"""
一般的にクラスメソッドと呼ばれるものは、
インスタンス化しなくても直接呼び出せるメソッドの事です。
大体は、

オブジェクト＝クラス名()
オブジェクト.メソッド()

このようにメソッドを呼び出しますよね。
クラスメソッドとは、このように呼び出す事が出来る便利なものなんです！
関数をクラスメソッド化させたい場合は、@classmethodを使用しましょう。
以下のコードをご覧ください。
"""

class MyClass():
	@classmethod
	def myfunc(cls):
		print('I am a class method')

MyClass.myfunc()
# I am a class method

"""
上記コードでは、MyClassという名のクラス内にmyfuncという関数を定義しました。
myfuncをデコレートしたので、myfuncはクラスメソッドとなります。
このようにすると、クラスメソッドを呼び出せる形でmyfuncを呼び出す事が出来ました。
見ての通りMyClassのインスタンスを作成しなくても、きちんと文字列が出力されています。
注意したい点は、myfuncの引数です。
クラスメソッドは第一引数にクラスを受け取ります。
引数名は特に決まりはありませんが、今回のようにclsを指定するのが一般的です。
"""


print("--- @staticmethodの使い方 ---")













