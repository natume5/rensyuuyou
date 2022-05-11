# フォルダがなければ作成し、ファイルがあれば上書きするかどうか確認する


import os
from random import randint


# 保存フォルダとファイルパス
folder = "C:/Program Files/Sublime Text 3/"\
         "python3  Guide note Sample/chapter13/data"
file = folder + "sample.txt"

# ファイルを保存する
def filewrite():
    if not os.path.exists(folder):
        os.makedirs(folder)    # フォルダを作る
        # フォルダがなければ作ってファイルを保存
    with open(file, "w", encoding="utf_8") as fileobj:
        num = randint(0, 100)
        fileobj.write(f"{num}が出ました。")
        print("ファイルを保存しました。")

# 既存のファイルの有無をチェック
if os.path.exists(file):    # 既存ファイルがある場合
    while True:
        answer = input("上書きしてもいいですか？(y/n)")
        # "上書きしてもいいですか？  既存ファイルがあった時上書きするかどうか確認する
        if answer == "y":
            filewrite()
            break
        elif answer == "n":
            break
else:
    filewrite()
