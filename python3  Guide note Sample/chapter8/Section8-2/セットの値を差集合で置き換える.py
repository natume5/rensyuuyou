# セットの値を差集合で置き換える
data = {"red", "blue", "green", "yellow"}
data2 = {"blue", "black", "yellow"}
data.difference_update(data2)     # 差集合で更新する
print(data)
