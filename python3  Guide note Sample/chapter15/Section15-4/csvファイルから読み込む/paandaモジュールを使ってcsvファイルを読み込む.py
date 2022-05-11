# paandaモジュールを使ってcsvファイルを読み込む
import pandas as pd    # pandaモジュール


df = pd.read_csv("data.csv")    # CSVファイルを読み込む
header = df.columns.values    # ヘッダ行
data = df.values    # データ部分
print(header)
print(data)
