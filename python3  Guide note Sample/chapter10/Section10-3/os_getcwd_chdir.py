# カレントディレクトリを移動出来るか確認
import os


os.chdir("../")
print(os.getcwd())
"""os.chdir()で作業ディレクトリ（カレントディレクトリ）を変更できる。
引数に移動先のパスを指定する。絶対パスでも相対パスでもOK。
上の階層への移動は'../'。'..'でもよい。
UNIXのcdコマンドと同じように移動し、カレントディレクトリを変更することが可能。"""


print(os.getcwd())
"""os.getcwd()は現在Pythonが実行されている作業ディレクトリ
（カレントディレクトリ）の絶対パスを文字列として返す。
"""


os.chdir(os.path.dirname(os.path.abspath(__file__)))
"""実行しているスクリプトファイル（.py）があるディレクトリに移動する場合は
__file__およびos.pathの関数を使う。"""
print(os.getcwd())
