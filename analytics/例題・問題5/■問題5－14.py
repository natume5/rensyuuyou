# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－14
九九の表を作るプログラムを，掛け算の答えだけでなく，
それぞれが何と何の掛け算なのか，
つまり　3∗5=15　3*5=15　3∗5=15　のように表示するプログラムを作れ．

参考　　より
"""
"""
九九の表作成について


プログラミング初心者です。
pythonを使って九九の表を作りました。
しかしデータが縦持ちになってしまいました。

1段目は1の段（計算式を含めた九九） 例）1×1=1,1×2=2,…1×9=9
2段目は2の段（〃）　　　　　　　　　　 2×2=2,…2×9=18
…　　　　　　　　　　　　　　　　　　  …
9段目は9の段（〃）　　　　　　　　　　 9×1=9,…9×9=81
のようにするにはどうすればよでしょうか？

for a in range(1,10):
  for b in range(1,10):
    print('{}*{}={}'.format(a,b,a*b))


checkベストアンサー

for a in range(1,10):
    for b in range(1,10):
        print('{}*{}={}'.format(a,b,a*b), end=" ")
    print()

"""

for a in range(1, 10):
    for b in range(1, 10):
        print('{}*{}={} '.format(a, b, a * b), end=" ")
        ans = str(a * b)
        result = ans.rjust(4)
    print()
