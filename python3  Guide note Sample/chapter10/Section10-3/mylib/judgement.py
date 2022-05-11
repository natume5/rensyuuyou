# mylibフォルダにあるjudgement.pyでaverage()が定義されている
def average(* args):
    if args:    # argsが空でない時に実行する
        ave = sum(args) / len(args)
        return ave
    else:
        return None
