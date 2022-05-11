# カレントディレクトリを相対パスで移動する
import os


print(os.getcwd())    # カレントディレクトリを確認
os.chdir("./Section10-3")
# 現在のディレクトリにあるSection10-3フォルダに移動する
print(os.getcwd())    # カレントディレクトリを確認する
os.chdir("../Section10-4")    # 同じ階層のSection10-4フォルダに移動
print(os.getcwd())    # カレントディレクトリの確認する
