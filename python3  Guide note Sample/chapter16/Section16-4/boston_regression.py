# 実際のデータと回帰直線をグラフ表示する
from sklearn import datasets
from pandas import DataFrame    # pandasモジュールを利用
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np



boston = datasets.load_boston()
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target
print(boston_df[:10])    # 最初の10行だけ
# 訓練データを作る
rooms_train = DataFrame(boston_df["RM"])    # 部屋数のデータを抜き出す
y_train = boston.target    # ターゲット
model = linear_model.LinearRegression()    # 回帰モデルを作る
model.fit(rooms_train, y_train)

# 部屋数のテストデータを作る
rooms_test = DataFrame(np.arange(rooms_train.min()[0], rooms_train.max()[0], 0.1))
prices_test = model.predict(rooms_test)
# グラフ表示をする
plt.scatter(rooms_train, y_train, c="b", alpha=0.5)    # 訓練データ
plt.plot(rooms_test, prices_test, c="r")    # 回帰直線
plt.title("Boston House Price dataset")
plt.xlabel("roomss")     # x軸のラベル
plt.ylabel("Price $1000's")    # y軸のラベル
plt.show()
"""
line 22, in <module>
rooms_test = DataFrame(np.arange(rooms_train.min(), rooms_train.max(), 0.1))
の所が
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
のエラーが出る。
→ネットのエラー対応を見てmin()とmax()の後ろに[0]を付けたらグラフが出た。
"""
