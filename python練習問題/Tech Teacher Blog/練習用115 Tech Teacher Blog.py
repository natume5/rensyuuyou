#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- Pythonのassertをマスターしよう！基礎から具体例まで ---")


"""
Python初心者の方でassert文について

「なんとなくしか理解できない」
「assertの基礎知識から使い方まで網羅的に知りたい」
「assert文とif文やunittestとの違いを知りたい」

と思う人も多いでしょう。

そこで今回はassert文の構文や基礎知識から基本的な使い方、
さらにはif文やunittestとの違いを詳しく説明していきます。それでは見ていきましょう。
"""


print("--- assert文について ---")


"""
assert文について説明する前に、プログラムの「テスト」とは何か説明します。
テストとはコードが予期しない動作をしないかどうかを調査する作業のことです。
バグを取り除く「デバッグ」を行うためには予期しない動作を洗い出す作業が必要になるため、
このassert文を使用してテストを行います。
「assert文」とは基本的に条件をテストするデバッグ支援ツールで、構文は次のようになっています。

1.　assert 条件式 , 条件式がfalseになったときに出力するメッセージ

条件式が「false」の場合には例外「AssertionError」が起きてしまいます。
「true」の場合には何も起きずに次の命令を実行します。
Pythonではテストを行うためのクラス「unittest」が用意されていますが、
unittestを使用するよりもassert文を使用する方が簡単にテストを行うことができますよ。
このように、assert文を使うことで少しでも想定外の動作をした場合にすぐにエラーを出力して
プログラムを終了させることができますよ。
"""


print("--- assert文の使い方 ---")


"""
ここからは実際にassert文の使い方を解説していきます。

    基本的な使い方
    無効にする方法

それでは見ていきましょう。


基本的な使い方

assert文の書式は以下の通りです。
1.　＃　Falseの場合
2.　assert False , error
3.　Traceback ( most recent call last ) :
4.　 File ‘’ , line 1, in
5.　AssertError : error
6.
7.　Trueの場合
8.　assert True , ‘何も起きずに次の命令を実行’

それでは、ここからは実際にコードを使用して説明していきましょう。
1.　text1 = “何も起こらない”
2.　text2 = “エラー“
3.　text3 = “何も起こらない“
4.　assert text1 == text3
5.　assert text1 == text2
6.　print ( ‘Hello World’ )
7.　＃　実行結果
8.　AssertionError

この例では、まず4行目でassert文を使用していますが
「text1== text3」はTrueになるため何も起こりません。
しかし、5行目でのassert文では「text1 == text2」
がFalseになるためAssertionErrorが出て、そこでプログラムが終了します。
6行目のprint文が実行されていないことを確認してください。
assert文では条件式の後にカンマを付けて記述することでエラーメッセージを記述することができます。

1.　text1 = “何も起こらない“
2.　text2 = “エラー“
3.　assert text1 == text2 , ‘text1 is not equal to text2’
4.　＃　実行結果
5.　AssertionError : text1 is not equal to text2

このプログラムでは条件「text1 == text2」が成立していないためAssertionErrorが起きています。
このとき、指定したエラーメッセージが出力されていることが分かるでしょう。
このようにassert文を使用することで、プログラム中で想定と異なる振る舞いをしている場合に、
すぐに気づくことができますよ。


無効にする方法

プロセス内のすべてのassert文を無効にするには、-Oフラグを使用しましょう。
1.　$ python -Oc ‘assert False’
2.
3.　$ pyton -c ‘assert False’
4.　Traceback ( most recent call last ) :
5.　 File ‘’ , line 1 , in
6.　AssertionError

assert文は組み込み定数「 _debug_ 」がTrueのときだけ実行されます。
Pythonスクリプト実行時のコマンドラインオプションに「-O」を付けると
「 _debug_ 」が「False」になるのでassert文が無効になりますよ。
"""


print("--- assert文とif文の違い ---")


