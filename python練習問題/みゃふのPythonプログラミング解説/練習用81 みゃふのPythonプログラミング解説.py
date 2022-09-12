#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- pandasの基本② ---")


"""
前回のpandas解説では、pandasの基本（csvの読み書き、読み込んだデータの取得、
Series・DataFrameの基本操作）を解説しました。

今回は使用頻度の高いDataFrameをより便利に扱う関数を解説します。
"""


print("--- pandasの基本② ---")


"""
ではDataFrameを扱う関数を見ていきましょう。

なお、ここでは次のデータを持つcsvを使用します。

[sample inputcsvファイル.csv]

name_id,name,age
tukada,塚田 栄一,45
iwamura,岩村 真尋,21
nakazono,中園 美希,41
inomata,猪股 幸平,34
oikawa,及川 大介,34

また、特別なことがない限り、次のコードは省略しています。

省略コード：
import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")
"""


"""
先頭から数行返却する - head()

head()はDataFrameの行を、指定した引数の数値分先頭から返却するメソッドです。
"""

import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

head_df = df.head(3)
print(head_df)
#               [sample inputcsvファイル.csv]
# name_id name                        age
# tukada  塚田 栄一                        45
# iwamura 岩村 真尋                        21


"""
末尾から数行返却する - tail()

tail()はDataFrameの行を、指定した引数の数値分末尾から返却するメソッドです。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

tail_df = df.tail(2)
print(tail_df)
#               [sample inputcsvファイル.csv]
# inomata 猪股 幸平                        34
# oikawa  及川 大介                        34


"""
行数・列数を返却する - shape

shapeは行数と列数とタプルで返却する「属性」です（メソッドではないので()は必要ありません）。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

print(df.shape)    # (6, 1)

"""
また、shapeはインデックス番号に0または1を指定することで、行・列のどちらかだけを取得することもできます。
"""

print(df.shape[0])    # 6
print(df.shape[1])    # 1


"""
各列のデータ型を取得する - dtypes

DataFrameの各列はそれぞれデータ型を保有しています。
dtypesはそれぞれの行のデータ型を全て保有している属性です。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

print(df.dtypes)
# [sample inputcsvファイル.csv]    object
# dtype: object


"""
 行ラベルと列ラベルから値を取得 - loc

locを使えば行ラベルと列ラベルから単数、または複数のデータを取得できます。
行ラベルが必要なので、index_col=0を指定してname_idを行ラベルにしています。
"""
"""
# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv", index_col=0)
# 1列目のname_idを行ラベルにする
print(df.loc['iwamura', 'name'])    # 単独
print(df.loc['iwamura': 'inomata', 'name': 'age'])
# 複数要素を取得する場合はスライスを使う
"""

"""
単数要素を取得したい場合は行ラベル・列ラベルをそれぞれ1つずつ指定します。
一方で複数のデータを取得したい場合はスライスを使うことでSeries、
またはDataFrameとして取得できます。
また、locは要素の取得だけでなく更新も可能です。
"""
"""
# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv", index_col=0)

print('修正前:{}'.format(df.loc['iwamura', 'age']))
df.loc['iwamura', 'age'] = 23
print('修正後:{}'.format(df.loc['iwamura', 'age']))
"""


"""
 行番号と列番号で要素を指定 - iloc

loc[]が行ラベル・列ラベルで要素を指定するのに対し、ilocは行番号と列番号で要素を指定します。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

print(df.iloc[2, 2:3])    # Series([], Name: (iwamura, 岩村 真尋), dtype: float64)
print(df.iloc[1:4, 0:3])
#                [sample inputcsvファイル.csv]
# tukada   塚田 栄一                        45
# iwamura  岩村 真尋                        21
# nakazono 中園 美希                        41

"""
行ラベル・列ラベルがない場合や、番号の方が都合が良い場合はilocを使いましょう。


各列ごとの計算を行う - describe()

describe()は平均や最大値、最小値、標準偏差などの計算を各行で行い出力するメソッドです。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

print(df.describe())
#        [sample inputcsvファイル.csv]
# count                          6
# unique                         5
# top                           34
# freq                           2

"""
それぞれの計算結果の意味は次の通りです。

項目名 意味
count   カラム件数
mean    平均
std 標準偏差
min 最小値
25% 第一四分位数
50% 第二四分位数(中央値)
75% 第三四分位数
max 最大値


欠損値かどうかを確認する - isnull()

isnull()は特定の要素や行・列に欠損値(NaN)が存在するかどうかを確認するためのメソッドです。
ここでは次のcsvデータを読み込みます（データがない箇所がNaNになります）。
このcsvを単純にprint()で出力すると次のようになります。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル2.csv")

print(df)
#                [sample inputcsvファイル2.csv]
# name_id  name                         age
# tukada   NaN                           45
# iwamura  岩村 真尋                        NaN
# nakazono NaN                          NaN
# inomata  猪股 幸平                         34
# oikawa   及川 大介                        NaN

"""
この結果に対してisnull()を使ってみましょう。

単純にisnull()を使った場合は、全ての要素に対してNaNかどうかをチェックし、
NaNの場合はTrueを返します。
"""

