#! -*- coding:utf-8 -*-


# テキストファイルを読み込んで中身を表示する
f1 = "fox.txt"
fileobj = open(f1, encoding="utf_8")
text = fileobj.read()
fileobj.close()
print(text)
"""
ファイルを開くopen()の完全な書式
open(file, mode="r", buffering=-l, encoding=None,
     errors=None, newline=None, clsefd=True, opener=None)

一般的に使われる簡易的な書式
ファイルを開く
open(file名, mode="r", encoding=None)

第一引数のfileはファイルの相対パスor絶対パス。modeではファイルのデータを
読み込むのか("r")、書き込むのか("w")、テキストファイルなのか、
バイナリデータなのかといったモードを指定する。
テキストの読み込み"rt"、追記"at"、バイナリの読み込み"rb"
modeを省略すると"rt"扱いになり、テキストファイルを読み込み専用モードで開く。

encodingはテキストファイルを読み込む場合に、そのテキストファイルのエンコーディングを
指定する引数。encodingを省略すると現在のプラットフォームと同じになる。
読み込もうとしたファイルとエンコーディングの指定が合っていないとエラーになる。

encoding　　　　説明
"utf_8"　　　　　UTF8
"euc_jp"　　　　日本語EUC
"iso2022_jp"　　JIS
"shift_jis"　　　Shift_JIS
"""
