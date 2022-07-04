#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- jinja2入門 その1---")


"""
jinja2とは
jinja2とはpythonのweb開発でよく使用されるテンプレートエンジンライブラリの１つです。
変わったネーミングですが、テンプレート→テンプル→神社となったそうです（神社とお寺とはちょっと違いますが）。
pipコマンドでインストールできます。

1
pip install jinja2
一般的なテンプレートエンジンと同様、テンプレートファイルの読み込み、文字列の埋め込み、
分岐・ループの制御文をサポートします。制御文はpythonの文法とは異なるので注意してください。
テンプレートは以下の式、文、コメントから構成されます。


記法	                概要
{% ... %}	     Statements
{{ ... }}	     Expressions
{# ... #}	     コメント
# ... ##	     Line Statements
"""
"""
基本的な使い方
文字列の埋め込み
プレースホルダに{{変数名}}を使用します。
"""

from jinja2 import Template

tpl_text = '僕の名前は{{name}}です！！{{lang}}が好きです！'
template = Template(tpl_text)

data = {'name': 'Kuro', 'lang': 'Python'}
disp_text = template.render(data)    # 辞書で指定する
print(disp_text)    # 僕の名前はKuroです！！Pythonが大好きです！！

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
テンプレートファイルはsample.tplというテキストファイルでカレントディレクトに配置しているものとします。

