# fileオブジェクトを開く
fp = open("C:/Program Files/Sublime Text 3"
          "/ゲームを作りながら楽しく学べるpythonプログラミング"
          "/5章/演習/身の回りの物の特徴を列挙してみる.txt", "r")

# for文でオブジェクトをループし中身を行ごと取得
for line in fp:
    print(line)

# オブジェクトを閉じる
fp.close()
