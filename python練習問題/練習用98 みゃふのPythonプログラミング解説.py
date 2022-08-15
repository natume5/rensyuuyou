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
print(ren_s)    # Hello 佐藤!

"""
tmp_sがテンプレート文字列です。{{ }} で囲まれたnameはrender()のタイミングで置き変わります。
Template()にテンプレート文字列を渡した結果をtemplate変数に格納しています。
templateはjinja2.environment.Templateというjinja2専用のオブジェクトです。
最後にtemplateのrender()を使ってテンプレート文字列に変数を渡し、
結果を文字列で取得しています。name=’佐藤’で {{ }} で囲まれたnameを置き換えています。


用途に応じてファイルを分ける

最も基本的なjinja2の使い方を見てきましたが、
上記のプログラムは「テンプレート文字列」「テンプレートに渡すパラメータ」「レンダリング」
が全て同じ場所に記述されています。

これらを分割することでより管理しやすくなるので、3つのファイルに分けてみましょう。


コード(template.j2)：

Hello {{ name }}!


コード(parameter.json)：

{"name" : "佐藤"}


コード(rendering.py)：

from jinja2 import Template, Environment, FileSystemLoader
import json

#テンプレート読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('template.j2')

#設定ファイル読み込み
with open('parameter.json') as f:
    params = json.load(f)

#レンダリングして出力
rendered_s = tmpl.render(params)
print(rendered_s)    # Hello 佐藤!


少し長いので、一つずつ見ていきましょう。

まずtemplate.j2です。これはテンプレートファイルです。
拡張子をj2にしていますが、tmplでもjinjaでもtxtでも問題ありません。
次にparameter.jsonです。
これはレンダリングする際に必要なパラメータをjson形式で記述しています。
今回はnameを佐藤に置き換えるので、keyを「name」、valueを「佐藤」にしています。
なお、ここではjsonを使っていますが、
パラメータを管理するファイルもxmlやyaml等、別の形式でも問題ありません。
最後にrendering.pyです。
これは実際にテンプレートファイルとパラメータファイルを読み込んでレンダリングして、
結果を出力するメインファイルです。
FileSystemLoaderはテンプレートファイルを読み込むためのモジュール、
Environmentはjinja2の環境設定用のモジュールです。
Environment()で生成したenvのget_template()でtemplate.j2ファイルを読み込みます。
次にparameter.jsonを読み込み、jsonモジュールのloadで辞書に変換します。
最後にtmplのrender()に辞書形式のパラメータを渡してレンダリングしています。
"""


"""
htmlを出力する

jinja2を使って動的にhtmlを生成し、ファイルに出力してみましょう。


コード(template.j2)：

<html>
  <body>
    <h1>{{ shop_name }}</h1>
    <p>{{ item }}は{{ price }}円です。</p>
  </body>
</html>


コード(parameter.json)：

{
	"shop_name": "雑貨屋",
	"item": "お皿",
	"price": "200"
}

コード(rendering1.py)：

from jinja2 import Template, Environment, FileSystemLoader
import json

#テンプレート読み込み
〜省略〜

#設定ファイル読み込み
〜省略〜

#レンダリングしてhtml出力
rendered_html = tmpl.render(params)
with open('result.html', 'w') as f:
    f.write(rendered_html)

[出力結果結果(result.html)]

<html>
  <body>
    <h1>雑貨屋</h1>
    <p>お皿は200円です。</p>
  </body>
</html>

生成されたファイルをブラウザで開いたら、htmlとして表示されます。
"""

"""
テンプレート内でループする

テンプレート内でループ処理は次のようにすることで実現できます。


コード(template2.j2)：

<html>
  <body>
    <h1>{{ shop_name }}</h1>
{% for item in items %}
    <p>{{ loop.index }} : {{ item.name }}は{{ item.price }}円です。</p>
{% endfor %}
  </body>
</html>


コード(parameter2.json)：

{
    "shop_name": "雑貨屋",
    "items": [
        {"name": "羊の置き物", "price": 550},
        {"name": "ねずみの貯金箱", "price": 1290},
        {"name": "猫のキャンドル", "price": 840}
    ]
}


[出力結果結果(result1.html)]

<html>
  <body>
    <h1>雑貨屋</h1>

    <p>1 : 羊の置き物は550円です。</p>

    <p>2 : ねずみの貯金箱は1290円です。</p>

    <p>3 : 猫のキャンドルは840円です。</p>

  </body>
</html>


template.j2ファイルの{% for item in items %}が重要な点です。
itemsはparameter.jsonのitemsキーを指していますので、
itemにはnameとpriceの要素のあるオブジェクトが、ループごとに一つずつ入っていきます。
あとは{{ item.name }}の形でjson内（正確には辞書内）の値と置き換えます。
また、loop.indexはループ中のインデックス番号を取得できます。
最後に{% endfor %}でループを終了します。
※話は少しそれますが、今回rendering.pyは変更していません。
これはファイルを用途に応じて3つに分けたからです。
修正の必要な箇所がファイル単位で切り出せるのは利点です。
"""


