# with-asを使ってテキストファイルを読み込む

file = "fox.txt"
with open(file, encoding="utf_8") as fileboj:    # ファイルオブジェクトを作る
    # as fileboj  filebojになる
    text = fileboj.read()    # ファイルを読み込む
    print(text)
