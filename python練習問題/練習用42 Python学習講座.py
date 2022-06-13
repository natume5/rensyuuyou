#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- pandas入門 Seriesの演算---")


"""
pandasのSeriesには独自に演算が定義されています。
あまりこのトピックを扱った資料は少ないのですが、この後学ぶDataFrameの操作でも使用するため、
今後の理解の支えになると思います。


スカラー演算

Seriesオブジェクトに対し、スカラーの演算をすることができます。

以下、四則演算のサンプルとなります。
"""

import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

# 足し算
print(s + 10)

# 引き算
print(s - 10)

# 掛け算
print(s * 1)

# 割り算
print(s / 2)

"""
演算が定義されていないオブジェクトをSeriesに格納している場合は
「TypeError: unsupported operand」が発生します。


Series同士の演算

Series同士も同様に演算を行うことができます。まずは足し算のサンプルです。
"""

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s1)

s2 = pd.Series([3, 4, 5, 6], index=['a', 'b', 'c', 'd'])
print(s1 + s2)

"""
index同士をひも付けて演算が行われます。試しにindexをずらしてみましょう。
"""

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([3, 4, 5, 6], index=['c', 'd', 'e', 'f'])

print(s1 + s2)

"""
演算対象の2つのSeries双方にindex設定されていない場合はNaNとなります。
引き算、掛け算、割り算も同様なので説明は割愛します。


Seriesの論理演算

最後になりましたが、この後のDataFrameの操作を理解する際に非常に重要になります。

Seriesには論理演算が定義されていて、条件に該当するかどうかでindexごとにbool型の値が設定されます。

例えば、「2より大きいかどうか」という論理演算の結果は以下のようになります。
"""

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s > 2)

"""
また、indexに対して論理演算をすることも可能です。
indexが'c'かどうか、という論理演算の結果は以下のようになります。
"""

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s.index == 'c')

"""
ただし、この場合の戻り値の型はnumpy.ndarrayとなります。
"""


print("--- pandas入門 DataFrameの生成の基本---")


"""
次に分析の中核となるDataFrameの生成についてです。
まずは操作に馴染むためにリストなどのシーケンシャルオブジェクトからDataFrameを生成する方法について学習します。

別項にて説明しますが、実際の業務ではこのページのサンプルのようにコードに値を書くことはまずなく、

    CSVやTSVなどのテキストファイル
    Excel
    MySQLやPostgresのようなRDB

などからデータを取得してDataFrameを生成することが一般的です。

（サンプルでは読者がコピペしやすいように記述していますが、
スクリプトを毎回書くのは手間がかかるためipythonを使用することをおすすめします。）


DataFrameの生成の基本
index、columnを指定しないで生成する

まずは2列×4行のDataFrameを生成してみましょう。
DataFrameのコンストラクタに2次元リストを指定します。
"""

# import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]])
print(df)

"""
出力結果の上段がcolumnです。生成時に指定していなかったためデフォルト値として0,1が設定されています。

出力結果の左側がindexです。こちらも生成時に指定していなかったためデフォルト値として0〜3が設定されています。


index、columnを指定する

こちらでも説明しましたが、DataFrameではindex、columnと呼ばれる行、列のラベルを設定することができます。
生成時の引数にそれぞれindex、columnsを指定すると設定されます
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
index=['a', 'b', 'c', 'd'], columns=['col1', 'col2'])
print(df)

"""
列名としてcol1、col2が、行名としてa〜dが設定されていることが確認できます。


辞書から生成する

Seriesと同じく辞書から生成することも可能です。
"""

data = {'col1': [1, 2, 3], 'col2': [10, 20, 30]}
df = pd.DataFrame(data)
print(df)

"""
SeriesからDataFrameを生成する

最後にSeriesからDataFrameを生成する方法についてです。
この方法はindexを考慮してマージしてくれるため非常に便利でよく使います。
"""

s1 = pd.Series([100, 101, 102], index=['a', 'b', 'c'])
s2 = pd.Series([100, 101, 102], index=['b', 'c', 'd'])
df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)

"""
2つの生成済みのSeriesがあり、ここからDataFrameを生成しています。
このときSeriesで設定されているindexが同じものを同じ行としてマージしてくれます。
当該indexがない場合はNaNが設定されます。

