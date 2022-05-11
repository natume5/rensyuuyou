# セットの値を和集合で更新する
data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}
data.update(data2, data3)      # 和集合で更新
print(data)
