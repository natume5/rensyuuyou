# テキストファイルから10文字ずつ読み込む
file = "fox.txt"
with open(file, "r", encoding="utf_8") as fileobj:    # ファイルオブジェクトを作る
    while True:
        text = fileobj.read(10)    # 10文字ずつ読み込む
        if text:    # 文字列があれば出力する
            # if text  textに文字列があればTrue
            print(text)
        else:
            break    # 読み込みを終了する
