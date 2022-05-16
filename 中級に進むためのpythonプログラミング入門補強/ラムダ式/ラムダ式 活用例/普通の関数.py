def func_conv(val):
    if "" in val:
        res = val.title()
    else:
        res = val.upper()
    return res


req_list = ["hello",
            "WORLD",
            "helloworld",
            "heLLo world",
            "hello world"]


for res in map(func_conv, req_list):
    print(res)
