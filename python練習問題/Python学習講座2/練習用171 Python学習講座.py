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


"""
一般的にスタティックメソッド（静的メソッド）と呼ばれているものは、
クラスメソッドと同様にインスタンス化しなくても呼び出し可能な関数の事です。
では、実際に関数を静的メソッドに装飾してみましょう。
こちらのコードをご覧ください。
"""

class MyClass():
	@staticmethod
	def myfunc():
		print('I am a static method')

MyClass.myfunc()
# I am a static method

"""
こちらのコードでは、MyClassという名のクラス内にmyfuncという関数を定義しました。
その関数をデコレートし、静的メソッドにしました。
ご覧いただけるように、先ほどと同じような形でmyfuncを呼び出す事ができました。
クラスメソッドとは違い、
静的メソッドの場合myfuncにclsのような引数を与える必要はありません。
"""


print("--- @classmethodと@staticmethodの違い ---")


"""
結論から言ってしまうと、二つの違いはクラスに依存しているかどうかという事です。
では、これがどういう事が詳しく見て行きましょう。
classmethodとstaticmethodの違いは引数を受け取るかどうかだけではありません。
これらの違いはクラスで継承を行った時に現れます。
実際、コードで確認してみましょう。
こちらをご覧ください。
"""

class ParentClass():
	test_str = 'Hello, I am Parent Class'

	@classmethod
	def myclassmethod(cls):
		print('classmethod: ' + cls.test_str)

	@staticmethod
	def mystaticmethod():
		print('staticmethod: ' + ParentClass.test_str)

ParentClass.myclassmethod()
ParentClass.mystaticmethod()
# classmethod: Hello, I am Parent Class
# staticmethod: Hello, I am Parent Class

"""
上記コードでは、ParentClassという名のクラス内に
myclassmethodとmystaticmethodを定義し、呼び出しました。
すると、ParentClassが保有する文字列を出力しました。
しかし、親クラスを継承した子クラスから呼び出すと、少し変わります。
以下のコードをご覧ください。
"""

class ChildClass(ParentClass):
	test_str = 'Hello, I am Child Class'

ChildClass.myclassmethod()
ChildClass.mystaticmethod()
# classmethod: Hello, I am Child Class
# staticmethod: Hello, I am Parent Class

"""
上記コードでは、ChildClassといったParentClassを継承したクラスを作成しました。
同じようにふたつの関数を呼び出してみると、
myclassmethodの方は子クラスが保有している文字列を表示しました。
mystaticmethodは先ほどと変わらず、親クラス保有の文字列を表示しています。
これは、classmethodは継承した後、clsが子クラスに差し替えられる為です。
したがって、ChildClassで宣言したstrが優先されてしまうのです。
その点、静的メソッドはクラスに依存をしない為、
これらを使い分けることが出来ると便利です。
"""


print("--- @propertyの使い方 ---")


"""
Pythonのクラスは通常、プロパティ（属性）に直接読み書きを行う事が可能です。
クラス作成時に実行される__init__メソッドの引数としてselfが設定されていますよね、
プロパティとは「self.〜」の形の変数のことです。
@propertyを使うとこのデコレータで装飾された関数は
getterという読み取りしかできないプロパティになります。
読み取ることしかできないということは、
新たに値を変更することなどができないということです。
こちらのコードをご覧ください。
"""

class MyClass:
	def __init__(self):
		self._x = '12345'
	@property
	def x(self):
		return self._x

instance = MyClass()
print(instance.x)

"""
上記コードでは、xという読み取り専用プロパティを作成しました。
＠propertyというデコレートを使って、xというメソッドを装飾しました。
ということは、こちらのコードでは以下のようにも書くことが出来ます。

x = property(x)

property()関数は引数にgetter関数を受け取り、その属性の値を返します。
その為、xに格納されている値12345を出力しました。
仮に、xプロパティに値を設定してみると、読み取り専用プロパティの為エラーが発生します。
以下をご覧ください。

instance.x = 1234

実行結果

AttributeError: can't set attribute

こちらエラーは、Python2系では発生しません。
このことからプロパティを定義する時は、Python3系を使用することをおすすめします。
"""


print("--- デコレータの応用的な使い方 ---")


