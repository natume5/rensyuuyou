# ジェネレータを作るmenu_generator()関数
def menu_generator():
    yield "ワイン"     # 呼ばれたならば返す値を順にyieldで指定する
    yield "サラダ"
    yield "スープ"
    yield "ステーキ"
    yield "アイスクリーム"

menu = menu_generator()    # menuジェネレータが作られた
print(type(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
