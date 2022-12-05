#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール6 一覧画面の作成 ---")


print("--- 一覧参照処理の実装 ---")


"""
models.pyの修正

一覧参照のために、結果全件取得処理が必要となります。
models.pyに以下の関数を追加してください。

def select_all(con):
    """""" SELECTする """"""
    cur = con.execute('select id, title, data, img, created from results order by id desc')
    return cur.fetchall()

resultテーブルの内容を全件取得して返します。


run.pyの修正

モデルの呼び出し処理をrun.pyに実装します。
view関数を以下のように修正してください。

@app.route('/')
def index():
    """""" 一覧画面 """"""
    con = get_db()
    results = models.select_all(con)
    return render_template('index.html', results=results)

DBアクセスして取得した結果をテンプレートに渡します。


テンプレートの修正

一覧画面のテンプレートを修正します。
run.pyから渡された値を表示するために、
index.htmlを以下のように修正しましょう。

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


print("--- 削除処理の実装 ---")


"""
次に削除処理を実装しましょう。
画面はありません。

models.pyの修正

DBのレコード削除処理を実装します。
models.pyに以下を追記してください。

def delete(con, pk):
    """""" 指定したキーのデータをDELETEする """"""
    cur = con.cursor()
    cur.execute('delete from results where id=?', (pk,))
    con.commit()

指定したidのレコードに対してdelete文を発行します。


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


print("--- 動作確認 ---")


"""
お疲れ様です。これで一通りの機能が実装されました。
一覧画面にアクセスして、登録したデータが表示されること、
削除ができることを確認してください。

http://localhost:5000

今回ビジネスロジックに散布図行列を使いましたが、
Pythonを使えば主成分分析やK-meansによるクラスター分析
といった表計算ソフトで難しい分析処理を簡単にWeb上に実装することが可能です。
みなさまも日々使用する処理のWeb化に挑戦してみてください。
"""
