# カレントディレクトリにdataファイルがあるかどうかチェックする
import os    # osモジュールをインポートしておく


print(os.path.exists("C:/Program Files/Sublime Text 3/"
                     "python3  Guide note Sample/chapter13/data"))
# dataフォルダがある?
print(os.path.exists("C:/Program Files/Sublime Text 3/"
                     "python3  Guide note Sample/chapter13/data2"))
# data2フォルダがある?
