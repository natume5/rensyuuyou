file = "C:/Program Files/Sublime Text 3/サンプル/chapter13/area.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        text = fileobj.rea(10)
        if text:
            print(text)
        else:
            break
