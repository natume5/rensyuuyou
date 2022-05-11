# セットの値を積集合で置き換える
data = {"red", "blue", "green", "yellow"}
data2 = {"blue", "black", "yellow"}
data.intersection_update(data2)     # 積集合で更新する
print(data)
