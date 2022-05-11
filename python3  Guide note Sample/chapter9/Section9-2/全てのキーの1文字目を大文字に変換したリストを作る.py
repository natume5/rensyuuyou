# 全てのキーの1文字目を大文字に変換したリストを作る
fruits = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
keys = [key.capitalize() for key in fruits.keys()]
print(keys)
