#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Flaskで作る簡易分析ツール5 参照画面の作成---")


"""
データの登録処理が成功したら、結果を参照できるようにしましょう。


参照処理の実装
models.pyの修正
参照のためにデータベースから指定したキーのデータを取得する必要があります。
select文を発行する関数を追加します。models.pyに以下の関数を追加してください。

def select(con, pk):
    """""" 指定したキーのデータをSELECTする """"""
    cur = con.execute('select id, title, data, img, created from results where id=?', (pk,))
    return cur.fetchone()


指定したキーのデータを取得して返します。
"""
"""
run.pyの修正
run.pyに以下のコードを追加してください。

@app.route('/view/<pk>')
def view(pk):
    """""" 結果参照処理 """"""
    con = get_db()
    result = models.select(con, pk)
    return render_template('view.html', result=result)

URLの/viewの後ろにpkを指定しますが、
flaskではデコレータの引数に山カッコでそういった変数を定義することができます。

テンプレートにselectした値を渡すため、render_templateの第２引数にresultを渡しています。
"""
"""
テンプレートの修正
view.htmlを以下のように修正してください(そのままペーストしていただいても構いません)。
id、タイトル、日付などが動的になっています。

{% extends "base.html" %}
{% block body %}
<h1>結果参照</h1>
 
<h3>{{ result.id }}:{{ result.title|safe}}</h3>
<p>{{ result.created }}</p>
<div class="row">
    <img src="{{ url_for('static', filename=result.img) }}">
</div>
 
<div class="row">
    <textarea class="form-control" name="data" rows="5">{{result.data}}</textarea>
</div>
 
<br><br>
{% endblock %}
"""
"""
動作確認
では動作を確認してみましょう。再度以下の登録画面アクセスします。
http://localhost:5000/create

タイトルに適当な文字列、データに以下の文字列を貼り付けて送信ボタンをクリックしてください。


col1,col2,col3
100,200,300
300,400,100
200,100,100
以下のような散布図行列が表示されると成功です。
"""


print("--- Flaskで作る簡易分析ツール6 一覧画面の作成---")


"""
前回までで分析処理と結果の参照処理の実装が終わりました。
次に結果一覧が参照できるトップページを作成しましょう。

一覧参照処理の実装
models.pyの修正
一覧参照のために、結果全件取得処理が必要となります。
models.pyに以下の関数を追加してください。

def select_all(con):
    """""" SELECTする """"""
    cur = con.execute('select id, title, data, img, created from results order by id desc')
    return cur.fetchall()


resultテーブルの内容を全件取得して返します。
"""
"""
run.pyの修正
モデルの呼び出し処理をrun.pyに実装します。view関数を以下のように修正してください。

@app.route('/')
def index():
    """""" 一覧画面 """"""
    con = get_db()
    results = models.select_all(con)
    return render_template('index.html', results=results)

DBアクセスして取得した結果をテンプレートに渡します。
"""
"""
テンプレートの修正
一覧画面のテンプレートを修正します。
run.pyから渡された値を表示するために、index.htmlを以下のように修正しましょう。

{% extends "base.html" %}
{% block body %}
<h1>分析一覧</h1>
<a href="/create">新規分析</a>
<table class="table table-striped table-hover">
    <tr>
        <th>id</th>
        <th>title</th>
        <th>date</th>
        <th>操作</th>
    </tr>
    {% for result in results %}
    <tr>
        <td>{{ result.id }}</td>
        <td>{{ result.title|safe}}</td>
        <td>{{ result.created }}</td>
        <td>
            <a href="/view/{{ result.id }}"><button class="btn btn-primary">参照</button></a>
            <form action="/delete/{{ result.id }}" style="display: inline" method="post">
                <input class="btn btn-danger" type="submit" value="削除" onclick='return confirm("削除しますがよろしいですか？")';>
            </form>
 
        </td>
    </tr>
    {% endfor %}
 
</table>
 
{% endblock %}


複数結果を表示するため、for文を使用しています。
また、結果の削除処理のため、削除フォームにpkをhiddenで設定しています。
"""
"""
削除処理の実装
次に削除処理を実装しましょう。画面はありません。

models.pyの修正
DBのレコード削除処理を実装します。models.pyに以下を追記してください。

def delete(con, pk):
    """""" 指定したキーのデータをDELETEする """"""
    cur = con.cursor()
    cur.execute('delete from results where id=?', (pk,))
    con.commit()


指定したidのレコードに対してdelete文を発行します。
"""
"""
run.pyの修正
delete処理を呼び出す処理を追加します。
run.pyのdelete関数を以下のように修正してください。

@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
    """""" 結果削除処理 """"""
    con = get_db()
    models.delete(con, pk)
    return redirect(url_for('index'))

削除処理の完了後、Top画面にリダイレクトします。
"""
"""
動作確認
お疲れ様です。これで一通りの機能が実装されました。
一覧画面にアクセスして、登録したデータが表示されること、削除ができることを確認してください。

http://localhost:5000

今回ビジネスロジックに散布図行列を使いましたが、
Pythonを使えば主成分分析やK-meansによるクラスター分析といった表計算ソフトで
難しい分析処理を簡単にWeb上に実装することが可能です。
みなさまも日々使用する処理のWeb化に挑戦してみてください。
"""


