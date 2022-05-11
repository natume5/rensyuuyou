# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題４－１
「0<10という条件が成り立つならOKと表示する」というプログラムを作って， ifの使い方を練習する．
0は10より小さいので0<10は必ず成り立つ．
よって，以下を実行すると，OKが表示される．

if 0 < 10:
    print('OK')

OK
"""
a = 0


while True:
    try:
        A = int(float(input("整数を入力して下さい。条件が成り立つならOKと表示します。: ")))
        if 0 < 10:
            print("OK")
            a = a + 1
        if a > 3:
            print("終わりにします。")
            break
    except ValueError:
        print("もう一度やり直してください。")
    except KeyboardInterrupt:
        print("終了します。")
        break
    else:
        print("もう一度入力して下さい。")
        continue
