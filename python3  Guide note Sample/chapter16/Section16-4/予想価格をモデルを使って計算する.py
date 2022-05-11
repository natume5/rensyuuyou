# 予想価格をモデルを使って計算する
from sklearn import datasets
from pandas import DataFrame    # pandasモジュールを利用
from sklearn.linear_model import LinearRegression as LR
import numpy as np


boston = datasets.load_boston()
dir(boston)
boston.DESCR
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target
rooms_train = DataFrame(boston_df["RM"])    # 部屋数のデータを抜き出す
y_train = boston.target    # ターゲット
model = LR()    # 回帰モデルを作る
model.fit(rooms_train, y_train)

# 部屋数のテストデータを作る
rooms_test = DataFrame(np.arange(rooms_train.min()[0], rooms_train.max()[0], 0.1))
price_test = model.predict(rooms_test)    # モデルを使って住宅価格を予想する
