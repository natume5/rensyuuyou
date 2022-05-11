# discade()でセットの要素を削除する
color_set = {"blue", "yellow", "red"}
color_set.discard("green")     # 含まれていない要素を削除しようとしてもエラーにならない
print(color_set)
color_set.discard("red")
print(color_set)
