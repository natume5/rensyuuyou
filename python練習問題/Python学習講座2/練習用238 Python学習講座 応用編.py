#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- jinja2入門 その3 フィルタ ---")



print("--- フィルタ ---")


"""
組込みフィルタ

jinja2には予め組込みでフィルタが用意されています。
よく使用するのはescapeというフィルタで、
これはhtmlの特殊文字をエスケープしてくれます。
xss対策に便利なフィルタですね。サンプルを見てみましょう。
まず、テンプレートには以下のように出力部分にパイプでescapeをつなげます。


{# sample7.tpl #}
<ul> 
    {% for item in items -%}
    <li>{{ item | escape}}</li>
    {% endfor %}
</ul>

python側は以下のように記述します。
出力する文字列にカッコやスペースが入っています。
"""

from jinja2 import Template, Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('sample7.tpl')

data = {'items': ['<みかん>', '<りんご>', '<バナナ オーレ>']}
disp_text = template.render(data)
print(disp_text)

"""
上のスクリプトを実行すると、
以下のようにエスケープされた状態で出力されます
"""

# <ul>
#     <li>&lt;みかん&gt;</li>
#     <li>&lt;りんご&gt;</li>
#     <li>&lt;バナナ オーレ&gt;</li>

# </ul>

"""
スペースやカッコがエスケープされていることが確認できます。
その他の組込みフィルタはここをご参照ください。


自作フィルタ

次にフィルタを自作してみましょう。
（関数オブジェクトについて理解していない場合
はさきにそちらを復習することをおすすめします。）
フィルタとして処理させる関数を定義し、
その関数をEnvironmentオブジェクトのfilters辞書に設定します。
例えば出力文字列の前後をアスタリスクで装飾したい場合、
以下のようにします。
"""

def sample(arg):
	""" 引数をアスタリスクで装飾した文字列を返す """
	return "*** " + str(arg) + " ***"

from jinja2 import Template, environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)

# 自作フィルタを設定する
env.filters['sample_filter'] = sample
template = env.get_template('sample8.tpl')

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
テンプレートファイルには以下のように
フィルタに先ほど設定したsample_filterをパイプでつなげます。

{# sample8.tpl #}
<ul>
    {% for item in items -%}
    <li>{{ item | sample_filter}}</li>
    {% endfor %}
</ul>

実行してみると、以下のように出力されます。
"""

# <ul>
#     <li>*** みかん ***</li>
#     <li>*** りんご ***</li>
#     <li>*** バナナ ***</li>

# </ul>
































