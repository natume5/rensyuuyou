# list_aを変更するとlist_bが同じ値になる
list_a = [1, 2, 3]
list_b = list_a       # list_bにlist_aを代入
list_c = [1, 2, 3]
list_a[0] = 99      # list_aの値を変更
print(list_a)
print(list_b)
