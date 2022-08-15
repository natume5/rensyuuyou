from jinja2 import Template, Environment, FileSystemLoader
import json

#テンプレート読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf-8_sig'))
tmpl = env.get_template('template2.j2')

#設定ファイル読み込み
with open('parameter2.json', encoding='utf-8_sig') as f:
    params = json.load(f)

#レンダリングしてhtml出力
rendered_html = tmpl.render(params)
with open('result1.html', 'w') as f:
    f.write(rendered_html)
