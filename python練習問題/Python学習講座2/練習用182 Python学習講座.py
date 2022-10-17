#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- クラスデコレータ ---")


print("--- 型オブジェクト（クラスオブジェクト）の復習 ---")


"""
型オブジェクト（クラスオブジェクト）で説明したとおり、
Pythonではクラスもただのオブジェクトですので、
変数にセットして関数の引数や戻り値として扱うことができます。
"""

def add_member(cls):
	""" 型オブジェクト(クラスオブジェクト)に対し属性を追加する """

	cls.x = 'sample'

	return cls

class Sample:
	""" 何もしないクラス """
	pass

NewSampleCls = add_member(Sample)    
# Sampleクラスから新たなクラスを作成する
obj = NewSampleCls()    # 新たなクラスをインスタンス化する
print(obj.x)    # Sampleクラスにはなかった属性xが取得できる  sample

"""
add_member関数は、型オブジェクトに対し、属性xを追加する関数です。
また、Sampleクラスには属性がありません。
ここでSampleクラスをadd_member関数に渡すと、
属性xを持つクラスが新たに作成されます。
実際にインスタンス化してみると、属性xを持つことが確認できます。
"""


print("--- クラスデコレータ ---")


"""
勘の良い方ならもうお気づきかもしれません。
そう、クラスデコレータは関数デコレータのクラス版、
つまりクラスの機能を追加・変更するデコレータです。
上のコードをデコレータを使った記述に変えてみましょう。
"""

def add_member(cls):
	""" 型オブジェクト(クラスオブジェクト)に対し属性を追加する """

	cls.x = 'sample'

	return cls

@add_member
class Sample:
	""" 何もしないクラス """
	pass

obj = Sample()    # Sampleクラスをインスタンス化する
print(obj.x)    # Sampleクラスにはなかった属性xが取得できる

"""
関数デコレータと同様に、
元のクラスに変更を加えることなく機能追加をすることができました。
"""
