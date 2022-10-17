#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- プロパティ ---")


print("--- 属性へのアクセス ---")


"""
これまで見てきたように、Pythonで属性にアクセスする際は
 [オブジェクト名.メンバ名] の形式で記述しました。
 ですが、例えば「参照するときはカッコを付けたい」
 「更新するときはチェックをしたい」「削除処理を禁止したい」など、
 アクセスする際に処理を挿入するような要件がでてくるかもしれません。
 この時、専用のsetter、getter、deleterを作成すると問題は解決しますが、
 毎回それらの専用メソッドを呼びださなければ効果がでません。
 また、クラスを利用する側がかならずそれらのメソッドを利用してくれる保証もありません。
"""

class Sample:

	def __init__(self):
		self.text = 'sample'

	def get_text(self):
		return '({0})'.format(self.text)

	def set_text(self, text):
		if text is None:
			self.text = ''
		else:
			self.text = text

	def delete_text(self):
		pass

# いちいち専用メソッド経由でアクセスしなければならない・・・
obj = Sample()

print(obj.get_text())    # (sample)

obj.set_text(None)

obj.delete_text()


print("--- プロパティ ---")


"""
これでは、せっかくのgetter、setterなしで気軽にアクセスできる
Pythonの特徴が活きてきません。
ところが、Pythonには通常のアクセスの記述をしつつ
専用メソッド経由で処理を行うプロパティとよばれる組込みデコレータがあります。
上のコードをプロパティを用いて書きなおしてみましょう。
"""

class Sample:

	def __init__(self):
		self.__text = 'sample!'

	@property
	def text(self):
		return '({0})'.format(self.__text)

	@text.setter
	def text(self, text):
		if text is None:
			self.__text = 'None'
		else:
			self.__text = text

	@text.deleter
	def text(self):
		pass

# 通常のアクセス方法で利用できる！！
obj = Sample()
print(obj.text)    # (sample!)

obj.text = None
print(obj.text)    # (None)

del obj.text
print(obj.text)    # (None)

"""
通常のアクセスで専用メソッド経由で処理がされるようになりました。
以下にプロパティをまとめます。

プロパティ 	             役割
@property 	         getter
@属性名.setter 	     setter
@属性名.deleter 	     deleter
"""


print("--- プロパティの注意点 ---")


"""
上のコードですが、疑問に思われた点はないでしょうか？
そう、修正したコードはアンダースコアを2つつけたプライベートなメンバ名になっています。
setterを利用する際はかならずプライベートなメンバにしないと、
無限再帰処理に入る、という問題が発生します。
仮にプライベートにしない場合、
先ほどの処理のsetter部分は以下のようになります。

self.text = text

ここでまたにsetterが呼び出され、
さらにsetterが呼び出され、、、というループに入ってしまいますので注意してください。
"""
