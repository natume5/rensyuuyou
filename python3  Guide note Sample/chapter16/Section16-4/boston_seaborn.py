# seabornモジュールを使って散布図と回帰直線を引く
from sklearn import datasets
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


# データセットを読み込む
boston = datasets.load_boston()
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names    # 列名を設定する
boston_df["Price"] = boston.target    # 住宅価格を追加する

# 部屋数と住宅価格から回帰直線を引く
sns.set_style('whitegrid')
sns.lmplot(x = "RM", y = "Price", data = boston_df)
plt.show()
