# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題３－３【難】
上で勉強したinput，print，変数の3つだけで 借金返済計画を立てるプログラムを作りたい．
ただし，簡単のため利子は無しとする．
まず，借金の総額と，ひと月に返済する金額を入力すると，返済にかかる年数を表示し，
さらに，毎年のボーナスから返済する金額を入力すると，返済完了が何年早まるかを表示し，
その次に返済を完了したい年数を入力すると，
ボーナスからいくら返せばよいかを表示するプログラムを作成せよ．

（この問題は記述があやふやで，自分で仕様を決めてあげる部分が残されている．
実際問題のプログラムでは，お客さんの要望にしたがって仕様を決めていくが，
ここでは解きやすいように自分で仕様を決めてかまわない．
たとえば，「年数」は半端もあり（浮動小数点数）で出力し，
ボーナスは年始に1回だけ渡されるものと仮定しても良い．）
"""


def debt(borrowed, annual, repayment):
    """borrowed=借金額,annual=年利,repayment=返済額
    debt(借金)という関数に、引数を３つ渡します.
    """
    month = 0
    total = 0
    finished = False
    while finished == False:
        """finishedがTrueになるまでループする、While文を書いていきます。
        まず、FinishedをFalseで定義してからWhile文を書きます。"""
        if borrowed > repayment:
            month += 1
            """残高(borrowed)が返済額(repayment)より多い場合と
            少ない場合の条件分岐"""
            borrowed = borrowed * (1 + annual / 12 / 100) - repayment
            total += repayment
            print(month, '月: 返済額', repayment,
                  '円 あと', int(borrowed), "円", sep='')

        else:
            month += 1
            borrowed = borrowed * (1 + annual / 12 / 100)
            """年利を月利に変える(1 + annual / 12 / 100)
            これを、借金額にかけて残高を出し、残高から返済額を引きます。
            また、totalに返済額を足していき、返済総額を計算していきます。"""
            total += borrowed
            print(month, '月: 返済額', int(borrowed),
                  '円 返済総額: ', int(total), '円', sep='')
            finished = True
            """何ヶ月かかったか数えるコード"""


print("借金返済プログラムその1")
b = int(input("借金総額を入力して下さい。 → "))
a = float(input("年利率(%)があれば入力して下さい。 → "))
r = int(input("月々の返済額を設定して下さい。 → "))
debt(b, a, r)


print("借金返済プログラムその2")
debt = int(input('借金額はいくらですか？> '))
rate = float(input('年利率(%)表示して下さい。> '))
payment = int(input('返済額の設定して下さい。> '))
total = 0
month = 0
"""
目的：
借金額から返済までどのくらいの期間がかかり、どのような返済額になっていくのか表示する。

フロー：
①　借金額記載
②　利息年率(%)
③　返済額/月
④　借金額と返済額から返済額より借金額が少なくなるまで、月数と金額表示
⑤　返済額より借金額が少なくなった後の月数と返済総額表示

借金の金額と、利息の年利率(%)、月々の返済額を入力すると、
毎月、借金がなくなるまで月数と借金の金額を表示し、
月々の借金は、借金の利息年利率/12（月割り）分増加するが、
返済分だけ減るというイメージのプログラムを作成します。

入力欄を設け、debt, rate, payment変数を作る。
今まで返済した合計のカウント並びかかった月数をカウントする為、
total = 0, month = 0 と設定する。
"""


while debt > payment:
    month += 1
    debt = debt * (1 + rate/12/100) - payment
    print(str(month)+'月: 返済額', payment, '円', '残り',
          int(debt), sep=' ')
    total += payment
    """
    次にdebtの返済額がどのくらいまで繰り返されるかをWhile文を使って、
    paymentを下回るまでとします。月数は１ヶ月ずつ増やし、残りの返済額には、
    debtに利率の12ヶ月の%表記(100)を掛け合わせたものから毎月のpaymentを
    差し引くようにします。
    """
month += 1
debt = debt * (1 + rate/12/100)
total += debt
print(str(month)+'月: 返済額', int(debt), '円', 'これで完済になります。',
      '返済総額: ', int(total), '円', sep=' ')
"""
更にdebtがpaymentを下回った後の返済額と返済を表示します。
ここでのdebt変数は、上記debtを基にしたdebtになります。
int(total)のtotalは、total +で今までpaymentでの合計値とdebtからの足算になります。
"""
