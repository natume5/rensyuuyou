# aセットがbセットのサブセットかどうかを判定する
a = {"blue", "red"}
b = {"blue", "green", "red", "pink", "white"}
print(a.issubset(b))      # aはbのサブセットである
print(a <= b)             # aはbのサブセットである
