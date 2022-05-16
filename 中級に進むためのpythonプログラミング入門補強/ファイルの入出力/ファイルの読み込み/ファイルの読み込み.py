# -*-coding:utf-8-*-


# fileオブジェクトを開く
fp = open("C:/Program Files/Sublime Text 3"
          "/ゲームを作りながら楽しく学べるpythonプログラミング"
          "/5章/演習/身の回りの物の特徴を列挙してみる.txt", "r", "encoding"="utf-8")

# readメゾットで中身を取得
content = fp.read()
print(content)

# オブジェクトを閉じる
fp.close()
