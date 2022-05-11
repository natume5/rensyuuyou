#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys


def main(cod3, name):
	print("main処理を実行します。")
	# 以下省略

if __name__ == '__main__':
	args = sys.argv

	if len(args) == 3:
		code = args[1]
		name = args[2]
		main(code, name)
	else:
		print('以下形式でcodeとnameを指定してください')
		print('$ sample.py <code> <name>')
		quit()
