#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール 補足 ---")


print("--- プロジェクト ---")


"""
構成は以下のとおりとなります。

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
);


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


print("--- Pythonコード ---")


"""
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


print("--- テンプレート ---")


"""
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


index.html

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

2018/4/27 index.htmlのdelete部分に誤記があったため修正しました。
(ご指摘くださった方ありがとうございます。)


view.html

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
