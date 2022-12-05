#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール4 分析処理 ---")


print("--- DB接続機能の追加 ---")


"""
まず、データベースの接続とその管理機能を実装しましょう。
データベースの接続を管理するために、run.pyで
flaskからのimport文にsqlite3及びgというモジュールのインポートを追加します。
また、ビジネスロジックモジュールをよびだすためにmodelも追加します。
2019/4/14 model、sqlite3のimport文が漏れていたため追記。
(ご指摘くださった方ありがとうございます。)


from flask import Flask, redirect, url_for, render_template, request, g
import sqlite3
import models

また、以下３つ、connect_db、get_db、close_db関数を追加します。


# 以下、DB接続関連の関数

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

# 以下、画面/機能毎の関数
@app.route('/')
def index():
    """""" 一覧画面 """"""
   # 以下省略
   # :


新たにインポートしたgという変数ですが、これはグローバル変数です。
g.任意の変数名で代入することができます。
上の例ではg.sqlite_db = connect_db()でコネクションをgに格納しています。
connect_db関数はデータベースに接続し、コネクションを返します。
get_dbはコネクションを取得する関数です。
gに格納されていればそれを使用し、
なければconnect_dbを呼び出して新たにコネクションを作成します。
最後のclose_dbは、処理終了時に呼び出され、コネクションがあればクローズします。
close_dbには@app.teardown_appcontextデコレータがつけられていますが、
このデコレータをつけことによりリクエスト終了時に自動的にその関数が呼び出されます。
"""


print("--- ビジネスロジックの修正 ---")


"""
分析処理の追加

では、メインのビジネスロジックを作成しましょう。
今回作成するWebアプリケーションでは、
textareaに貼り付けたcsvもしくはtsv形式のデータに対し、
matplotlibで散布図行列を作成します。
models.pyに以下をペーストしてください。


""""""
ビジネスロジックモジュール
""""""
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
import pandas as pd
import time
import io


def create_scatter(data):
    """"""
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

dataはcsvかtsvの文字列とします。
上のコードの１３行目、１４行目ではそのCSV、
TSV文字列からデータフレームを生成しています。
その後、生成したデータフレームを元に散布図行列を作成しています。
作成した散布図行列は一旦ファイルとして保存して処理を終了します。
保存先ですが、後ほどアプリケーション上で参照するために
静的ファイル配置用のディレクトリに格納します。


挿入処理の追加

次に、データの登録処理を実装しましょう。

models.pyに以下を追記してください。


def insert(con, title, data, img):
    """""" INSERT処理 """"""
    cur = con.cursor()
    cur.execute('insert into results (title, data, img) values (?, ?, ?)', [title, data, img])

    pk = cur.lastrowid
    con.commit()

    return pk


引数で指定されたDBコネクションと挿入するデータをもとに挿入処理を行います。
run.pyでコネクションをグローバル領域に格納したため、
引数ではなくそこから取得しても構いません。
ただし、ビジネスロジックがflaskに依存してしまうため、
再利用性が下がってしまう点に注意してください。
"""


print("--- run.pyの修正 ---")


"""
run.pyのanalysis関数を以下のように修正してください。


@app.route('/analysis', methods=['POST'])
def analysis():
    """""" 分析実行処理 """"""

    title = request.form['title']
    data = request.form['data']
    img = models.create_scatter(data)

    con = get_db()

    pk = models.insert(con, title, data, img)
    return redirect(url_for('view', pk=pk))


request.formでhtmlのフォームから送信された値を取得しています。
models.create_scatterで散布図行列を生成した後、
送信されたデータをデータベースに登録します。
最後に参照画面にリダイレクトします。
url_forでURLと引数を指定することができます。
"""


print("--- 動作確認 ---")


"""
最後に動作確認をしてみましょう。以下にアクセスして画面を表示してください。
http://localhost:5000/create

タイトルに適当な文字列、データに以下の文字列を貼り付けて
送信ボタンをクリックしてください。

col1,col2,col3
100,200,300
300,400,100
200,100,100

エラーが発生せずに参照画面のmockに遷移すると成功です。
また、static/resultディレクトリの配下に画像が生成されていること、
resultsテーブルにデータが挿入されていることを確認してください。
"""

















