#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- chardet 文字コードを判定する---")


"""
日本語サイトのスクレイピング等でマルチバイト文字を含んだバイナリ文字列データを扱う場合、
デコードのために文字コード（正確にはエンコーディングですが）が何なのかを事前に把握する必要がなります。
ですが、Webサイト等ではそれがわからない場合も往々にしてあります。
そんなとき便利なのが今回学習するchardetという文字コード判定ライブラリです。


インストール
pipでインストールできます。

pip install chardet
基本的な使い方
detectメソッドにバイナリ文字列データを指定します。
以下のサンプルでは、yahooのサイトの文字コードを判定しています。
webサイトのデータ取得はurllibモジュールを使用しています。
"""

import chardet
from urllib.request import urlopen

r = urlopen('http://yahoo.co.jp/')
rowdata = r.read()
print(chardet.detect(rowdata)) 
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}   

"""
結果は辞書形式で、encodingが文字コード、confidenceが判定結果の信頼性を表します。
"""

"""
応用的な使い方
文字列判定時、比較的大きなサイズのデータで判定をすると時間がかかります。
そんな場合、UniversalDetectorを利用しfeedメソッドで少しずつ判定を行い、
信頼性がある一定以上になればそこで判定を終わる、という方法があります。
サンプルを見てみましょう。
"""

from chardet.universaldetector import UniversalDetector
from urllib.request import urlopen

detector = UniversalDetector()

r = urlopen('http://yahoo.co.jp/')
for line in r:
	detector.feed(line)
	if detector.done:
		break

detector.close()
print(detector.result)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

"""
detector.doneは、信頼性が一定を超えるとTrueを返します。
detector.resultで結果を取得できますが、
その前にclose()メソッドを呼び出す必要があるので注意してください。
"""


print("--- mojimoji 半角⇔全角の変換---")


"""
mojimoji
自然言語処理の前処理として全半角の変換を行うことが多いと思いますが、
その際に便利なmojimojiというライブラリについて学習します。
全半角処理ができるライブラリは色々あるのですが、
その中でもmojimojiは処理が比較的高速である点に特徴があります。

インストールは以下の通りpipで行います。
一部のlinuxではgcc-c++がインストールがなくエラーが出るかもしれません。
ページ下部の補足を参照してください。

pip install mojimoji
では使い方について見ていきましょう。

全角から半角へ変換する
その名もズバリzen_to_hanメソッドを使用します。
kana、digit、asciiというオプションをキーワード引数で指定すると、
カナ、数字、アルファベットの無効化を指定することができます。
"""

import mojimoji

text = "Ｐｙｔｈｏｎ パイソン　１０００"
print(mojimoji.zen_to_han(text))    # Python ﾊﾟｲｿﾝ 1000

print(mojimoji.zen_to_han(text, kana=False))    # Python パイソン 1000

print(mojimoji.zen_to_han(text, digit=False))    # Python ﾊﾟｲｿﾝ １０００

print(mojimoji.zen_to_han(text, ascii=False))    # Ｐｙｔｈｏｎ ﾊﾟｲｿﾝ　1000

"""
特に解説は不要かと思います。
形態素解析の前処理ではkana=Falseのみを指定するケースが多いのではないでしょうか。
"""

"""
こちらの処理は使う機会があまりないかもしれませんが、参考のため掲載します。
han_to_zenメソッドを使用します。
やはりzen_to_hanと同様、kana、digit、asciiというオプションをキーワード引数で指定すると、
カナ、数字、アルファベットの無効化を指定することができます。
"""

import mojimoji

text = "python パイソン 1000"
print(mojimoji.han_to_zen(text))    # ｐｙｔｈｏｎ　パイソン　１０００

print(mojimoji.han_to_zen(text, kana=False))    # ｐｙｔｈｏｎ　パイソン　１０００

print(mojimoji.han_to_zen(text, digit=False))    # ｐｙｔｈｏｎ　パイソン　1000

print(mojimoji.han_to_zen(text, ascii=False))    # python パイソン １０００


print("--- IPython 入門---")


"""
pythonは対話形式のインタプリタが便利ですが、それをさらに強力にしたインタラクティブシェル、
IPythonについて学習しましょう。


IPythonとは
データ分析でよく利用するIPythonですが、どういったものなのでしょうか？
IPython公式の説明を引用してみます。

強力なインタラクティブシェル
Jupyterのカーネル
インタラクティブなデータの視覚化とGUIツールキットの使用をサポート
柔軟で組み込み可能なインタプリタをプロジェクトから読み込める
並列コンピューティングのための使いやすい高性能ツール

簡単にいうと、データ分析のための分析・可視化ツールを対話形式で利用できるライブラリです。
Jupyterについては今後別途ご紹介する予定です。

この対話形式は非常に協力なので、データ分析をする目的以外にも使えます。

僕は通常のPythonの対話形式よりIPythonの方が便利なので、
対話形式の場合はほとんどIpythonを使用します。

IPython入門
(このページではデータ分析関連の内容は書きません。IPythonの初歩的な操作についてご説明します。)

IPythonには通常のPythonの対話形式より強力な点は補完機能、オブジェクト内容表示、
外部シェル実行機能などがあります。詳細は以下のチュートリアルをご参照ください。
Introducing IPython

インストールと起動
まずはインストールです。以下のpipコマンドでインストール可能です。
anacondaを利用している場合は、予めインストールされているので不要です。


pip install ipython
ipythonと打ち込むと以下のように起動します。
"""

