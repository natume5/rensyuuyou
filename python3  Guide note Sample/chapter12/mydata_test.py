from datalog import Datalog


class Mydata(Datalog):
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)


obj = Mydata()
obj.log("あいう")
obj.log("abc")
obj.log(123)
obj.printlog()
