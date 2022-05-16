req_list = ["hello",
            "WORLD",
            "helloworld",
            "heLLo world",
            "hello world"]


for res in map(lambda val:val.title() if "" in val else val.upper(), req_list):
    print(res)