"""
テンプレート内で条件分岐する

テンプレート内での条件分岐は次のようにすることで実現できます。

コード(template3.j2)：

<html>
  <body>
    <h1>{{ shop_name }}</h1>
{% if user.birth_month == 11 %}
    <p>{{ item.name }}は10%引きで{{ item.price|int * 0.9 }}円です。</p>
{% else %}
    <p>{{ item.name}}は通常価格で{{ item.price }}円です。</p>
{% endif %}
  </body>
</html>

コード(parameter3.json)：

{
    "shop_name": "雑貨屋",
    "item": {"name": "お皿", "price":"200"},
    "user": {"id":1, "name":"鈴木", "birth_month": 11}
}

[出力結果結果(result2.html)]

<html>
  <body>
    <h1>雑貨屋</h1>

    <p>お皿は10%引きで180.0円です。</p>

  </body>
</html>


{% if user.birth_mondh %}と{% else %}と{% endif %}で、
テンプレート内でif〜else文を表現しています。
endifは忘れやすいので注意しましょう。
また、item.priceは文字列なので、そのまま計算式に使うとエラーになってしまいます。
そこでフィルターのintを使い、数値に変換しています。フィルターはpythonの関数のようなものです。
jinja2のテンプレートでpythonの関数を使う場合は「｜（パイプ記号）」
で区切ってフィルター名を記述します。
こちらにjinja2で使えるフィルターの一覧を載せておきます。
trimやreplaceなど、文字列に対して使うフィルターも多数存在します。
"""


"""
テンプレートの継承

jinja2の便利な使い方にテンプレートの継承があります。
テンプレートの継承は「ベーステンプレートと子テンプレートに分けて、
子テンプレートがベーステンプレートをオーバーライドできる」機能です。
ためしに使ってみましょう。まずはベーステンプレートを作ります。

コード(base.j2)：

<html>
<head>
  {% block head %}
  <link rel="stylesheet" href="style.css" />
  <title>Sample - Web Page</title>
  {% endblock %}
</head>
<body>
  <div id="content">{% block content %}{% endblock %}</div>
  <div id="footer">{% block footer %}{% endblock %}</div>
</body>
</html>

htmlタグやhead、bodyタグなどのよく使うタグが配置され、
さらにbody内にcontentやfooterのdivを記述しており、よくあるページレイアウトとなっています。
重要なのは{% block %}と{% endblock %}です。
この2つに挟まれた箇所は子テンプレート側でコンテンツが埋め込まれます。

次は子テンプレートを見てみましょう。

コード（child.j2)：

{% extends "base.j2" %}
{% block head %}
  {{ super() }}
  <style type="text/css">
    .important { color: #336699; }
    #footer { font-size: 10px; }
  </style>
{% endblock %}
{% block content %}
  <h1>テンプレート継承テスト</h1>
  <p class="important">テンプレートが継承されています。</p>
{% endblock %}
{% block footer %}
  <p>Copyright 2020</p>
{% endblock %}

まず{% extends "base.j2" %}でbase.j2を読み込んでいます。
次に「base.j2側で定義したblockと同じ名前のblock」
でベーステンプレートにコンテンツを埋めていきます。
例えば{% block content %}では<h1>タグや<p>タグでコンテンツを埋めています。
また、{% block header %}では{{ super() }}という記述があります。
これはベーステンプレートの内容を継承するという意味です。
それではrendering.pyを実行して、
結果を見てみましょう(child.j2を読み込んでレンダリングましょう)。

[出力結果結果(result2.html)]

<html>
<head>
  
  
  <link rel="stylesheet" href="style.css" />
  <title>Sample - Web Page</title>
  
  <style type="text/css">
    .important { color: #336699; }
    #footer { font-size: 10px; }
  </style>

</head>
<body>
  <div id="content">
  <h1>テンプレート継承テスト</h1>
  <p class="important">テンプレートが継承されています。</p>
</div>
  <div id="footer">
  <p>Copyright 2020</p>
</div>
</body>
</html>


ベーステンプレートのレイアウトに子テンプレートで追加したコンテンツが埋め込まれているのがわかります。
headerで{{ super() }}を使っているので、
ベーステンプレート側で定義していた<link>タグや<title>タグもレンダリングされています。
"""


"""
テンプレート内でコメントアウトする

最後にコメントアウトの方法を見てみましょう。

コメントアウトは{# #}で括ります。

コード(template.j2)：

<html>
  <body>
    <h1>{{ shop_name }}</h1>
    {# <p>{{ item }}は{{ price }}円です。</p> #}
  </body>
</html>

[出力結果]

<html>
  <body>
    
  </body>
</html>

{# #}で括った箇所がコメントアウトされ、結果に出力されなくなりました。
"""
