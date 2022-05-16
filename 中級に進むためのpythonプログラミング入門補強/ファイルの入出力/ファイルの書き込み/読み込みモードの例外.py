# -*-coding:utf-8-*-


# text_no_exist.txtは存在しないので例外が発生する
fp = open("C:/Program Files/Sublime Text 3/"
          "中級に進むためのpythonプログラミング入門補強/"
          "ファイルの入出力/ファイルの書き込み/text_no_exist.txt", "w")
contet = fp.read()
print(content)
fp.close()
