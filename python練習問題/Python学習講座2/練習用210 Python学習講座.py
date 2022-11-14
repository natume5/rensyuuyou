#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- unittest 単体テスト入門 その2 テストパッケージとテストスイート ---")


print("--- プロジェクト構成とテストの実行 ---")


"""
Pythonに限らずプロジェクトの構成として、
アプリケーションのソースコードとテストのソースコードは
別パッケージとしてディレクトリを分けることが一般的です。
以下のような構成の場合の実行方法について考えてみましょう。

.                        # プロジェクトディレクトリ(ここで実行する)
├── sample_lib        # アプリケーションのパッケージ
│   ├── __init__.py
│   ├── mod1.py
│   └── mod2.py
└── test              # テストのパッケージ
    ├── __init__.py
    ├── test_mod1.py
    └── test_mod2.py

mod1.py、mod2.pyというコードに対するテストコードが用意されているものとします。これらのテストを実行する際、プロジェクトディレクトリ直下で以下のように-mオプションでunittestモジュールを実行し、相対パスでテストスクリプトを指定します。

$ python -m unittest test/test_mod1.py 
test_add_num
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ python -m unittest test/test_mod2.py 
test_is_positive
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

それぞれのテストスクリプトにif __name__ == '__main__':
をつけて実行する方法もあるのですが、
その場合はエントリーポイントがtestディレクトリ配下になってしまいますので、
予めPYTHON_PATHをエクスポートするなどの措置が必要になります。
"""


print("--- テストスイート（テストのグループ化） ---")


"""
上のプロジェクトの場合テストスクリプトがたった2つなので順番に
pythonコマンドを実行しても良いのですが、
プロジェクトによってはこれが数十、数百になることも考えられます。
こういった時のためPythonはunittestを
グループ化してまとめて実行することが可能です。
（一般的にテストスイートと呼ばれています。）


テストスイートの作成方法

さっそくテストスイートを作成してみましょう。
runner.pyという名前でテストクラスを作成します。

.
├── sample_lib2
│   ├── __init__.py
│   ├── mod1.py
│   └── mod2.py
└── test3
    ├── __init__.py
    ├── runner.py        # テストスイートクラス
    ├── test_mod1.py
    └── test_mod2.py

runner.pyは以下のように書きます。

# runner.py
import unittest
import test.test_mod1
import test.test_mod2

class TestRunner(unittest.TestCase):

    def test_runner(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.makeSuite(test.test_mod1.TestMod1))
        test_suite.addTest(unittest.makeSuite(test.test_mod2.TestMod2))
        unittest.TextTestRunner().run(test_suite)

unittest.TestSuite()オブジェクトを生成し、
addTestでテストクラスを指定します。
TextTestRunner().run()が呼び出されると
addしたテストクラスが実行されます。

今までと同様に-mオプションをつけ、
テストスイートクラスを指定すると、
addしたテストケースが実行されていることが確認できます。

$ python -m unittest test/runner.py 
.
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK


discover（テストスイート作成の自動化）

上のテストスイートではaddTestで1つ1つ追加していきましたが、
これもモジュール数が多いと管理が大変そうですね。
このため、ディレクトリ単位でテストモジュールを探索し、
自動でテストスイートを作成してくれる仕組みがあります。
これをdiscoverと呼びます。
実はテストモジュールを指定せずに以下のように打ち込むと、
プロジェクト全体を走査してテストを見つけ実行してくれます。

python -m unittest

ですが、サブプロジェクト単位でテストスイートを実行したい場合などは、
上で作成したrunnerに自分でdiscoveryを記述して
カスタマイズすることが可能です。
上のrunner.pyをdiscoverを使用したものに修正してみましょう。

# runner.py
import unittest
import test.test_mod1
import test.test_mod2

class TestRunner(unittest.TestCase):

    def test_runner(self):
        test_suite = unittest.TestSuite()

        # testクラスを見つけ出す
        tests = unittest.defaultTestLoader.discover("test", pattern="test_*.py")

        # 見つけたtestクラスを追加する
        test_suite.addTest(tests)
        unittest.TextTestRunner().run(test_suite)

discoverの引数にはディレクトリを指定します。
ローカルでテストを実行する場合は、
機能単位でテストをする等をして時間を節約することが可能です。
"""
