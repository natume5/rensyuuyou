# -*-coding:utf-8-*-


# text_win_utf.txt(WindowsならUTF-8で保存)
fp = open("C:/Program Files/Sublime Text 3"
          "/ゲームを作りながら楽しく学べるpythonプログラミング"
          "/5章/演習/身の回りの物の特徴を列挙してみる_w_utf.txt",
          "r", encoding="utf-8")
content = fp.read()
print(content)
fp.close()
