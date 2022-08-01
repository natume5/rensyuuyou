#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- スクレイピングで必須のライブラリの使い方② （Selenium） ---")


"""
PythonでスクレイピングをするにはrequestsやBeautiful Soupなどを使いますが、
Seleniumを使う方法もあります。
Seleniumを使えばJavaScriptを使った動的なページにも対応できます。
ここでは「Seleniumって何？」「urllibやrequestsと何が違うの？」
「Seleniumの使い方が知りたい」といった方へ、Seleniumについて解説します。
"""


print("--- スクレイピングする際のルール ---")


"""
スクレイピングは他のサイトの情報を取得する行為なので、著作権法を守る必要があります。
こちらにスクレイピングするルールを載せていますので、
スクレイピングする場合は以下の記事のスクレイピングをする際のルールをご一読ください。
"""


print("--- Seleniumとは ---")


"""
今回はスクレイピングをする上でのSeleniumの紹介となりますが、
Seleniumuは本来スクレイピングをするものとして作られたライブラリではなく
「ブラウザをプログラムから操作し、テストを自動化する」目的で作られたものです
（いわゆるオートメーションツール）。
しかし、ブラウザを操作する際にhtmlを取得することができるので、
結果スクレイピングもできるようになっています。
また、Seleniumは人間と同じようにブラウザを操作できるので、
やろうと思えばスクレイピングやテスト自動化以上のことも可能です。
今まで手作業で行なっていたことが、Seleniumを使うことで自動化することができます
"""


print("--- Seleniumとurllib、requestsの違い ---")


"""
上述したようにSeleniumはブラウザの自動操作ができるツールなので、
urllibやrequestsのような、htmlを取得するライブラリよりも多くのことが可能です。
スクレイピングの観点で言えば、urllibやrequestsの場合は取得したhtmlを
Beautiful Soupに通してから要素を取得するのが一般的ですが、
Seleniumの場合はBeautiful Soupを通さずに要素を取得できます
（Beautiful Soupを使うこともできます）。
また、Seleniumはブラウザを操作することができるので、
JavaScriptを使った動的なページに対しても行うことが可能です。
"""


print("--- Seleniumの使い方 ---")


"""
では実際にSeleniumを使ってみましょう。

なお、今回はMacOS Mojave(10.14.6)  
+ Google Chrome(80.0.3987.122)の環境で実行します。
特にGoogleChromeのバージョンは非常に重要なので、先に調べておきましょう。
左上のリンゴマークの隣のChromeをクリックして「Googe Chromeについて」
を選択するとバージョン情報が表示されます。

Web Driverをインストールする

Seleniumを使うにはそのブラウザのWebDriverを使う必要があります。
このWebDriverはブラウザのバージョンと対応しているので、
バージョンが合っていないとSeleniumはうまく動作してくれません。
Chromeの場合はChromeDriverをダウンロードします。以下のURLからダウンロード画面へいけます。

クリックするとダウンロードが始まるので、終わったらzipファイルを解凍します。
これでChromeDriverのダウンロードは完了です。

Seleniumでスクレイピングする

それではこれからSeleniumを使ってスクレイピングを実施していきます。
まずはpipでSeleniumをインストールしましょう。

$ pip install selenium

次が今回のコードです。長いですが、一つずつ見ていきましょう。
"""
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# マウスオーバーするために必要

# アクセスするurl
URL = 'https://myafu-python.com/'

# 各動作間の待ち時間(秒)
INTERVAL = 3

# 検索するidの一覧
ID_LIST = ['menu-item-680', 'menu-item-681', 'menu-item-682']

# ブラウザ起動
driver_path = './chromedriver'
driver = webdriver.Chrome("D:/ソフト/Google Chrome/chromedriver_win32/Chromedriver.exe")

# windowサイズをmaxにする
driver.maximize_window()
time.sleep(INTERVAL)

# サイトを開く
driver.get(URL)
time.sleep(INTERVAL)

# IDに紐づくリストをクリックして画面遷移する
for ID in ID_LIST:
	# マウスオーバーを使うための宣言
	actions = ActionChains(driver)
	# 「文法」にマウスオーバー
	target_text = '文法'
	actions.move_to_element(driver.find_elements_by_xpath( "//*[text()='%s']" %
	 target_text)).perform()
	time.sleep(INTERVAL)
	# 遷移先画面のクラス名がentry-card-titleの要素を全て取得(記事のタイトル)
	titles = driver.find_elements_by_class_name('entry-card-title')

	# 取得した記事のタイトルを出力する
	for title in titles:
		print(title.text + ":" + ID)
	# 前の画面に戻る
	driver.back()
	time.sleep(INTERVAL)

