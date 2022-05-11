# テキストを読み込んで単語リストを作る

file = "fox.txt"
with open(file, encoding="utf_8") as fileboj:
    text = fileboj.read()
    newtext = text.rstrip(".")    # 末尾のピリオドを消しておく
    wordlist = newtext.split(" ")    # スペースを区切ってリストにする
    print(wordlist)
