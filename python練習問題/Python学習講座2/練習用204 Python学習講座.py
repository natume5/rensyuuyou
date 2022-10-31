#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- traceback スタックトレースの取得 ---")


print("--- tracebackモジュール ---")


"""
基本的な使い方

try文で例外処理は施したものの、
どういった原因かを調査するためにスタックトレースを
ログなどに出力したい場合があります。
JavaのprintStackTrace等、
言語によっては例外オブジェクト自身に
スタックトレースを表示したり取得するメソッドが予め用意されていますが、
Pythonの場合は標準ライブラリのtracebackを
別途インポートして使用する必要があります。
まずは簡単な例で使い方を見てみましょう。
"""

"""
import traceback

try:
	hoge = 1/0
except Exception as e:
	# 文字列を取得する　format_exec()メソッド
	print("エラー情報\n" + traceback.format_exc())
"""

"""
以下のように出力されます。

エラー情報
Traceback (most recent call last):
  File "trace_back_sample.py", line 4, in <module>
    hoge = 1/0
ZeroDivisionError: division by zero


Traceback (most recent call last):
  File "D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題\Python学習講座2\練習用204 Python学習講座.py", line 30, in <module>
    hoge = 1/0
ZeroDivisionError: division by zero


tracebackオブジェクトの取得とファイルへの保存

tracebackに用意されている、print_exc()メソッドを使用すると、
ファイルに出力することができます。
実務上ではloggingの設定を使用して
ファイル出力する場合のほうが多いと思いますが、参考として掲載します。
sys.exc_info()の(0から数えて)
2番目の戻り値にトレースバックオブジェクトが格納されていますので、
それを使用します。
また、トレースバックのみ取得したい場合はprint_tb()メソッドを使用します。
"""

import traceback, sys

# トレースバックと例外情報の取得
try:
	hoge = 1/0
except Exception as e:
	# fileを指定しない場合はsys.stderr(標準エラー)に出力
	with open("error.log", "a", encoding='UTF-8') as f:
		traceback.print_exc(file=f)

# トレースバックのみ出力
try:
	hoge = 1/0
except Exception as e:

	# ファイルに出力する print_tb
	tb = sys.exc_info()[2]
	# fileを指定しない場合はsys.stderr(標準エラー)に出力
	with open("error.log", "a", encoding='UTF-8') as f:
		traceback.print_tb(tb, file=f)
