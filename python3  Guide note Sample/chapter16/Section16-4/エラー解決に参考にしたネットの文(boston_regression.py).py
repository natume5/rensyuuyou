# エラー解決に参考にしたネットの文
"""
[ValueError]Series の真理値が曖昧と言われる


こんばんは!技術評論社の「データサイエンス養成読本」の第3章 Pythonによる機械学習を
Jupyter Notebookに写経しているのですが、単回帰分析で
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().が出ます。

「指摘された行の関係性をはっきりさせればよい」との情報は得られたのですが、

px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
このコードをこれ以上どうやってはっきりさせればよいのでしょうか。
np.arangeで等差数列を生成して、
np.newaxisでこの数列を縦方向にするという意味のコードであり、過不足ないように思うのですがorz


該当コード

# リスト17 単回帰分析
LinerRegr = linear_model.LinearRegression()
X = setosa[["SepalLength"]]
Y = setosa[["SepalWidth"]]
LinerRegr.fit(X, Y)
plt.scatter(X, Y, color="black")
px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
# px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
py = LinerRegr.predict(px)
plt.plot(px, py, color = "blue", linewidth=3)
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.show()

print(LinerRegr.coef_)# 回帰係数
print(LinerRegr.intercept_) # 切片

エラー文

ValueError
Traceback (most recent call last)
<ipython-input-16-dcbb1a892a19> in <module>()
      5 LinerRegr.fit(X, Y)
      6 plt.scatter(X, Y, color="black")
----> 7 px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
      8 # px = np.arange(X.min(), X.max(), .01)[:, np.newaxis]
      9 py = LinerRegr.predict(px)

~/anaconda3/lib/python3.7/site-packages/pandas/core/generic.py in __nonzero__(self)
   1574         raise ValueError("The truth value of a {0} is ambiguous. "
   1575                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
-> 1576                          .format(self.__class__.__name__))
   1577
   1578     __bool__ = __nonzero__

ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

 できましたー(≧▽≦)
can110 様、ありがとうございます(≧▽≦) できましたー!

    px = np.arange(X.min()[0], X.max()[0], 0.01)[:,np.newaxis]
    「最小/大値の0番目の要素」で指定するのですね(ﾟдﾟ)！


完成コード

# リスト17 単回帰分析
LinerRegr = linear_model.LinearRegression()
X = setosa[["SepalLength"]]
Y = setosa[["SepalWidth"]]
LinerRegr.fit(X, Y)

plt.scatter(X, Y, color="black")
px = np.arange(X.min()[0], X.max()[0], 0.01)[:,np.newaxis]
py = LinerRegr.predict(px)

plt.plot(px, py, color = "blue", linewidth=3)
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
plt.show()

print(LinerRegr.coef_)# 回帰係数
print(LinerRegr.intercept_) # 切片



元ソースはデータサイエンティスト養成読本vol.1（Python 機械学習）でしょうか？

X.min()とX.max()がSeries型だったので
px = np.arange(X.min[0], X.max[0], 0.01)[:,np.newaxis]を
px = np.arange(X.min()[0], X.max()[0], 0.01)[:,np.newaxis]
と修正することで結果表示されるようになりました。

なお、他にも元ソースが古いため（2013年？）FutureWarningなどの警告がいくつか発生しました。
この本は改訂版が出ているようなので、それを買いなおすか、
コードは参考程度にとどめて自力で書くか修正しないとダメだと思います。

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import linear_model
np.random.seed(0)


linear_regr = linear_model.LinearRegression()
X = setosa["SepalLength"]
Y = setosa["SpealWidth"]
linear_regr.fit(X, Y)

plt.scatter(X, Y)
# px = np.arange(X.min[0], Xmax[0], 0.01)[:, np.newaxis]
px = np.arange(X.min()[0], Xmax()[0], 0.01)[:, np.newaxis]
py = linear_regr.predict(px)

plt.plot(px, py, color="blue", linewidth=3)
plt.Xlabel("SepalLength")
plt.Ylabel("SpalWidth")

linear_regr.coef_, linear_regr.intercept_, linear_regr.score(X, Y)




X = setosa[["SepalLength"]]
を
X = setosa["SepalLength"]
にしてみてはいかがでしょう。

import numpy as np
import pandas as pd
n = 10
b = pd.DataFrame(np.random.randint(4, size=(n, 2)))
b.columns = ['a','b']
b.index = np.array([str(i) for i in b.index])
print(b)

c = b[['a']]
d = b[['b']]
a = np.arange(c.min()[0], d.max()[0], 0.1)[:, np.newaxis]
print(a)

c = b['a']
d = b['b']
a = np.arange(c.min(), c.max(), 0.1)[:, np.newaxis]
print(a)



 mkgrei様、回答ありがとうございます(≧▽≦)
> X = setosa["SepalLength"]
これやったら「2次元期待してたのに渡されたのは1次元だった」というエラーが出ましたf^^;
1次元配列だったらよかったのか。。。(・_・)?

2018/11/07 22:04
リストを渡すとDataFrameになって、.min()したあとに[0]が必要になるようになります。

確かにエラーではSeriesになっているので、違和感がありました。

"""
