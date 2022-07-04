#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- beautifulsoup4入門 htmlをパース、スクレイピングする---")


"""
requestsの使い方 webサイトのデータを取得するで、
web上のデータを取得する方法について学習しました。
取得したデータの形式はjsonだったりxmlだったり色んな形式があると思いますが、
ここではhtmlデータを解析し、業務で必要となるデータを抽出する方法について学習しましょう。


beautifulsoup4とは

beautifulsoup4とは、pythonでよく使用されているサードパーティ製のhtmlパーサライブラリです。
特徴的の1つとして、
インスランス生成時に使用するパーサライブラリを指定することができる、という点でしょうか。
これにより、html以外にxmlをパースすることも可能です。

PyPIで配布されているため、pipでインストールすることが可能です。

pip install beautifulsoup4

あと、学習前に知っておいたほうが良いのが、htmlをパースする方法が大きく分けて以下の3つある、
という点です。

    Tagオブジェクトを使用したパース
    find_allメソッドを使用したパース
    selectメソッドを使用したCSSセレクタによるパース

このページではTagオブジェクトについて学習しますが、
実務上ではfind_allメソッドの使用でほとんどが事足りると思います。


基本的な使い方

基本的な使い方のフローは以下のようになります。

    html文字列を用意する
    パーサを指定してhtml文字列を元にBeautifulSoupオブジェクトを生成する
    BeautifulSoupから必要となるデータを抽出する

簡単なサンプルを見てみましょう
"""

from bs4 import BeautifulSoup

html = "<body><h1>python入門</h1><p>pythonの基礎について学習します</p></body>"
soup = BeautifulSoup(html, "html5lib")
print(soup.h1)

"""
実行すると、h1タグとその内容が出力されます。

<h1>python入門</h1>
"""

"""
BeautifulSoupの生成とパーサの種類

それではまず、BeautifulSoupオブジェクト（長いので以降はbsオブジェクトと呼称）生成についてです。
前述のとおり、パーサを生成時に指定することができます。以下の種類があります。

パーサ 	                           説明
html.parser 	              Python付属のパーサーです。
lxml 	                      外部ライブラリlxmlのhtmlパーサーです。
                              外部のCライブラリに依存しますが、高速です。
lxml-xml 	                  外部ライブラリlxmlのxmlパーサーです。
                              外部のCライブラリに依存しますが、高速です。
html5lib 	                  外部ライブラリhtml5libのhtmlパーサーです。遅いです。

私が実際に使ってみて、解析しやすかったのはhtml5libですが、
上述の通り非常に遅いので注意が必要です。
特に、domの構造が汚かったり不整合のあるhtmlだと(めったにあることではないですが、)
CPUが100%に張り付いて、最悪応答が帰ってこない場合があります。

lxmlとhtml5libは外部ライブラリですので、
使用する場合は以下の通りpipでインストールする必要があります。

pip install lxml
pip install html5lib
"""

"""
Tagオブジェクト

お手軽なパースを通してbeautifilsoupの基本となるTagオブジェクトの操作について学習しましょう。
最初の例で書いているとおり、bsオブジェクト.タグ名　
でタグとその内容の情報を保持したTagオブジェクトを取得することが可能です。
また、Tagオブジェクトはタグ名を連ねて子要素を取得することも可能です。
以下の属性があります。

htmlタグの属性

htmlタグにはid、name、classといった属性がありますが、
大カッコでくくることで属性を取得することができます。

tag['class']

また、.attrsで属性を辞書形式で取得することが可能です。

tag.attrs

.name

タグ名を取得します。
.string

内部テキストにアクセスできます。
.contents/.children/.parent

.contentsは直下の子要素をlist形式で返します。
.childrenは直下の子要素をlistイテレータで返します。

.parentは親要素を取得することができます。
サンプル

上記の属性を使用したサンプルを掲載します。

まずは解析対象のhtmlです。


<!DOCTYPE html> 
<html> 
    <head>
        <title>Page Title</title>
    </head> 
    <body>
        <h1 class="one" >H1_String</h1>                                                                   
        <p>おすすめ商品</p>
        <div class="description">                                                                         
            <p>とってもキュートな商品。</p>                                                               
        </div>
    </body>                                                                                               
</html> 

次にpythonファイルです。
"""

