global_val = "global"
if True:
    print("0:{0}".format(global_val))
    # ifブロックからグローバル変数の変更
    global_val = "local"
    local_val = "local"
    print("1:{0}".format(global_val))
    print("2:{0}".format(global_val))
print("3:{0}".format(global_val))
print("4:{0}".format(global_val))

