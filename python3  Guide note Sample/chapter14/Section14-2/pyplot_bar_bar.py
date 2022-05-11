# 積み上げ棒グラフを描く
import matplotlib.pyplot as plt


labels = ["Green", "Red", "Yellow", "Blue", "Black", "White"]
x_pos = range(0, 6)
A = [34, 46, 54, 45, 56, 37]
B = [17, 47, 55, 67, 38, 49]
bar1 = plt.bar(x_pos, A, color="g")    # グラフAを描く
bar2 = plt.bar(x_pos, A, color="c", bottom=A)    # グラフBを描く
# bottom=A  グラフAの上に積み上げる
plt.xticks(x_pos, labels, rotation="vertical")    # x軸ラベル(垂直)
plt.legend((bar1, bar2), ("man", "woman"), loc="upper right")    # 凡例を作る
plt.show()