# ブラウザを閉じる
driver.close()
"""

"""
上のコードでやっていることは「文法タブの下にある3つのリンク先の記事タイトルの収集」です。

一つずつ見ていきましょう。まずはimportからです。

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

timeはChromeの立ち上げや画面遷移の時に、
ちゃんと読み込んでから次の処理へ移るためのsleep処理を入れるために使います。
webdriverはSeleniumを動かすために必須です。
またActionChainsはSeleniumを使ってマウスオーバー処理をするために使います。
次に設定です。

URL = "https://myafu-python.com/"
INTERVAL = 3
ID_LIST = ['menu-item-680', 'menu-item-681', 'menu-item-682']

URLはアクセスするURL、INTERVALはtimeを使う時の待ち時間（秒数）です。
重要なのはID_LISTで、最初に開く画面の、文法タブ配下のリンクのidが入っています。
それぞれ [menu-item-682:Python入門][menu-item-681:ライブラリ]
[menu-item-680:Tips] に紐づいています。

driver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

driver_pathには先ほどダウンロードしたChromeDriverのパスを指定します。
今回はソースコードと同じディレクトリに配置しています。
次にChromeDriverを使ってChromeを立ち上げます。

driver.maximize_window()
time.sleep(INTERVAL)

ここではブラウザの最大化をしています。
また、ここでtime.sleepを呼び出しています。
INTERVALに指定した秒数処理をストップし、ブラウザがちゃんと起動し終わるまで待ちます。

driver.get(URL)
time.sleep(INTERVAL)

driver.getにURLを渡すことでサイトを開きます。サイトが開き終わるまでまた処理をストップさせます。
次にID_LIST分ループさせます。ループ内では次のような処理をしています。

actions = ActionChains(driver)
target_text = "文法"
actions.move_to_element(driver.find_element_by_xpath("//*[text()='%s']" % target_text)).perform()
time.sleep(INTERVAL)

ここでは遷移先リンクをクリックするために、文法タブへのマウスオーバー処理を実行しています。
SeleniumではJavaScriptによって動的にページを変えながら操作できるので、このようなことが可能です。
これはurllibやrequestsではできません。

driver.find_element_by_id(ID).click()
time.sleep(INTERVAL)

driver.find_element_by_idに遷移先リンクのidを渡して要素を取得し、
click()で画面遷移しています。

titles = driver.find_elements_by_class_name('entry-card-title')

遷移先の記事のタイトルを、今度はfind_elements_by_class_nameに
クラス名を渡して複数取得しています。

for title in titles:
    print(title.text + ":" + ID)
driver.back()
time.sleep(INTERVAL)

後は取得した記事タイトルを出力して、driver.back()で前の画面に戻ります。
前の画面に戻ったら次のIDに対応した画面を一つずつ開いていき、記事タイトルを取得していきます。

driver.close()

全てのリンクを辿ってタイトルを収集し終えたらブラウザを閉じて、終了です。
"""


print("--- PythonでSeleniumを使ってスクレイピング (基礎) ---")


"""
スクレイピングを勉強しようと思い立って、Selenium を使ってでブラウザを操作してみたので、
軽くまとめておこうと思います。

使用したもの

    Selenium
        自動でブラウザを操作する為のライブラリ
    Chrome
        ブラウザ

ブラウザに合わせたドライバーを用意する

ブラウザを操作するには、各ブラウザに合わせてドライバーを用意する必要があります。
今回は Chrome を使用するので 公式サイトから ChromeDriver をダウンロードします。
Selenium をインストール

pip で selenium を インストール

pip install selenium
webページを開いてみる

ブラウザを開く
webdriver.Chrome(driver_path)

webページを開く
driver.get(URL)

webページを閉じる
driver.close()

ブラウザを終了 (全てのウィンドウを閉じる)
driver.quit()
"""

"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# マウスオーバーするために必要


# アクセスするurl
URL = 'https://myafu-python.com/'

# 各動作間の待ち時間(秒)
INTERVAL = 4

# 検索するidの一覧
ID_LIST = ['menu-item-680', 'menu-item-681', 'menu-item-682']

# ブラウザ起動
driver_path = './chromedriver'
driver = webdriver.Chrome("D:/ソフト/Google Chrome/chromedriver_win32/Chromedriver.exe")


# サイトを開く
driver.get(URL)
time.sleep(INTERVAL)

# IDに紐づくリストをクリックして画面遷移する
for ID in ID_LIST:
	# マウスオーバーを使うための宣言
	actions = ActionChains(driver)
	# 「文法」にマウスオーバー
	target_text = '文法'
	actions.move_to_element(driver.find_elements_by_xpath( "//*[text()='%s']" %
	 target_text)).perform()
	time.sleep(INTERVAL)
	# 遷移先画面のクラス名がentry-card-titleの要素を全て取得(記事のタイトル)
	titles = driver.find_elements_by_class_name('entry-card-title')

	# 取得した記事のタイトルを出力する
	for title in titles:
		print(title.text + ":" + ID)
	# 前の画面に戻る
	driver.back()
	time.sleep(INTERVAL)

driver.close()

driver.quit()
"""

