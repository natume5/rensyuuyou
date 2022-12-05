#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- jinja2入門 その2 ---")



print("--- 空白行の制御 ---")


"""
trim_blocksとlstrip_blocks

テンプレートブロックはレンダリング時に空白行に置換されます。
trim_blocksとlstrip_blocksの両方を有効にすると、
テンプレートブロック行は削除され、他の空白は保持されます。
以下のテンプレートについて考えてみましょう。


    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>

まず、デフォルトでEnvironmentを生成して出力を確認してみます。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample3.tpl')
data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
ブロック部分は空行に置換され、以下の出力が得られます。

    <ul>

        <li>みかん</li>

        <li>りんご</li>

        <li>バナナ</li>

    </ul>


trim_blocksを有効にしてみるとどうなるでしょうか。
trim_blocks=Trueを指定してみましょう。

# インスタンス生成時に指定する
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
# もしくは、インスタンス生成後に指定する
env.trim_blocks = True

出力は以下の通りとなります。
"""

env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
template = env.get_template('sample3.tpl')
data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

#     <ul>
#             <li>みかん</li>
#             <li>りんご</li>
#             <li>バナナ</li>
#         </ul>

"""
ブロック直後の空白をトリムする場合はlstrip_blocksを指定します。
ただし、ブロック直後が空白のみの場合は
lstrip_blocksの指定にかかわらず自動で空白が削除されます。


個別の設定

個別のブロックについて空白出力有無を設定することも可能です。
以下のようにマイナスをつけると空行がなくなります。


    <ul>
    {% for item in items -%}
        <li>{{ item }}</li>
    {%- endfor %}
    </ul>
"""

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample4.tpl')
data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

#     <ul>
#     <li>みかん</li><li>りんご</li><li>バナナ</li>
 #    </ul>


print("--- 特殊文字のエスケープ ---")


"""
{%などを含んだ文字列等がある場合、
エスケープしたい箇所をrawブロックで囲みます。
例えば、jinja2のテンプレート構文をテンプレートに書きたい場合は
以下のように記述します。

sample5.tpl

    {% raw %}
        <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% endraw %}
"""

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('sample5.tpl')
data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

#         <ul>
#         {% for item in items %}
#             <li>{{ item }}</li>
#         {% endfor %}
#         </ul>


print("--- Line Statements ---")


"""
line_statement_prefixを指定すると
ブロックの記述方法を変更することができます。
利用する側のpythonで以下のように設定します。

env.line_statement_prefix = '#'

すると、テンプレートファイルは以下のように記述することができます。

sample6.tpl

# for member in members
{{ member }}
# endfor
"""

env = Environment(loader=FileSystemLoader('.'))
env.line_statement_prefix = '#'
template = env.get_template('sample6.tpl')
data = {'members': ['物部', '大伴', '蘇我']}
n_text = template.render(data)
print(n_text)

# 物部
# 大伴
# 蘇我
