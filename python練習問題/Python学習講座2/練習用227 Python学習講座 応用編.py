#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール5 参照画面の作成 ---")


print("--- 参照処理の実装 ---")


"""
models.pyの修正

参照のためにデータベースから指定したキーのデータを取得する必要があります。
select文を発行する関数を追加します。
models.pyに以下の関数を追加してください。

def select(con, pk):
    """""" 指定したキーのデータをSELECTする """"""
    cur = con.execute('select id, title, data, img, created from results where id=?', (pk,))
    return cur.fetchone()

指定したキーのデータを取得して返します。


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
テンプレートにselectした値を渡すため、
render_templateの第２引数にresultを渡しています。


テンプレートの修正

view.htmlを以下のように修正してください
(そのままペーストしていただいても構いません)。
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


print("--- 動作確認 ---")


"""
では動作を確認してみましょう。再度以下の登録画面アクセスします。
http://localhost:5000/create

タイトルに適当な文字列、データに以下の文字列を貼り付けて
送信ボタンをクリックしてください。

col1,col2,col3
100,200,300
300,400,100
200,100,100

以下のような散布図行列が表示されると成功です。
"""












