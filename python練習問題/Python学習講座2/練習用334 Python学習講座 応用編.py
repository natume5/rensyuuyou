#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Tkinterで電卓を作ってみよう 前編 ---")


"""
それではいよいよここから、
これまで学んだ内容を総合して電卓のデスクトップアプリを作成してみましょう。
"""


print("--- デザインの作成 ---")


"""
通常、GUIアプリケーションを開発する際、
よほど簡単なものでない限りはドローツールや専用のCAD等を使用して
画面デザインのの設計から行います。
いきなりコードを書くのではなく、
手書きやExcel方眼紙などでもかまわないので
一旦配置位置を作成してから開発することをおすすめします。
今回は以下のような座標でウィジェットを配置しましょう。
配置座標の計算を簡単にするため30px間隔にしています。


機能の解説

先程のデザイン図ですが、簡単にウィジェットの説明をします。

エントリーと各種ボタン

0～9、小数点ボタン、演算ボタンをクリックすると、
その入力値がエントリーに表示されます。

イコールボタン

イコールボタンをクリックすると、エントリー上の数式が計算され、
計算結果がエントリー上に表示されます。

Cボタン

エントリー上の値がクリアされます。
少し不格好ですが、
解説の本筋から外れるため細かいエラーハンドリングや
入力制限は今回省略することにします。

イベントハンドラ

上の各ウィジェットの動作をまとめると、
イベントハンドラは以下3つが必要となります。

    数字、小数点、演算をクリックした際のイベントでエントリーに入力する
    イコールボタンをクリックした際のイベントでエントリーに入力された数式を計算する
    Cボタンをクリックした際のイベントでエントリーをクリアする
"""


print("--- プロトタイプ：0と1の足し算だけできる電卓 ---")


"""
電卓アプリのような簡単なものは最初から全部実装してもいいのですが、
今回は解説の都合も兼ねてまずは2ボタンの足し算だけの電卓を
プロトタイプとして作成してみることにします。
"""

from tkinter import StringVar, Tk, Button, Entry


entry_text = ""
entry_var: StringVar


def press_0_event_handler():
	global entry_text
	entry_text = entry_text + str(0)
	entry_var.set(entry_text)

def press_1_event_handler():
	global entry_text
	entry_text = entry_text + str(1)
	entry_var.set(entry_text)

def press_pulse_event_handler():
	global entry_text
	entry_text = entry_text + '+'
	entry_var.set(entry_text)

def press_equal_event_handler():
	try:
		global entry_text
		total = str(eval(entry_text))
		entry_var.set(total)
		entry_text = str(total)

	except:
		# 0除算等、エラー発生時
		entry_var.set('ERR!')
		entry_text = ''

def main():
	root = Tk()

	global entry_var
	entry_var = StringVar()

	num_entry = Entry(root, textvariable=entry_var)
	num_entry.pack()

	btn0 = Button(root, text='0', command=press_0_event_handler)
	btn0.pack()
	btn1 = Button(root, text='1', command=press_1_event_handler)
	btn1.pack()
	plus = Button(root, text='+',
		command=press_pulse_event_handler)
	plus.pack()
	equal = Button(root, text='=',
		command=press_equal_event_handler)
	equal.pack()

	root.mainloop()

if __name__ == '__main__':
	main()

"""
ずいぶん不格好ですが、
以下のような0、1の足し算ができる電卓が起動しします。

コードの解説をします。
モジュール変数のentry_textは一時的な値を計算するために使用し、
entry_varはその結果を表示します。
main関数の中で、ウィンドウを生成した後
Entryと0、1、+、=の4つのButtonウィジェットを配置しています。
それぞれのボタンにはイベントハンドラとして
press_XXX_event_handlerという名称の関数を指定しています。
また、=ボタンをクリックすると、
press_equal_event_handlerが実行されますが、
これはEntryに入力された数式をeval関数で計算し、
結果を表示する仕組みになっています。
"""


print("--- 高階関数の活用 ---")


"""
ところで、上のコードでイコール以外の
press_XXX_event_handlerはほとんど内部が同じ関数です。
この後0～9の10ボタンと演算子の分、
同様の処理を書くのはなかなか大変そうですが、
こういった場合は高階関数を使用するときれいに書くことができます。

例えば、以下のようにすると他のボタンに対しても使いまわしすることができます。

def press_num_ope_event_handler(key):
    def handler():
        global entry_text
        entry_text = entry_text + str(key)
        entry_var.set(entry_text)

    return handler

:
btn0 = Button(root, text='0', command=press_num_ope_event_handler(0))
btn1 = Button(root, text='0', command=press_num_ope_event_handler(1))
:

GUIではイベント処理時に関数を引数や戻り値として扱うことが多い、
ということは知っておくとPythonに限らずGUI開発の役に立つと思います。
"""
