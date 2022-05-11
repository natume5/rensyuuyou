# リストに削除したい値が含まれていたならば削除する
colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "yellow"      # "yellow"を削除する
# 削除する値が含まれているならば削除する
if target in colors:
    colors.remove(target)
print("削除後", colors)
