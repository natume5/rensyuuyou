#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- requestsの使い方 webサイトのデータを取得する ---")


"""
pythonを使用する1つの目的として
マーケティング等で使用する分析データの取得が挙げられるのではないでしょうか。
サードパーティ製のライブラリであるrequestsを使用すると、
web上のデータを簡単に取得することができます。
学習前にhttpの基本（ヘッダ、ステータスコード等の単語がわかる程度）
を予め学習することをおすすめします。
"""


print("--- 学習前の注意点 ---")


"""
公開されているwebサーバーに対してアクセスを連続して行うと、
対象webサーバーに対し負荷をかけてしまいます。
このことによりサーバーのレスポンスが遅くなったりダウンしたりすると、
業務妨害等で訴訟を受ける可能性があります。
アクセスとアクセスの時間間隔を十分空け（5秒程度）、
相手先サーバーの迷惑にならないように心がけましょう。
"""


print("--- requestsとは ---")


"""
requestsとはサードパーティ製のhttp通信を行うためのライブラリです。
これを使用すると、webサイトのデータのダウンロードやrestapiの使用が簡単にできます。
PyPIで配布されていますので、インストールはpipですることができます。

pip install requests
"""


print("--- 使い方の基本 ---")


"""
リクエストして結果を取得する

それでは早速使ってみましょう。
まずはヤフーのニュース一覧ページのhtmlを取得してみます。
requstsにはhttpのメソッドがそれぞれ用意されています。
ここでは取得なのでgetメソッドを使ってみましょう。
"""

import requests

url = "http://news.yahoo.co.jp/topics"
r = requests.get(url)
print(r.text)

"""
getの戻り値としてレスポンス内容が格納されたオブジェクトが返されます。
textという属性にhtmlが格納されます。
上のコードを実行するとhtmlの文字列がコンソールに出力されます。


レスポンスオブジェクト

レスポンスオブジェクトにはhtml文字列以外にエンコーディング、
httpステータスコード、レスポンスヘッダなどが格納されています。
以下のように取得することが可能です。
"""

# エンコーディング
print(r.encoding)

# httpステータスコード
print(r.status_code)

# レスポンスヘッダ
print(r.headers)

# byte形式
print(r.content)


print("--- エンコーディングの判定仕様と自動判定 ---")


"""
さて、requestsを手当たり次第色んなサイトで使っていると、
よく文字化けに遭遇することが多々あります。
分析データの取得等で様々なサイトに対して使用する場合は
requestsのエンコーディング決定ロジックを知っておくと解決の糸口になるかもしれません。
以下、requestsのエンコーディングの決定ロジックのメソッドを抜粋したものです。
"""

def get_encoding_from_headers(headers):
	"""Returns encodings from given HTTP Header Dict.

	:param headers: dictionary to extract encoding from.
	:rtype: str
	"""

	content_type = headers.get('content-type')

	if not content_type:
		return None

	content_type, params = cgi.parse_header(content_type)

	if 'charset' in params:
		return params['charset'].strip("'\'")

	if 'text' in content_type:
		return 'ISO-8859-1'

"""
レスポンスヘッダを元に判定しています。
content-typeがなければNone、
あってもcharsetが設定されていない場合は
ISO-8859-1（ラテンアルファベット）が設定されます。
このため、設定が誤ったサーバーにアクセスした場合は
不適切なエンコーディングとなります。
この場合は、以下のように手動でエンコーディングを設定することができます。
"""

r.encoding = 'Shift_JIS'

"""
ただし、レスポンスオブジェクトにはエンコーディングを判定する
apparent_encodingプロパティが用意されています。
以下のようにエンコーディングを設定する。
"""

r.encoding = r.apparent_encoding

"""
内部の実装には以下の通り
chardetが使用されているという点も知っておくと良いでしょう。
"""

@property
def apparent_encoding(self):
	"""The apparent encoding, provided by the chardet library"""
	return chadet.detect(self.content)['encoding']


print("--- tips ---")


"""
最後にいくつか雑多な内容を列挙します。
以下の内容以外にも.netrc、Cookie、Keep-Alive、ベーシック認証
といったhttp通信で使用する設定を行うことが可能なので、
公式サイトも確認してみてください。

get以外のメソッド

冒頭で少し振れましたが、get以外にも各種httpメソッドが用意されています。
また、後述する引数などはメソッドによらず共通です。
"""

r = requests.put(url)
r = requests.delete(url)
r = requests.head(url)
r = requests.options(url)

"""
URLパラメータの設定

辞書形式でURLのクエリ文字列のパラメータを付加することができます。


params = {'key1': 100, 'key2': 200}
r = requests.get("http://xxxxxxx.com", params=params)

上の場合、「http://xxxxxxx.com/?key1=100&key2=200」
にgetでアクセスした場合と等価となります。


リクエストヘッダの設定　（User-Agentなど）

リクエストにHTTPヘッダーを追加したい場合は辞書形式で付加することが可能です。
例えば、User-Agentを指定する場合は以下のようにします。

headers = {'User-Agent': ' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36'}
r = requests.get(url, headers=headers)


プロキシー

squid等のプロキシーを経由してアクセスすることも可能です。
http、httpsとで分けて設定することが可能です。
ホスト:ポート番号と形式で記述します。

proxies = {"http": "xxx.xxx.xxx.xxx:3128", "https": "xxx.xxx.xxx.xxx:3128"}
r = requests.get(url, proxies=proxies)


タイムアウト

引数にtimeoutを指定すると接続のタイムアウト時間を設定することができます。

r = requests.get(url, timeout=0.001)

ただし、接続処理時間のみが対象となるため、
ダウンロードが遅い場合のタイムアウト処理は自力で実装する必要があります。
"""
