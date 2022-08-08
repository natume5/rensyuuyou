#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- テンプレートエンジンの使い方（jinja2） ---")


"""
jinja2とは「python用の、htmlを動的作成できるテンプレートエンジン」です。
Webアプリケーションを作成する際に役立つもので、
Flaskという有名なWebアプリケーションフレームワークでも使われています。
ここでは「jinja2とは？」「jinja2はどうやって使うの？」といった方に向け、
jinja2について解説します。
"""


print("--- jinja2のインストール ---")


"""
まずはjinja2をインストールしましょう（ここではpipを使ってインストールしますが、
Anacondaでも環境作成は可能です）。

次のコマンドを実行します。

$ pip install Jinja2

これでjinja2がインストールされました。


jinja2の使い方

テンプレート文字列を使う

では一番シンプルな使い方から見ていきましょう。
Template()にテンプレート文字列を渡し、render()で結果を出力します。
"""

from jinja2 import Template

tmp_s = 'Hello {{name}}!'
template = Template(tmp_s)
ren_s = template.render(name='佐藤')
print(ren_s)
















