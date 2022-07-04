#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Flask入門---")


"""
Flaskとは
PythonのWebフレームワークといえばDjangoが有名ですが、
軽量なフレームワークでは最近Flaskの人気が高まっています。

非常に薄くマイクロフレームワークと言われることもありますが、その分学習コストは非常に低いため、
敷居の低いフレームワークといえるでしょう。

軽量とはいえ、URLのルーティング、テンプレート、セッション等といった基本的な機能は予め使用可能です。

このため、簡単なREST APIをさくっと作りたい場合には非常に適しているといます。

また、近年プラグインが非常に充実してきており、
機能を拡張すると様々な機能を簡単に構築したりできるため、
ある程度の規模のシステムの構築にも耐えられるでしょう。

また、もう１点利用局面としておすすめしたいのが、社内だけで使うような簡単な分析ツールの構築です。

データセットと分析た結果を整理したり管理するのはちょっと面倒ですが、
Web化して結果をDBで管理しておくといつでも見られるし、人に見せることもできます。

次回以降、簡単に作れる簡易分析ツールの構築例を紹介したいと思います。

簡単に使ってみる
ここではFlaskを触ったことがない方向けに簡単に使い方を説明します。
詳しく知りたい方は以下の公式チュートリアルがおすすめです。

http://flask.pocoo.org/docs/0.12/tutorial/

Flaskのインストール
pipでインストールすることができます。


pip install flask
Webアプリケーションの作成
それではWebアプリケーションを早速作ってみましょう。


run1.py


from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return '<html><body><h1>sample</h1></body></html>'
 
if __name__ == '__main__':
    app.run()
以下のコマンドを実行してください。


python run1.py
http://127.0.0.1:5000/


以前はPythonコマンドから実行していたのですが、
最近は環境変数で実行ファイルを指定してflaskコマンドから起動する方法が一般的です。
Unix系の場合は以下のように実行することができます。


$ export FLASK_APP=run.py
$ flask run
"""
"""
テンプレートの使用
また、flaskはデフォルトでjinja2のテンプレートが利用可能です。
(jinja2の使い方はこちらを参照してください。)

run.pyを配置したディレクトリの下にtemplatesというディレクトリを作成し、
その直下にindex.htmlというhtmlファイルを作成してください。

<!doctype html>
<title>サンプル</title>
<head>
    <title></title>
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
                    <strong>サンプル</strong>
                </a>
            </div>
        </div>
    </header>
    <div class="content container">
        <h2>値の表示</h2>
        <p>値１：{{ values.val1 }}</p>
        <p>値２：{{ values.val2 }}</p>
    </div>
 
</body>
</html>
./run.pyは以下のように修正します。



from flask import Flask
from flask import render_template
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    values = {"val1": 100, "val2" :200}
    return render_template('index.html', values=values)
 
if __name__ == '__main__':
    app.run()

テンプレートはtemplatesディレクトリに配置します。
render_templateメソッドの第１引数にテンプレートファイル名を指定します。
また、第２引数に辞書を指定すると、テンプレート側で辞書の値を受け取ることができます。

上のコードを実行して先ほどのURLにアクセスすると、以下のような画面が表示されるはずです。

動的なWeb画面を簡単に作成することができました。

それでは冒頭に書いたとおり、次回以降はflaskを利用して簡単なWebアプリケーションを作ってみましょう。
"""


print("--- Flaskで作る簡易分析ツール1---")


"""
これから作るもの
業務で分析を行う際、いろいろ試しながらデータセットと結果の両方を管理するのは意外と面倒なものです。
このため、Flaskを利用してデータと結果を保存して人に見せられるような
Webアプリケーションを作成してみましょう。

今回は以下のような散布図行列を題材とします。


CSV、TSV形式データの入力データに対し、散布図行列を作成してデータを保存します。
また、保存したデータを一覧から参照できるようにします。
データの保存先にはsqlite3を使用しますので、コマンドラインから使用できるようにしておいてください。
(Macをお使いの方は大抵そのままで使えると思います。)

作成する画面は以下のとおりです。

新規分析画面：データの登録を行い散布図行列を作成します。
一覧画面：過去に登録した分析の一覧です。
         分析データの削除と参照画面への遷移を行うことができます。
参照画面：分析の結果を参照します。
また、あくまでもLan内で使用する簡易ツールということで、
ノンプログラマの分析の方にも実装できるよう、以下の方針で説明を行います。

とにかくお手軽に
エラーハンドリングなし
認証なし
csrfトークンもなし
"""

"""
画面毎の仕様
各画面のレイアウトです。

新規分析画面
データの登録とタイトルを入力することができます。
送信ボタンをクリックすると、登録したデータに対する散布図行列を作成し、
参照画面で参照することができます。

テキストエリア「分析データ」には以下のような多変量のデータをペーストします。一行目はヘッダーとします。

項目1   項目２   項目３   ・・・
0.7     0.11    0.46    ・・・
0.68    0.7     0.35    ・・・
0.34    0.22    0.01    ・・・
0.09    0.26    0.54    ・・・
0.65    0.55    0.62    ・・・
0.19    0.66    0.03    ・・・
:        :       :       :


参照画面
登録したデータや分析結果を参照します。

一覧画面
過去に登録したデータを一覧で参照します。
"""

