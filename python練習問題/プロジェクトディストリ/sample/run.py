# run.py
"""
    メイン処理 
    ~~~~~~~~~~~~~~~~~~

    メインの処理を行うスクリプトです 

    概要 
    --------

    pythoのドキュメンテーションの説明用に作りました::


    :copyright: (c) 2017 by the Kuro.
    :license: BSD, see LICENSE for more details.
"""

from pkg.mod1 import SampleClass

def main(arg):
    """ 
    文字列を装飾して表示します 

    :param arg: パラメータ 
    :return: 文字列
    """
    obj = SampleClass(' ***** ')
    text = obj.func1(arg)
    print(text)


if __name__ == '__main__':
    main("python最高！！")
