#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Matplotlibの棒グラフをアニメーションにする ---")


print("--- Bar Chart Race ---")


"""
2020年の6月にPyPiに登録された
Bar Chart RaceというライブラリでDataFrameから簡単に
棒グラフのレースアニメーションを作成することができます。
バージョンは0.1ですが問題なく使えるレベルのものだと思いました。

https://pypi.org/project/bar-chart-race/

インストールはpipの場合は以下、

pip install bar_chart_race

また、condaを使用する場合は以下のとおりとなります。

conda install -c conda-forge bar_chart_race

私はUbuntu18.04のPython3.8で実行したのですが、
別途ffmpegが必要となりました。現時点で他のOSでは動作確認していません。

sudo apt install ffmpeg

pip install ffmpeg
"""


print("--- コロナの国別感染者数の棒グラフ ---")


"""
それでは早速使ってみたいと思います。
大まかな処理の流れは以下のようになります。

データのダウンロード
まず、国別の感染者数の時系列CSVデータを入手します。
色々ソースがありますが私は以下サイトのTotal confirmed casesを借用しました。
Coronavirus Source Data

DataFrameへの変換
次にpandasでCSVデータをDataFrameに変換します。
データ形式は1列目が日付、それ以降が国別となっています。
1列目のdateをindexとして使用します。
全ての国を対象とすると少し動作が重くなるため、
今回は主要な国を10日おきにピックアップします。

Bar Chart Raceで描画する
あとはBar Chart Raceのbar_chart_race関数に
DataFrameを指定して実行するとmp4形式の動画を得ることができます。

コード例

以下のサンプルはこれらの処理を記述したものです。
カレントディレクトリにファイルをダウンロードしています。
"""

import requests
import pandas as pd
import bar_chart_race as bcr


# cvsデータをダウンロードする
r = requests.get('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
with open('covid19.csv', 'w', encoding='UTF-8') as f:
	f.write(r.text)

# DataFrameにする
raw_df = pd.read_csv('covid19.csv', index_col='date', parse_dates=['date'])

# 主要な国を抽出、10行おきのDataFrameを抽出
df = raw_df.loc[:, ["Brazil", "China", "France", "India", "Iran",
 "Italy", "Japan", "Spain", "United Kingdom", "United States"]].dropna()[::10]

# アニメーションをmp4で保存する
bcr.bar_chart_race(
df=df, filename='sample.mp4', orientation='h', sort='desc', n_bars=6,
fixed_order=False, fixed_max=True, steps_per_period=10, interpolate_period=False,
label_bars=True, bar_size=.95, period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
period_fmt='%B %d, %Y', 
period_summary_func=lambda v, r: {'x': .99, 'y': .18, 's': f'Total confirmed cases: {v.nlargest(6).sum():,.0f}', 'ha': 'right', 'size': 8},
period_length=500, figsize=(5, 3), dpi=144, cmap='dark12', 
title='COVID-19 Total confirmed cases by country', title_size='',
bar_label_size=7, tick_label_size=7, scale='linear', writer=None, fig=None,
bar_kwargs={'alpha': .7}, filter_column_colors=False) 

"""
実行すると以下動画のようなmp4ファイルを得ることができます。
比較された増加状況が視覚的に表現できるのが良いと思いました。

上のサンプルは以下の公式サンプルをカスタマイズしました。
その他パラメータやカスタマイズ方法も以下で詳しく解説されています。
bar_chart_race
"""
