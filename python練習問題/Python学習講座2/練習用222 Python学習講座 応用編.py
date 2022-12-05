#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flask入門 ---")


print("--- Flaskとは ---")


"""
PythonのWebフレームワークといえばDjangoが有名ですが、
軽量なフレームワークでは最近Flaskの人気が高まっています。
非常に薄くマイクロフレームワークと言われることもありますが、
その分学習コストは非常に低いため、敷居の低いフレームワークといえるでしょう。
軽量とはいえ、URLのルーティング、テンプレート、
セッション等といった基本的な機能は予め使用可能です。
このため、簡単なREST APIをさくっと作りたい場合には非常に適しているといます。
また、近年プラグインが非常に充実してきており、
機能を拡張すると様々な機能を簡単に構築したりできるため、
ある程度の規模のシステムの構築にも耐えられるでしょう。
また、もう１点利用局面としておすすめしたいのが、
社内だけで使うような簡単な分析ツールの構築です。
データセットと分析た結果を整理したり管理するのはちょっと面倒ですが、
Web化して結果をDBで管理しておくといつでも見られるし、人に見せることもできます。
次回以降、簡単に作れる簡易分析ツールの構築例を紹介したいと思います
"""


print("--- 簡単に使ってみる ---")


"""
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

python run.py

http://127.0.0.1:5000/

sampleの文字が表示されると成功です。

以前はPythonコマンドから実行していたのですが、
最近は環境変数で実行ファイルを指定して
flaskコマンドから起動する方法が一般的です。
Unix系の場合は以下のように実行することができます。

$ export FLASK_APP=run1.py
$ flask run

テンプレートの使用

また、flaskはデフォルトでjinja2のテンプレートが利用可能です。
(jinja2の使い方はこちらを参照してください。)
run.pyを配置したディレクトリの下にtemplatesというディレクトリを作成し、
その直下にindex.htmlというhtmlファイルを作成してください。

./templates/index.html

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

./run1.pyは以下のように修正します。

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
また、第２引数に辞書を指定すると、
テンプレート側で辞書の値を受け取ることができます。
上のコードを実行して先ほどのURLにアクセスすると、
値の表示と画面が表示されるはずです。

動的なWeb画面を簡単に作成することができました。

それでは冒頭に書いたとおり、
次回以降はflaskを利用して簡単なWebアプリケーションを作ってみましょう。
"""
