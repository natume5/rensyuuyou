# -*-coding:utf-8-*-


fname = "text_no_exist.txt"


try:
    fp = open(fname, "r")
    content = fp.read()
    fp.close()
except FileNotFoundError:
    print(fname + "は見つかりませんでした")
except UnicodeDecodeError:
    print(fname + "のデコードが出来ませんでした、ファイルの文字コードを"
          "確認して下さい")
except Exception as e:
    print(fname + "において例外")
    print(e)
    print("が発生しました")
    
