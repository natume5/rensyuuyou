global_val_1 = "global"
global_val_2 = "global"
def scope_test():
    global global_val_1
    local_val_1 = "local"
    local_val_2 = "local"
scope_test()
print("global_val_1:{0}".format(global_val_1))
print("global_val_2:{0}".format(global_val_2))


    

