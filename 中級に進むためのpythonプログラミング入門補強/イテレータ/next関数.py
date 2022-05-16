color_list = ["red", "green", "blue",
              "yellow", "cyan", "magenta"]
color_iter = iter(color_list)
# 一つ目の値、"red"を取る
print(next(color_iter))
# 更に次の二つ目の値、"green"を取る
print(next(color_iter))
print("-" * 10)
# 二つ目まで取ってあるので、ループは"blue"から始まる
for color in color_iter:
    print(color)




