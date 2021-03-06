#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- 初めてのプログラミング編 Pythonとは？---")


"""
Pythonとは

　Pythonとは近年人気が高まっているプログラミング言語の1つです。
高度な科学技術計算や機械学習などに向いている一方、
スクリプト言語の一種でコンパイルせずにすぐに動かすことができるため、
プログラミング未経験の方にも比較的優しい言語です。

Pythonで何ができる？

　Pythonでできること、と見出しを打ちましたができないことのほうが少ないのかもしれません。
身近な例を挙げると以下のような便利ツールを自分で作れるようになります。
仕事の効率化や趣味、研究に活用できそうですね。

    インターネット上からのデータの自動収集
    ブラウザの自動操作
    PCの自動操作
    LineやTwitterのチャットボット
    データの可視化
    画像処理

趣味から離れた高度な分野だと、データのバッチ処理、Webアプリケーションといった業務系処理や、
統計分析、機械学習といった科学技術計算でも広く使用されています。


バッチ処理

　データを一括で更新したり抽出するような処理をバッチ処理と呼びます。
複雑な計算もPythonだとシンプルに記述することができ、
また、リレーショナルデータベースやExcel、CSVといったデータ連携ライブラリが数多く提供されているため、
Pythonを使用すると業務や分析向けのバッチをすばやく実装することが可能です。


ウェブアプリケーション

　我々が日々使用するSNSやニュースサイト等のウェブサービスはウェブアプリケーションと呼ばれる
アプリケーションがサーバーで動作してサービスを提供しています。
Pythonでウェブサービスを作ることも可能です。
Pythonが使用されている有名なサービスにInstagram、DropBoxなどが挙げられます。


科学技術計算

　Pythonの最大のメリットの1つが、統計計算を始めとした科学技術演算のライブラリが充実している点が
挙げられます。このため、近年注目を集めている機械学習には外せない言語となっています。
また、統計計算ライブラリも充実しているため、業務データの分析や可視化にも大活躍します。

Pythonのメリット

　Pythonのメリットとして挙げられるのが、上にも書いたとおり難しい処理のライブラリが
非常に充実しているという点です。このため、何か実装する場合、
既存のコードをつなぎ合わせるだけで複雑なプログラムを短期間で作ることが可能となります。

また、プラットホームを選ばないというメリットも有ります。
一部例外はありますが、例えばWindowsで記述したコードをMacやLinuxで動かすことが可能です。

Pythonのデメリット

　Pythonのデメリットとして、実行速度は速くない、という点が挙げられます。
ただし、これはスクリプト言語全般に当てはまることでしょう。

　また、Pythonは動的型付け言語と呼ばれる種類の言語で、
さらに、スコープが曖昧、(ほぼ)どこからでもコードの書き換えが可能、
といった「ゆるい」特徴があります。
このため、様々なレベルの大勢のエンジニアが参加する大規模な業務システムの開発で
使用する場合はかなりの注意を要します。

初心者向けの学習方法

　初めてのプログラミング編ではプログラミング未経験者向けに解説を進めます。
私がおすすめする学習方法はとにかくサンプルをたくさん動かす、ということです。

細かい用語や動作原理を学習することはもちろん大切ですが、
むしろそういったことを学習する前にある程度慣れておくとその後の学習がスムーズになります。
"""


print("--- 初めてのプログラミング編 Pythonスクリプトを動かしてみよう---")


"""
インストールと実行

Windowsをお使いの方はこちらのページを参考にPythonをインストールしてください。
Macの場合はXcodeをインストールすると同梱されてインストールされます。
以降、Windows向けに説明しますが、Macをお使いの方は適宜読み替えてください。

Pythonスクリプトの作成

インストールが終わったら適当な名前で作業用のディレクトリを作成し、
そこにメモ帳で「sample.py」というテキストファイルを作成してください。
テキストファイルの中身には以下の1行を記入します。
"""

print("Hello World!")

"""
Pythonはこのようなテキストファイルにプログラムを書き実行しますが、
このような拡張子が.pyとなるテキストファイルをPythonスクリプトと呼びます。
"""

