# sort()の比較関数をラムダ式で書く
sizelist = ["XS", "S", "M", "L"]    # この並びに替える
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "L", "M"]
data.sort(key=lambda item: sizelist.index(item))
# lambda item: sizelist.index(item)   ラムダ式
print(data)
