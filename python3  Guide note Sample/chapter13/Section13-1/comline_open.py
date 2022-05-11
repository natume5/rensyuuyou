# コマンドライン変数で渡されたファイルのパスを開く
import sys

if len(sys.argv) < 2:    # 1個目の引数はファイル名なので2個以上の時に処理する
    print("読み込むファイル名を指定してください。")
    sys.exit()    # プログラムを中断する

file = sys.argv[1]    # ファイルのパスはargv[1]に入っている
with open(file, encoding="utf_8") as fileobj:    # ファイルオブジェクトを作る
    text = fileobj.read()    # ファイルを読み込む
    print(text)
