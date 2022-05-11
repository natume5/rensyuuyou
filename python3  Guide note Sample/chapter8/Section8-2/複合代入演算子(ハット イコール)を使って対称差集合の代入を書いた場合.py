# 複合代入演算子(ハット イコール)を使って対称差集合の代入を書いた場合
data = {"red", "blue", "green", "yellow"}
data2 = {"blue", "black", "yellow"}
data ^= data2     # 対称差集合で置き換える
print(data)