"""
まずif文とは何かを説明していきます。
「if文」とはプログラム中で条件分岐を記述したい場合に用いられる構文です。
ある条件式が成り立つ「True」であるか、
成り立たない「False」であるかを判定して処理を分岐させることができます。

if文の構文は次の通りです。
1.　if 条件式1 :
2.　　条件式1がTrueの場合の処理
3.　elif 条件式2 :
4.　　条件式1がFalseかつ条件式2がTrueの場合の処理
5.　else :
6.　　条件式1,2がどちらもFalseの場合の処理

「elif」はif文の条件に当てはまらなかった場合に
さらに他の条件に当てはまるかをチェックしたいときに使用します。
「else」はifとelifのどちらの条件にも当てはまらなかった場合に
処理を実行したいときに使用しますよ。
このことからassert文とif文の違いは、次の通りです。


構文\条件式の真偽 	  True 	     False
assert文 	      何も起こらない 	エラーを出力
if文 	            処理を実行 	何も起こらない

このようにassert文とif文には明確な違いがあるので気をつけましょう。
"""


print("--- assert文とunittestの違い ---")


"""
Pythonにはテストを行うためのクラス「unittest」が用意されています。
「unittest」とは、Pythonに標準搭載されているテスト用のツールで、
プログラムを記述したあとに正しく動作するかのテストを行えます。
プログラムの規模が大きかったり、ユーザー定義関数が多くなったりする場合、
ひとつひとつテストしていくのは大変です。
unittestを使用すると複数のテストをまとめて実行できるため便利ですよ。
unittestは次のように利用します。

1.　 ＃例として和を計算する関数を使用
2.　 def addition ( x , z ) :
5. 　return x + z6. 　＃正しく実行されているか確認
7. 　import unittest10.　class addition ( unittest . TestCase ) :
14. 　def test _ addition ( self ) :
17. 　 value1 = 25
18. 　 value2 = 75
19. 　 expected = 100
20. 　actual =addition ( value1 , value2 )
21. 　 self . assertEqual ( expected , actual )
22.
23.　if __name__ == “__main__” :
34.　 unittest . main ( )

assert文とunittestの違いはテストケースを作成して実行するかどうかです。
"""


print("--- assertを使用する上での注意点 ---")


"""
assert文を使用する上では、注意すべき点が2つあります。

    assert文はエラー処理ではない
    assertの有無がプログラムに影響しないようにする

それでは詳しく説明していきます。
assert文はエラー処理ではない

これまで説明したように、少しでもプログラムが想定外の動作をした場合には
assert文がエラーを返します。
しかし、エラーを返すだけでエラー処理を行うものではないので注意しましょう。
そのため、例外が投げられた場合には開発者自身が
戻り値をチェックしたりエラー処理をしたりするなどの対応をする必要があります。


assertの有無がプログラムに影響しないようにする

assert文はアサーションを有効化した場合、
つまりプログラムが正常に動作しているかチェックする方法が有効な時にのみ
実行されるようになっています。
そのため、プログラムの実行結果がassertの有無によって変わらないように注意しなければなりません。
assertが有効化された場合とされていない場合でローカル変数の値が変化しないように注意しましょう。
"""


print("--- まとめ ---")


"""
今回はassert文の基礎知識や使い方、
さらにはif文やunittestとの違いについて説明してきましたがいかがでしたでしょうか。

今回説明した要点をまとめると以下のようになります。

    assert文は条件をテストするデバッグ支援ツール
    構文は「assert 条件式 , エラーメッセージ」
    無効にするには「 -O 」を使用
    unittestとの違いはテストケースを実行してテストを行うかどうか
    assert文はエラー処理を行わない
    assertの有無がプログラムに影響しないように注意

assert文を使用することで簡単にテストを行うことができます。
個人で開発を行う際は意識する必要はありませんが、
プログラムを商品として扱ったり会社に所属して開発を行ったりする際には必須の知識となっています。
しっかり理解を深めて動作確認に役立ててください。
"""




