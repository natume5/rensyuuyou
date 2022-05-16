# -*-coding:utf-8-*-
import sys
import os
import re


try:
    # ドラッグアンドドロップされたファイルのパスを取得
    for r_file_path in sys.argv[1:]:
        # 出力ファイル名
        base, ext = os.path.splitext(r_file_path)
        w_file_path = base + "_done" + ext
        # 内容、初期化しておく
        r_content = ""
        # ファイル読み込み、内容を取得
        with open(r_file_path, "r") as r_fp:
            r_content = r_fp.read()
        # 4文字から8文字までの数字を********に置換
        w_content = re.sub("[0 - 9]{4, 8}", "********", r_content)
        # ファイル書き込み
        with open(w_file_path, "w") as w_fp:
            w_fp.write(w_content)

        print("読込:" + r_file_path)
        print("出力:" + w_file_path)
        print("-" * 30)
except Exception as e:
    print(str(e) + "が発生しました")
    
