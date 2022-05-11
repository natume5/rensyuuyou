# データセットをDataFrame型に変換し出力する
from sklearn import datasets
from pandas import DataFrame    # pandasモジュールを利用


boston = datasets.load_boston()
dir(boston)
boston.DESCR
boston_df = DataFrame(boston.data)    # DataFrame型にする
boston_df.columns = boston.feature_names    # 列名を設定  列データを名前で
boston_df["Price"] = boston.target    # 住宅価格を追加する  取り出せるようになる
print(boston_df[:5])    # 最初の5行だけ
