#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- beautifulsoup4入門 htmlをパース、スクレイピングする ---")


"""
requestsの使い方 webサイトのデータを取得するで、
web上のデータを取得する方法について学習しました。
取得したデータの形式はjsonだったりxmlだったり色んな形式があると思いますが、
ここではhtmlデータを解析し、
業務で必要となるデータを抽出する方法について学習しましょう。
"""


print("--- beautifulsoup4とは ---")


"""
beautifulsoup4とは、
pythonでよく使用されているサードパーティ製のhtmlパーサライブラリです。
特徴的の1つとして、インスランス生成時に使用するパーサライブラリを指定することができる、
という点でしょうか。これにより、html以外にxmlをパースすることも可能です。

PyPIで配布されているため、pipでインストールすることが可能です。

pip install beautifulsoup4

あと、学習前に知っておいたほうが良いのが、
htmlをパースする方法が大きく分けて以下の3つある、という点です。

    Tagオブジェクトを使用したパース
    find_allメソッドを使用したパース
    selectメソッドを使用したCSSセレクタによるパース

このページではTagオブジェクトについて学習しますが、
実務上ではfind_allメソッドの使用でほとんどが事足りると思います。
"""


print("--- 基本的な使い方 ---")


"""
基本的な使い方のフローは以下のようになります。

    html文字列を用意する
    パーサを指定してhtml文字列を元にBeautifulSoupオブジェクトを生成する
    BeautifulSoupから必要となるデータを抽出する

簡単なサンプルを見てみましょう。
"""

from bs4 import BeautifulSoup

html = "<body><h1>python入門</h1><p>pythonの基礎について学習します</p></body>"
soup = BeautifulSoup(html, "html5lib")
print(soup.h1)

"""
実行すると、h1タグとその内容が出力されます。

<h1>python入門</h1>


BeautifulSoupの生成とパーサの種類

それではまず、BeautifulSoupオブジェクト
（長いので以降はbsオブジェクトと呼称）生成についてです。
前述のとおり、パーサを生成時に指定することができます。
以下の種類があります。

パーサ 	                            説明
html.parser 	               Python付属のパーサーです。
lxml 	                       外部ライブラリlxmlのhtmlパーサーです。
                               外部のCライブラリに依存しますが、高速です。
lxml-xml 	                   外部ライブラリlxmlのxmlパーサーです。
                               外部のCライブラリに依存しますが、高速です。
html5lib 	                   外部ライブラリhtml5libのhtmlパーサーです。
                               遅いです。

私が実際に使ってみて、解析しやすかったのはhtml5libですが、
上述の通り非常に遅いので注意が必要です。
特に、domの構造が汚かったり不整合のあるhtmlだと
(めったにあることではないですが、)CPUが100%に張り付いて、
最悪応答が帰ってこない場合があります。

lxmlとhtml5libは外部ライブラリですので、
使用する場合は以下の通りpipでインストールする必要があります。

pip install lxml
pip install html5lib
"""


print("--- Tagオブジェクト ---")


"""
お手軽なパースを通してbeautifilsoupの基本となる
Tagオブジェクトの操作について学習しましょう。
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
空白行を考慮したりする必要がありあまり使い勝手が良くないと思うため、
説明は省略します。)
"""


print("--- find_allメソッド ---")


"""
find_allメソッドは引数に条件を指定することにより、
条件に合致したdomノードがbs4.element.ResultSet
という前回紹介したTagオブジェクトのシーケンスが返されます。


タグを指定する

引数にタグ名を指定すると、そのタグのdomノードがリストで取得できます。
例えば、h1タグを取得する場合、以下のように記述します。
"""

soup.find_all('h1')

"""
また、番目なのかを指定する場合はシーケンスですので
インデックスで指定することが可能です。
例えば、(0から数えて)0番目のh1タグのテキストを取得する場合
は以下のように記述します。
"""

chapter3 = soup.find_all('h1')[0].text
print(chapter3)    # H1_String

"""
キーワード引数で属性を指定する

また、キーワード引数で属性を指定することが可能です。


属性の指定

例えば、id="sample"となるようなタグ指定する場合は以下のように記述します。
"""

print(soup.find_all(id='sample'))    # []

"""
idはhtmlでは原則ユニークですが、戻り値はリストである点に注意してください。

タグのclassを指定する場合は注意してください。
"class"をpythonでは予約語なのでclass_を使用します。
例えばclass="sample"となるようなノードを取得する場合は以下のように記述します。
"""

print(soup.find_all(class_='sample'))    # []

"""
タグ名と属性を指定する

また、タグ名と合わせて使用することもできます。
例えば、上の条件でさらにdivタグであるもの、つまり以下のようなdivを取得したい場合、

<div class="description">
  <p>aaaaa</p>
</div>

タグ名とキーワード引数を並べて記述します。
"""

print(soup.find_all('div', class_='description'))
# [<div class="description">
# <p>とってもキュートな商品。</p>
# </div>]

"""
属性の指定に正規表現を使用する

正規表現を使用することも可能です。
たとえば、見出しのタグ(h1、h2、h3、、、)を全て取得したい場合、
以下のように記述します。
"""

import re

for tag in soup.find_all(re.compile("^h[0-9]")):
	print(tag.name)    # h1


"""
取得したいタグを列挙する

引数に取得したいタグをリストで列挙すると、
それらを全て取得することができます。
例えば、a、link、scriptタグを取得したい場合、
以下のように記述します。
"""

print(soup.find_all(['a', 'link', 'script']))    # []


print("--- findメソッド ---")


"""
find_allメソッドは条件に合致するタグを全て取得してくれますが、
最初に出現するものだけ取得したい場合はfindメソッドを使用します。
使い方はfind_allと同じなので説明は割愛します。
"""


print("--- selectメソッド ---")


"""
selectメソッドを使用すると、CSSセレクタを使用することができます。
フロントを書くのが得意な方はこちらのほうが書きやすいかもしれませんね。
使い方ですが、fund_allと同様に引数に文字列で条件を記述するだけです。
例えば、id="sample"のタグを取得したい場合は以下のように記述します。
"""

print(soup.select('#sample'))    # []

"""
ただし、こちらもやはりidを指定しても戻り値はシーケンスなので注意してください。
もうひとつ例です。divタグでclass="description"となるものを取得する場合です。
"""

print(soup.select('div[class="description"]'))
# [<div class="description">
# <p>とってもキュートな商品。</p>
# </div>]

"""
これでhtml内にあるあらゆるdomノードに対し、
Tagオブジェクトとして取得することが可能となりました。
中の属性やテキストを取得したい場合は
前回のTagオブジェクトの操作方法を参照してください。
"""