"""
要素にアクセスしてみる

HTMLの要素にアクセスする為に id、class、name 等から要素を指定して取得する事ができます。

参考資料   https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

id で取得
driver.find_element_by_id('ID')

class で取得
driver.find_element_by_class_name('CLASS_NAME')

name で取得
driver.find_element_by_name('NAME')

link textで取得
driver.find_elements_by_link_text('LINK_TEXT')

ネストされた要素は path を指定して取得
driver.find_elements_by_xpath(".//a")


アクション

取得した要素に対して、アクションを起こす事でwebページを操作します。

ボタンをクリックする
driver.find_element_by_id('Btn').click()

Form に文字を入力する
driver.find_element_by_name('From').send_keys("text")


待機する

よくあるのが、画面のロードが完了する前に、処理が走ってしまいエラーになる。
これに対処する為に必要な要素が準備できるまで、数秒待機する事ができます。

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait(driver, WAIT_SECOND).until(EC.presence_of_element_located((By.CLASS_NAME, 'Btn')))


ブラウザの操作

では上記をふまえて軽く操作してみます。
ボタンをクリックしてみる

例えば、某サイトの購入ボタンを押したい場合

from selenium import webdriver
driver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.find_element_by_class_name('new_addToCart').click()
driver.quit()

こんな感じで find_element_by_class_name() で要素を取得して click() 
でクリックアクションを起こします。


テキスト入力してみる

検索ボックスに検索キーワードを入力して、検索ボタンを押してみます。

from selenium import webdriver
driver = webdriver.Chrome(driver_path)
driver.get(URL)
driver.find_element_by_id('searchWords').send_keys("search text")
driver.find_element_by_id('searchBtn').click()  

これで検索ボックスに自動で "search text" が入力され検索されます。


まとめ

ボタンを押したり、テキスト入力をしたりの基本動作を覚えると、だいたいの操作が簡単に出来る印象です。
やはり、ブラウザ操作をプログラムで行う事で、並列処理が出来る事の恩恵は大きいですね。
ただ、ブラウザをたくさん立ち上げると PC がめちゃくちゃ重くなるので、そこは気をつけないといけませんね。
"""


print("--- 【完全版】PythonとSeleniumでブラウザを自動操作(クローリング／スクレイピング)するチートシート ---")


"""
Pythonの『Selenium』というサードパーティ製のモジュールを用いれば、
Google ChromeやFirefoxなどのブラウザで行っている操作を自動化することができます。

ある特定のWebページからデータを収集したりやファイルをダウンロードしたり…。


基本設定
モジュールのインポート

まず、PythonでSeleniumを使うために必要なモジュールをインポートします。

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

WebDriverのオプション設定

次に、あらゆる環境(ローカル、サーバー上)でSeleniumが動作するようにChromeOptionsを設定します。

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

補足

ヘッドレスモードとは、画面やページ遷移を表示せずに動作するモードです。
Herokuなどのサーバー上でSeleniumを動かす場合は必須になります。


WebDriver(ブラウザ)の起動

DRIVER_PATH = '{{ WebDriverのパスを指定(絶対でも相対パスでも可) }}'
# DRIVER_PATH = '/Users/Kenta/Desktop/Selenium/chromedriver' # ローカル
# DRIVER_PATH = '/app/.chromedriver/bin/chromedriver'        # heroku

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

Webページにアクセス

# Webページにアクセスする
url = '{{ クローリング/スクレイピングするURL }}'
driver.get(url)

サンプルプログラム

ここでは章のまとめとして、GoogleにアクセスしてSeleniumと検索して、
検索1位の記事のタイトルと飛び先のURLを取得するサンプルプログラムを紹介します。

Seleniumのプログラムの全容がつかめると思うので、ぜひトライしてみて下さいね。

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#
# Seleniumをあらゆる環境で起動させるオプション
#
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

#
# Chromeドライバーの起動
#
DRIVER_PATH = '{{ ChromeDriverのPath }}'
driver = webdriver.Chrome("D:/ソフト/Google Chrome/chromedriver_win32/Chromedriver.exe")



#
#
# クローリング/スクレイピング
#
#

# Googleにアクセスする
url = 'https://google.com/'
driver.get(url)

# 検索窓にSeleniumと入力する
selector = '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
element = driver.find_element_by_css_selector(selector)
element.send_keys('Selenium')

# enterキーを押す
element.send_keys(Keys.ENTER)

# 1位の記事のタイトルを取得する
selector = '#rso > div > div:nth-child(1) > div > div.r > a > h3'
element = driver.find_element_by_css_selector(selector)
page_title = element.text

# 1位の記事のURLを取得する
selector = '#rso > div > div:nth-child(1) > div > div.r > a'
element = driver.find_element_by_css_selector(selector)
page_url = element.get_attribute('href')

# ブラウザを終了する(全てのウィンドウを閉じる）
# Chromeのショートカットキー(Command+Q)と同じ動作
driver.quit()

print(page_title, page_url)
# 10分で理解する Selenium - Qiita https://qiita.com/Chanmoro/items/9a3c86bb465c1cce738a


"""
ページ全体の操作
タイトル／URLを取得する

