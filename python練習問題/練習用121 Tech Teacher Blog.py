#!/usr/bin/python
# -*- coding: UTF-8 -*-


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


print("--- Tech Teacher Blog ---")
print("--- 効率化を図ろう！PythonのGUIライブラリ比較や具体例を紹介！ ---")


"""
プログラミングの勉強をしていると「GUIアプリケーション」「GUIライブラリ」など「GUI」
という言葉を聞いたことがあるのではないでしょうか。
「GUIって何？」「GUIを使うと何ができるの？」という疑問を抱いている方もいるでしょう。
そこで今回は、GUIとは何か、どのような特徴があって何ができるのかといった基本的なことから、
実践方法まで詳しく説明します。
"""


print("--- GUIとは？ ---")


"""
GUIとは「Graphical User Interface」の略称です。
その名の通り「ユーザーが視覚的に操作できるインターフェース」を指します。
実は普段行っている「ファイルをダブルクリックで開く」「ウィンドウを開いて操作する」
といった操作はすべて「GUI」を使っています。
このようにGUIを使って操作できるアプリケーションのことを「GUIアプリケーション」、
GUIアプリケーションを開発するためのライブラリを「GUIライブラリ」と呼びます。
GUIを使うことで、文字だけでなくアイコンなどの画像で操作対象を分かりやすくしたり、
マウスで直感的に操作したりできるようになります。
コンピュータの操作に慣れていない人でもGUIアプリケーションであれば簡単に操作できますよね。
"""


print("--- おすすめのGUIライブラリ5選 ---")


"""
ここからは、Pythonで使えるGUIライブラリを5種類紹介していきます。

    Tkinter
    Kivy
    PyQt
    wxPython
    PySide

それぞれ、どのような特徴があるのか説明していきますね。


Tkinter

「Tkinter」はPythonに標準搭載されているライブラリです。
1988年に登場したスクリプト言語「Tcl」を使ってGUI開発を行うためのツールキットに
「Tk」というものがあります。これを指して「Tcl/Tk」と呼びますが、
TkinterはPythonでTcl/Tkを扱うためのライブラリとなっています。
標準搭載されているために環境構築がいらないのは楽ですが、
機能面で物足りなさを感じている開発者も多く、
外部のGUIライブラリを利用する人が多くなっています。

【Tkinterの特徴】

    Pythonに標準搭載
    GUIライブラリTcl/TkのPythonバージョン
    作成したGUIアプリはクロスプラットフォームで動作可能


Kivy

「Kivy」はWindows・Mac・iOS・Androidなど、どんな環境でも動作するGUIライブラリです。
また、マウス・キーボード・マルチタッチなど多彩な入力に対応しているGUIライブラリですよ。
様々なOS間で外観を統一することができ、特にゲームに強みがあるライブラリとなっています。

【Kivyの特徴】

    TkinterよりクロスプラットフォームなGUIアプリを作成可能
    ゲームやアプリも制作可能
    OpenGL使用


PyQt

C++言語で記述された「Qt」というGUIツールキットをPythonで扱えるようにしたものが「PyQt」です。

C++言語の知識がなくてもPythonの文法でGUI作成でき、GUIデザインを美しく制作しやすいことから、
多くのソフトが制作されていますよ。

【PyQtの特徴】

    設計がモダンでデザイン面のメリットが豊富
    商用利用するにはロイヤリティが発生


wxPython

C++言語で記述されたクロスプラットフォームGUIツールキット
「wxWidgets」のPythonバージョンが「wxPython」です。
多数の言語で利用できるようになっていますが、こちらを利用するにはPython3が必要です。
wxPythonは安定した動作に定評があり、ライブラリが充実していることから、
少し手間のかかったものを制作するのにも最適ですよ。

【wxPythonの特徴】

    機能が充実している
    商用利用ができる


PySide

「PySide」はPyQtと同様にQtをベースとしたクロスプラットフォームのGUI作成のための
Pythonライブラリです。
PyQtの方が利便性が高いと言われていますが、PySideは商用利用が可能になっています。
そのため、用途によってどちらを利用するか選択しましょう。

【PySideの特徴】

    クロスプラットフォームに対応したアプリ開発可能
    Qtベース
"""


