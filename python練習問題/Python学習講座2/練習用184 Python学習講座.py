#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- ディスクリプタ ---")


print("--- ディスクリプタとは ---")


"""
特殊メソッド__get__、__set__、__delete__
のうちいずれかのメソッドが定義されたオブジェクトをディスクリプタと呼びます。
ディスクリプタをメンバにもつオブジェクトに対し、
そのメンバにアクセスしたときの挙動をカスタマイズすることが可能となります。
ディスクリプタそのものに対するアクセス時に
__get__、__set__、__delete__が実行されるわけではない点に注意してください。
まずはサンプルとしてディスクリプタを実装したサンプルを紹介します。
以下のコードでは、属性textをもったクラスMyDescriptorに
ディスクリプタを実装しています。
参照、更新、削除した際の挙動がカスタマイズされています。
"""

class MyDescriptor:
	""" ディスクリプタクラス """

	def __init__(self, text):
		self.text = text

	def __get__(self, instance, owner):
		return "* " + self.text

	def __set__(self, instance, text):
		self.text = text + "!"

	def __delete__(self, instance):
		del self.text
		print('text属性が削除されました')

class Sample:
	""" 属性にディスクリプタを持つ """
	descriptor = MyDescriptor('sample')

obj = Sample()
print(obj.descriptor)    # * sample

obj.descriptor = 'sample2'
print(obj.descriptor)    # * sample2!

del obj.descriptor    # text属性が削除されました
# print(obj.descriptor)    # AttributeError


print("--- ディスクリプタのメソッド ---")


"""
ではここから先程のサンプルを上から順に解説していきます。

__get__

メンバを参照した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバにアクセスした際に
__get__が呼び出されています。
このことにより、アクセスした結果に対し、先頭に*が付加されるようになっています。

__set__

メンバを更新した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバを更新した際に
__set__が呼び出されています。
このことにより、設定した内容に対し、末尾に!が付加されるようになっています。

__delete__

メンバを削除した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバを削除した際に
__delete__が呼び出されています。
このことにより、削除時にメッセージが表示されるようになっています。
"""



print("--- YUMARU BLOG ---")
print("--- 【Python】ディスクリプタの使い方について解説 ---")


"""
この記事では、Pythonのディスクリプタ(Descriptor)について解説します。
ディスクリプタを使うことでユーザー定義クラスの属性の
書き込み、読み込み、削除する際の動作をカスタマイズすることができます。
それでは、ディスクリプタの使い方を見ていきましょう❗️
"""


print("--- ディスクリプタとは？ ---")


"""
ディスクリプタとは、ディスクリプタプロトコルのメソッドが1つでも定義されている
オブジェクトのことを言います。

ディスクリプタプロトコル

    descr.__get__(self, obj, type=None) --> value
    descr.__set__(self, obj, value) --> None
    descr.__delete__(self, obj) --> None

上記のメソッドいずれかを定義したオブジェクトを
属性として参照させることでそれぞれのメソッドに対応した動作を
オーバーライドすることができます。
それぞれのメソッドが定義する動作は以下の通りです。

__get__ 	属性が参照された際の動作を定義します
__set__ 	属性が更新された際の動作を定義します
__delete__ 	属性が削除された際の動作を定義します

それでは、実際に定義して挙動を確かめてみましょう！
"""


print("--- ディスクリプタの使い方 ---")


"""
ディスクリプタは以下のように使用します。

    STEP1
    定義

    クラスとしてディスクリプタを定義します。

    class ディスクリプタ名:

        def __init__(self):
            # 省略可能
            
        def __get__(self, obj, objtype=None):
            # 参照する際の動作の定義
            return 戻り値

        def __set__(self, obj, value)
            # 更新する際の動作の定義

        def __delete__(self, obj)
            # 削除する際の動作の定義

    STEP2
    参照
    定義したディスクリプタをオブジェクトの属性として参照させます。

    class クラス名:

        変数名 = ディスクリプタ名()

    STEP3
    呼び出し
    あとは普通にインスタンス化し、
    その変数にアクセスすることで
    ディスクリプタプロトコルで定義した動作を呼び出すことができます。

    インスタンス名 = クラス名()

    インスタンス名.変数名
    # __get__が呼び出される

    インスタンス名.変数名 = なんかしらの値
    # __set__が呼び出される

    del インスタンス名.変数名
    # __delete__が呼び出される

サンプル

以下のコードでは、ディスクリプタで動的にプライベートな_valueを生成しています。
"""

# ディスクリプタ
class Descriptor:

	def __get__(self, obj, objtype=None):
		print('__get__')
		return obj._value

	def __set__(self, obj, value):
		print('__set__')
		obj._value = value

	def __delete__(self, obj):
		print('__delete__')
		del obj._value

class MyClass:

	value = Descriptor()

	def __init__(self, value):
		self.value = value

mc = MyClass(1)
# __set__

print(mc.value)
# __get__
# 1

mc.value = 100
# __set__

# ディスクリプタで動的に生成された「_value」にもアクセスできる
print(mc._value)
# 100

del mc.value
# __delete__

"""
ポイントは、MyClassクラスのコンストラクタでインスタンス変数を
初期化する際にもディスクリプタが呼び出されることです。
"""


print("--- まとめ ---")


"""
この記事では、Pythonのディスクリプタについて解説しました。
使いこなせばかなり色々できそうなポテンシャルを感じますね〜😄 
ディスクリプタはまだまだ奥深いのでさらに学びたい方は
公式ドキュメントを参照してください。
それでは今回の内容はここまでです。ではまたどこかで〜( ・∀・)ﾉ
"""



print("--- Pythonプログラミング日記 ---")
print("--- デスクリプタのサンプルプログラム ---")


"""
Pythonにはデスクリプタという仕組みがあり、
こいつを使えば何やらPythonチックなプログラムが書けるらしい。
『Python実践入門』を読みながら、さっそくサンプルプログラムを書いてみます。
まずは、価格を表すディスクリプタをPriceFieldクラスとして定義します。
"""
"""
class PriceField:
    def __set_name__(self, owner, name):
        """"""
        owner: このディスクリプタを使用するクラス
        name: このディスクリプタに割り当てられる変数名
        """"""
        self.ctax = owner.CTAX    # 消費税
        self.name = name

    def __set__(self, instance, value):
        """"""
        instance: プロパティに代入されるインスタンス
        value: 代入する値
        """"""
        # 数値以外は例外発生
        if not isinstance(value, float) and not isinstance(value, int):
            raise AttributeError('must be float or int')
        # 税込み価格を代入する
        instance.__dict__[self.name] = value * self.ctax

    def __get__(self, instance, owner):
        # 税込み価格を整数値にして返す
        return int(instance.__dict__[self.name])

""""""
次に、PriceFieldを使用するクラスとして、Bookクラスを定義します。
""""""

class Book:
    CTAX = 1.1
    price = PriceField()

    def __init__(self, title, price):
        self.title = title
        self.price = price

    @property
    def info(self):
        return f'{self.title}({self.price}円)'

book = Book('Python入門', 1000)
print(book, info)
"""
