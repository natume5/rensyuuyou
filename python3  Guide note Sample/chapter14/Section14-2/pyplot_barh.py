# 横棒グラフを作る
import matplotlib.pyplot as plt


labels = ["A", "B", "C", "D", "E"]
y_pos = range(0, 5)
V = [91, 45, 17, 88, 47]
plt.barh(y_pos, V, tick_label=labels)    # 横棒グラフを描く
plt.show()    # 表示
