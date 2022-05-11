import sys
if len(sys.argv) < 2:
    print("読み込むファイル名を指定してください。")
    sys.exit()

file = sys.argv[1]
with open(file) as fileobj:
    text = fileobj.read()
    print(text)
