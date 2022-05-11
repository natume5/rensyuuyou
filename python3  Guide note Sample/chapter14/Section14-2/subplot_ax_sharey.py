# Y軸を共有したサブプロットにグラフを表示する
import matplotlib.pyplot as plt


X1, Y1, = range(0, 5), [61, 45, 27, 88, 47]
X2, Y2, = range(0, 5), [17, 39, 46, 40, 27]
labels = ["A", "B", "C", "D", "E"]

# Y軸を共有する2個のサブプロットを追加する
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
# 1行2列のサブプロットを追加
ax1.bar(X1, Y1, color="b", tick_label=labels)    # Y軸を共有したグラフ
ax1.set_title("dog")    # グラフのタイトルを設定
ax2.bar(X2, Y2, color="g", tick_label=labels)    # Y軸を共有したグラフ
ax2.set_title("cat")    # グラフのタイトルを設定
plt.show()    # 図を表示