"""
ここからは、様々なデコレータの使い方について解説していきます。


元の関数のメタデータを維持する

実は先ほどまで解説してきたデコレータの定義方法では、
元の関数のメタデータ(名前等)がデコレータで使用された
関数のメタデータに置き換わってしまっていました。
元の関数の名前は__name__メソッドで確かめることができます。
以下のコードをご覧ください。
"""

def sample_decorator(myfunc):
	def inner_func():
		return 'I am the decorator!'
	return inner_func

@sample_decorator
def myfunc(text):
	return text


print(myfunc.__name__)    # inner_func

"""
このように、本来myfuncと表示したいところが、
デコレータの内部の関数inner_funcに置き換わっています。
そこで、myfuncのメタデータに変更を加えたくないときには、
functools.wrapsを使えば解決できます。
以下のコードをご覧ください。
"""

from functools import wraps


def sample_decorator(myfunc):
	@wraps(myfunc)
	def inner_func():
		return 'I am the decorator!'
	return inner_func

@sample_decorator
def myfunc(text):
	return text

print(myfunc.__name__)
# myfunc

"""
このように、ちゃんとmyfuncが返ってくるように書き直せました。
functools.wrapsはもとの関数の
メタデータに変更を加えないようにするためのデコレータです。
なので、inner_funcの前に変更を加えたくない関数
(今回はmyfunc)を引数として渡してあげることで、
メタデータに変更を加えないように処理してくれます。
"""


print("--- 複数のデコレータを使う ---")


"""
デコレータは一つの関数に対して、複数使用することもできます。
以下のコードをご覧ください。
"""

def A(myfunc):
	def inner_func():
		print('I am the A decorator!')
		myfunc()
		print('I am the A decorator!')
	return inner_func

def B(myfunc):
	def inner_func():
		print('I am the B decorator!')
		myfunc()
		print('I am the B decorator!')
	return inner_func

@B
@A
def myfunc():
	print('Hello, decorator')

myfunc()
# I am the B decorator!
# I am the A decorator!
# Hello, decorator
# I am the A decorator!
# I am the B decorator!

"""
このように、複数のデコレータがA→Bと実行されていることがわかります。
まずは、デコレータAで処理されたあとに、
その結果を再度デコレータBに入力値として使用しています。
複数の場合、元の関数(今回はmyfunc)に近い方から実行されるので、
注意が必要です。
"""


print("--- まとめ ---")


"""
今回はPythonにおけるデコレータの基本的な使い方と、その活用法について解説しました。
デコレータの仕組みを理解していると、様々なシチュエーションなどで使えてとても便利です。
この記事でご紹介したサンプルコードなどを実際に試しながら、理解を深めてくださいね！
"""



print("--- CodeGraffitiより ---")
print("--- 【Python入門】デコレータの作り方、書き方、使い方 ---")


"""
Pythonにはコードを書き換えずに、関数の処理に変更を加えたいようなことがあります。
これはデコレータを使うことで可能になります。デコレータは関数を入力として持ち、
別の関数を返す関数です。
関数内関数に似たようなものですが、
ちょっとPython初心者にはややこしい感じがするかもしれません。
このようなものがあるということを今の時点では頭に入れておきましょう。
"""


print("--- デコレータの作り方・書き方 ---")


"""
デコレータは、*argsと**kwargs、関数内関数、引数としての関数を持ちます。
コードで見た方が早いと思うので、コードを書いていきましょう。
まず、次のような関数のコードを用意します。
"""

def add_calc(a, b):
	return a + b

r = add_calc(10, 100)
print(r)    # 110

"""
関数の引数に値を入れて足し算させるコードですが、ここはわかりますよね。
実行するとこうなります。

10と100が足し算されて、110の値が出力されています。
このadd_calc(10, 100)を実行する時に何か別の処理を行いたいとします。
ここでは、関数を呼び出す前後にメッセージを出力することにします。
次のようにコードを加えてみます。
"""

def add_calc(a, b):
	return a + b

print('計算を開始します')
r = add_calc(10, 100)
print('計算が終了しました。結果を表示します。')
print(r)
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 110

"""
計算時にメッセージを表示するprint文を加えただけですね。
元の関数の処理に、print文を付け加えた形になっています。


デコレータのコードを書く

このような関数の処理に何か付け加えたい時に使えるのがデコレータです。
このコードを、デコレータを使って書き換えていきましょう。
"""

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

def add_calc(a, b):
	return a + b

