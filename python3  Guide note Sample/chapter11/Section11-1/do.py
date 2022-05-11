# do()に引数で渡された関数を実行する
def do(funk):
    funk()    # 引数で受け取った関数を実行する


def thanks():
        # do()に渡して実行する関数
    print("ありがとう")


def hi():
        # do()に渡して実行する関数
    print("やあー！")

# do()を実行
condition = 1
if condition == 1:
    do(thanks)
    # conditionが1なので、引数でthanks関数を渡す。
    # 1でなければhiが渡されてhi()が実行

else:
    do(hi)
