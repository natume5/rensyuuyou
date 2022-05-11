# ファイルを閉じる

f1 = "fox.txt"
fileobj = open(f1, encoding="utf_8")
text = fileobj.read()
fileobj.close()    # ファイルを閉じる
