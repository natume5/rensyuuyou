# リストからイテレータを作る
colors = ["red", "blue", "green", "yellow"]    # リストはイテラブル
colors_iter = iter(colors)    # イテレータを作る
print(type(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))
