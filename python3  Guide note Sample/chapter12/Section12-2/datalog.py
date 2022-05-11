# Datalogクラス(スーパークラス)
# datetimeモジュール
from datetime import datetime


# Datalogクラス
class Datalog:
    # 初期化メゾット
    def __init__(self):
        self.loglist = []    # インスタンス変数loglistを初期化

    # インスタンスメゾット
    def log(self, data):
        now = datetime.now()    # 現在の日時データ
        item = (now, data)    # タプルを作る
        self.loglist.append(item)    # loglistリストに追加する
