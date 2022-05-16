class Test:
    def __init__(self, pub_val = "pub",
                 pri_val = "pri"):
        self.pub_val = pub_val
        self.__pri_val = pri_val

test = Test()
print(test.pub_val)
# __が先頭についている変数に突然アクセスしようとしているので、AttributeError:となる
print(test.__pri_val)

