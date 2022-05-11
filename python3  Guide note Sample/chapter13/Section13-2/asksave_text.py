from tkinter import filedialog as fd


# 保存ダイアログを表示する
file = fd.asksaveasfilename(
    initialfile="mydata"    # 拡張子を除いたファイル名
    defaultextension=".txt",    # 拡張子
    title="保存場所を選んでください。",
    filetypes=[("TEXT", ".txt")]
)
