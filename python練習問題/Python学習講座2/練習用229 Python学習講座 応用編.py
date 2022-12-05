#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール7 flashメッセージ ---")


print("--- flaskのflashメッセージ ---")


"""
flashメッセージとは、処理が終わったりエラーが発生した際に
その旨を通知するメッセージのことです。
flaskにはデフォルトでflashメッセージ機能がありますのでそれを使ってみましょう。


テンプレートの修正

まずは、テンプレートにflashメッセージを挿入する部分を追加しましょう。
base.htmlのcontainer部分を以下の通り修正してください。
（block bodyの前に追加します。）

<div class="container">
    {% for message in get_flashed_messages() %}
    <div class="alert alert-success">{{ message }}</div>
    {% endfor %}
    {% block body %}{% endblock %}
</div>

get_flashed_messagesメソッドを使用することにより、
セッションに格納されたメッセージを取得することができます。


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


print("--- 動作確認 ---")


"""
登録、削除処理を行ってみてください。

登録、削除処理後に画面上部にメッセージが表示されたら成功です。
"""