"""
最初にも書きましたが、デコレータは、*argsと**kwargs、関数内関数、
引数としての関数を持ちます。
すでに定義しているadd_calc()の上側に、
新たにprint_passage()という関数を定義しています。
この関数は、関数funcを引数に持つ関数内関数となっています。
関数内にpassage(*args, **kwargs)という関数を定義して、
引数である関数を実行してその結果をresultで返し、
この関数内の結果をpassage()として返すのではなく、
passsageのオブジェクトとして返していることに注意です。
これを、上でやった計算と同じように引数を入れて実行するには、次のように書きます。
"""

f = print_passage(add_calc)
r = f(10, 100)
print(r)
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 110
"""
print_passage(add_calc)と引数に計算する関数を入れてオブジェクト化します。
これを変数fに入れ、丸括弧をつけて値を入れることで実行されます。
その値を変数rに代入し、printで出力しているわけです。

先ほどやったことと同じように、関数に処理を加えることができました。
デコレータはこう言った処理を元の関数を書き換えずに行うことができるのですが、
この方法だと最後の呼び出し実行時にデコレータだと理解して書かないといけないので、
複雑でわかりにくい面があります。


デコレータの書き方

このわかりにくさを避けたいので、デコレータは@を使って次のように書くことができます。
"""

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

@print_passage
def add_calc(a, b):
	return a + b

r = add_calc(10, 100)
print(r)
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 110

"""
違いがわかるでしょうか。

デコレータは、元の関数の上に@をつけて処理を加えたい関数名を記述すればいいだけです。
実行する時も元の計算したい関数に引数を入れて出力しているだけなので、
わかりやすいと思います。

同じ結果が得られています。
コードのわかりにくさ、複雑さの違いを確認しておきましょう。
"""


print("--- デコレータの使い方 ---")


"""
デコレータの便利なところは、一度デコレータのコードを書いておけば、
違う関数を使う時に同様にデコレータを使うことができる点ですね。


デコレータを何度も使う
"""

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

@print_passage
def add_calc(a, b):
	return a + b

r = add_calc(10, 100)
print(r)

@print_passage
def multiplication_calc(a, b):
	return a * b

r2 = multiplication_calc(10, 100)
print(r2)
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 110
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 1000

"""
このようにデコレータは一度書いてしまえば、何度も使えるということがわかりますね。


２つのデコレータを使う

今度は、デコレータを複数作って使う場合について見ていこうと思います。
ここでは2つのデコレータを用意することにします。
先ほどのコードに、もう１つ次のデコレータのコードを加えてみましょう。
"""

def print_info(func):
	def info(*args, **kwargs):
		print('関数の情報を表示します。')
		print('関数名:', func.__name__)
		print('引数の値:', args)
		print('キーワード:', kwargs)
		result = func(*args, **kwargs)
		return result
	return info

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

@print_info
def add_calc(a, b):
	return a + b

r = add_calc(10, 100)
print(r)
# 関数の情報を表示します。
# 関数名: add_calc
# 引数の値: (10, 100)
# キーワード: {}
# 110
"""
関数の情報を表示する処理を行っています。
func.__name__ というものが見慣れ無いと思いますが、
引数で渡した関数の名前を出力するということだけ今は理解しておきましょう。
引数の値と、ここでは使っていませんがキーワードも表示するようにしています。
あとは計算結果ですね。

それぞれ情報が表示されているのがわかります。
（見やすくするために、print_passage関数のデコレータの表示を閉じています。）
これで２つのデコレータの用意ができました。
複数のデコレータを使うには、デコレータを重ねることで使うことができます。
2つ用意したデコレータを一緒に使ってみましょう。
ただし、今回の場合は使い方が２通りあります。
どちらのデコレータを上にするかで挙動が違います。
"""

print("まずはこちらのデコレータの使い方です。")

def print_info(func):
	def info(*args, **kwargs):
		print('関数の情報を表示します。')
		print('関数名:', func.__name__)
		print('引数の値:', args)
		print('キーワード:', kwargs)
		result = func(*args, **kwargs)
		return result
	return info

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

@print_info
@print_passage
def add_calc(a, b):
    return a + b

r = add_calc(10, 100)
print(r)
# 関数の情報を表示します。
# 関数名: passage
# 引数の値: (10, 100)
# キーワード: {}
# 計算を開始します
# 計算が終了しました。結果を表示します。
# 110
"""
まずはこちらのデコレータの使い方です。

次はこちらのデコレータの使い方です。
"""

