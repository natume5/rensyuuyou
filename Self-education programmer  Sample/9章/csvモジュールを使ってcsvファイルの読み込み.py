# ここで開くファイルは、
# 前のコード例を実行して
# 作られる。

import csv

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
