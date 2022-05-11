file = "./data/tsuretsuregusa.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    while True:
        line = fileobj.readline()
        aline = line.rstrip()
        if aline:
            print(aline)
        else:
            break
