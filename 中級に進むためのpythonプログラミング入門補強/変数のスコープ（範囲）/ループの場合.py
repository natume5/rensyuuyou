global_val = "global"
for i in ["1回だけループ用"]:
    print("0:{0}".format(global_val))
    # forブロックからグローバル変数の変更
    global_val = "local"
    local_val = "local"
    print("1:{0}".format(global_val))
    print("2:{0}".format(global_val))
print("3:{0}".format(global_val))
print("4:{0}".format(global_val))

