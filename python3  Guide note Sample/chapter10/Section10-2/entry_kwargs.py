# 必須の引数と**kwargsを組み合わせて辞書を作る
def entry(name, gender, **kwargs):
    data = {"name": name, "gender": gender}    # 必須の引数の辞書
    data.update(kwargs)    # 必須の辞書とオプションの辞書を1つに合わせる
    print(data)

# entry()を試す
entry(name="大山坂道", gender="男性", age=27, course="E")
