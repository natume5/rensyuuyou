file = "C:/Program Files/Sublime Text 3/サンプル/chapter13/area.txt"
with open(file) as fileobj:
    text = fileobj.read()
    newtext = text.rstrip(".")
    wordlist = newtext.split(" ")
    print(wordlist)
