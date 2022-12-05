#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- jinja2入門 その4 テンプレートの部品化 ---")



print("--- インクルード ---")


"""
冒頭で説明したとおり、
インクルードを使用するとテンプレートファイルを分割して部品化することができます。
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


{# sample9.tpl #} 

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
template = env.get_template('sample9.tpl')

data = {'items': ['みかん', 'りんご', 'バナナ']}
disp_text = template.render(data)
print(disp_text)

"""
コンテンツ側sample.tplの{% include "nav.tpl" %}で
ナビゲーションの部品を読み込んでいます。
これにより、出力結果は以下のように、
ナビゲーション部分が埋め込まれた形で出力されます。

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

このように、画面間の共通項目は別のテンプレートファイルとして
部品にしておくと同じことを何度も書かずに済むので便利ですね。
"""
