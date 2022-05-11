# &=演算子を使って積集合を書いた場合
data = {"red", "blue", "green", "yellow"}
data2 = {"blue", "black", "yellow"}
data &= data2     # 積集合で置き換える
print(data)
