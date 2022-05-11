# 辞書を複製する
data = {"a": 100, "b": 200, "c": 300}
data_b = data.copy()     # dataを複製する
data_b["c"] = 0      # data_bの"c"の値を変更する
print(data_b)
print(data)
