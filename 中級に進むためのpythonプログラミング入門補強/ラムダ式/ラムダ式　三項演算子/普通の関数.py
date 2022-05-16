def func_conv(val):
    if "" in val:
        res = val.title()
    else:
        res = val.upper()
    return res


print(func_conv("hello world"))