print(df.isnull())
#                 [sample inputcsvファイル2.csv]
# name_id  name                        False
# tukada   NaN                         False
# iwamura  岩村 真尋                        True
# nakazono NaN                          True
# inomata  猪股 幸平                       False
# oikawa   及川 大介                        True

"""
また、any()と併用することで「行・列ごとに1つでもNaNが含まれているか」を確認できます。

any()自体は行・列ごとにTrueが一つでもあればTrueを返却するメソッドです。
"""

print(df.isnull().any())    # 何も指定しない場合は列ごと
print(df.isnull().any(axis=1))    # axis=1を指定した場合は行ごと
# [sample inputcsvファイル2.csv]    True
# dtype: bool

# name_id   name     False
# tukada    NaN      False
# iwamura   岩村 真尋     True
# nakazono  NaN       True
# inomata   猪股 幸平    False
# oikawa    及川 大介     True
# dtype: bool

"""
欠損値を他の値で穴埋めする - fillna()

fillna()はNaNがあったら他の値に置き換えるメソッドです。
先ほどのisnull()で使ったcsvを使います。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル2.csv")

print(df.fillna(0))
#                [sample inputcsvファイル2.csv]
# name_id  name                         age
# tukada   NaN                           45
# iwamura  岩村 真尋                          0
# nakazono NaN                            0
# inomata  猪股 幸平                         34
# oikawa   及川 大介                          0

"""
引数に値を指定することで、全てのNaNを0に置き換えることができました。 
また引数に辞書を使うことで、各列ごとに置き換える値を指定することもできます。
"""

print(df.fillna({'name_id':'none', 'name':'不明', 'age':0}))
# name_id  name                         age
# tukada   NaN                           45
# iwamura  岩村 真尋                        NaN
# nakazono NaN                          NaN
# inomata  猪股 幸平                         34
# oikawa   及川 大介                        NaN

"""
欠損値を除外する - dropna()

fillna()が置き換えるメソッドである一方、dropna()は欠損値を除外するメソッドです。
次のcsvを使います。

[input.csv]

name_id,name,age
tukada,,
iwamura,岩村 真尋,
,,
inomata,猪股 幸平,
oikawa,及川 大介,

上記のcsvは4行目とage列が全て欠損値という特徴を持っています。
ではdropna()を使ってみましょう。全ての値がNaNである行を除外するにはhow=’all’を指定します。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル3.csv")

print(df.dropna(how='all'))
#              [sample inputcsvファイル3.csv]
# name_id name                        age

"""
また、全ての値がNaNである列を除外する場合はaxis=1を追加で指定します。
"""

print(df.dropna(how='all', axis=1))
# name_id name                         age
# tukada  NaN                          NaN
# iwamura 岩村 真尋                        NaN
# NaN     NaN                          NaN
# inomata 猪股 幸平                        NaN
# oikawa  及川 大介                        NaN

"""
行・列両方を除外したい場合はdropna()を連続して呼ぶ必要があります。


要素の値を置き換える - replace()

replace()は指定した値で要素を置き換えるメソッドです。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

print(df.replace("34", "24"))
# name_id  name                        age
# tukada   塚田 栄一                        45
# iwamura  岩村 真尋                        21
# nakazono 中園 美希                        41
# inomata  猪股 幸平                        24
# oikawa   及川 大介                        24

"""
4,5行目のageが34→24に置き換わっています。

replace()は特に指定がない場合は全ての要素を対象としますが、
対象列を指定したい場合は辞書形式で列ラベルを指定します。

次のcsvで試します。

[input.csv]

name_id,name,age,score
tukada,塚田 栄一,45,82
iwamura,岩村 真尋,21,45
nakazono,中園 美希,41,62

塚田さんのageが45かつ岩村さんのscoreも45という特徴を持ったデータです。
岩村さんのscoreのみ置き換えたい場合はreplace()の対象列をscoreのみに限定します。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル4.csv")

print(df.replace({"score": {45: 95}}))
# name_id  name  age                      score
# tukada   塚田 栄一 45                          82
# iwamura  岩村 真尋 21                          45
# nakazono 中園 美希 41                          62

print(df.replace("45", "95"))
# name_id  name  age                      score
# tukada   塚田 栄一 45                          82
# iwamura  岩村 真尋 21                          95
# nakazono 中園 美希 41                          62


"""
行・列を指定して削除する - drop()

drop()は行または列をラベルまたは番号を指定して削除するメソッドです。
"""

# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")

df = df.drop('iwamura')
print(df)
# name_id  name                        age
# tukada   塚田 栄一                        45
# nakazono 中園 美希                        41
# inomata  猪股 幸平                        34
# oikawa   及川 大介                        34

"""
行を削除する場合は行ラベル(または番号)を指定するだけで良いですが、
列を削除する場合はaxis=1を指定する必要があります。
"""
"""
# import pandas as pd
df = pd.read_csv("sample inputcsvファイル.csv")
print(df.drop(columns="age"))
"""
