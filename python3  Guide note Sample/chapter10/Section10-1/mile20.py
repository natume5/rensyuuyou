# マイルをメートルに換算する
def mile2meter(mile):    # mileが引数
    meter = mile * 1609.344    # 引数で受け取った値を使って計算
    return meter    # mile2meter()関数定義

# 20マイルをメートルに換算する
distance = mile2meter(20)    # 引数に20を渡す   20の場合を計算
print(distance)
