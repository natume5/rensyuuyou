# キーワード引数を辞書で受け取る
def fruits(** kwargs):    # *が1個でなく2個ついている
    print(kwargs)

fruits(apple=2, orange=3, banana=1)