"""
Pythonスクリプトの実行

それではいよいよPythonを実行してみましょう。
まず、コマンドプロンプトかWindows PowerShellを起動し、
さきほど作成した作業用ディレクトリに移動してください。
例えば、c:\pyworkというディレクトリに移動する場合、以下のようにコマンドを実行します。

cd C:\pywork\ 

次に、pythonコマンドでpythonスクリプトを実行します。
pythonの後ろに先ほど作成したPythonスクリプト、sample.pyを指定します。

python sample.py

いかがでしょうか？「Hello, World!」という文字列が出力されると成功です。
先ほど作成したPythonスクリプトは「print関数」と呼ばれるもので、
クォーテーションで囲んだ文字列を表示します。

なお、メモ帳のようにコードを書くアプリケーションのことをエディタと呼びます。
また、PowerShellのようなコマンドラインを実行するアプリケーションのことをターミナルと呼びます。
最初のうちは以下のようにエディタとターミナルを並べて実行するとはかどるかと思います。

また、文字列が表示されましたがこれを「出力される」と呼ぶ場合があります。
"""

"""
補足2 対話モード

Pythonにはスクリプトを実行する以外に対話モードと呼ばれる実行方法があります。
これはスクリプトを作成せずにコマンドライン上で対話的にPythonを実行できる機能で、
非常に便利なPythonの機能の1つです。
ただし、最初のうちはどこから実行したのか混乱する場合が多いため、
当講座では終盤までスクリプトを作成して実行する方法で解説します。

演習

それでは、演習です。たくさんコードを書いて実行することはプログラミング上達のコツの1つです。
演習1

　以下のように「こんにちは」というテキストを出力させるスクリプトを作成してみてください。

こんにちは。

演習1解答例

さきほどのprintの中に適当な文字列を設定することができます。
ただし、次回以降に説明しますが一部の文字列は指定することができません。
"""

print("こんにちは～。")

"""
演習2

以下のように3行の自己紹介のテキストを出力させるスクリプトを作成してみてください。

こんにちは。
私の名前は鈴木です。
Pythonが趣味です。
"""

print("こんにちは")
print("私の名前は鈴木です。")
print("Pythonが趣味です。")

"""
演習2解答例

さきほどのprintを追加していくらでも出力を追加することができます。

print("こんにちは。")
print("私の名前は鈴木です。")
print("Pythonが趣味です。")

上の演習以外にもいろいろな文字列を出力して遊んでみてください。
"""


print("--- 初めてのプログラミング編 変数を使って計算してみよう---")


"""
変数とは？

　プログラミングでは基本的に、数字や文字と言ったデータは変数というものを介して使用します。
最初のうちはデータを格納するメモリ上の空間の箱に変数というラベルが付いている状態をイメージすると
わかりやすいかもしれません。

例えば、箱に入った2つの数字2、3を足した結果を別の箱に入れる場合、次のようなイメージとなります。

こういったイメージから「変数にデータを格納する」と表現したりもします。
プログラミング初心者にとって非常にややこしいのですが、
変数の意味合いは文脈によって微妙に異なり、箱を指す場合とラベルを指す場合、
その両方を指す場合があります。ともかく今はデータを格納する場所だと思っていて差し支えありません。

　変数を使用するには様々な決まりがあるのですが、
プログラミング基礎編では細かい説明は避け、いくつかの例で感覚を掴んでいただきたいと思います。
というわけで早速コードを書いてみましょう。
適当な名前で以下内容のPythonスクリプトを作成して実行してみてください。
"""

a = 2
b = 3
c = a + b
print(c)

"""
最初の2行は変数aに2が、変数bに3が設定されていることを示しています。
この変数に=で値を設定することを代入と呼ぶ場合があります。
「変数aに2を代入、変数bに3を代入する」などと言います。
3行目で2数の合計を計算し、変数cに設定します。
また前回学習したprint関数は文字列だけではなく変数の内容を表示することもでき、
4行目でcの内容を確認しています。

上のコードですが、以下のように変数a、bを使用せずに、変数cに直接計算結果を代入することもできます。
"""

c = 2 + 3
print(c)


"""
さまざまな計算をしてみよう

　それでは練習として変数同士で足し算以外の計算をしてみましょう。
+、-、*、/演算子でそれぞれ足し算、引き算、かけ算、割り算ができます。
以下のサンプルでは、変数a、bの四則演算を行い、結果をprint出力しています。
"""

a = 6
b = 3

c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b

print(c1)
print(c2)
print(c3)
print(c4)


