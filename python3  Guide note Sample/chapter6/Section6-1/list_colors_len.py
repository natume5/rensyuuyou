# リストの長さをlen()で調べてインデックスエラーにならないようにする
pos = int(input("取り出す位置:"))     # リストから取り出す位置を入力する
colors = ["blue", "red", "green", "yellow"]
length = len(colors)        # リストの長さ(要素の個数)
if -length <= pos < length:
    item = colors[pos]
    print(item)
else:
    print("エラーになりました。")
