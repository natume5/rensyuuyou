# 辞書を変数に代入する
data = {"a": 100, "b": 200, "c": 300}
data_b = data    # 代入している   辞書を代入すると参照が入る
data_b["c"] = 0    # data_bの"c"の値を変更する
print(data_b)
print(data)
