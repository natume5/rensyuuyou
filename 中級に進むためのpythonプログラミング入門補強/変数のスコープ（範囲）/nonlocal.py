def scope_test():
    val_1 = "val_1"
    val_2 = "val_2"
    def scope_test_inner():
        nonlocal val_1
        val_1 = "val_10"
        val_2 = "val_20"
    scope_test_inner()
    return val_1, val_2
res = scope_test()
print(res)



    

