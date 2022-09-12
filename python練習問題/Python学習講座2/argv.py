

# ---------------
#  argv.py
# ---------------
import sys

# コマンドライン引数を変数argsに代入
args = sys.argv

print(args)

# コマンドライン引数をそれぞれ変数x, yに格納
x = int(sys.argv[1])
y = int(sys.argv[2])

# コマンドライン引数x, yの和を出力したい
print(x + y)

