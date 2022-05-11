# カンマ区切りのデータを読み込み、各行を大きさ判定結果のリストに変換する

file = "C:/Program Files/Sublime Text 3/python3  Guide note Sample/"\
       "chapter13/data/numdata.txt"
limit = 2.0
with open(file, "r", encoding="utf_8") as fileobj:
    # ファイルオブジェクトから1行ずつ取り出す
    for i, line in enumerate(fileobj):
        if line == "\n":
            continue    # 改行コードのみはスキップ
        datalist = line.split(",")    # リストにする
        # limit以下の時1、大きい時0に変換する
        result = [int(float(num) <= limit) for num in datalist]
        print(f"{1}:{result}")
