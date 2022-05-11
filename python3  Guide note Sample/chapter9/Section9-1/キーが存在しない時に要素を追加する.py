# キーが存在しない時に要素を追加する
data = {"yellow": 3, "blue": 6, "green": 5}
data.setdefault("blue", 10)     # "blue"キーがあるので変更しない
data.setdefault("white", 10)    # "white"キーはないので要素を追加する
print(data)
