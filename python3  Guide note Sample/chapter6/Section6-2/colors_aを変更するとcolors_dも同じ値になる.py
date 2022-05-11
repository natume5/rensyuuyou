# colors_aを変更するとcolors_dも同じ値になる
colors_a = ["gree", "blue", "red"]
colors_b = ["gree", "blue", "red"]
colors_c = ["gree", "red", "blue"]
print(colors_a)
colors_d = colors_a     # 代入する
print(colors_d)
print(colors_a == colors_d)       # 同じ値かどうか比較
colors_a.append("white")    # 要素を追加
print(colors_a)
print(colors_d)
