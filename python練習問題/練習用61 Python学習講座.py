#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- sphinx入門 その2 コード内のdocstringの記述---")


"""
前回はsphinxによるソースコードからのドキュメント自動生成について学習しました。
今回はコード内のdocstringの記述方法について学習します。
pythonのdocstringの記法はEpytext、google、Numpydocなどがあるのですが、
ここではPEP287で推奨されているreSTでのdocstringの書き方について説明します。


docstringの書き方

クラス概要

クラス定義の直下にダブルクォート3つで囲った部分に記述します。

クラス属性

クラス属性には属性の宣言直下にdocstringを記述するか、直前に「#: コメント」と記述します。

関数・メソッド

概要はクラスと同様、定義の直下にダブルクォート3つで囲った部分に記述します。
パラメータ、戻り値、型情報について:field:というフィールドを使って記述します。

""""""
:param int arg1: 引数の説明
""""""

パラメータの型は上記のように:paramの後に続けて書いても良いですし、
以下のように:paramと:typeを分けて記述することも可能です。

""""""
:param arg2: 引数
:type arg2: int
""""""
"""

"""
Sample機能提供モジュール
"""

class Sample:
	"""
	sample機能を実装したクラスです。
	"""

    bar = 1
    """ xxを保持するメンバです """

    # yyを保持するメンバです
    foo = 1

    def __init__(self):
    	"""
    	初期化処理を行います。
    	"""
    	self.x = 'hoge'


    def add(self, arg1, arg2):
    	"""
    	引数で指定した値を足し算して返します。 ''arg1 + arg2''

    	:param int arg1: 足される値。
    	:param arg2: 足す値。
    	:type arg2: int
    	:rtype: int
    	:return: 足し算した結果。
    	"""
    	return a + b

"""

"""








