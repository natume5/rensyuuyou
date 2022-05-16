class Test:
    def __init__(self, pub_val = "pub",
                 pri_val = "pri"):
        self.pub_val = pub_val
        self.__pri_val = pri_val
    def get_pri_val(self):
        return self.__pri_val

test = Test()
print(test.pub_val)
pri_val= test.get_pri_val()
print(pri_val)

