from sklearn import datasets
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns


boston = datasets.load_boston()
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target

sns.set_style('whitegrid')
sns.lmplot(x="RM", y="Price", data=boston_df)
plt.show()
