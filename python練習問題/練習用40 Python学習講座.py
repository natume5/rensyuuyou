#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　matplotlibの棒グラフをアニメーションにする---")


"""
TouTubeでコロナの国別感染者数の棒グラフがレースのようにアニメーションになっている動画があったのですが、
視覚的に分かりやすかったためPythonでできないか調べていたところ、
PyPiに使いやすいライブラリが登録されていたため紹介したいと思います。

Bar Chart Race

2020年の6月にPyPiに登録されたBar Chart RaceというライブラリでDataFrameから
簡単に棒グラフのレースアニメーションを作成することができます。
バージョンは0.1ですが問題なく使えるレベルのものだと思いました。

https://pypi.org/project/bar-chart-race/

インストールはpipの場合は以下、

pip install bar_chart_race

また、condaを使用する場合は以下のとおりとなります。

conda install -c conda-forge bar_chart_race

私はUbuntu18.04のPython3.8で実行したのですが、別途ffmpegが必要となりました。
現時点で他のOSでは動作確認していません。

sudo apt install ffmpeg

pip install ffmpeg


コロナの国別感染者数の棒グラフ

それでは早速使ってみたいと思います。大まかな処理の流れは以下のようになります。

データのダウンロード
まず、国別の感染者数の時系列CSVデータを入手します。
色々ソースがありますが私は以下サイトのTotal confirmed casesを借用しました。
Coronavirus Source Data

DataFrameへの変換
次にpandasでCSVデータをDataFrameに変換します。データ形式は1列目が日付、それ以降が国別となっています。
1列目のdateをindexとして使用します。全ての国を対象とすると少し動作が重くなるため、
今回は主要な国を10日おきにピックアップします。

Bar Chart Raceで描画する
あとはBar Chart Raceのbar_chart_race関数に
DataFrameを指定して実行するとmp4形式の動画を得ることができます。

コード例

以下のサンプルはこれらの処理を記述したものです。カレントディレクトリにファイルをダウンロードしています。
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML
# %matplotlib inline


df = pd.read_csv('https://gist.githubusercontent.com/johnburnmurdoch/\
4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/\
city_populations', usecols=['name', 'group', 'year', 'value'])
df.head(3)

current_year = 2020
dff = (df[df['year'].eq(current_year)]
       .sort_values(by='value', ascending=False)
       .head(10))
dff

fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(dff['name'], dff['value'])

# matplotlibで作成した図を画像として保存した場合はfig.savingを使う。
# fig.savefig('1-1_a.png',
#             facecolor=fig.get_facecolor(), edgecolor=fig.get_edgecolor())

colors = dict(zip(
    ['India', 'Europe', 'Asia', 'Latin America',
     'Middle East', 'North America', 'Africa'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50']
))
group_lk = df.set_index('name')['group'].to_dict()

fig, ax = plt.subplots(figsize=(15, 8))
dff = dff[::-1]   # flip values from top to bottom

# pass colors values to `color=`
ax.barh(dff['name'], dff['value'], 
	color=[colors[group_lk[x]] for x in dff['name']])

# iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
	ax.text(value, i, name, ha='right')  # Tokyo: name
    ax.text(value, i,.25, group_lk[name], ha='right')  # Asia: group name
    ax.text(value, i, value, ha='left')   # 38194.2: value
 
    # Add year right middle portion of canvas
ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')

fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value - dx, i, .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'The most populous cities in the world from 1999 to 2020',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0, 'by @Mark; credit @https://life100create.com/',
    	    transform=ax.transAxes, ha='right', color='#777777',
    	    bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)


draw_barchart(2020)

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1999, 2021))
HTML(animator.to_jshtml())
# or use animator.to_html5_video() or animator.save()