# タイトルを取得する
title = driver.title

# URLを取得する
url = driver.current_url
"""

"""
戻る／進む／更新する

# ブラウザバック(戻る)
driver.back()

# ブラウザバックの取り消し（進む）
driver.forward()

# ページを更新（リロード）する
driver.refresh()
"""

"""
閉じる／終了する

# ページを閉じる(Command + W と同じ)
driver.close()

# ブラウザを終了する(Command + Q と同じ)
driver.quit()
"""

"""
ウィンドウを最大化する

driver.maximize_window()でもウィンドウを最大化できるみたいですが、
出来ないといった声が多かったので別の方法を紹介します。

ChromeOptionsにoptions.add_argument('--kiosk')を追加することで画面が最大化されます。

# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless');
options.add_argument('--kiosk') # <= 追加する
"""

"""
スクリーンショットを取る

screenshot_path = '{{ 保存先のパス(絶対パスまたは相対パス) }}'
driver.save_screenshot(screenshot_path)
"""

"""
アラートダイアログの操作

# YESかNOかのダイアログアラートが出現したとき
Alert(driver).accept() # YESを押す
Alert(driver).dismiss() # NOを押す
"""

"""
操作するウィンドウを切り替える

リンクテキストのtarget="_blank"で別ウィンドウに飛ばされたときに使います。

# ウィンドウハンドルを取得する(list)
handle_array = driver.window_handles

# 一番最後に表示されたブラウザにドライバーを切り替える
driver.switch_to.window(handle_array[-1])
"""

"""
要素の指定

Webページの要素(element)は、id属性、class属性、name属性、CSSセレクタ、
XPath等で指定することが出来ます。

Webページの要素を指定する 
指定先 	                        メソッド
id属性 	           driver.find_element_by_id('{{ ID }}')
class属性 	       driver.find_element_by_class_name('{{ CLASS }}')
name属性 	       driver.find_element_by_name('{{ NAME }}')
CSSセレクタ 	       driver.find_element_css_selector('{{ CSSセレクタ }}')
XPath 	           driver.find_element_by_xpath('{{ XPath }}')

個人的にオススメなのは、CSSセレクタを使用して要素を指定するやり方です。

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

なぜかと言うと、ID属性やclass属性はCSSセレクタで指定出来る上に、
後述するBeautiful Soupモジュールを使ったスクレイピングのやり方と親和性が高いからです。
"""

"""
よく使うCSSセレクタまとめ
基本のセレクタ(タグ、ID、class)

    タグ
    ID
    class

タグ
CSSセレクタ

タグ名

使用例

h2
------------
<div>
    <h2>基本のセレクタ</h2> # Here!
    <p>文章１</p>
    <p>文章２</p>
    <p>文章３</p>
</div>

ID名
CSSセレクタ

#ID名

使用例

#title
------------
<div>
    <h2 id="title">基本のセレクタ</h2> # Here!
    <p>文章１</p>
    <p>文章２</p>
    <p>文章３</p>
</div>

class名
CSSセレクタ

.class名

使用例

.red
------------
<div>
    <h2>基本のセレクタ</h2>
    <p class="red">文章１</p> # Here!
    <p class="red">文章２</p> # Here!
    <p>文章３</p>
</div>

属性セレクタ

    ある属性名を含む要素だけ
    【完全一致】ある属性名で指定した値と一致した要素だけ
    【前方一致】ある属性名の値が指定した値で始まる要素だけ
    【後方一致】ある属性名の値が指定した値で終わる要素だけ
    【部分一致】ある属性名の値が指定した値を含む要素だけ