"""
タブキーによる自動補完
まず、通常のPythonと比較して、圧倒的に便利なのがこのタブキーによる自動補完機能です。
途中まで入力してTabキーを押下すると、補完候補が選べます。

# 適当に変数を定義する
In [1]: var_hoge = 1
# 途中まで入力してTabキーを押下する
In [2]: v
"""
"""
?コマンド
オブジェクトの内容を確認する際、便利なのが?コマンドです。
変数やオブジェクトのあとに?をつけると、その説明が表示されます。
"""
"""
マジック関数
予め用意されているユーティリティ的な関数です。以下の形式で利用します。
%[マジック関数名] パラメータ
複数行パラメータとして渡したい場合は、%%をつけます。この説明だけだと、
何のことかわけがわからないと思いますので、いくつか例を交えて説明します。
全ては説明しきれないので、詳細はBuilt-in magic commandsを参照してください。
"""
"""
%timeit
%timeitは後に渡されたパラメータを実行する時間を返します。
例えば、1000個のリストを生成する実行、その最大値を算出する時間を調べたい場合、
以下のようになります。

%timeit range(1000)
738 ns ± 36.9 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

: %%timeit x = range(10000)
   ...: max(x)
   ...:
   ...:
806 µs ± 61.6 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
"""
"""
%run
runは外部のpythonスクリプトを起動します。
例えば、文字列を出力するsample.pyというスクリプトがあった場合、以下のように実行します。


%run sample.py
2022-07-02 09:07:38,130 - mod1 - ERROR - エラー発生っ!!
"""
"""
%history, %save, %load
%historyで履歴を確認します。
%saveは履歴の中で保存したいものを番号指定してスクリプトとして保存できます。
当然saveしたものをloadすることができます。
サンプルを見てみましょう。

In [1]: s = 'sample'
 
In [2]: print(s)
sample
 
In [3]: %history
s = 'sample'
print(s)
%history
 
In [4]: save save_sample.py 1 2
The following commands were written to file `save_sample.py`:
s = 'sample'
print(s)
 
In [5]: load save_sample.py
 
In [6]: # %load save_sample.py
   ...: s = 'sample'
   ...: print(s)
   ...: 
sample
 
In [7]: run save_sample.py
sample

実行したスクリプトの説明です。

1から2行目まで適当な文を実行しています。

3行目で履歴を確認し、4行目で1行目から2行目をsave_sample.pyというファイルに保存しています。

5行目でsave_sample.pyをloadし6行目でその内容が表示されています。

7行目で%runでそのスクリプトを実行しています。
"""
"""
その他のマジック関数
%editでエディタが起動し、対話モードの途中で指定したスクリプトを編集することができます。
%debugでデバッグモードとなります。

その他にも色々あってすべては紹介しきれないのですが、
%quickrefでマジック関数のリファレンスが表示されますので一読しておくと良いでしょう。
"""
"""
システムコール
bash等のシェルの入力が可能になります。

In [12]: pwd
/home/work/ipython
"""
"""
設定ファイル等
通常、~/.ipython/profile_defaultに配置されます。
また、その中の~/.ipython/profile_default/startup/にスクリプトを配置すると、
それらがIPython起動時に毎回実行されます。
"""
"""
終了方法
通常のPythonの対話モードと同様でquit()で終了します。
"""

"""
タブ補完、?コマンド、マジック関数の3つがポイント
いかがだったでしょうか。
タブ補完、?コマンド、マジック関数の3つを抑えれば通常のPythonの対話モードより
断然効率的に使用できるようになると思いますのでおすすめです。
"""


print("--- requestsの使い方 webサイトのデータを取得する---")


