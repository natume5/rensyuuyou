#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- sphinx入門 その1 ドキュメントの自動生成 ---")


"""
メジャーなプログラム言語ではプログラムのコメントから
ドキュメントを生成するライブラリがあります。
例えばjavaだとjavadocが有名ですね。
Pythonではsphinxというライブラリでドキュメントを生成することができます。
このページではdocstringからsphinxを用いてhtmlのドキュメントを生成してみましょう。
"""


print("--- sphinxとは ---")


"""
sphinxとはPythonドキュメントのために作られたpython製のドキュメント作成ツールです。
reStructuredText(reST)という形式のマークアップで扱います。
出力はwebで参照できるhtml形式以外に、LaTex形式等にも対応しています。
"""


print("--- 簡単な使い方 ---")


"""
ではサンプルを通して簡単な使い方について学習しましょう。
インストール

まずはインストールです。pipでインストール可能です。

pip install sphinx

サンプルプログラム

以下の構成のプログラムを題材としてみます。

プロジェクトディレクトリ
├── docs # 空のディレクトリ
├── html # 空のディレクトリ
└── sample # ソース
    ├── pkg # パッケージ
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   └── mod1.cpython-35.pyc
    │   └── mod1.py
    └── run.py

とりあえずpythonファイルはrun.py、
pkg/__init__.py、pkg/__init__.py、pkg/mod1.pyの3つ用意してみましょうか。
また、rstファイルのためのdocsディレクトリと
htmlドキュメントを格納するhtmlディレクトリを準備します。


run.py

# run.py
""""""
    メイン処理 
    ~~~~~~~~~~~~~~~~~~

    メインの処理を行うスクリプトです 

    概要 
    --------

    pythoのドキュメンテーションの説明用に作りました::


    :copyright: (c) 2017 by the Kuro.
    :license: BSD, see LICENSE for more details.
""""""

from pkg.mod1 import SampleClass

def main(arg):
    """""" 
    文字列を装飾して表示します 

    :param arg: パラメータ 
    :return: 文字列
    """"""
    obj = SampleClass(' ***** ')
    text = obj.func1(arg)
    print(text)


if __name__ == '__main__':
    main("python最高！！")

pkg/__init__.py

# pkg/__init__.py
""""""
    sampleパッケージ 
    ~~~~~~~~~~~~~~~~~~

    sampleパッケージの説明文です 

    概要 
    --------

    sampleパッケージです::


    :copyright: (c) 2017 by the Kuro.
    :license: BSD, see LICENSE for more details.
""""""
pkg/mod1.py

# pkg/mod1.py
""""""
sampleモジュール sampleクラス等の説明文
""""""


class SampleClass:
    """"""
    sampleクラスの説明文
    """"""

    def __init__(self, arg):
        """"""
        引数の文字列表現の前後を装飾する 

        :param arg: パラメータ 
        :return: 結果文字列
        """"""
        self.d_str = arg

    def func1(self, arg):
        """""" 
        引数の文字列表現の前後を装飾する 

        :param arg: パラメータ 
        :return: 結果文字列
        """"""
        result = self.d_str + str(arg) + self.d_str 
        return result 

rstの生成

sphinx-apidocコマンドを以下のように実行します。

sphinx-apidoc -F -o ./docs ./sample

docsディレクトリにファイルが生成されていることが確認できます。


htmlの生成

最後にhtmlを生成しましょう。
その前に、前の処理で生成されたconf.pyの以下のコードのコメントアウトを解除します。

# docs/conf.py
import os
import sys
sys.path.insert(0, '/home/....')

では生成です。
sphinx-buildコマンドを以下のように実行します。
htmlディレクトリ配下にhtmlドキュメントが生成されます。

sphinx-build -a ./docs ./html

生成されたhtmlの内容を確認してみましょう。
ブラウザhtml/index.htmlを確認すると以下のような画面が表示されます。
"""


print("--- コマンドオプション ---")


"""
sphinx-apidoc
オプション 	                       意味
-F 	          fullで生成します。指定しない場合はrstファイルのみ生成されます。
-f 	          出力時に強制上書きをします。
-o 	          出力先を指定します。
-H 	          プロジェクト名を指定します。
-A 	          authorを指定します。
-V 	          versionを指定します。

最初のサンプルではプロジェクト名にソースディレクトリ名が設定されますが、
例えばソースディレクトリがsrcなどの場合はHオプションで設定すると良いでしょう。


sphinx-build

以下の形式で記述します。

sphinx-build [options] 入力元 出力先 

オプション 	                          意味
-b 	             ビルダー（≒出力形式）を指定します。
                 デフォルトではhtmlですが、
                 xml、latexなどを指定することができます。
-a 	             すべての出力ファイルを書き出します。
                 このオプションをつけない場合は新規に作成されたり、
                 変更のあったソースファイルに関連する
                 出力ファイルだけを出力します。
"""


print("--- tips ---")


"""
sphinx-apidocですが、1回めに-Fオプションを指定してconf.pyを修正し、
2回め以降は-Fオプションを付ける、という方法でも良いのですが、
ゴミが残ったりビルドの失敗に気づかなかったりするので、
私は以下のようにrmとsedと組み合わせて毎回全部作り直しています。
linuxやmacを利用している方は参考にしてください。

rm -rf docs/*
rm -rf html/*
sphinx-apidoc -F -o ./docs ./sample
sed -i -e 's/# import os/import os/' docs/conf.py
sed -i -e 's/# import sys/import sys/' docs/conf.py
sed -i -e 's/# sys.path.insert/sys.path.insert/' docs/conf.py
sphinx-build -a ./docs ./html

ただし、後述しますがsphinxでドキュメントを自動生成したあと、
rstファイルを手動で追記することが多いです。
その場合はls、egrep、xargsを組み合わせて
特定ファイルは削除しないようにする必要があります。
"""