ある属性名を含む要素だけ
CSSセレクタ

タグ名[属性名]

使用例

a[target]
------------
<p><a href="#">内部リンク</a></p>
<p><a href="xxx" target="_blank">外部リンク</a></p> # Here!

【完全一致】ある属性名で指定した値と一致した要素だけ
CSSセレクタ

タグ名[属性名="値"]

使用例

input[type="text"]
------------
<input type="text"> # Here!
<input type="password">
<input type="radio">

【前方一致】ある属性名の値が指定した値で始まる要素だけ
CSSセレクタ

タグ名[属性名^="値"]

使用例

p[class^="en"]
------------
<p class="english">文章1</p> # Here!
<p class="enable">文章2</p>  # Here!
<p class="japan">文章3</p>
<p class="coen">文章4</p>

【後方一致】ある属性名の値が指定した値で終わる要素だけ
CSSセレクタ

タグ名[属性名$="値"]

使用例

p[class$="n"]
------------
<p class="english">文章1</p>
<p class="enable">文章2</p>
<p class="japan">文章3</p> # Here!
<p class="coen">文章4</p>  # Here!

【部分一致】ある属性名の値が指定した値を含む要素だけ
CSSセレクタ

タグ名[属性名*="値"]

使用例

p[class*="en"]
------------
<p class="english">文章1</p> # Here!
<p class="enable">文章2</p>  # Here!
<p class="japan">文章3</p>
<p class="coen">文章4</p>    # Here!


かゆいところに手が届くCSSセレクタ



    複数のセレクタを同時にみたす要素を指定
    カンマ区切りで複数のセレクタを指定
    絞り込み指定(半角スペース区切り)
    『>』で子要素にのみ指定
    『+』で同じ階層の直後の要素にのみ指定
    『~』で同じ階層の後ろに並ぶ要素に指定

複数のセレクタを同時にみたす要素を指定
CSSセレクタ

selector1selector2

使用例

.color.blue
------------
<ul>
    <li>1つ目のliタグ</li>
    <li class="color">2つ目のliタグ</li>
    <li class="blue">3つ目のliタグ</li>
    <li class="color blue">4つ目のliタグ</li> # Here!
</ul>

カンマ区切りで複数のセレクタを指定
CSSセレクタ

selector1, selector2

使用例

.red, .blue
------------
<ul>
    <li>1つ目のliタグ</li>
    <li class="red">2つ目のliタグ</li>  # Here!
    <li class="green">3つ目のliタグ</li>
    <li class="blue">4つ目のliタグ</li> # Here!
</ul>

絞り込み指定(半角スペース区切り)
CSSセレクタ

selector1 selector2

使用例

nav ul .example
------------
<nav>
    <li class="example">1つ目のliタグ</li>
    <ul>
        <li class="example">2つ目のliタグ</li> # Here!
        <li>3つ目のliタグ</li>
        <li>4つ目のliタグ</li>
    </ul>
</nav>

『>』で子要素にのみ指定
CSSセレクタ

selector1 > selector2

使用例

.example > p
------------
<div class="example">
    <p>文章１</p> # Here!
    <div>
        <p>文章２</p>
    </div>
</div>

『+』で同じ階層の直後の要素にのみ指定
CSSセレクタ

selector1 + selector2

使用例

.example + li
------------
<ul>
    <li>1つ目のliタグ</li> # Here!
    <li class="example">2つ目のliタグ</li>
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li>
</ul>

『~』で同じ階層の後ろに並ぶ要素に指定
CSSセレクタ

selector1 ~ selector2

使用例

.example ~ li
------------
<ul>
    <li>1つ目のliタグ</li> # Here!
    <li class="example">2つ目のliタグ</li>
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li> # Here!
</ul>


n番目の要素を指定するCSSセレクタを表示する

    最初の要素のみ
    最後の要素のみ
    n番目の要素のみ
    nの倍数番目の要素のみ

最初の要素のみ
CSSセレクタ

selector:first-child

使用例

ul li:first-child
------------
<ul>
    <li>1つ目のliタグ</li> # Here!
    <li>2つ目のliタグ</li>
    <li>3つ目のliタグ</li>
    <li>4つ目のliタグ</li>
</ul>

最後の要素のみ
CSSセレクタ

selector:last-child

使用例

ul li:last-child
------------
<ul>
    <li>1つ目のliタグ</li>
    <li>2つ目のliタグ</li>
    <li>3つ目のliタグ</li>
    <li>4つ目のliタグ</li> # Here!
</ul>

n番目の要素のみ
CSSセレクタ

