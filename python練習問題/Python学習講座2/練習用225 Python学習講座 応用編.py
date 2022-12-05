#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール3 mockの作成 ---")


print("--- テンプレートの作成 ---")


"""
templatesディレクトリの配下にあるhtmlファイルを記述してmockを作成しましょう。
先に予防線を張っておきますが、私はフロントはそれほど詳しくないため、
書き方やデザインがイマイチかもしれません。大目に見ていただけると幸いです。

共通テンプレートの作成

まずは親となる共通点プレートを作成しましょう。
フロントのフレームワークにbootstrap4のCDNを使用します。
以下のコードをbase.htmlに記述してください。

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
    {% block body %}
    {% endblock %}
</div>
</body>
</html>

１６行目の{{ url_for('static', filename='style.css') }}ですが、
これはstaticディレクトリのstyle.cssを指定しています。


index.html

ここからは子テンプレートの作成を行います。
index.htmlに以下をコピーペーストしてください。

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
    <tr>
        <td>0</td>
        <td>サンプルタイトル</td>
        <td>2020/01/01 12:00</td>
        <td>
            <a href="/delete/0">削除</a>
            <a href="/view/0">参照</a>
        </td>
    </tr>

</table>


{% endblock %}

１行目で共通テンプレートを継承しています。


edit.html

次に分析作成画面のテンプレートです。
edit.htmlに以下をコピーペーストしてください。

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


view.html

最後に分析参照画面のテンプレートです。
view.htmlに以下をコピーペーストしてください。

{% extends "base.html" %}
{% block body %}
<h1>結果参照</h1>

<h3>0:サンプルタイトル</h3>
<p>2020/01/01 12:00</p>
<div class="row">
    ここにグラフを配置
</div>

<div class="row">
    <textarea class="form-control" name="data" rows="5">テストデータ</textarea>
</div>

<br><br>
{% endblock %}
"""


print("--- mockの起動 ---")


"""
それでは、flaskを起動してmockを参照することができるか確認してみてください。

python run.py

http://localhost:5000もしくは
http://127.0.0.1:5000にアクセスして以下の画面が参照できれば成功です。

リンクをクリックして画面を遷移できるかも試してみてください。
"""
