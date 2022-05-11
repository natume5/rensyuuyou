# ["XS","S","M","L"]の順になるようにソートする
def size(item):    # 比較関数を定義する
    sizelist = ["XS", "S", "M", "L"]    # この並びに替える
    pos = sizelist.index(item)    # itemのインデックス番号を値として返す
    return pos

# 並び替えるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "L", "M"]
data.sort(key=size)    # dataをサイズ順に並べる
print(data)
