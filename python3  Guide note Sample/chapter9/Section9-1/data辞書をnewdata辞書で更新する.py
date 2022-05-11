# data辞書をnewdata辞書で更新する
data = {"a": 10, "b": 20, "c": 30}    # 元の辞書
newdata = {"a": 15, "d": 99}     # 更新用の辞書
data.update(newdata)     # dataを更新する
print(data)
