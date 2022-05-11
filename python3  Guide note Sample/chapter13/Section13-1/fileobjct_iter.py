# ファイルオブジェクトをイテレータとして操作し文字を検索する

file = "C:/Program Files/Sublime Text 3/python3  Guide note Sample"\
       "/chapter13/data/tsuretsuregusa.txt"
target = "心"    # "心"を検索する
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        try:
            line = next(fileobj)    # イテレータから1行取り出す
            if line.find(target) >= 0:    # 文字を検索する
                # line.find(target) >= 0  find()は見つかった位置を返す
                print(f"「{target}」が見つかりました。")
                print(line, end="")
                break
        except StopIteration:    # EOF
            print(f"「{target}」が見つかりませんでした。")
            break