selector:nth-child(n)

使用例

ul li:nth-child(3)
------------
<ul>
    <li>1つ目のliタグ</li>
    <li>2つ目のliタグ</li>
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li>
</ul>

nの倍数番目の要素のみ
CSSセレクタ

selector:nth-child(n)

使用例

ul li:nth-child(2n-1)
------------
<ul>
    <li>1つ目のliタグ</li> # Here!
    <li>2つ目のliタグ</li>
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li>
</ul>


否定セレクタを表示する

    あるセレクタを含まない要素を指定
    あるセレクタとあるセレクタを含まない要素を指定

あるセレクタを含まない要素を指定
CSSセレクタ

selector1:not(selector2)

使用例１

ul > li:not(.blue)
------------
<ul>
    <li>1つ目のliタグ</li>               # Here!
    <li class="red">2つ目のliタグ</li>   # Here!
    <li class="green">3つ目のliタグ</li> # Here!
    <li class="blue">4つ目のliタグ</li>
</ul>

使用例２

ul > li:not(:first-child)
------------
<ul>
    <li>1つ目のliタグ</li>
    <li>2つ目のliタグ</li> # Here!
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li> # Here!
</ul>

あるセレクタとあるセレクタを含まない要素を指定
CSSセレクタ

selector1:not(selector2):not(selector3)

使用例1

ul > li:not(.blue):not(.red)
------------
<ul>
    <li>1つ目のliタグ</li>               # Here!
    <li class="red">2つ目のliタグ</li>
    <li class="green">3つ目のliタグ</li> # Here!
    <li class="blue">4つ目のliタグ</li>
</ul>

使用例２

ul > li:not(:first-child):not(:last-child)
------------
<ul>
    <li>1つ目のliタグ</li>
    <li>2つ目のliタグ</li> # Here!
    <li>3つ目のliタグ</li> # Here!
    <li>4つ目のliタグ</li>
</ul>

"""

"""
開発ツールでCSSセレクタを取得する

Chromeの開発ツール(ディベロッパーツール)を使うと、
操作する要素のCSSセレクタを一発で取得することができます。

『要素をダイレクトで指定』→『右クリック』→『Copy selector』
で簡単にCSSセレクタを取得することができます。
"""

"""
要素の操作

前章で要素を指定できたら、今度は指定した要素に実行したい処理を設定します。

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# 要素を操作する
element.xxx
"""

"""
テキスト／属性値を取得する

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# テキストを取得する
element.text

# 属性値を取得する
element.get_attribute('属性名')
"""

"""
テキストを入力／削除する

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# テキストを入力する
element.send_keys('{{ inputやtextareaに入力する文字列 }}')

# テキストを削除する
element.clear()

まれにWebページによって、element.clear()で文字列を削除できない場合があります。

そういうときは、消したい文字数分だけバックスペースキーを押して、無理やり削除します。

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# 文字数分バックスペースキーを押す
for _ in range(len(element.text)):
    element.send_keys(Keys.BACK_SPACE)
"""

"""
クリックする

# 要素をクリックする
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
element.click()

まれにWebページによって、element.click()でクリック出来ないことがあります。

そういうときは、driver.execute_scriptメソッドを使用して、
JavaScriptを呼び出し、無理やりクリックさせます。

# 要素をクリックする(JavaScript)
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
driver.execute_script('arguments[0].click();', element)

また、検索フォームなどでクリックする要素がない場合は、
エンターキーを押すことでクリックと同等のアクションを行うこともできます。

# エンターキーを押す
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
element.send_keys(Keys.ENTER)
"""

"""
特殊キーを押す

# 要素を指定する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# エンターキー
element.send_keys(Keys.ENTER)

# バックスペースキー
element.send_keys(Keys.BACK_SPACE)

# エスケープキー
element.send_keys(Keys.ESCAPE)

# タブキー
element.send_keys(Keys.TAB)
"""

"""
select要素を操作する

SELECT要素のOPTIONはelement.click()などでクリックしても反応しません！
選択する

# 要素を指定する(※Selectを指定する)
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# 【オススメ】option要素のvalue属性値で選択する
Select(element).select_by_value('{{ value属性値 }}')

# option要素のインデックスで選択する
Select(element).select_by_index('{{ インデックス }}')

# option要素の表示テキストで選択する
Select(element).select_by_visible_text('{{ 文字列 }}')

選択解除する

# 要素を指定する(※Selectを指定する)
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)

# 【オススメ】option要素のvalue属性値で選択解除する
Select(element).deselect_by_value('{{ value属性値 }}')

# option要素のインデックスで選択解除する
Select(element).deselect_by_index('{{ インデックス }}')

