# fruits辞書からキーと値を順に取り出す
fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
for key in fruit:
    value = fruit[key]     # 取り出したキーで値を調べる
    print(f"{key}が{value}個")
