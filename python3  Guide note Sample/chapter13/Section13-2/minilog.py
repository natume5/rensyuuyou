# コマンドライン引数をlog.txtに追記していく

import sys
from datetime import datetime

file = "log.txt"

if len(sys.argv) < 2:    # 1個目の引数はファイル名なので2個目以上の時に処理する
    sys.exit()    # プログラムを中断する

now = str(datetime.now())    # 現在の日時データ
memo = sys.argv[1]    # コマンドライン引数から受け取ったメモ
line = "-" * 10    # 区切り線
with open(file, "a") as fileobj:
    # "a"  追記モードで開く
    fileobj.write(now + "\n")    # コマンドライン引数で受け取ったメモ
    fileobj.write(memo + "\n")    # コマンドライン引数で受け取ったメモ
    fileobj.write(line + "\n")    # コマンドライン引数で受け取ったメモ
