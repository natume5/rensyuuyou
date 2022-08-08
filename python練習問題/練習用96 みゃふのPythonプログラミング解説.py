#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- 環境変数の取得やフォルダの作成など（osモジュール） ---")


"""
osモジュールは「環境変数を取得・変更したり、フォルダやファイルを作成・変更・削除したりできる」
モジュールです。
ここではosモジュールの各関数の使い方をご紹介します。
"""


print("--- 環境変数の情報を取得・変更する - environ - ---")


"""
プログラムの中で環境変数の情報を取得したり、
設定を追加・変更・削除するにはos.environ()を使います。
なお、変更した環境変数はそのプログラム内でのみ有効で、
OS上の環境変数自体が変わるわけではないので注意が必要です。


環境変数を取得する

環境変数を全て取得したい場合はそのままprint()で出力します。
"""

import os

print(os.environ)
# environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\rn\\AppData\\Roaming',
# 以下省略

"""
os.environで取得できるパラメータは辞書のようにkeyとvalueで構成されています。
辞書と同じくitems()を加えることでkey, valueそれぞれをループ処理で取得できます。
"""

import os

for k, v in os.environ.items():
	print(f'{k} = {v}')
# ALLUSERSPROFILE = C:\ProgramData
# APPDATA = C:\Users\rn\AppData\Roaming
# COMMONPROGRAMFILES = C:\Program Files\Common Files
# COMMONPROGRAMFILES(X86) = C:\Program Files (x86)\Common Files
# 以下省略

"""
同様に、keys()やvalues()で各値を取得したり、in()で環境変数が存在するかを確認できます。
また、os.environのあとに環境変数のkeyを指定することでvalueを取得することもできます。
"""

import os

# keys()
print(f'keys = {os.environ.keys()}')
# keys = KeysView(environ({'ALLUSERSPROFILE': 'C:\\ProgramData',
# 以下省略

# values()
print(f'values = {os.environ.values()}')
# values = ValuesView(environ({'ALLUSERSPROFILE': 'C:\\ProgramData',
# 以下省略

# in
print('TERM' in os.environ)    # False

"""
# key設定
print(os.environ['TERM'])    # KeyError: 'TERM'
"""
"""
なお、key指定は存在しないkeyを指定するとKeyErrorになります。
KeyErrorではなく指定したデフォルト値を取得したい場合はgetenv()を使います。
"""

import os
print(os.getenv('ABC', 'default')) #’ABC’は存在しない
# default

"""
環境変数を変更する

os.environで環境変数を変更するにはos.environ[環境変数のkey]
の値を上書きすることで変更できます。
"""

import os

"""
print('変更前 : {}'.format(os.environ['TERM_PROGRAM']))    # KeyError: 'TERM_PROGRAM'
"""
os.environ['TERM_PROGRAM'] = 'program'
print('変更後 : {}'.format(os.environ['TERM_PROGRAM']))    # 変更後 : program

"""
なお、最初にも書きましたが、os.environでの環境変数の書き換えは
このプログラム内でのみ有効です。
OS上の環境変数は変わらないので注意してください。


環境変数を削除する

環境変数を削除するにはpop()を使うかdel文を使います。
ここではpop()を使って環境変数を削除します。
"""

import os

print('削除前 : {}'.format(os.getenv('TERM_PROGRAM')))    # 削除前 : program
os.environ.pop('TERM_PROGRAM')
print('削除後 : {}'.format(os.getenv('TERM_PROGRAM')))    # 削除後 : None

"""
削除後のgetenv()ではTERM_PROGRAMはすでに削除されているので、Noneが返却されています。
"""


print("--- フォルダを作成する - mkdir() - ---")


"""
新しいフォルダ（ディレクトリ）を作成するにはos.mkdir()を使います。
1つ目の引数にフォルダパスを指定することで、フォルダを作成できます。
"""

"""
import os
os.mkdir('./os sample')
"""

"""
上のコードを実行すると、実行したpythonファイルと同じ階層にsampleフォルダが作成されます。
なお、mkdir()は「既に存在しているフォルダパスを指定する」または
「存在しないフォルダ内にフォルダを作ろうとする」とエラーになるので、
そこにフォルダを作成できるかチェックする必要があります。
フォルダが存在するかチェックするにはos.path.exists()が便利です。
os.path.exists()はフォルダ、ファイル問わず、存在していればTrueを返却します。
"""

import os

path = 'D:/テキストドキュメント１/IT・エンジニア・プログラミング/sublime text3関係/python練習問題/os sample'
prev_dir = 'D:/テキストドキュメント１/IT・エンジニア・プログラミング/sublime text3関係/python練習問題'
if os.path.exists(path):
    print('既にフォルダが存在しています')
elif not os.path.exists(prev_dir):
    print(f'{prev_dir} フォルダが存在しません')
else:
    os.mkdir(path)

# D:/テキストドキュメント１/ITエンジニアプログラミング/sublime text3関係/python練習問題 フォルダが存在しません

"""
このように使うことで、フォルダの作成が可能かどうかチェックできます。
"""


print("--- フォルダを深い階層まで作成する - makedirs() ----")


"""
mkdir()では1つのフォルダしか作成できませんが、
os.makedirs()を使えば深い階層のフォルダを再帰的に作成できます。
"""

"""
import os
os.makedirs('D:/テキストドキュメント１/IT・エンジニア・プログラミング/sublime text3関係/python練習問題')
"""

"""
深い階層にフォルダを作成したい場合はmakedirs()がおすすめです。
"""


print("--- ファイル・フォルダの名前を変更する - rename() - ----")


"""
rename()を使うことで、ファイルやフォルダの名前を変更できます。
変更前のパスを1つ目の引数、変更後のパスを2つ目の引数に指定します。
"""

"""
import os
os.rename('./os sample', './abc') #フォルダ名変更
"""

"""
また、rename()もmkdir()と同じく存在しないファイルやフォルダを指定すると
FileNotFoundErrorになるので、
あらかじめos.path.exists()で変更前のパスのチェックをしましょう。
"""


print("--- ファイルを削除する - remove() - ----")


"""
os.remove()を使うことでファイルを削除できます（フォルダは削除できません）。
引数にファイルパスを指定することで削除できます。
"""

import os
os.remove('./os sample1.txt')

"""
これもファイルが存在しない場合エラーになるのでチェックが必要です。
"""


print("--- 空のフォルダを削除する - rmdir() - ----")


"""
os.rmdir()は空のフォルダを削除できます。
"""

import os
os.rmdir('./abc')

"""
rmdir()は削除対象のフォルダが空じゃなかった場合はOSErrorになります。
例外処理を使うことでエラーだった場合（空ではなかった場合）の処理を記述できます。
"""

import os
try:
    os.rmdir('./abc')
except FileNotFoundError:
    print('フォルダが存在していません。')
except OSError:
    print('フォルダ内にファイルが存在してます。')


print("--- パスとパスを結合する - path.join() - ----")


"""
引数の文字列をパスとして結合するにはos.path.join()を使います。
ただの文字列連結ではなく、結合された文字列がパスになるよう調整してくれます。
"""

import os

path = os.path.join('./', 'abc', 'def', 'ghi.py')
print(path)    # ./abc\def\ghi.py
