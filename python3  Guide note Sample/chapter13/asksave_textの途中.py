file = fd.asksaveasfilename(
    initialfile="mydata",
    defaultextension=".txt",
    title="保存場所を選んでください。",
    filetypes=[("TEXT", ".txt")]
)
