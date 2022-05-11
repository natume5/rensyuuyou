# Mydataクラス(サブクラス)の定義
# Datalogクラスが定義してあるモジュールをインポートする
from datalog import Datalog    # スーパークラスとして指定するためにインポートする


# Datalogクラスを継承したMydataクラス
class Mydata(Datalog):    # Datalogクラスをスーパークラスに
    def printlog(self):
        # スーパークラスのインスタンス変数を取り出す
        for date, data in self.loglist:
            print(date, data)

# Mydataクラスのインスタンスを作って試す
obj = Mydata()
obj.log("あいう")    # スーパークラスのインスタンスメゾットを実行
obj.log("abc")
obj.log(123)
obj.printlog()    # サブクラスのインスタンスメゾットを実行
