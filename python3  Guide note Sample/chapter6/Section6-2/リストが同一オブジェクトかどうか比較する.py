# リストが同一オブジェクトかどうか比較する
list_a = [1, 2, 3]
list_b = list_a       # list_bにlist_aを代入
list_c = [1, 2, 3]
print(list_a is list_b)     # 同じオブジェクトかどうか比較
print(list_a is list_c)     # 同じ値だが、別のオブジェクトかどうか確認
print(list_a is not list_c)    # 同じ値だが、別のオブジェクトかどうか確認