# option要素の表示テキストで選択解除する
Select(element).deselect_by_visible_text('{{ 文字列 }}')

# すべて選択解除する
Select(element).deselect_all()
"""

"""
実践テクニック集
待機処理

Seleniumのエラーの原因の95%以上は、Seleniumの処理が速すぎて、指定した要素が見つからないことだと思います。
MEMO

通常の人間が行うブラウザ操作であれば、ページの読み込みが完了していないのに、ボタンをクリックしたりテキストを取得したりなんて出来ませんよね。

つまり、Web Driverに正しく『待ち』の時間を設定してあげることでSeleniumのエラーは、大幅に減少します。
暗黙的な待機

implicitly_waitメソッドを使用すると、暗黙的な待機時間を設定することができます。デフォルト：0秒。

driver.implicitly_wait(10) # 秒

一度設定すると、全てのfind_element等の処理時に、要素が見つかるまで指定した最大時間待機させるようにすることができます。
明示的な待機

暗黙的な待機(implicitly_wait)で対応しきれなかった処理に対して、WebDriverWait.untilメソッドで、任意のHTMLの要素が特定の状態になるまで待つ明示的な待機時間を設定することができます。

# 指定した要素が表示されるまで、明示的に30秒待機する
selector = '{{ CSSセレクタ }}'
element = WebDriverWait(driver, 30).until(
	EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
)

先程、WebDriverWait.untilメソッドの説明を、任意のHTMLの要素が『特定の状態になる』と説明をしました。

例では、visibility_of_element_locatedメソッドが、ここで言う『特定の状態になる』部分を指しています。
expected_conditionsクラスの例 
メソッド 	                                説明
alert_is_present 	                Alertが表示されるまで待機する
element_to_be_clickable 	        要素がクリック出来る状態になるまで待機する
visibility_of_element_located 	    指定した要素が表示されるまで待機する
invisibility_of_element_located 	指定した要素が非表示になるまで待機する
text_to_be_present_in_element 	    指定したテキストが表示されるまで待機する
presence_of_element_located 	    指定した要素がDOM上に現れるまで待機する


最終手段

暗黙的な待機(implicitly_waitメソッド)と明示的な待機(expected_conditionsクラス)でも、
うまくいかなかった場合の最終手段を紹介します。

それは、Pythonの標準ライブラリのtimeクラスのsleepメソッドを使用して、
要素が表示されていようがいまいが強制的に指定した時間だけプログラムをスリープさせる方法です。

import time
time.sleep(30) # 秒


人間っぽく待機する

NumPyのrandomクラスを用いて、待機時間に幅をもたせます。

import numpy as np
import time

# 10.000~12.000秒のランダムな乱数を生成する
wait_time = float('{:.3f}'.format(np.random.rand()*2+10))

# 待つ
time.sleep(wait_time)

BeautifulSoupと組み合わせる

実際では、クローリングをSelenium、スクレイピングをBeautifulSoupで行うことがほとんどです。

スクレイピングはelement.textでも出来るのですが、処理スピードが段違いなので…。

driver.page_sourceでWebページのソースコードを抜き出し、あとはBeautifulSoup側でスクレイピングの処理を行います。
基本構文

from bs4 import BeautifulSoup

#
# 中略
#

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'lxml') # または、'html.parser'

# CSSセレクタ
selector = '{{ CSSセレクタ }}'

単一(str)

# テキスト
text = soup.select_one(selector).get_text()

# 属性値
attr = soup.select_one(selector).get('{{ 属性名 }}')

複数(list)

# テキスト
texts = [i.get_text() for i in soup.select(selector)]

# 属性値
attrs = [i.get('{{ 属性名 }}') for i in soup.select(selector)]


tableをpandas.DataFrameに格納する

Seleniumでクローリング、BeautifulSuopでWebページのテーブルをスクレイピングした場合、
それらのデータは一旦pandas.DataFrameに格納してから前処理することが多いと思います。
Webサイトによってtableの構成は様々だと思いますが、80%くらい以下のプログラムで取得できます。
1発で取得格納出来なかった場合は、正規表現部分を都度変更して下さい。

import re
from bs4 import BeautifulSoup
import pandas as pd

#
# 中略
#

# ソースコードを取得
html = driver.page_source

# HTMLをパースする
soup = BeautifulSoup(html, 'lxml') # または、'html.parser'

selector = '{{ tableのCSSセレクタ }}' + ' tr'
tr = soup.select(selector)

pattern1 = r'<t[h|d].*?>.*?</t[h|d]>'     # tdまたはｔｈタグに囲まれた要素を検索
pattern2 = r'''<(".*?"|'.*?'|[^'"])*?>''' # htmlタグを検索

