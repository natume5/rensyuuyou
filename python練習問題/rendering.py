from jinja2 import Template, Environment, FileSystemLoader
import json

#テンプレート読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf-8_sig'))
tmpl = env.get_template('template.txt')

#設定ファイル読み込み
with open('parameter.json', encoding='utf-8_sig') as f:
    params = json.load(f)

#レンダリングして出力
rendered_s = tmpl.render(params)
print(rendered_s)
