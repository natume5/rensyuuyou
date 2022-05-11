import csv
# 引数としてnewlineというパラメータに空文字を渡す必要あり
# open(file, mode, newline=”)のnewlineの後の点はshift+7を２回続けたもの
with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
