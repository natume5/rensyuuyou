#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- jinja2入門 その6 テンプレートの継承---")


"""
Webアプリケーションを作成する際、画面ごとにhtmlを全てコーディングすることはあまりなく、
大枠のテンプレートをbaseテンプレート(親テンプレート)として用意し、
個別画面は親テンプレートを継承して画面ごとの可変項目のみ実装することが一般的ではないでしょうか。
jinja2でもテンプレートを継承して大枠部分とコンテンツ部分を分離することが可能です。


継承
jinja2の継承を使用するとサイトのすべての共通要素を含む
基本的なbaseテンプレートを作成することができます。
これにより、画面ごとにhtmlタグから書き出す必要がなくなります。
baseテンプレートにはヘッダーやフッターのような共通項目と、
コンテンツ部分のような子テンプレート側が上書きできるブロックを定義します。

baseテンプレート
ではまず、baseテンプレートについてです。以下のサンプルを見てください。

{# base.tpl baseテンプレート #}  
<!DOCTYPE html>
<html lang="ja">
    <head>
        <!-- 共通ヘッダ -->
        {% block head %}
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}{% endblock %} - My Webpage</title>
        {% endblock %}
    </head>
    <body>
 
        <!-- コンテンツ部分 -->
        <div id="content">
            {% block content %}
            {% endblock %}
        </div>
 
        <!-- 共通フッター -->
        <div id="footer">
            {% block footer %}
            &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.
            {% endblock %}
        </div>
    </body>
</html>


子テンプレートで上書きさせる箇所は{% block ブロック名 %}と{% endblock %}を記述します。
上のコードのヘッダー、フッター部分のように、ブロック内部に何かを記述することもできます。
また、内容の全てを子テンプレート側で出力させたい場合は、
上コードのコンテンツ部分のようにブロック内部に何も書かなくても良いです。
"""

"""
子テンプレート
次にbaseテンプレートを継承した子テンプレートの書き方です。

{# childe.tpl 子テンプレート #}  
 
{% extends "base.tpl" %} {# 親テンプレートを指定 #}
     
{% block title %}Index{% endblock %}
 
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
         
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>
{% endblock %}

extendsで親テンプレートを指定します。
{% block ブロック名 %}と{% endblock %}に囲まれたブロック内に内容を記述します。
また、親テンプレートのブロック内の内容を出力したい場合は８行目のように{{ super() }}を記述します。
"""

"""
出力結果
それでは出力してみましょう。テンプレートファイルに子テンプレートを指定します。
親テンプレートの指定は必要ありません。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('childe.tpl')
disp_text = template.render()
print(disp_text)

"""
実行結果は以下のとおりとなります。

<!DOCTYPE html>
<html lang="ja">
    <head>
        <!-- 共通ヘッダ -->


        <link rel="stylesheet" href="style.css" />
        <title>Index - My Webpage</title>

    <style type="text/css">
        .important { color: #336699; }
    </style>

    </head>
    <body>

        <!-- コンテンツ部分 -->
        <div id="content">

    <h1>Index</h1>
    <p class="important">
      Welcome to my awesome homepage.
    </p>

        </div>

        <!-- 共通フッター -->
        <div id="footer">

            &copy; Copyright 2008 by <a href="http://domain.invalid/">you</a>.

        </div>
    </body>
</html>
"""