"""
pythonを使用する1つの目的としてマーケティング等で使用する
分析データの取得が挙げられるのではないでしょうか。
サードパーティ製のライブラリであるrequestsを使用すると、
web上のデータを簡単に取得することができます。
学習前にhttpの基本（ヘッダ、ステータスコード等の単語がわかる程度）
を予め学習することをおすすめします。

学習前の注意点

公開されているwebサーバーに対してアクセスを連続して行うと、
対象webサーバーに対し負荷をかけてしまいます。
このことによりサーバーのレスポンスが遅くなったりダウンしたりすると、
業務妨害等で訴訟を受ける可能性があります。
アクセスとアクセスの時間間隔を十分空け（5秒程度）、
相手先サーバーの迷惑にならないように心がけましょう。

requestsとは
requestsとはサードパーティ製のhttp通信を行うためのライブラリです。
これを使用すると、webサイトのデータのダウンロードやrestapiの使用が簡単にできます。
PyPIで配布されていますので、インストールはpipですることができます。

pip install requests

使い方の基本
リクエストして結果を取得する

それでは早速使ってみましょう。まずはヤフーのニュース一覧ページのhtmlを取得してみます。
requstsにはhttpのメソッドがそれぞれ用意されています。
ここでは取得なのでgetメソッドを使ってみましょう。
"""

import requests

url = "https://news.yahoo.co.jp/topics"
r = requests.get(url)
print(r.text)

"""
getの戻り値としてレスポンス内容が格納されたオブジェクトが返されます。
textという属性にhtmlが格納されます。
上のコードを実行するとhtmlの文字列がコンソールに出力されます。
"""
"""
レスポンスオブジェクト

レスポンスオブジェクトにはhtml文字列以外にエンコーディング、
httpステータスコード、レスポンスヘッダなどが格納されています。
以下のように取得することが可能です。

# エンコーディング
print(r.encoding)

# httpステータスコード
print(r.status_code)

# レスポンスヘッダ
print(r.headers)

# byte形式
print(r.content)
"""

"""
エンコーディングの判定仕様と自動判定

さて、requestsを手当たり次第色んなサイトで使っていると、よく文字化けに遭遇することが多々あります。
分析データの取得等で様々なサイトに対して使用する場合は
requestsのエンコーディング決定ロジックを知っておくと解決の糸口になるかもしれません。
以下、requestsのエンコーディングの決定ロジックのメソッドを抜粋したものです。

def get_encoding_from_headers(headers):
    """"""Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    """"""

    content_type = headers.get('content-type')

    if not content_type:
        return None

    content_type, params = cgi.parse_header(content_type)

    if 'charset' in params:
        return params['charset'].strip("'\"")

    if 'text' in content_type:
        return 'ISO-8859-1'

レスポンスヘッダを元に判定しています。content-typeがなければNone、
あってもcharsetが設定されていない場合はISO-8859-1（ラテンアルファベット）が設定されます。
このため、設定が誤ったサーバーにアクセスした場合は不適切なエンコーディングとなります。
この場合は、以下のように手動でエンコーディングを設定することができます。

r.encoding = 'Shift_JIS'

ただし、レスポンスオブジェクトにはエンコーディングを判定する
apparent_encodingプロパティが用意されています。以下のようにエンコーディングを設定する。

r.encoding = r.apparent_encoding

内部の実装には以下の通りchardetが使用されているという点も知っておくと良いでしょう。

@property
def apparent_encoding(self):
    """"""The apparent encoding, provided by the chardet library""""""
    return chardet.detect(self.content)['encoding']
"""

"""
tips

最後にいくつか雑多な内容を列挙します。
以下の内容以外にも.netrc、Cookie、Keep-Alive、
ベーシック認証といったhttp通信で使用する設定を行うことが可能なので、
公式サイトも確認してみてください。

get以外のメソッド

冒頭で少し振れましたが、get以外にも各種httpメソッドが用意されています。
また、後述する引数などはメソッドによらず共通です。

r = requests.put(url)
r = requests.delete(url)
r = requests.head(url)
r = requests.options(url)

URLパラメータの設定

辞書形式でURLのクエリ文字列のパラメータを付加することができます。

params = {'key1': 100, 'key2': 200}
r = requests.get("http://xxxxxxx.com", params=params)

上の場合、「http://xxxxxxx.com/?key1=100&key2=200」にgetでアクセスした場合と
等価となります。
リクエストヘッダの設定　（User-Agentなど）

リクエストにHTTPヘッダーを追加したい場合は辞書形式で付加することが可能です。
例えば、User-Agentを指定する場合は以下のようにします。

headers = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36'}
r = requests.get(url, headers=headers)

プロキシー

squid等のプロキシーを経由してアクセスすることも可能です。
http、httpsとで分けて設定することが可能です。ホスト:ポート番号と形式で記述します。

proxies = {"http": "xxx.xxx.xxx.xxx:3128", "https": "xxx.xxx.xxx.xxx:3128"}
r = requests.get(url, proxies=proxies)

タイムアウト

引数にtimeoutを指定すると接続のタイムアウト時間を設定することができます。

r = requests.get(url, timeout=0.001)

ただし、接続処理時間のみが対象となるため、
ダウンロードが遅い場合のタイムアウト処理は自力で実装する必要があります。
"""
