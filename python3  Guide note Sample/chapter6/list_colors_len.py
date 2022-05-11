pos = int(input("取り出す位置"))
colors = ["blue", "red", "green", "yellow"]
length = len(colors)
if -length <= pos < length:
    item = colors[pos]
    print(item)
else:

    print("エラーになりました。")
