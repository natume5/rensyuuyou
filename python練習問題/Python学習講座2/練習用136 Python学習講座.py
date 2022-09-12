#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 識別子 ---")


"""
本格的な学習を始める前に、少々面倒ですが、
Pythonの識別子と予約語について学習しましょう。


識別子

プログラミングでは、さまざまなモノ（クラス、関数、変数など）
に対して名前をつけていく作業が発生します。こういった名前のことを識別子と呼びます。
識別子はある程度は自由にプログラマが決めることが可能なのですが、ある一定のルールがあり、
そこから逸脱すると実行に失敗したり予期せぬ動作を引き起こすことがあります。

識別子に利用できる文字

アルファベットの大文字、小文字、アンダースコア、半角数字が利用できます。
数字は識別子の先頭には使えません。
実は、ASCII以外の文字も利用できますが、本講座では利用しません。
詳しく知りたい方は、PEP-3131で調べてみてください。

予約語

また、制御に利用するような特定の文字列は一般的に予約語と呼ばれ、
識別子として利用することはできません。
Pythonでは予約語のことをkeywordとも呼びます。以下、Python3.8の予約語です。

False 	await 	else 	import 	pass
None 	break 	except 	in 	raise
True 	class 	finally 	is 	return
and 	continue 	for 	lambda 	try
as 	def 	from 	nonlocal 	while
assert 	del 	global 	not 	with
async 	elif 	if 	or 	yield

バージョンを重ねるにつれ増えているため、下記の公式ドキュメントも合わせて確認してください。

2.3.1. キーワード (keyword)

なお、手元の環境の予約語を調べる場合は
以下のPythonスクリプトを実行すると予約語がリストとして列挙されます。

from keyword import kwlist
print(kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
  'else', 'except', 'finally', 'for', 'from', 'global', 'if',
   'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
    'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


識別子の注意点

アンダースコアで始まる識別子は、特別な意味があります。
このページでは細かい説明を割愛しますが、アンダースコアをつけた識別子は、
インポートやクラスを利用する際の挙動に特徴がある、ということを覚えておきましょう。
"""
