#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- ファイルシステムの操作 ---")


print("--- ファイル/ディレクトリの存在チェック ---")


"""
指定したパスが存在するかどうかはos.path.existsを使用します。
いずれもスクリプトの実行ディレクトリがカレントディレクトリとなります。
また、指定したパスがファイルかディレクトリかの判定はそれぞれos.path.isfile、
os.path.isdirを使用して得ることができます。
以下のサンプルでは、指定したパスに対して存在するかどうか、
存在する場合はファイルかディレクトリかを判定して
メッセージをprintで出力しています。
"""

import os

path = 'sample.py'

if os.path.exists(path):
	print('指定したパスは存在します')

	if os.path.isfile(path):
		print('ファイルです')

	if os.path.isdir(path):
		print('ディレクトリです')

else:
	print('指定したパスは存在しません')


print("--- ファイル/ディレクトリの作成と削除 ---")


"""
ファイルの削除

os.removeにpathを指定するとファイルの削除ができます。
なお、pathがディレクトリの場合はOSErrorが送出されます。
ディレクトリを削除する場合は後述のrmdirを使用します。
以下のサンプルではカレントディレクトリにあるfile1.txtを削除しています。
"""

f = open('file1.txt', 'w', encoding="UTF-8")
f.write('file1.txt作成')
f.close()

# import os
os.remove('file1.txt')
print('file1.txtを削除しました')

"""
ディレクトリの作成と削除

単一階層のディレクトリを作成する場合はos.mkdirを、
複数階層を作成する場合はos.makedirsを使用します。
また、逆にディレクトリを削除する場合はそれぞれos.rmdir、
os.removedirsを使用します。
以下のサンプルではディレクトリの作成と削除を行っています。
"""

# import os

# ディレクトリを作成する
os.mkdir('dir_11')
os.makedirs('dir_2/dir_3')

# ディレクトリを削除する
os.rmdir('dir_11')
os.removedirs('dir_2/dir_3')


print("--- ファイル/ディレクトリの移動とコピー ---")


"""
コピーと移動の場合はshutilモジュールを使用します。
単一のファイルかディレクトリの場合はcopyメソッドを、
ディレクトリごと再帰的にコピーする場合はcopytreeメソッドを使用します。
以下のサンプルではそれぞれ単一のファイルのコピーと
ディレクトリごとのコピーを行っています。
"""

# import os
import shutil

shutil.copy('sample.txt', 'sample2.txt')    # 単一コピー
shutil.copytree('dir_1', 'dir_2')    # ディレクトリごとに再帰的にコピー
