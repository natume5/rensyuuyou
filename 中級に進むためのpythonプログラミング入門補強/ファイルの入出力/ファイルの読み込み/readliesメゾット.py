# fileオブジェクトを開く
fp = open("C:/Program Files/Sublime Text 3"
          "/ゲームを作りながら楽しく学べるpythonプログラミング"
          "/5章/演習/身の回りの物の特徴を列挙してみる.txt", "r")

# readlinesメゾットで値が行ごとのリストの取得ができます。
list = fp.readlines()
print(list)
for line in list:
    print(line)

# オブジェクトを閉じる
fp.close()