print("次はこちらのデコレータの使い方です。")

def print_info(func):
	def info(*args, **kwargs):
		print('関数の情報を表示します。')
		print('関数名:', func.__name__)
		print('引数の値:', args)
		print('キーワード:', kwargs)
		result = func(*args, **kwargs)
		return result
	return info

def print_passage(func):
	def passage(*args, **kwargs):
		print('計算を開始します')
		result = func(*args, **kwargs)
		print('計算が終了しました。結果を表示します。')
		return result
	return passage

@print_passage
@print_info
def add_calc(a, b):
    return a + b

r = add_calc(10, 100)
print(r)
# 計算を開始します
# 関数の情報を表示します。
# 関数名: add_calc
# 引数の値: (10, 100)
# キーワード: {}
# 計算が終了しました。結果を表示します。
# 110
"""
デコレータを先ほどとは順序を逆にしています。
この２つの結果を比べて見ると、処理の流れが違っています。
このように、複数のデコレータを利用する場合は、
その使い方で挙動が違うと言うことを理解して使う必要があります。
"""


print("まとめ")


"""
Pythonの関数を使う時に、コードを変更することなく別の処理を加えたい場合は、
デコレータを使います。
デコレータは*argsと**kwargs、関数内関数、引数としての関数を持ちます。
これを変更を加えたい関数を引数にして実行すれば良いのですが、
コードが複雑になるので、関数の上に@を使ってデコレータを置くことで
処理がわかりやすくなります。
デコレータは一度定義すれば、あらたな関数が出てくるたびに
何度も利用することができます。
複数のデコレータは重ねて使うことができますが、
重ねる順番によって挙動が変わることも頭に入れて使いましょう。
デコレータもPython入門レベルでは少し難しいところでもあるので、
こういったものがあるということだけでも最初は頭に入れておきましょう。
"""


print("--- レコチョクのエンジニアブログ ---")
print("--- Pythonのデコレータについて理解した話 ---")


"""
先輩が読んでいた 『Effective Python 』を読んでいたのですが、
途中から何を書いているのかサッパリ分からなかったので、
レベルを一つ落として『入門 Python3 』で基礎から勉強しなおしている江藤です。
Python もう半年近くやってるんですが、まだ門の中にいるのかすら微妙なところです…
今回、Python のシンタックスシュガーのひとつである「デコレータ」
という機能について勉強しました。
デコレータとは、関数の上に “@デコレータ名” を書くと、
その関数に対して色んなことをしてくれる機能です。
例えば、特定のWebページを描画する関数の上に
デコレータ requires_login を付けると
関数が呼ばれたときに一緒にログインのチェックもしてくれる、
という機能が実現可能です。

@requires_login
def login_page():
    render_edit_page()

これは、以下と同じ動きをしてくれます。

	
def login_page():
    if is_authorized(current_user):
        render_edit_page()
    else:
        redirect_403_page()

このような書き方を利用したことは何度もあったのですが、
その中身はどうなっているのか分かっていませんでした。
この、requires_login って一体どんな中身を書いているのでしょう…？
これって自分で作ろうと思ったら、何をしないといけないのでしょう…？

今回、『入門 Python3 』を読んで仕組みから理解しました。
この記事は勉強した内容のまとめです。
"""


print("デコレータの正体")


"""
Python のデコレータが行っているのは、関数の上書きです。
(Java的には上書きだと「Override」ですが、
PythonのデコレータはServletの「Filter」に近いと思います。)
Pythonでは関数も第一級オブジェクトのため(今回はじめて知りました…)、
関数を関数の引数や返り値として使うことが出来ます。
関数を関数の引数や返り値として使うことで何が出来るのか、
を実際にコードで試しながら考えてみます。
ログインチェックの例は複雑すぎて分かりにくいので、
もうちょっとシンプルな例でいきます。
以下の関数 add_two_ints は引数に取った二つの整数を足します。
"""

def add_two_ints(a: int, b: int):
	return a + b

add_two_ints(3, 5)

"""
出力結果は…

なにも出ません。print 文がないので当然なのですが。
この関数を上書きして、計算結果を出力させるようにします。
"""

def print_result(func):
	def new_func(*args, **kwargs):
		result = func(*args, **kwargs)
		print(result)
		return result
	return new_func

def add_two_ints(a: int, b: int):
	return a + b

