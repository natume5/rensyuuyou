# 同じキーを持った辞書を作る
fruits = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
fruits2 = dict.fromkeys(fruits, 0)    # fruits辞書をもとにfruits2辞書を作る
print(fruits2)