"""
演習

　演習です。
演習1

　変数xに100を、変数yに200を、変数zに300を代入し、
和を適当な変数に代入してprint関数で出力してください。

演習1解答例

　変数が3つ出てきましたが、上のサンプルとほぼ同様です。
"""

x = 100
y = 200
z = 300
w = x + y + z
print(w)

"""
演習2

　変数xに100を、変数yに200を代入し、
それらを2倍したの結果を適当な変数に代入してprint関数で出力してください。
"""

x = 100
y = 200
w = (x + y) * 2
print(w)

"""
演習2解答例

　今度は整数とのかけ算がでてきました。かけ算は*を使用します。
かけ算の前に足し算をしますがその場合は括弧を使用します。
また、変数と普通の数値を演算することができます。
"""


print("--- 初めてのプログラミング編 文字列を使ってみよう---")


"""
文字列

　変数には前回解説した整数以外に文字列を格納することができます。
整数を格納した変数をint型、文字列を格納した変数をstr型と呼びます。
整数や文字列など、格納されているデータの種類ごとに「型」というものが定められているわけです。

細かい説明はさておき、まずはコードを書いてみましょう。
"""

text1 = 'こんにちは、'
text2 = '今日はいい天気ですね'

print(text1)
print(text2)

"""
実行すると以下のように文字列が出力されます。

こんにちは、
今日はいい天気ですね

ダブルクォートで囲んだ文字列はstr型として扱われ、変数に代入することができます。
上のコードでは、2つの変数text1、text2に対しそれぞれ「こんにちは」「今日はいい天気ですね」
というstr型を代入しています。その後print関数で文字列を出力しています。
また、ダブルクォートの代わりにシングルクォートを使用することもできます。


文字列をつなげてみる

　次に、複数の文字列をつなげてみましょう。+記号で文字列と文字列をつなげることができます。
"""

text1 = 'こんにちは、'
text2 = '今日はいい天気ですね'
text3 = text1 + text2
print(text3)

"""
実行すると以下のように文字列が出力されます。

こんにちは、今日はいい天気ですね

変数text1、text2を連結した結果を、変数text3に代入しています。
int型の場合は足し算になりましたが、文字列の場合はこのように連結されたことが確認できます。

ちなみに、変数に代入せずにそのままprint関数で出力することもできます。
上のコードは以下のように書き換えることもできます。
"""

text1 = 'こんにちは、'
text2 = '今日はいい天気ですね'

print(text1 + text2)

"""
また、変数に格納せずに文字列を直接つなげることもできます。以下のように書き換えることもできます。
"""

text = 'こんにちは、' + '今日はいい天気ですね'
print(text)

"""
さらに、+記号の連結はいくつでもできます。ページ下部の演習で試してみましょう。
"""


"""
文字列と数字をつなげてみる

　print関数で文字列と数字を同時に出力したくなる場合がありますが、
文字列と数字を直接+でつなげることはできません。
例えば、何かの回数を表示させたい場合、以下のようなコードはエラーが発生します。

count = 18
text = "回数:" + count 
print(text)

こういった場合、以下のコードのようにstrで数字を一旦文字列に変換することにより
つなげることが可能となります。
"""

count = 18
text = '回数' + str(count)
print(text)

"""
strはこれまで使用してきたprintと同じく「関数」と呼ばれるものなのですが、
これについてはまた別途説明します。今はstrで「変数を文字列に変えられる」と思ってください。
"""


"""
演習

　それでは演習です。
演習1

　以下の変数を定義し、順に連結してprint関数で出力してください。

    text1："こんばんは、"
    text2："いい夜ですね。"
    text3："今日の夕食はなんですか？"
"""

text1 = 'こんばんは、'
text2 = 'いい夜ですね。'
text3 = '今日の夕食は何ですか？'
text4 = text1 + text2 + text3
print(text4)

"""
演習2

　以下の変数を定義し、順に連結してprint関数で出力してください。

    text1："私の年齢は"
    age：22
    text2："歳です。"
"""

text1 = '私の年齢は'
age = 22
text2 = '歳です。'
text3 = text1 + str(age) + text2
print(text3)

"""
演習2解答例

　今度は文字列と整数の結合です。strで文字列に変換します。

text1 = "私の年齢は"
age = 22
text2 = "歳です。"

text3 = text1 + str(age) + text2
print(text3)
"""
