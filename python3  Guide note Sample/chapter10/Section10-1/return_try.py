# 数値に変換できない文字が入力されたならばNoneを返す
def calc(num):
    unit_price = 180    # 単価
    try:
        # 数値に変換できずにエラーになる場合は例外で処理する
        num = float(num)    # 数値に変換する
        return num * unit_price
    except:
        return None    # 変換がエラーになったらNoneを返す
"""
F821 undefined name 'xxxx'
未定義の名前
    変数など使用する場所で宣言する
F841 local variable 'id' is assigned to but never used
ローカル変数名が割り当てられているが使われていない
    未使用のローカル変数を削除する
"""


# キーボードから引数を入力して試す
while True:
    num = input("個数を入力して下さい。(qで終了。)")
    if num == "":
        continue
    elif num == "q":
        break

    # calc()で計算する
    result = calc(num)
    print(result)
