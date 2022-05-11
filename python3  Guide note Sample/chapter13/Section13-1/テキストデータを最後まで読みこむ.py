# テキストデータを最後まで読みこむ

f1 = "fox.txt"
fileobj = open(f1, encoding="utf_8")
text = fileobj.read()    # テキストデータを読みこむ
