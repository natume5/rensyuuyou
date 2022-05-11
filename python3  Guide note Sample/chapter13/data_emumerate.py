file = "C:/Program Files/Sublime Text 3/サンプル/chapter13/numdata.txt"
limit = 2.0
with open(file, "r", encoding="utf_8") as fileboj:
    for i, line in enumerate(fileobj):
        if line == "\n":
            continue
        datalist = line.split(",")
        result = [int(float(num) <= limit) for num in datalist]
        print(f"{i}:{result}")
