# 回帰モデルを作って部屋数と価格の訓練データで訓練する
from sklearn import datasets
from pandas import DataFrame    # pandasモジュールを利用
from sklearn.linear_model import LinearRegression as LR


boston = datasets.load_boston()
dir(boston)
boston.DESCR
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target
rooms_train = DataFrame(boston_df["RM"])    # 部屋数のデータを抜き出す
y_train = boston.target    # ターゲット
model = LR()    # 回帰モデルを作る
model.fit(rooms_train, y_train)    # 訓練する
"""
model = linear_model.LinearRegression()の所で
name 'linear_model' is not definedと出てつまずく
→linear_model.LinearRegression()をLR()に
一番上の文にfrom sklearn.linear_model import LinearRegression as LR
を追加したらエラーを吐かなくなった。
"""
