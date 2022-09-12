

# ---------------
# sample1.py
# ---------------

import sys

# sys.argvの長さが2より小さい = コマンドライン引数無し
if len(sys.argv) < 2:
    print("No argument!")
    sys.exit()
print("Argument:{}".format(sys.argv[1]))

# sys.argvの内容を確認
print("sys.argv = {}".format(sys.argv))
