class Test:
    def __init__(self, pub_val = "pub",
                 pri_val = "pri"):
        self.pub_val = pub_val
        self.__pri_val = pri_val
    def set_pri_val(self, pri_val="pri"):
        self.__pri_val = pri_val
    def get_pri_val(self):
        return self.__pri_val

test = Test()
print(test.pub_val)

print(test.get_pri_val())
test.set_pri_val("PRI")
print(test.get_pri_val())