"""
データベース定義
データベースにはsqlite3を使用します。テーブルは結果格納用にresultsというテーブルのみを使用します。
定義は以下のとおりです。

resultsテーブルの定義

カラム           属性                             説明
id       integer primary key autoincrement   分析データのキー
title    text not null                       分析データのタイトル
data     text not null                       分析データ本体
img text not null                            分析結果の画像（散布図行列）
created  datetime default CURRENT_TIMESTAMP  分析日時
"""


print("--- Flaskで作る簡易分析ツール2 学習環境の構築---")


"""
ここでは分析ツールの雛形をダウンロードし環境を構築してみましょう

環境構築
プロジェクト構成
適当なディレクトリの下に、以下のzipファイルをダウンロードして解凍してください。
2018/4/21追記　schema.sqlが漏れておりました。下記リンクからダウンロードしてください。
(ご指摘くださった方ありがとうございます。)

flask_init_sample

解凍するとプロジェクトの雛形が配置されます。構成は以下のとおりとなります。
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

"""
"""
ファイル、ディレクトリの解説
簡単にですが、ファイルとディレクトリの説明をします。

run.py
Webアプリケーションを起動するモジュールです。URLごとに処理のルーティングを行います。
Webアプリケーションとしてflaskが関わるのはこのモジュールのみとなります。
ページ下部でもう少々細かく説明します。

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
テンプレートは親子関係があり、base.htmlが共通となる親テンプレート、
それ以外が子テンプレートとなります。

必要なモジュールのインストール
matplotlibを使用しますので、Ubuntの方は以下でTkinterをインストールしておいてください。

sudo apt install python-tk tk-dev
pipで必要なモジュールをインストールします。

pip install -r requirements.txt
使用する主なモジュールは以下のとおりです。

flask
pandas
matplotlib
scipy
"""
"""
データベースの構築
sqlite3コマンドが使用できることを前提とします。
以下のコマンドを実行すると、sqlite3のデータベースファイルが作成されます。

sqlite3 db.sqlite3 < schema.sql
テーブルレイアウトは以下の通りとなります。

カラム       型           内容
id        integer       主キー
title      text         タイトル
data       text         分析対象となるデータ内容
img        text         画像出力パス
created   datetime      作成日時
"""
"""
flaskとURLルーティング
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
    """" 新規作成画面 """"""
    return render_template('edit.html')


@app.route('/analysis', methods=['POST'])
def analysis():
    """" 分析実行処理 """"""
    return redirect(url_for('view', pk=0))


@app.route('/delete/<pk>')
def delete(pk):
    """" 結果削除処理 """"""
    return redirect(url_for('index'))


@app.route('/view/<pk>')
def view(pk):
    """" 結果参照処理 """"""
    return render_template('view.html', result={})


if __name__ == '__main__':
    app.run()

app.config.updateでflaskの設定を行うことができます。データベース接続情報と、
セッションに利用する鍵の定数設定を行っています。

１２行目以下のindex、create、analysis、delete、viewは
Webアプリケーションの画面や処理に対応する関数です。

@app.routeデコレータでURLと関数のひも付けによりルーティングを行うことができます。
本講座でのURLと関数の対応は以下のとおりとなります。

URL 関数  画面/機能   メソッド
/   index   Top画面（結果一覧） GET/POST
/create create  新規分析作成画面    GET/POST
/analysis   analysis    分析処理    POST
/delete/    delete  削除処理    POST
/view/  vies    参照処理    GET/POST
app.routeの第２引数でメソッドを指定することができます。
また、URLにパラメータを加えたい場合は37行目のように<pk>のように記述します。
"""
"""
補足
sqlite3とjinja2に関する内容が出てきます。
学習をすすめる上で必要に応じて以下リンクを参照してください。
（必ずしも前もって学習する必要はありません。）
"""


print("--- Flaskで作る簡易分析ツール3 mockの作成---")


"""
テンプレートの作成
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
"""
"""
index.html
ここからは子テンプレートの作成を行います。index.htmlに以下をコピーペーストしてください。


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
"""
"""
edit.html
次に分析作成画面のテンプレートです。edit.htmlに以下をコピーペーストしてください。


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
"""
view.html
最後に分析参照画面のテンプレートです。view.htmlに以下をコピーペーストしてください。


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
"""
mockの起動
それでは、flaskを起動してmockを参照することができるか確認してみてください。


python run.py
http://localhost:5000もしくはhttp://127.0.0.1:5000にアクセスして
以下の画面が参照できれば成功です。

リンクをクリックして画面を遷移できるかも試してみてください。
"""


print("--- Flaskで作る簡易分析ツール4 分析処理---")


"""
DB接続機能の追加
まず、データベースの接続とその管理機能を実装しましょう。
データベースの接続を管理するために、run.pyでflaskからのimport文にsqlite3及び
gというモジュールのインポートを追加します。
また、ビジネスロジックモジュールをよびだすためにmodelも追加します。
2019/4/14 model、sqlite3のimport文が漏れていたため追記。
(ご指摘くださった方ありがとうございます。)

from flask import Flask, redirect, url_for, render_template, request, g
import sqlite3
import models
"""
"""
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
get_dbはコネクションを取得する関数です。gに格納されていればそれを使用し、
なければconnect_dbを呼び出して新たにコネクションを作成します。

最後のclose_dbは、処理終了時に呼び出され、コネクションがあればクローズします。

close_dbには@app.teardown_appcontextデコレータがつけられていますが、
このデコレータをつけことによりリクエスト終了時に自動的にその関数が呼び出されます。
"""