# 1行目をDataFrameのヘッダーにする
columns = [re.sub(pattern2, '', s) for s in re.findall(pattern1, str(tr[0]))]

# ２行目以降をDataFrameのデータにする
data = [[re.sub(pattern2, '', s) for s in re.findall(pattern1, str(tr[i]))] for i in range(1, len(tr))]

# DataFrameを作成する
df = pd.DataFrame(data=data, columns=columns)


ファイルの保存場所を変更する

# ファイルのデフォルトの保存先を変更する
driver.command_executor._commands['send_command'] = (
    'POST',
    '/session/$sessionId/chromium/send_command'
)
params = {
    'cmd': 'Page.setDownloadBehavior', 
    'params': {
        'behavior': 'allow',
        'downloadPath': '{{ ファイルの保存先(絶対または相対パス) }}'
    }
}
driver.execute('send_command', params=params)

ファイルのダウンロード先のフォルダをリセットしたい場合

import os, shutil

FILE_DOWNLOAD_DIR = '{{ ファイルの保存先(絶対または相対パス) }}'

# ダウンロード専用フォルダをリセットする
shutil.rmtree(FILE_DOWNLOAD_DIR)
os.makedirs(FILE_DOWNLOAD_DIR, exist_ok=True)


display:none;で隠された要素を表示する

driver.execute_scriptメソッドでJavaScriptを実行し、
CSSプロパティのdisplay:none;を削除します。

# display:none;で隠された要素を表示する
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
driver.execute_script('arguments[0].style.display="";', element)


BASIC認証を突破する

# BASIC認証のID、PWとURLをセットする
ID = '{{ ID }}'
PW = '{{ PASSWORD }}'
URL = '{{ URL }}'

# BASIC認証用のURLを定義
url = '{}:{}@{}'.format(ID, PW, URL)

# BASIC認証を突破する
driver.get(url)
"""

"""
【おまけ】Seleniumの雛形

記事の最後に、普段私がSeleniumのプログラムで使っているプロトタイプを紹介します。

import os, shutil, re, json
from glob import glob
import time
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Jupyter Notebookで全カラムを表示させる
pd.set_option('display.max_columns', None)



"""
初期設定
"""
#
# 定数定義
#
DRIVER_PATH = '{{ ローカルに保存したchromeドライバーのパス }}'
# DRIVER_PATH = '/app/.chromedriver/bin/chromedriver' # Heroku
FILE_DOWNLOAD_DIR = '{{ ファイルをダウンロードするダウンロード先のディレクトリ }}'

# 環境変数を使う場合(例：Slackに投稿する)
SLACK_ACCESS_TOKEN = os.environ['{{ 環境変数 }}']
CHANNEL_ID = '{{ チャンネルID }}'


#
# Seleniumをあらゆる環境で起動させるオプション
#
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す


#
# Chromeドライバーの起動とオプション
#
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

# 要素が見つからないときの暗黙的な待機処理
driver.implicitly_wait(10)

# ファイルのデフォルトの保存先を変更する
driver.command_executor._commands['send_command'] = (
    'POST',
    '/session/$sessionId/chromium/send_command'
)
params = {
    'cmd': 'Page.setDownloadBehavior', 
    'params': {
        'behavior': 'allow',
        'downloadPath': FILE_DOWNLOAD_DIR
    }
}
driver.execute('send_command', params=params)


#
# ダウンロード専用フォルダをリセットする
#
shutil.rmtree(FILE_DOWNLOAD_DIR)
os.makedirs(FILE_DOWNLOAD_DIR, exist_ok=True)



"""
クローリング/スクレイピング
"""
# Googleにアクセスする
url = '{{ URL }}'
driver.get(url)

# 処理1(テキストの入力)
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
element.send_keys('{{ 入力するテキスト }}')

# 処理2(クリック)
selector = '{{ CSSセレクタ }}'
element = driver.find_element_by_css_selector(selector)
element.click()

# ︙

# ブラウザを終了する(全てのウィンドウを閉じる）
# Chromeのショートカットキー(Command+Q)と同じ動作
driver.quit()

# ︙



"""
Slackに投稿する
"""
url = 'https://slack.com/api/chat.postMessage'
params = {
    'token': SLACK_ACCESS_TOKEN,
    'channel': CHANNEL_ID,
    'text': '{{ 投稿するテキスト }}',
    'username': '{{ Botの名前 }}',
    'icon_emoji': '{{ Botのアイコン }}',
}
response = requests.post(url, params=params)
data = response.json()
"""