print("--- GUIライブラリを使用したアプリ作成 ---")


"""
ここからは、どのような環境でも動作する「Kivy」
を使ったアプリケーション作成について説明していきます。


インストール

まずKivyのパッケージをインストールしましょう。
pipでインストールする場合、最初に「pip install –upgrade pip」
を実行してpipをアップデートします。
その後、次のコマンドを実行してKivyをインストールします。

1.　pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
2.　pip install kivy.deps.gstreamer
3.　pip install kivy.deps.angle
4.　pip install kivy

これでKivyのインストールは完了です。

万が一動かない場合には「Pygame」や「Cython」をインストールすると解決しますよ。


三目並べの作成

ここからはKivyを利用して「三目並べ」を作成してみましょう。
"""

# from kivy.appimport App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix button import Button


SYMBOLS = ("×", "○")


def symbol_generator():
	while True:
		for symbol in SYMBOLS:
			yield symbols


class Board(GridLayout):
	grid = None
	symbols = None


def __init__(self, **kwags):
	super(Board, self).__init__(**kwargs)

	self.cols = 3
	self.rows = 3
	self.symbols = symbols_generator()

	self.grid = [[None for cla in range(self.cols)] for row in rande(self.rows)]

	self.draw_tiles()


def draw_tiles(self):
	"""
	Adds all tiles to the GridLayout - Board
	"""
	for row in range(self.rows):
		for col in range(self.cols):
			tile = Button()
			tile.grid(on_press=self.on_pressd)
			self.grid[row][col] = tile
			self.add_widget(tile)


def on_pressd(self, instance):
	"""
	Handles a click on a tile
	"""
	# 取得済みの場合
	if instance.text:
		return None

		# 利用可能の場合
		instance.text = next(self.symbols)
		instance.text = next(self.symbols_next_())
		instance.font_size = 100

		self.is_finished()


def is_finished(self):
	"""
	"○": "○" wins
	"×": "×" wins
	"引き分け": drow
	None: on going
	"""
	winner = self.get_winner()

	if winner:
		content = BoxLayout(orientation="vertical")
		if winner == "引き分け":
			content.add_widget(label(text="Draw"))
	else:
		contenr.add_widget(Label(text="%s あなたの勝ちです！" % winner))
		close_button = Button(text - "Close")
		content.add_widget(close_button)

		popup = popup(title="ゲーム終了", contenr=content, auto_dismiss=False)
		popup.open()
		# popup(title="ゲーム終了", content=content, auto_dismiss=False).open()

		close_button.bind(on_release=popup.dismiss)

		self.restart_board


def get_winner(self):
	"""
	Return winner symbol, "引き分け", or None
	"""
	# 勝ちパターン
	winning_lines = (
		((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2))
		((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))
		((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 2))
	)
	for line in winning_lines:
		row = []
		for cell in line:
			row, append(self.grid[cell[0]][cell[1]].text)

	for symbol in SYMBOLS:
		if all([s == symbol for s in row]):
			return symbol

	# ゲーム進行中
	for row in self.grid:
		for col in row:
			if col.text == " ":
				return None

	# 引き分け
	return "引き分け"


def restart_board(self):
	# クリアボード
	for row in self.grid:
		for col in row:
			col.text = " "

	# 初期化
	if next(self.symbols) == "○":
		return
	else:
		next(self.symbols)
		return

"""
上記のコードを実行すると、三目並べを作成することができます。
"""


print("--- まとめ ---")


"""
今回、GUIライブラリの基本的な知識や5種類のGUIライブラリ比較、
実践方法まで説明してきましたがいかがでしたでしょうか。

今回の要点をまとめると以下のようになります。

    GUIとは直感的に操作可能なUIのこと
    TkinterはPythonに標準搭載されているGUIライブラリ
    KivyはOS問わずに操作するオープンソースのライブラリ
    PyQtはQtのPythonバージョン
    wxPythonはwxWidgetsのPythonバージョン
    PySideはQtベースのGUIライブラリ

GUIは視覚的に使用できるため初心者でも比較的簡単に利用できるでしょう。
ぜひ積極的にGUIライブラリを活用してプログラミングを効率化してみてください。
"""