add_two_ints = print_result(add_two_ints)
add_two_ints(3, 5)    # 

"""
(詳しくは割愛しますが、args, kwargsには、関数funcの引数リストが入っています)
print_result 関数で何が起こっているか上から見ていくと

    引数として関数 func を取っている
    ローカル関数 new_func の中で func を実行しつつ、
     その返り値を出力している
    new_func の中で func の結果を返している
     (これがないと、上書き後の関数が値を返さなくなってしまいます)
    print_result の返り値として、ローカル関数 new_func を返している

という流れです。
そして、最後から二番目の行で、
add_two_ints という関数に print_result の結果を代入することで、
add_two_ints の実行内容は new_func で定義した中身に上書きされます。
出力結果は…
8
と、計算結果を自動的に出力してくれるようになりました！
Python のデコレータとは、この代入処理を
”アットマーク”を用いた構文で書いているだけで、
先ほどの例を次のように書き直すだけで、デコレータを使うことが出来ます
"""

def print_result(func):
	def new_func(*args, **kwargs):
		result = func(*args, **kwargs)
		print(result)
		return result
	return new_func

@print_result
def add_two_ints(a: int, b: int):
	return a + b

# add_two_ints = print_result(add_two_ints) ← いらないのでコメントアウト
add_two_ints(3, 5)    # 8

"""
出力結果は…
8
と、先ほどと同じ結果が返ってきました。
関数を返す関数、というのがデコレータの正体です
"""


print("ちょっとだけ応用")
print("デコレータを複数つける")


"""
デコレータは複数付けることが出来るようなので、
引数を出力する関数も作り、デコレータとしてくっつけてみましょう。
"""

def print_args(func):
	def new_func(*args, **kwargs):
		print(args)
		print(kwargs)
		return func(*args, **kwargs)
	return new_func

def print_result(func):
	def new_func(*args, **kwargs):
		result = func(*args, **kwargs)
		print(result)
		return result
	return new_func

@print_args
@print_result
def add_two_ints(a: int, b: int):
	return a + b

add_two_ints(3, 5)
print()
add_two_ints(a=3, b=5)
# (3, 5)
# {}
# 8

# ()
# {'a': 3, 'b': 5}
# 8

"""
これで、引数も表示されました。
ちなみにですが、この例で分かるように
*args には 位置引数のタプルが、
**kwargs にはキーワード引数の辞書が入っています。
"""


print("デコレータに引数を付ける")


"""
デコレータ自体に引数を渡して、
それによって振る舞いを変えたいというときがあると思います。
デコレータにも引数を渡すことは可能です。
例として、引数にとったメッセージを処理の前後で表示する
print_message を書いてみました。
"""

def print_result(func):
	def new_func(*args, **kwargs):
		result = func(*args, **kwargs)
		print(result)
		return result
	return new_func

def print_message(start_message: str, end_message: str):
	def _print_args(func):
		def new_function(*args, **kwargs):
			print(start_message)
			result = func(*args, **kwargs)
			print(end_message)
			return result
		return new_function
	return _print_args

@print_message('処理開始', '処理終了')
@print_result
def add_two_ints(a: int, b: int):
	return a + b

add_two_ints(3, 5)
# 処理開始
# 8
# 処理終了

"""
出力結果は
	
処理開始
8
処理終了

となります。
"""


print("複数のデコレータを書いたときの処理の順番")


"""
上記の例を見て気付いた方がいらっしゃると思いますが、
「8」と「処理終了」の出力順番は必ずしもこうなるとは限りません。
どちらも “func の処理が終わったら” としか書いていないからです。
これは、仕様として決まっていて、
デコレータは下に書かれているものから順番に実行されます。
一番下のデコレータで返ってきた結果が、
次のデコレータの func 引数として渡ります。

実際

@print_message('処理開始', '処理終了')
@print_result
def add_two_ints(a: int, b: int):
    return a + b

を
	
@print_result
@print_message('処理開始', '処理終了')
def add_two_ints(a: int, b: int):
    return a + b

とすると、出力結果も変わり

	
処理開始
処理終了
8

となります。

この順番の仕様を勘違いしていると、想定外の処理が起こる可能性があります。
(私は最初上から順に実行されると思っていて「あれ？思った結果と違う」
となっていました…)
"""


print("おわりに")