print("--- Flaskで作る簡易分析ツール7 flashメッセージ---")


"""
前回で、ツールとして使うための最低限の機能の実装は終わりました。
ここからは補足機能の追加としてflushメッセージの追加をしてみましょう。


flaskのflashメッセージ
flashメッセージとは、処理が終わったりエラーが発生した際にその旨を通知するメッセージのことです。
flaskにはデフォルトでflashメッセージ機能がありますのでそれを使ってみましょう。

テンプレートの修正
まずは、テンプレートにflashメッセージを挿入する部分を追加しましょう。
base.htmlのcontainer部分を以下の通り修正してください。（block bodyの前に追加します。）


<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-success">{{ message }}</div>
    {% endfor %}
    {% block body %}{% endblock %}
</div>

get_flashed_messagesメソッドを使用することにより、
セッションに格納されたメッセージを取得することができます。
"""
"""
各処理の修正
run.pyで、flaskのflash機能をインポートします。

from flask import Flask, request, g, redirect, url_for, render_template, flash

また、更新系の処理終了後にflashメッセージを追加するように修正しましょう。

# run.py
@app.route('/analysis', methods=['POST'])
def analysis():
    """""" 分析実行処理 """"""
 
    title = request.form['title']
    data = request.form['data']
    img = models.create_scatter(data)
 
    con = get_db()
 
    pk = models.insert(con, title, data, img)
    flash('登録処理が完了しました。')    # ←ここを追記
    return redirect(url_for('view', pk=pk))
 
 
@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
    """""" 結果削除処理 """"""
    con = get_db()
    models.delete(con, pk)
    flash('削除処理が完了しました。')    # ←ここを追記
    return redirect(url_for('index'))
"""

"""
動作確認
登録、削除処理を行ってみてください。

登録、削除処理後に画面上部にメッセージが表示されたら成功です。
"""


print("--- Flaskで作る簡易分析ツール 補足---")


"""
プロジェクト
構成は以下のとおりとなります

.
├── db.sqlite3
├── models.py
├── requirements.txt
├── run.py
├── schema.sql
├── static
│   ├── result
│   └── style.css
└── templates
    ├── base.html
    ├── edit.html
    ├── index.html
    └── view.html


schema.sql

drop table if exists results;
create table results (
  `id` integer primary key autoincrement,
  `title` text not null,
  `data` text not null,
  `img` text not null,
  `created` datetime default CURRENT_TIMESTAMP


requirements.txt
利用するライブラリは以下のとおりです。(2018/4/21 修正 scipyを追記しました。)


click==6.7
cycler==0.10.0
Flask==0.12.2
itsdangerous==0.24
Jinja2==2.10
kiwisolver==1.0.1
MarkupSafe==1.0
matplotlib==2.2.0
numpy==1.14.1
pandas==0.22.0
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2018.3
scipy==1.0.1
six==1.11.0
Werkzeug==0.14.1
"""

