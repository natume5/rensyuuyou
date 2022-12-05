#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- jinja2入門 その1 ---")



print("--- jinja2とは ---")


"""
jinja2とはpythonのweb開発でよく使用される
テンプレートエンジンライブラリの１つです。
変わったネーミングですが、テンプレート→テンプル→神社となったそうです
（神社とお寺とはちょっと違いますが）。pipコマンドでインストールできます。

pip install jinja2

一般的なテンプレートエンジンと同様、テンプレートファイルの読み込み、
文字列の埋め込み、分岐・ループの制御文をサポートします。
制御文はpythonの文法とは異なるので注意してください。
テンプレートは以下の式、文、コメントから構成されます。

記法 	      概要
{% ... %} 	Statements
{{ ... }} 	Expressions
{# ... #} 	コメント
# ... ## 	Line Statements
"""


print("--- 基本的な使い方 ---")


"""
文字列の埋め込み

プレースホルダに{{変数名}}を使用します。
"""

from jinja2 import Template

tpl_text = '僕の名前は{{name}}です！！{{lang}}が好きです！！'
template = Template(tpl_text)

data = {'name': 'Kuro', 'lang': 'Python'}
disp_text = template.render(data)    # 辞書で指定する
print(disp_text)    # 僕の名前はKuroです！！Pythonが好きです！！

"""
プレースホルダをもった文字列tpl_textから、テンプレートオブジェクトを生成します。
renderメソッドで値を指定すると、戻り値として文字が埋め込まれたデータが返されます。


テンプレートファイルの読み込み

さて、通常、上のコードのようにコードにテンプレートを埋め込むようなことはせず、
テンプレートを記述した別ファイルから読み込む方法が一般的でしょう。
jinja2ではEnvironmentを使用してファイルからテンプレートオブジェクトを生成します。

書き方は以下の通りです。


env = Environment(loader=FileSystemLoader('テンプレートファイル配置ディレクトリのルート'))
templete = env.get_template('テンプレートファイル名')

ではサンプルを見てみましょう。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample.tpl')

data = {'name': 'Kuro', 'lang': 'Python'}
disp_text = template.render(data)    # 辞書で指定する
print(disp_text)

"""
次にテンプレートファイルは以下の通りとします。

僕の名前は{{ name }}です！！{{ lang }}が好きです！！

テンプレートファイルはsample.tpl
というテキストファイルでカレントディレクトに配置しているものとします。


コメント

テンプレートファイルに{# ... #}でコメントを打つことができます。


変数を定義する

setを使用すると、テンプレート内で使える変数を定義することができます。

    {% set text='aaaa' %}
    {{ text }}


if文

if文で条件分岐の制御ができます。
{% if 条件式 %}で条件を指定します。
{% endif %}で制御文を閉じます。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample1.tpl')

data = {'x': 0}
disp_text = template.render(data)
print(disp_text)

"""
次にテンプレートファイルは以下の通りとします。

{# if文のsample #}
{% if x > 0 %}
xは0より大きいです
{% elif x == 0 %}
xは0です
{% else %}
xは0より小さいです
{% endif %}

感覚的に解ると思いますので細かい説明は割愛します。


for文

for文で繰り返し処理ができます。
{% for ループ変数 in シーケンス %}でループを記述します。
{% endfor %}で制御文を閉じます。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample2.tpl')

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
次にテンプレートファイルは以下の通りとします。

{# for文のsample #}
商品一覧
{% for item in items %}
・　{{ item }}
{% endfor %}

こちらも感覚的に解ると思いますので細かい説明は割愛します。
"""
