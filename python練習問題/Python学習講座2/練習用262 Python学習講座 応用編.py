#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 pandasの基礎知識 ---")


print("--- pandasのインストール ---")


"""
pipでインストールできます。

pip install pandas

numpyも一緒にインストールされます。
比較的サイズ（pandasとnumpyを合わせて40M程度）
が大きため少し時間がかかります。
anacondaを使えば一通り揃っているため、
pyenvで環境が簡単に切り替えられる方はそちらを使うのも手でしょう。
pandasだけで使用することはまれでnumpyと併用することが一般的なのですが、
この講座では概要の理解を主眼としているため、生のpythonの型を元に説明します。
numpyを使い慣れている方は適宜そちらに置き換えて読んでください。
"""


print("--- pandasのデータ形式 ---")


"""
pandasには大きく分けて3つのデータ形式があります。
Series

一次元の配列です。一列しかない行列とみなしても構いません。

indexと呼ばれる行ラベルをつけることができます。


Dataframe

行と列をもった配列データです。seriesを複数まとめたもととみなして見良いでしょう。
pandas入門のメインです。


Panel

3次元の配列データです。
白状すると管理人はこのデータ形式を業務で使用したことがないので、
当面は説明する予定はありません。
"""


print("--- pandasの用語 ---")


"""
学習を始める前に、pandas特有の用語を抑えておきましょう。

以下の説明だけだと何のことかわからないと思いますが、
実際にDataframeを生成して操作すると理解できると思います。


index

SeriesやDataframeの行データに付与することができるラベルのことを
indexと呼びます。行ラベルと呼称することもあります。
indexを使用してSeriesやDataframeの行データにアクセスすることができます。


columns

Dataframeの列データに付与することができるラベルのことをcolumnsと呼びます。
列のラベルと呼称することもあります。

indexを使用してDataframeの列データにアクセスすることができます。


integer-location

行(列)形式なので、番号指定でデータにアクセスすることもできます。
このアクセス方法をinteger-locationと呼びます。
"""