"""
デコレータを使うと、関数にコードを書き足すことなく、機能を追加することが出来ます。
「この処理、どこにでも出てきてるじゃん」、という処理や
「この処理、本来は関数中に含めない方がいいじゃん」という処理があれば、
今後はデコレータ化するという選択肢も考えながら設計が出来ればと思います。
(と同時に、なんでもデコレータ化したがる”デコレータ病”にならないように気をつけます…)
"""



print("--- TechAcademyマガジン ---")
print("--- Pythonのデコレータについて現役エンジニアが解説【初心者向け】 ---")


"""
初心者向けにPythonのデコレータについて現役エンジニアが解説しています。
デコレータとは、関数の中身を書き換えずに関数を修飾するための仕組みです。
関数の引数に関数を指定します。
既存の関数の先頭に@デコレータ関数名とすることで、
関数を修飾することが出来ます。
"""


print("デコレータとは")


"""
デコレータとは、関数の中身を書き換えずに関数を修飾するための仕組みです。
ライブラリ内の関数の機能を変更したいときなどに役立ちます。
また、自身でクラスメソッドやスタティックメソッドを定義する際には
@classmethodや@staticmethodと記述するのがPythonでは一般的となっています。
"""


print("デコレータの使い方")


"""
デコレータは以下のような構文で記述できます。

@デコレータ関数名

def 修飾される関数名:

   ・・・

要は既存の関数の先頭に「@デコレータ関数名」と付けるだけで
簡単に関数を修飾できるわけです。
ただし、この構文はシンタックスシュガー（糖衣構文）と呼ばれ、
簡単に書ける代わりにプログラムの流れが初心者にはわかりにくい
というデメリットがあります。
苦い薬（=複雑なプログラム）が砂糖（=簡略化した構文）
でコーティングされているというわけですね。
"""


print("実際に書いてみよう")


"""
ここでは本質を理解するために、
まずはあえて@を使わずにデコレータを実装してみたいと思います。
これから書くコードはもちろん@を使っても書くことができます。
まず、コードの概要をご説明します。

    デコレータ関数deco()を定義する
    deco()は関数を引数funcで受け取るように設計する
    deco()の中にwrapper()関数を定義し、この中で元々の関数を修飾する
    deco()の戻り値として、修飾した関数のオブジェクトを返すように設計する

ここで、wrapper()は関数内関数なので、
引数funcを受け取っている点に注意が必要です。
【@なしでコーディングした場合】
"""

def deco(func):
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		print('今日はいい天気ですね！')
		return res
	return wrapper

def print_something(str):
	print(str)

print_something = deco(print_something)
print_something('hello!')
# hello!
# 今日はいい天気ですね！

"""
通常のprint_something()の出力の後に「今日はいい天気ですね！」
という一言を添えることができました。
このような感じで関数を装飾できるのです。
それでは次は上のソースコードを@を使って書いてみます。
【@を使ってコーディングした場合】
"""

def deco(func):
	def wrapper(*args, **kwargs):
		res = func(*args, **kwargs)
		print('今日はいい天気ですね!')
		return res
	return wrapper

@deco
def print_something(str):
	print(str)
print_something('hello!')
# hello!
# 今日はいい天気ですね!

"""
先ほどと同等の実行結果が得られました。
ソースコードの違いは、修飾したい関数定義の先頭に@decoを付けたのと、
print_something = deco(print_something)の行を削除した点です。
つまり、@decoと記述することによって
既存の関数を新しい関数で置き換えているわけですね。
"""


print("まとめ")


"""
この記事ではデコレータについてご紹介しました。
関数内で関数を定義するのでなかなか動きがわかりづらいデコレータですが、
一度理解してしまえば非常に便利な機能です。
最初は少し大変かもしれませんが、頑張って理解するようにしましょう。
"""



print("--- 藤の手帳 ---")
print("--- [Python]デコレータを理解する ---")


"""
デコレータは関数やクラスの前後に処理を追加するものですが、
その動きや書き方がいまいち腑に落ちず、放置していました。
しかし、DjangoやFlaskなど、他のパッケージを触っていると出てきますし、
よくわからないまま触るのも気持ちが悪く、この際ちゃんと理解しようと思ってまとめました。
"""


print("デコレータとは何か")


"""
デコレータの役割は、関数やクラスを書き換えずに処理を追加することです。
デコレータは関数であり、その構造は、基本的には引数として関数やクラスを受け取ります。
そして関数やクラスを返します。
次のような単純な関数に処理を付け加えたい、と思ったとします。
"""