"""
Pythonコード
run.py

import os
import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, flash
import models
 
app = Flask(__name__)
app.config.from_object(__name__)
 
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='foo-baa',
))
 
 
def connect_db():
    """""" データベス接続に接続します """"""
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con
 
 
def get_db():
    """""" connectionを取得します """"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
 
 
@app.teardown_appcontext
def close_db(error):
    """""" db接続をcloseします """"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
 
 
# 以下、画面に関わるメソッド
 
@app.route('/')
def index():
    """""" 一覧画面 """"""
    con = get_db()
    results = models.select_all(con)
    return render_template('index.html', results=results)
 
 
@app.route('/create')
def create():
    """""" 新規作成画面 """"""
    return render_template('edit.html')
 
 
@app.route('/analysis', methods=['POST'])
def analysis():
    """""" 分析実行処理 """"""
 
    title = request.form['title']
    data = request.form['data']
    img = models.create_scatter(data)
 
    con = get_db()
 
    pk = models.insert(con, title, data, img)
    flash('登録処理が完了しました。')
    return redirect(url_for('view', pk=pk))
 
 
@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
    """""" 結果削除処理 """"""
    con = get_db()
    models.delete(con, pk)
    flash('削除処理が完了しました。')
    return redirect(url_for('index'))
 
 
@app.route('/view/<pk>')
def view(pk):
    """""" 結果参照処理 """"""
    con = get_db()
    result = models.select(con, pk)
    return render_template('view.html', result=result)
 
 
if __name__ == '__main__':
    app.run()
"""
"""
models.py


""""""
ビジネスロジックモジュール
""""""
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
import time
import io
 
 
def create_scatter(data):
    data = data.replace(',', '\t').replace(' ', '\t')
    df = pd.read_csv(io.StringIO(data), sep='\t')
 
    # プロットマーカーの大きさ、色、透明度を変更
    scatter_matrix(df, diagonal='kde', color='#AAAAFF', edgecolors='#0000FF', alpha=0.5)
 
    # ファイル名
    filename = time.strftime('%Y%m%d%H%M%S') + ".png"
 
    # 保存先のパス
    save_path = "./static/result/" + filename
 
    # 表示用URL
    url = "result/" + filename
 
    # 保存処理を行う
    plt.savefig(save_path)
 
    # pltをclose
    plt.close()
 
    return url
 
 
def select_all(con):
    """""" SELECTする """"""
    cur = con.execute('select id, title, data, img, created from results order by id desc')
    return cur.fetchall()
 
 
def select(con, pk):
    """""" 指定したキーのデータをSELECTする """"""
    cur = con.execute('select id, title, data, img, created from results where id=?', (pk,))
    return cur.fetchone()
 
 
def insert(con, title, data, img):
    """""" INSERTする """"""
    cur = con.cursor()
    cur.execute('insert into results (title, data, img) values (?, ?, ?)', [title, data, img])
 
    pk = cur.lastrowid
    con.commit()
 
    return pk
 
 
def delete(con, pk):
    """""" 指定したキーのデータをDELETEする """"""
    cur = con.cursor()
    cur.execute('delete from results where id=?', (pk,))
    con.commit()
"""
"""
テンプレート
base.html

<!doctype html>
<title>簡易分析ツール</title>
<head>
    <title>簡易分析ツール</title>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
            crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" type=text/css href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
 
<header>
    <div class="navbar navbar-dark bg-dark box-shadow">
        <div class="container d-flex justify-content-between">
            <a href="/" class="navbar-brand d-flex align-items-center">
                <strong>簡易分析ツール</strong>
            </a>
        </div>
    </div>
</header>
 
<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-success">{{ message }}</div>
    {% endfor %} {% block body %}{% endblock %}
</div>
</body>
</html>
"""
"""
edit.html

{% extends "base.html" %}
{% block body %}
<h1>新規分析</h1>
<form action="{{ url_for('analysis') }}" method="post">
 
    <label>タイトル</label>
    <input class="form-control" type="text" size="30" name="title">
    <label>分析データ</label>
    <textarea class="form-control" name="data" rows="5"></textarea>
    <input class="btn btn-primary" type="submit" value="送信">
 
</form>
{% endblock %}
"""
