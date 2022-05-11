# with-as文を使ってテキストファイルを書き出す

file = "sample.txt"
with open(file, "w", encoding="utf_8") as fileobj:
    fileobj.write("こんにちは\n")
    fileobj.write("Pythonを始めよう\n")
