# -*-coding:utf-8-*-


content = """\
書き込み文１
書き込み文２
書き込み文３\
"""
fp = open("C:/Program Files/Sublime Text 3/"
          "中級に進むためのpythonプログラミング入門補強/"
          "ファイルの入出力/ファイルの書き込み/書き込み専用_w.txt", "w")
fp.write(content)
fp.close()
