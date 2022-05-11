# グリット表示とマーカー付きの折れ線グラフ
import matplotlib.pyplot as plt


price = [200, 300,  400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count, marker="o")    # グラフを描く(マーカー付き)
plt.title("count - price")    # タイトル
plt.xlabel("price")    # x軸のラベル
plt.ylabel("count")    # y軸のラベル
plt.grid(True)    # グリッド
plt.show()