from bs4 import BeautifulSoup


html = open('index.html', 'r', encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")

# 最初のh1タグ取得
h1 = soup.h1
print(h1)    # <h1 class="one">H1_String</h1>

# h1タグの属性を取得
print(h1.attrs)    # {'class': ['one']}

# h1タグのclassを取得
print(h1['class'])    # ['one']

# h1タグのタグ名を取得
print(h1.name)    # h1

# 最初のpタグ取得
print(soup.p)    # <p>おすすめ商品</p>

# divタグの次のpタグ取得
print(soup.div.p)    # <p>とってもキュートな商品。</p>

# divタグの次のpタグの内部テキストを取得
print(soup.div.p.string)    # とってもキュートな商品。

"""
いかがでしょうか？簡単にhtmlにアクセスできますね。
ですが、複雑な要素にアクセスするにはこれだけだと到達できないノードがでてきます。

htmlの要素を検索して欲しいノードを取得する必要があるのですが、
これにはfind、find_allメソッドを使用します。

(Tagオブジェクトにある
.next_sibling/.previous_sibling./next_elements/.previous_elements
などを使用すると、階層を前後横に移動することが可能なのですが、
空白行を考慮したりする必要がありあまり使い勝手が良くないと思うため、説明は省略します。)
"""

"""
find_allメソッド

find_allメソッドは引数に条件を指定することにより、
条件に合致したdomノードがbs4.element.ResultSet
という前回紹介したTagオブジェクトのシーケンスが返されます。

タグを指定する

引数にタグ名を指定すると、そのタグのdomノードがリストで取得できます。

例えば、h1タグを取得する場合、以下のように記述します。

soup.find_all("h1")

また、番目なのかを指定する場合はシーケンスですのでインデックスで指定することが可能です。
例えば、(0から数えて)2番目のh1タグのテキストを取得する場合は以下のように記述します。

chapter3 = soup.find_all("h1")[2].text

キーワード引数で属性を指定する

また、キーワード引数で属性を指定することが可能です。
属性の指定

例えば、id="sample"となるようなタグ指定する場合は以下のように記述します。

soup.find_all(id='sample') 

idはhtmlでは原則ユニークですが、戻り値はリストである点に注意してください。

タグのclassを指定する場合は注意してください。
"class"をpythonでは予約語なのでclass_を使用します。
例えばclass="sample"となるようなノードを取得する場合は以下のように記述します。

soup.find_all(class_='sample')
    

タグ名と属性を指定する

また、タグ名と合わせて使用することもできます。例えば、上の条件でさらにdivタグであるもの、
つまり以下のようなdivを取得したい場合、

<div class="sample">
  <p>aaaaa</p>
</div>

タグ名とキーワード引数を並べて記述します。

soup.find_all('div', class_='sample') 
    

属性の指定に正規表現を使用する

正規表現を使用することも可能です。たとえば、見出しのタグ(h1、h2、h3、、、)を全て取得したい場合、
以下のように記述します。

import re
for tag in soup.find_all(re.compile("^h[0-9]")):
    print(tag.name)

取得したいタグを列挙する

引数に取得したいタグをリストで列挙すると、それらを全て取得することができます。
例えば、a、link、scriptタグを取得したい場合、以下のように記述します。

soup.find_all(['a', 'link', 'script']) 
"""
"""
findメソッド

find_allメソッドは条件に合致するタグを全て取得してくれますが、
最初に出現するものだけ取得したい場合はfindメソッドを使用します。
使い方はfind_allと同じなので説明は割愛します。


selectメソッド

selectメソッドを使用すると、CSSセレクタを使用することができます。
フロントを書くのが得意な方はこちらのほうが書きやすいかもしれませんね。

使い方ですが、fund_allと同様に引数に文字列で条件を記述するだけです。
例えば、id="sample"のタグを取得したい場合は以下のように記述します。

soup.select("#sample")

ただし、こちらもやはりidを指定しても戻り値はシーケンスなので注意してください。

もうひとつ例です。divタグでclass="sample"となるものを取得する場合です。

soup.select('div[class="sample"]')

これでhtml内にあるあらゆるdomノードに対し、Tagオブジェクトとして取得することが可能となりました。
中の属性やテキストを取得したい場合は前回のTagオブジェクトの操作方法を参照してください。
"""


print("--- sphinx入門 その1 ドキュメントの自動生成---")


"""
メジャーなプログラム言語ではプログラムのコメントからドキュメントを生成するライブラリがあります。
例えばjavaだとjavadocが有名ですね。
Pythonではsphinxというライブラリでドキュメントを生成することができます。
このページではdocstringからsphinxを用いてhtmlのドキュメントを生成してみましょう。


sphinxとは

sphinxとはPythonドキュメントのために作られたpython製のドキュメント作成ツールです。
reStructuredText(reST)という形式のマークアップで扱います。
出力はwebで参照できるhtml形式以外に、LaTex形式等にも対応しています。


簡単な使い方

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

とりあえずpythonファイルはrun.py、pkg/__init__.py、pkg/__init__.py、pkg/mod1.pyの3つ用意してみましょうか。また、rstファイルのためのdocsディレクトリとhtmlドキュメントを格納するhtmlディレクトリを準備します。

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

""""""

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
"""
"""
rstの生成

sphinx-apidocコマンドを以下のように実行します。

sphinx-apidoc -F -o ./docs ./sample

docsディレクトリにファイルが生成されていることが確認できます。

sphinx-apidoc -F -o ./docs ./sample
Creating file ./docs\run.rst.
Creating file ./docs\pkg.rst.
"""
"""
htmlの生成

最後にhtmlを生成しましょう。
その前に、前の処理で生成されたconf.pyの以下のコードのコメントアウトを解除します。


# docs/conf.py
import os
import sys
sys.path.insert(0, '/home/....')

では生成です。sphinx-buildコマンドを以下のように実行します。
htmlディレクトリ配下にhtmlドキュメントが生成されます。

sphinx-build -a ./docs ./html

D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題\プロジェクトディストリ>sphinx-build -a ./docs ./html
Running Sphinx v4.4.0
loading translations [en]... done
building [mo]: all of 0 po files
building [html]: all source files
updating environment: [new config] 3 added, 0 changed, 0 removed
reading sources... [ 33%] index                                       reading sources... [ 66%] pkg                                         reading sources... [100%] run                                         
WARNING: autodoc: failed to import module 'mod1' from module 'pkg'; the following exception was raised:
No module named 'pkg'
WARNING: autodoc: failed to import module 'pkg'; the following exception was raised:
No module named 'pkg'
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [ 33%] index                                        writing output... [ 66%] pkg                                          writing output... [100%] run                                          
generating indices... genindex py-modindex done
highlighting module code... [100%] run                                
writing additional pages... search done
copying static files... done
copying extra files... done
dumping search index in English (code: en)... done
dumping object inventory... done
build succeeded, 2 warnings.

The HTML pages are in html.

生成されたhtmlの内容を確認してみましょう。
ブラウザhtml/index.htmlを確認すると以下のような画面が表示されます。
"""

"""
コマンドオプション
sphinx-apidoc
オプション                  意味
-F                fullで生成します。指定しない場合はrstファイルのみ生成されます。
-f                出力時に強制上書きをします。
-o                出力先を指定します。
-H                プロジェクト名を指定します。
-A                authorを指定します。
-V                versionを指定します。

最初のサンプルではプロジェクト名にソースディレクトリ名が設定されますが、
例えばソースディレクトリがsrcなどの場合はHオプションで設定すると良いでしょう。

sphinx-build

以下の形式で記述します。

sphinx-build [options] 入力元 出力先 

オプション                     意味
-b                ビルダー（≒出力形式）を指定します。デフォルトではhtmlですが、
                  xml、latexなどを指定することができます。
-a                すべての出力ファイルを書き出します。
                  このオプションをつけない場合は新規に作成されたり、
                  変更のあったソースファイルに関連する出力ファイルだけを出力します。


tips

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
その場合はls、egrep、xargsを組み合わせて特定ファイルは削除しないようにする必要があります。
"""
