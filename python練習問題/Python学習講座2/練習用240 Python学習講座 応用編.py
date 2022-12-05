#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- jinja2入門 その5 マクロとインポート ---")



print("--- マクロ ---")


"""
jinja2のマクロとは、
よく使用されるイディオムを関数として再利用可能な形にしたものです。
テンプレートファイルのmacroブロックに関数形式、
つまり関数名と引数を記述します。
公式のサンプルがわかりやすいため、そのまま引用します。
inputタグを自動で組み立ててくれるマクロです。
テンプレートファイルを以下のように記述します。

sample10.tpl

{% macro input(name, value='', type='text', size=20) -%}
<input type="{{ type }}" name="{{ name }}" value="{{
    value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>

呼び出し側のpythonは以下のように記述します。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('sample10.tpl')
disp_text = template.render()
print(disp_text)

"""
上のコードを実行すると、以下のように出力されます。
inputタグが自動で組み立てられることが確認できます。

<p><input type="text" name="username" value="" size="20"></p>
<p><input type="password" name="password" value="" size="20"></p>
"""


print("--- インポート ---")


"""
さて、非常に便利なマクロですが、
さらにそれらを外出しにしてインポートを使用すると
他のテンプレートファイルでも定義したマクロを呼び出すことが可能です。
マクロを使う場合は必ずこちらも合わせて使用したほうがよいでしょう。
先ほどのinputタグを組み立ててくれるマクロ部分だけを
inputhelper.tplという名前で保存します。
これを別のテンプレートファイルから呼び出すには、
以下のように記述します。

{% import 'inputhelper.tpl' as helper %}
<p>{{ helper.input('username') }}</p>
<p>{{ helper.input('password', type='password') }}</p>

出力は先程と同様なので省略します。

フォームの部品などを毎回自力で書くのは大変ですが、
一旦マクロを作れば次から他のプロジェクトでも使い回すことが可能なので、
開発速度の向上や省力化につながります。
是非活用してみてください。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('inputhelper.tpl')
disp_text = template.render()
print(disp_text)























