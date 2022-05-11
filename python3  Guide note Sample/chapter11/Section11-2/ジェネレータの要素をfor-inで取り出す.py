# ジェネレータの要素をfor-inで取り出す


def menu_generator():
    yield "ワイン"
    yield "サラダ"
    yield "スープ"
    yield "ステーキ"
    yield "アイスクリーム"

menu = menu_generator()    # menuジェネレータを作る
for item in menu:    # menuジェネレータからすべての値を順に取り出す
    print(item)
    # 全部取り出したところでfor文を抜ける
