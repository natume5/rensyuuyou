# ダイアログボックスで選んだテキストファイルを読み込んで表示する
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.filedialog as fd
# tkアプリウィンドウを表示しない
root = tk.Tk()    # Tkのkは小文字
root.withdraw()

# オープンダイアログを表示する
file = fd.askopenfilename(    # fileにはダイアログで選択したファイルのパスが入る
    title="ファイル名を選んでください。",
    filetypes=[("TEXT", "text"), ("TEXT", ".py"), ("HTML", "html")]
)

# ファイルが選択されたならば開く
if file:
    with open(file, "r", encoding="utf-8") as fileobj:    # ファイルを開く
        text = fileobj.read()    # ファイルを読み込む
        print(text)