def hello():
	print('Hello')

hello()

"""
追加の処理は、出力される「Hello」の前後に線を足す、というものにしましょう。
普通に考えるなら、関数を直接書き換えるか、
新しく関数を作ってその中で実行させると思います。
次のような感じでしょうか。
"""

def print_line():
	print('-----------')
	hello()
	print('-----------')

def hello():
	print('Hello')

# def hello():
#     print('----------')
#     print('Hello')
#     print('----------')

# hello()
print_line()
# -----------
# Hello
# -----------

"""
上記「sample.py」で定義した「print_line関数」は、デコレータではありません。
デコレータとして新しく関数を作るなら、関数を受け取り、
関数を返すものにする必要があります。
そのために関数内関数を定義し、戻り値として返します。
※ただし、戻り値となる関数には()をつけないこと。
実際に書き換えてみましょう。
"""

def print_line(func):
	def wrapper():
		print('----------')
		func()
		print('----------')
	return wrapper

"""
そしてデコレート（装飾）される側の関数定義の上に「@関数名」をつけます。

@装飾する関数
def 装飾される関数:
内容

装飾される関数()
"""

def print_line(func):
	def wrapper():
		print('----------')
		func()
		print('----------')
	return wrapper

@print_line
def hello():
	print('Hello')

hello()
# ----------
# Hello
# ----------

"""
これで「hello()」が実行されるときには、
「print_line」が自動的に呼ばれるようになります。

ポイント

    機能追加のための関数を定義する。
    ただし、その関数は引数に関数を受け取り、関数を返すもの。
    元の関数の上に「＠関数名」
    呼び出すときには元の関数だけで良い。


デコレータのメリット

デコレータの関数定義はわかりづらく、その中身の処理を追っていくのが難しいものです。
先に例示した「sample.py」のように書く方がはるかにわかりやすいでしょう。
なんでこんな書き方をするのだろう、
そもそもデコレータにメリットはあるのだろうかと考えていました。
私なりに、デコレータが元の関数やクラスを装飾するものであるなら、
関数やクラスを受け取って返す書き方は理にかなっている、という結論に至りました。
また「＠」をつけて表記することで、ここでなにかしらの機能を追加しているのだな、
とすぐ目につきます。
現状はまだ使いこなせていないためこのような感想しか出てきませんが、
複数のライブラリでも使われていることから
使い道は多いのだろうということはわかります。
"""


print("処理の流れを追う")


"""
デコレータがひとつの場合

デコレータでつまずきやすいのは、処理の流れだと思うので、
その流れを追っていきたいと思います。
またさっきの「hello.py」を使用し、デコレータと「hello()」
の呼び出しをコメントアウトします。
デコレータを使わずにデコレータを使ったのと同じ結果を得ようとすると、
次のような実行文を書きます。
"""

def print_line(func):
	def wrapper():
		print('----------')
		func()
		print('----------')
	return wrapper

# @print_line()
def hello():
	print('Hello')

# hello()
print_line(hello)()
# ----------
# Hello
# ----------

"""
print_line(hello)()

あまり見たことがない形です。

この文が実行されたときと、デコレータを使って「hello()」が呼ばれたときは、
ほぼ同じ処理をしているので、
この文の実行の流れを見ることでデコレータを理解していきましょう。

次の順序で実行されます。

    print_line(hello)が実行されます。

    そしてこのprint_lineは、内部でwrapperを返します。

    呼び出しもとに帰ってきたwrapperはそこで（）と合わさり実行されます。

    wrapper内部で、その外側の関数――print_line――
    の引数であるhelloが実行されます。


print_line(hello)()
|---------------|
     wrapper  +  ()
     |------|
      hello()


2.の補足。
関数に()をつけないと関数は実行されません。関数オブジェクトが返されます。

$ python
Python 3.10.0 (default, Oct 12 2021, 16:02:08) [GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def func():
...     print(1)
... 
>>> func()
1
>>> func
<function func at 0x7fc87d1615a0>


4.の補足。
関数内関数は、その外側の関数のものを使うことができます。

>>> def print_number(num):
...     def inner():
...             print(f'number: {num}')
...     inner()
... 
>>> print_number(100)
number: 100


デコレータがふたつあった場合

今度はデコレータがふたつの場合の流れを追ってみましょう。
「hello.py」ではなく、別のものを作りました。
"""

