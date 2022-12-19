#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- bar chart race ---")


import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('owid-covid-data.csv', index_col='date', parse_dates=['date'])
df.tail()

s = df.loc['2020-03-29']
print(s)

fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(6))
y = s.index
width = s.values
ax.barh(y=y, width=width, color=colors);

def nice_axes(ax):
	ax.set_facecolor('.8')
	ax.tick_params(labelsize=8, length=0)
	ax.grid(True, axes='x', color='white')
	ax.set_axissbelow(True)
	[spine.set_visible(False) for spine in ax.spines.values()]

nice_axes(ax)
fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5),
	dpi=144, tight_layout=True)
dates = ['2020-03-29', '2020-03-30', '2020-03-31']
for ax, date in zip(ax_array, dates):
	s = df.loc[date].sort_values()
	ax.barh(y=s.index, width=s.values, color=colors)
	









