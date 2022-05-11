import tkinter as tk
import tkinter.filedialog as fd
from random import random


def getdata():
    num = random()
    return str(num)


root = tk.TK()
root.withdraw()

file = fd.asksaveasfilename(
    initalfile="mydata",
    defaulttextension=".txt",
    title="保存場所を選んでください。",
    filetypes=[("TEXT"), "txt"]
)

savedata = getdata()
if file:
    with open(file, "w", encording="utf_8") as fileboj:
        len = fileboj.write(savedata)
        print(f"{len}文字保存しました。")
