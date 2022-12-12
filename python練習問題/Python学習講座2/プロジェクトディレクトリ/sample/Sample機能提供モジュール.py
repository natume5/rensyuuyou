"""
Sample機能提供モジュール

"""

class Sample:
    """ 
    sample機能を実装したクラスです。
    """

    bar = 1 
    """ xxを保持するメンバです """

    #: yyを保持するメンバです
    foo = 1 

    def __init__(self):
        """ 
        初期化処理を行います。
        """
        self.x = 'hoge'



    def add(self, arg1, arg2):
        """ 
        引数で指定した値を足し算して返します。``arg1 + arg2`` 
        
        :param int arg1: 足される値。
        :param arg2: 足す値。
        :type arg2: int 
        :rtype: int
        :return: 足し算した結果。
        """
        return a + b 