def decorator1(func):
	def wrapper1():
		print('wrapper1内で関数の実行前')
		func()
		print('wrapper1内で関数の実行後')
	print('decorator1がwrapper1を返す')
	return wrapper1

def decorator2(func):
	def wrapper2():
		print('wrapper2内で関数の実行前')
		func()
		print('wrapper2内で関数の実行後')
	print('decorator2がwrapper2を返す')
	return wrapper2

@decorator1
@decorator2
def myfunc():
	print('被装飾関数の実行')

if __name__ == '__main__':
	myfunc()
# decorator2がwrapper2を返す
# decorator1がwrapper1を返す
# wrapper1内で関数の実行前
# wrapper2内で関数の実行前
# 被装飾関数の実行
# wrapper2内で関数の実行後
# wrapper1内で関数の実行後
"""
「decorator1」の内部には「wrapper1」、
「decorator2」の内部では「wrapper2」が定義されていて、myfuncが実行されます。
出力がどういうものになるか想像できるでしょうか？
実際にやってみましょう。

$ python deco.py 
decorator2がwrapper2を返す
decorator1がwrapper1を返す
wrapper1内で関数の実行前
wrapper2内で関数の実行前
被修飾関数の実行
wrapper2内で関数の実行後
wrapper1内で関数の実行後

今度も前項のようにデコレータを使わずに呼び出そうとすると、
「myfunc()」の部分を次のように変えます。

decorator1(decorator2(myfunc))()

処理の流れは、

    decorator2が実行され、wrapper2を返します

    decorator1が実行され、wrapper1を返します

    wrapper1が実行され、その外側のdecorator1の引数である
    wrapper2を実行します

    wrapper2が実行されると、その外側のdecorator2の引数である
    myfuncを実行します

decorator1(decorator2(myfunc))()
           |------------------|
decorator1(     wrapper2     )
|-------------------------------|
            wrapper1             ()


このようにデコレータの実行順は、装飾される関数に近い方から、
コードから見ると下から上に向かって順に実行されます。

# decorator2 → decorator1の順
@decorator1
@decorator2
def myfunc():
    print('被装飾関数の実行')


if __name__ == '__main__':
    myfunc()
"""


print("注意が必要な仕様")


"""
デコレータを使うときに注意が必要なことが２つありました。

    デコレータは定義されたところで実行される
    元の関数の名前が置き換わる

定義されたところで実行される

つぎのモジュールを実行すると何が起きると思いますか？
"""

def print_test(func):
	print('test')
	def wrapper():
		func()
	return wrapper

@print_test
def myfunc():
	print('myfunc')
# test
myfunc()    # myfunc
"""
定義しか書いてないから何も起きない。
というのはちょっと違います。

$ python test.py 
test

print_test内の「print('test')」が実行されています。
デコレータ定義時に実行されたようで、最初に気づいたときには、
予期しないものだったので驚きました。
「myfunc()」と呼び出し文を末尾に追加して実行すると、

$ python test.py 
test
myfunc

意図通りの出力にはなりますが、
printなどの実行文はwrapper内で定義した方が良いかもしれません。
関数の名前が置き換わる

対話モードで起動して実例を見てもらいます。

$ python
Python 3.10.0 (default, Oct 12 2021, 16:02:08) [GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def test():
...     pass
... 
>>> test.__name__
'test'

test関数の名前は「test」です。
これは何もおかしくありません。

しかし、デコレータを使うと、この名前が置き換わります。

>>> def decorator(func):
...     def wrapper():
...             func()
...     return wrapper
... 
>>> @decorator
... def test():
...     pass
... 
>>> test.__name__
'wrapper'
>>> test(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: decorator.<locals>.wrapper() takes 0 positional arguments but 1 was given

「wrapper」に変わってしまいました。
これではエラー処理のときなど不便です。

これを解消するための標準ライブラリがあります。
デコレータの「functools.wraps」です。

>>> from functools import wraps
>>> def decorator(func):
...     @wraps(func)
...     def wrapper():
...             func()
...     return wrapper
... 
>>> @decorator
... def test():
...     pass
... 
>>> test.__name__
'test'
>>> test(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: test() takes 0 positional arguments but 1 was given

デコレータの引数の関数をwrapsデコレータに渡しています。

元の関数名もそのままですね。
"""





