# 折れ線の種類やマーカを違う種類に設定する
import matplotlib.pyplot as plt


X = [100, 200, 300, 400, 500]
Y1 = [40, 65, 80, 100, 90]
Y2 = [34, 56, 75, 91, 79]
Y3 = [25, 47, 68, 76, 73]
Y4 = [15, 40, 52, 64, 69]
plt.plot(X, Y1, marker="o", color = "blue", linestyle = "-")
plt.plot(X, Y2, marker="v", color = "red", linestyle = "--")
plt.plot(X, Y3, marker="^", color = "green", linestyle = "-.")
plt.plot(X, Y4, marker="d", color = "m", linestyle = ":")
plt.show()
"""
color　　　　　省略形
"green"　　　　"g"
"red"　　　　　"r"
"cyan"　　　　　"c"
"magenta"　　　"m"
"yellow"　　　　"y"
"black"　　　　"b"
"white"　　　　"w"

linestyle　　　省略形
"solid"　　　　"-"
"dashed"　　　　"--"
"dashdot"　　　"-."
"dotted"　　　　":"
線の太さはlinewidth = 2.5のように指定できる。

maker　　　　　省略形
"."　　　　　　点
","　　　　　　ピクセル
"o"　　　　　　丸
"v"　　　　　　三角形(下向き)
"^"　　　　　　三角形(上向き)
"<"　　　　　　三角形(左向き)
">"　　　　　　三角形(右向き)
"1"　　　　　　Y型(下向き)
"2"　　　　　　Y型(上向き)
"3"　　　　　　Y型(左向き)
"4"　　　　　　Y型(右向き)
"8"　　　　　　八角形
"s"　　　　　　四角形
"p"　　　　　　五角形
"P"　　　　　　十字(塗り)
"*"　　　　　　星
"h"　　　　　　六角形1
"H"　　　　　　六角形2
"+"　　　　　　十字
"x"　　　　　　x
"X"　　　　　　X(塗り)
"D"　　　　　　菱形
"d"　　　　　　薄い菱形
"|"　　　　　　縦線
"_"　　　　　　横線
"""
