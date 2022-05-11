# テキストデータをファイルに書き込む

file = "sample.txt"
fileobj = open(file, "w", encoding="utf_8")    # ファイルを開く
fileobj.write("こんにちは\n")    # テキストデータを書き込む
fileobj.write("Pythonを始めよう\n")    # 続きを書き込む
fileobj.close()