何らかのDataFrameをもとに計算した結果を複数のSeriesに格納し、
マージして新たなDataFrameを生成する、という操作は時系列データ分析でよく使用する方法です。
"""


print("--- pandas入門 DataFrame 基本統計量の算出---")


"""
DataFrameに格納されたデータは簡単に基本的な統計量を計算することができます。


行数、要素数
行数（レコード数）

行数を出力する場合はlen関数を使用します。また、sizeメソッドを使用すると要素数を取得することができます。
"""

# import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df)
print(len(df))

"""
上のサンプルでは2列3行のDataFrameの行の長さをlenで取得しています。
要素数

sizeプロパティで要素数を取得することができます。
"""

print(df.size)


"""
基本統計量

DataFrameのメソッドを使用して、列ごとの基本統計量を取得することができます。
平均、最大最小、標準偏差、分散など
"""

print(df.count())    # 要素数

print(df.mean())    # 平均

"""
なお、戻り値は全てDataFrame型オブジェクトとなります。
別項にて説明しますが、各列の統計量を取得する場合はインデックスを指定します。

例えば、列「col1」の平均値を取得する場合、df.mean()['col1'] と記述します。

その他、よく使うメソッドを以下にまとめます。
df.count()  要素数
df.mean()   平均
df.std()    標準偏差
df.max()    最大値
df.min()    最小値
df.var()    分散
df.sample()     ランダムサンプリング
まとめて取得

また、全体的にデータを俯瞰したい場合、describeを使用することで基本的な統計量が
一括で取得することができます。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df.describe())

"""
こちらも戻り値はDataFrameなので、個別の値を取得したい場合ば列、行をインデックスで順にしていします。

例えば、col2の平均を取得したい場合、df.describe()['col2']['mean'] と記述します。
"""

print(df.describe()['col2']['mean'])


print("--- pandas入門 DataFrameのデータ参照---")


"""
これまでDataFrameに関する説明と、基本的な統計量の算出方法について説明しました。

このページではDataFrame内部のデータを参照する方法について学習します。


列を取得する

カラムを指定して列データをSeriesとして取得する方法は2つあります。

DataFrameオブジェクト['カラム名']もしくは、DataFrameオブジェクト.カラム名と記述します。

DataFrameは以下の3行2列のDataFrameを使用するものとします。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'], 
index=['a', 'b', 'c'])

print(df)
print(df['col1'])
print(df.col2)

"""
取得できるオブジェクトの型は前述の通り、Series型となります。
したがって、このあと行を指定する場合は以下のように[]か.で記述します。
"""

# col2のa行目を[]で取得
print(df.col2['a'])    # 10

# col2のa行目を.で取得
print(df.col2.a)    # 10


"""
スライスする

またDataFrameはスライス構文を取得すると行を絞ったDataFrameが取得できます。

私はpandasのこの仕様で最初非常に混乱しました。スライスで指定できるのは行で、
取得できるのがDataFrameである点に注意してください。

サンプルです。3行2列のDataFrameでindexはデフォルトが使用されています。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df)

print(df[1:2])

"""
1行以降、2行目未満がDataFrameで取得されます。


loc、ilocで行データをSeries形式で取得

loc、ilocで行データをseries形式で取得することができます。

locはラベル名、つまりindexを指定し、ilocはinteger-location、つまり位置を表す整数でアクセスします。

DataFrameは以下の3行2列のDataFrameを使用するものとします。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]], columns=['col1', 'col2'])
print(df)

"""
loc

まずはlocです。たとえば、index=0を指定する場合以下のように記述します。
"""

print(df.loc[0])

"""
また、スライスを使用することも可能です。この場合取得できるのはDataFrameオブジェクトです。
"""

print(df.loc[1:2])

"""
例えば、0行目のcol1のデータを取得する場合は以下のように記述します。
"""

print(df.loc[0]['col1'])    # 1

"""
iloc

locと使用方法はほとんど同じです。integer-location形式で指定します。
例えば、0から数えて1行目を取得する場合は以下のように記述します。
"""

print(df.iloc[1])


"""
at、iatで行、列を指定して値を取得する

at、iatで行、列を指定して値を取得することができます。


at

