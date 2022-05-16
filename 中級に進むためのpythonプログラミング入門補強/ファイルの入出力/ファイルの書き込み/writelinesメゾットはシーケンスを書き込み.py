# -*-coding:utf-8-*-


list = ["書き込み文１\n",
        "書き込み文２\n",
        "書き込み文３\n"]

fp = open("C:/Program Files/Sublime Text 3/"
          "中級に進むためのpythonプログラミング入門補強/"
          "ファイルの入出力/ファイルの書き込み/書き込み専用_wl.txt", "w")
fp.writelines(list)
fp.close()
