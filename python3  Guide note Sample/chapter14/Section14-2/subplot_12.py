# グラフを左右に並べる
import matplotlib.pyplot as plt


X1, Y1 = range(0, 5), [61, 45, 27, 88, 47]
X2, Y2 = range(0, 5), [17, 39, 46, 40, 27]
labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()    # 図を作る
# 1行2列の左
ax1 = fig.add_subplot(1, 2, 1)    # サブプロットを追加する
# 1)  左側
ax1.bar(X1, Y1, color="b", tick_label=labels)    # グラフの描画
ax1.set_title("dog")    # グラフのタイトル
# 1行2列の右
ax2 = fig.add_subplot(1, 2, 2)    # サブプロットを追加する
ax2.bar(X2, Y2, color="g", tick_label=labels)
ax2.set_title("cat")
plt.show()    # 図を表示
"""
python 絶対パスから図が表示されない→pythonインタプリタから一文ずついれていくと
図が表示された。
最後の一分のfig.show()をplt.show()に書き換えたら図が表示された。
"""