atはラベル名でアクセスします。行、列の順で添字に指定します。
例えば、indexがaの行でカラムがcol1のデータを取得する場合、以下のように記述します。
Python 数値計算入門 より
"""

area = pd.Series({'徳島': 4147, '香川': 1877, '愛媛': 5676, '高知': 7104})
pop = pd.Series({'徳島': 755733, '香川': 976263, '愛媛': 1385262, '高知': 728276})

# 列ラベル割り当て
columns = {"面積": area, "人口":pop}

# DataFrameを作成
data = pd.DataFrame(columns)

print(data)
print(data.at["愛媛", "人口"])

"""
iat

atと使用方法はほとんど同じです。integer-location形式で指定します。

例えば0から数えて1行1列目の要素を取得する場合、以下のように記述します。
"""

print(data.iat[0, 0])


"""
補足

loc、iloc、at、iatに加え、axというメソッドがありますが、
最新バージョンではなくなっているため説明は割愛します。
"""


print("--- pandas入門 DataFrameのフィルタリング---")


"""
ここではDataFrameに対し、条件を満たす行を抽出する処理について学習します。
SQLでいうところのselect文のwhere句に相当します。


pandasのフィルタリングの基礎概念

pandasのフィルタリングは一見色々バリエーションがあって覚えづらいと感じる方が多いですが、
基本的な概念を先に理解しておくと理解がスムーズになるかもしれません。

もしよくわからない場合はこのセクションは読み飛ばしててここから読んでください。


bool型シーケンスの指定

まず、DataFrameの添字にindexと同じサイズのbool型のシーケンスを指定すると、
Trueとなるものだけ抽出することができます。

無論この説明だけだと意味不明ですので、サンプルを見てみましょう。
4行のDataFrameからindexが偶数つまり0、2の行だけ抽出する場合について考えてみます。
"""

# 4行2列のDataFrameを生成する
df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], 
columns=['col1', 'col2'])

# 行数と同じだけbool型のシーケンスを作成。0番目と2番目をTrueとする。
l = [True, False, True, False]

# 作ったシーケンスを添え字に指定するとフィルタリングされる。(０番目と２番目が抽出される)
print(df[l])

"""
サンプルでは、用意したDataFrameに対し、indexと同じサイズ、
つまり行数と同じ要素数のbool型のシーケンス（上のサンプルではリストl）を、dfの添字に指定しています。

シーケンスでは0番目と2番目にTrueが設定されていますが、
フィルター結果も同様に0番目と2番目に絞られていることが確認できます。


bool型シーケンスの取得

もちろん、このbool型のシーケンスをわざわざ手打ちで作るわけではありません。
ここでDataFrameの演算を使用することで、条件に合致するbool型のシーケンス（Series）
を取得することができるのです。

例えば、indexが偶数の列を表すシーケンスを取得したい場合は、以下のように記述します。
"""

df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], 
columns=['col1', 'col2'])

l = [True, False, True, False]

print(df.index % 2 == 0)    # [ True False  True False]

"""
比較すると、シーケンスが返される点が特徴的です。
この演算を利用すると、最初のサンプルは以下のように一般化することができます。
"""

print(df[df.index % 2 == 0])

"""
すこし回りくどい説明ですが、さらに以下の具体例でちゃんと理解が深まると思います。


完全一致するものを抜き出す

特定列で条件に完全一致するものを抽出する場合のサンプルです。
DataFrameの列col1の値が'C'のものを抽出してみます。
"""

df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], 
columns=['col1', 'col2'])

print(df[df.col1 == 'C'])
#   col1  col2
# 2    C    30

"""
大なり小なりでフィルタ

特定列で条件より大きいものを抽出する場合のサンプルです。
DataFrameの列col2の値が10より大きいものを抽出してみます。

DataFrame自体は前のサンプルと同じものとします。
"""

df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], 
columns=['col1', 'col2'])

print(df[df.col2 > 10])
#   col1  col2
# 1    B    20
# 2    C    30
# 3    D    40


"""
正規表現でフィルタ

細かい説明は割愛させてください。よく使うのでイディオムとして知っておくと便利だと思います。
Series.str.containsで正規表現を指定すると該当するbool型シーケンスが取得できます。

たとえば、正規表現「.*A」と合致する行を抽出する場合、以下のように記述します。
"""

df = pd.DataFrame([['A', 10], ['B', 20], ['C', 30], ['D', 40]], 
columns=['col1', 'col2'])

cond = df.col1.str.contains('.*A')
print(df[cond])
#   col1  col2
# 0    A    10
