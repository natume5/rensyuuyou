global_val = "global"
def scope_test():
    # 関数ブロックからグローバル変数の変更
    global_val = "local"
    local_val = "local"
    print("1:{0}".format(global_val))
    print("2:{0}".format(local_val))
scope_test()
print("3:{0}".format(global_val))
print("4:{0}".format(local_val))

    

