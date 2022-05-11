# 上に1個、下に2個のグラフを並べる
import matplotlib.pyplot as plt


X1, Y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
X2, Y2 = range(0, 5), [77, 49, 56, 47, 67]
X3, Y3 = range(0, 4), [56, 41, 67, 76]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()    # 図を作る

# 2行1列の上
ax1 = fig.add_subplot(2, 1, 1)     # サブプロットを追加する
ax1.bar(X1, Y1, color="b", tick_label=labels)    # グラフの描画
ax1. set_title("dog")    # グラフのタイトル

# 2行2列の3番(下の左)
ax2 = fig.add_subplot(2, 2, 3)    # サブプロットを追加する
ax2.bar(X2, Y2, color="g", tick_label=labels[:5])    # グラフの描画
ax2. set_title("cat")    # グラフのタイトル

# 2行2列の4番(下の右)
ax3 = fig.add_subplot(2, 2, 4)    # サブプロットを追加する
ax3.bar(X3, Y3, color="c", tick_label=labels[:4])    # グラフの描画
ax3. set_title("bird")    # グラフのタイトル
plt.tight_layout()    # 下の図のタイトルが重ならないようにする
plt.show()    # 図を表示
