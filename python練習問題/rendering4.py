from jinja2 import Template, Environment, FileSystemLoader
import json


#読み込み
env = Environment(loader=FileSystemLoader('./', encoding='utf-8_sig'))
tmpl = env.get_template('child.j2')

#レンダリングしてhtml出力
rendered_html = tmpl.render()
with open('result2.html', 'w') as f:
    f.write(rendered_html)