コメント
テンプレートファイルに{# ... #}でコメントを打つことができます。

変数を定義する
setを使用すると、テンプレート内で使える変数を定義することができます。

{% set text='aaaa' %}
{{ text }}
"""

"""
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
"""

"""
for文
for文で繰り返し処理ができます。{% for ループ変数 in シーケンス %}でループを記述します。
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


print("--- jinja2入門 その2---")


"""
空白行の制御
trim_blocksとlstrip_blocks
テンプレートブロックはレンダリング時に空白行に置換されます。
trim_blocksとlstrip_blocksの両方を有効にすると、
テンプレートブロック行は削除され、他の空白は保持されます。
以下のテンプレートについて考えてみましょう。

sample3.tpl
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>

まず、デフォルトでEnvironmentを生成して出力を確認してみます。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
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
trim_blocksを有効にしてみるとどうなるでしょうか。trim_blocks=Trueを指定してみましょう。


# インスタンス生成時に指定する
env = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
# もしくは、インスタンス生成後に指定する
env.trim_blocks = True
出力は以下の通りとなります。


<ul>
 
    <li>みかん</li>
 
    <li>りんご</li>
 
    <li>バナナ</li>
 
</ul>
ブロック直後の空白をトリムする場合はlstrip_blocksを指定します。
ただし、ブロック直後が空白のみの場合はlstrip_blocksの指定にかかわらず
自動で空白が削除されます。


個別の設定
個別のブロックについて空白出力有無を設定することも可能です。
以下のようにマイナスをつけると空行がなくなります。

<ul>
{% for item in items -%}
    <li>{{ item }}</li>
{%- endfor %}
</ul>
"""

"""
特殊文字のエスケープ
{%などを含んだ文字列等がある場合、エスケープしたい箇所をrawブロックで囲みます。
例えば、jinja2のテンプレート構文をテンプレートに書きたい場合は以下のように記述します。


{% raw %}
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul>
{% endraw %}
"""

"""
Line Statements
line_statement_prefixを指定するとブロックの記述方法を変更することができます。
利用する側のpythonで以下のように設定します。

env.line_statement_prefix = '#'
すると、テンプレートファイルは以下のように記述することができます。

<ul>
# for item in seq
    <li>{{ item }}</li>
# endfor
</ul>
"""


print("--- jinja2入門 その3 フィルタ---")


"""
前回の続きです。jinja2は出力文字列に対しhtmlエスケープ等の加工処理を付加することができます。
また、Linuxコマンドのパイプのように処理をつなげることができます。
様々な組込みフィルタが用意されていますが、自作することも可能です。
まずは組込みから見てみましょう。


フィルタ
組込みフィルタ
jinja2には予め組込みでフィルタが用意されています。
よく使用するのはescapeというフィルタで、これはhtmlの特殊文字をエスケープしてくれます。
xss対策に便利なフィルタですね。サンプルを見てみましょう。
まず、テンプレートには以下のように出力部分にパイプでescapeをつなげます。

{# sample4.tpl #}
<ul> 
    {% for item in items -%}
    <li>{{ item | escape}}</li>
    {% endfor %}
</ul>

python側は以下のように記述します。出力する文字列にカッコやスペースが入っています。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('sample4.tpl')

data = {'items': ['<みかん>', '<りんご>', '<バナナ オーレ>']}
disp_text = template.render(data)
print(disp_text)

"""
上のスクリプトを実行すると、以下のようにエスケープされた状態で出力されます。

<ul>
    <li>&lt;みかん&gt;</li>
    <li>&lt;りんご&gt;</li>
    <li>&lt;バナナ オーレ&gt;</li>
     
</ul>
スペースやカッコがエスケープされていることが確認できます。
その他の組込みフィルタはここをご参照ください。
https://jinja.palletsprojects.com/en/2.9.x/templates/#list-of-builtin-filters
"""

"""
自作フィルタ
次にフィルタを自作してみましょう。
（関数オブジェクトについて理解していない場合はさきにそちらを復習することをおすすめします。）

フィルタとして処理させる関数を定義し、
その関数をEnvironmentオブジェクトのfilters辞書に設定します。
例えば出力文字列の前後をアスタリスクで装飾したい場合、以下のようにします。
"""

def sample(arg):
	""" 引数をアスタリスクで装飾した文字列を返す """
	return "*** " + str(arg) + " ***"


from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)

# 自作フィルタを設定する
env.filters['sample_filter'] = sample
template = env.get_template("sample5.tpl")

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
テンプレートファイルには以下のようにフィルタに先ほど設定したsample_filterをパイプでつなげます。


{# sample5.tpl #}
<ul>
    {% for item in items -%}
    <li>{{ item | sample_filter}}</li>
    {% endfor %}
</ul>

実行してみると、以下のように出力されます。

<ul>
    <li>*** みかん ***</li>
    <li>*** りんご ***</li>
    <li>*** バナナ ***</li>
     
</ul>
"""


print("--- jinja2入門 その4 テンプレートの部品化---")


"""
ある程度規模のあるwebシステムを構築する際、
ヘッダーやグローバルナビ、ページャー、フッターなどの共通項目は部品化して使い回すことが一般的です。
jinja2にはインクルードと呼ばれるテンプレート分割機能があります。


インクルード
冒頭で説明したとおり、インクルードを使用するとテンプレートファイルを分割して部品化することができます。
ナビゲーション部分を切り出したサンプルを見てみましょう。

まずはナビゲーションの部品です。

{# nav.tpl グローバルナビ #}  
<nav>
<h1>メニュー</h1>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/items/index">商品一覧</a></li>
<li><a href="/analysis/index">分析</a></li>
</ul>
</nav>
次に、ナビゲーションを読み込むコンテンツ側のhtmlです。

{# sample.tpl #} 
 
{% include "nav.tpl" %}
<div class="content">
    <ul>
        {% for item in items -%}
        <li>{{ item}}</li>
        {% endfor %}
    </ul>
</div>
最後にpythonファイルです。
"""

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('sample6.tpl')

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
コンテンツ側sample.tplの{% include "nav.tpl" %}でナビゲーションの部品を読み込んでいます。
これにより、出力結果は以下のように、ナビゲーション部分が埋め込まれた形で出力されます。


<nav>
<h1>メニュー</h1>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/items/index">商品一覧</a></li>
<li><a href="/analysis/index">分析</a></li>
</ul>
</nav>
 
 
<div class="content">
    <ul>
        <li>みかん</li>
        <li>りんご</li>
        <li>バナナ</li>
         
    </ul>
</div>
このように、画面間の共通項目は別のテンプレートファイルとして部品にしておくと
同じことを何度も書かずに済むので便利ですね。
"""


print("--- jinja2入門 その5 マクロとインポート---")


"""
前回の続きで今回はマクロについて学習します。
railsライクなWebフレームワークにはhelperと呼ばれるhtmlの定型文を出力機能がありますが、
jinja2のマクロを使用するとそのhelperのような定型文出力の自動化処理を自作することができます。


jinja2のマクロとは、よく使用されるイディオムを関数として再利用可能な形にしたものです。
テンプレートファイルのmacroブロックに関数形式、つまり関数名と引数を記述します。
公式のサンプルがわかりやすいため、そのまま引用します。inputタグを自動で組み立ててくれるマクロです。

テンプレートファイルを以下のように記述します。

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
template = env.get_template('sample7.tpl')
disp_text = template.render()
print(disp_text)

"""
上のコードを実行すると、以下のように出力されます。
inputタグが自動で組み立てられることが確認できます。

<p><input type="text" name="username" value="" size="20"></p>
<p><input type="password" name="password" value="" size="20"></p>


"""

"""
インポート
さて、非常に便利なマクロですが、
さらにそれらを外出しにしてインポートを使用すると
他のテンプレートファイルでも定義したマクロを呼び出すことが可能です。
マクロを使う場合は必ずこちらも合わせて使用したほうがよいでしょう。
先ほどのinputタグを組み立ててくれるマクロ部分だけをinputhelper.tplという名前で保存します。
これを別のテンプレートファイルから呼び出すには、以下のように記述します。


{% import 'inputhelper.tpl' as helper %}
<p>{{ helper.input('username') }}</p>
<p>{{ helper.input('password', type='password') }}</p>
出力は先程と同様なので省略します。

フォームの部品などを毎回自力で書くのは大変ですが、
一旦マクロを作れば次から他のプロジェクトでも使い回すことが可能なので、
開発速度の向上や省力化につながります。是非活用してみてください。
"""
