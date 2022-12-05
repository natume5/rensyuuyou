#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール2 学習環境の構築 ---")


print("--- 環境構築 ---")


"""
プロジェクト構成

適当なディレクトリの下に、以下のzipファイルをダウンロードして解凍してください。
2018/4/21追記　schema.sqlが漏れておりました。
下記リンクからダウンロードしてください。(ご指摘くださった方ありがとうございます。)

flask_init_sample

解凍するとプロジェクトの雛形が配置されます。
構成は以下のとおりとなります。
Pythonファイルがたった２つしかないことに着目してください。

flask_sample
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

ファイル、ディレクトリの解説

簡単にですが、ファイルとディレクトリの説明をします。
run.py

Webアプリケーションを起動するモジュールです。URLごとに処理のルーティングを行います。Webアプリケーションとしてflaskが関わるのはこのモジュールのみとなります。ページ下部でもう少々細かく説明します。
models.py

ビジネスロジックのモジュールです。分析処理（散布図行列の生成）とDBアクセスを行います。
schema.sql

データベースのテーブル定義を記述しています。
requirements.txt

pipでインストールする対象モジュールです。
static

cssなどの静的ファイルを配置するディレクトリです。
また、配下のresultディレクトリには分析で作成したグラフの画像データを格納します。

templates

テンプレート（htmlの雛形）を配置するディレクトリです。
テンプレートは親子関係があり、
base.htmlが共通となる親テンプレート、
それ以外が子テンプレートとなります。

必要なモジュールのインストール

matplotlibを使用しますので、
Ubuntの方は以下でTkinterをインストールしておいてください。

sudo apt install python-tk tk-dev

pipで必要なモジュールをインストールします。

pip install -r requirements.txt

使用する主なモジュールは以下のとおりです。

    flask
    pandas
    matplotlib
    scipy


データベースの構築

sqlite3コマンドが使用できることを前提とします。
以下のコマンドを実行すると、sqlite3のデータベースファイルが作成されます。

sqlite3 db.sqlite3 < schema.sql

テーブルレイアウトは以下の通りとなります。
カラム 	型 	        内容
id 	    integer 	主キー
title 	text 	    タイトル
data 	text 	    分析対象となるデータ内容
img 	text 	    画像出力パス
created datetime 	作成日時
"""


print("--- flaskとURLルーティング ---")


"""
Webアプリケーションの主軸となるrun.pyについてもう少し説明させてください。
ダウンロードしたソースコードを見てみましょう。

import os
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='foo-baa',
))


@app.route('/')
def index():
    """""" 一覧画面 """"""
    return render_template('index.html', results={})


@app.route('/create')
def create():
    """""" 新規作成画面 """"""
    return render_template('edit.html')


@app.route('/analysis', methods=['POST'])
def analysis():
    """""" 分析実行処理 """"""
    return redirect(url_for('view', pk=0))


@app.route('/delete/<pk>')
def delete(pk):
    """""" 結果削除処理 """"""
    return redirect(url_for('index'))


@app.route('/view/<pk>')
def view(pk):
    """""" 結果参照処理 """"""
    return render_template('view.html', result={})


if __name__ == '__main__':
    app.run()

app.config.updateでflaskの設定を行うことができます。
データベース接続情報と、セッションに利用する鍵の定数設定を行っています。
１２行目以下のindex、create、analysis、delete、
viewはWebアプリケーションの画面や処理に対応する関数です。
@app.routeデコレータでURLと関数のひも付けによりルーティングを行うことができます。
本講座でのURLと関数の対応は以下のとおりとなります。

URL 	    関数 	    画面/機能 	        メソッド
/ 	        index 	Top画面（結果一覧） 	 GET/POST
/create 	create 	新規分析作成画面 	     GET/POST
/analysis 	analysis 	分析処理 	       POST
/delete/ 	delete 	    削除処理 	       POST
/view/ 	    vies 	    参照処理 	     GET/POST

app.routeの第２引数でメソッドを指定することができます。また、
URLにパラメータを加えたい場合は37行目のように<pk>のように記述します。
"""


print("--- 補足 ---")


"""
sqlite3とjinja2に関する内容が出てきます。
学習をすすめる上で必要に応じて以下リンクを参照してください。
（必ずしも前もって学習する必要はありません。）
次回、mockを作成してまず動くものを作成しましょう。
"""
