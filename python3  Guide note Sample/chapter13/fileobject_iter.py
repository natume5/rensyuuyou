file = "C:/Program Files/Sublime Text 3/サンプル/chapter13/area.txt"
target = "心"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        try:
            line = next(fileobj)
            if line.find(target) >= 0:
                print(f"「{target}」が見つかりました。")
                print(line, end="")
                break
        except StopIteration:
            print(f"「{target}」は見つかりませんでした。")
            break
