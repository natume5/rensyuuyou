# 凡例を表示する
import matplotlib.pyplot as plt


X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56, 75, 91, 79]
Y3 = [25, 47, 68, 76, 73]
plt.plot(X, Y1, marker="o", linestyle = "-", label = "Y1")
plt.plot(X, Y2, marker="v", linestyle = "--", label = "Y2")
plt.plot(X, Y3, marker="^", linestyle = "-.", label = "Y3")
# label = "Y1",label = "Y2",label = "Y3"  凡例で線のスタイル対応させるラベル
plt.legend(loc = "upper left")    # 凡例を作る
# legend(loc = "upper left")  凡例の位置をグラフの左上にする
plt.show()    # 表示
"""
凡例を表示する位置locは次の値で指定する。
"upper left"は2のようにコード(数値)でも指定できる。
loc　　　　　　　　コード
"best"　　　　　　　0
"upper right"　　　1
"upper left"　　　　2
"lower left"　　　　3
"lower right"　　　4
"right"　　　　　　5
"center left"　　　6
"center right"　　7
"lower center"　　8
"upper center"　　9
"center"　　　　　10
"""