#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- while文 ---")


print("--- while文 ---")


"""
Pythonはループ処理のためにwhile文が用意されています。
while文はfor文と異なりループ中の条件式の結果に応じて
続行するか否かを制御することができます。

while文の基本
以下の書き方となります。

while文
while 条件式:
    ループ内処理

まずは簡単なサンプルを紹介します。
以下のコードではループ内で変数numに1ずつ加算しています。
変数numが10より小さい場合、ループ処理が継続され、
10を超えるとループ処理が終了します。
"""

num = 0
while num < 10:
	num = num + 1
	print(num)

print("numの値:", num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# numの値: 10

"""
もう1つサンプルで使い方を見てみましょう。
以下のサンプルは、endとキー入力するまでキー入力を要求し続けます。
（input関数はキー入力値を返す関数です）
"""

loop_flg = True     # ループ処理を続行するかどうかのフラグ

while loop_flg:
	print('キーを入力して下さい')
	c = input()

	if c == 'end':
		loop_flg = False

	print(c + 'が入力されました')


print("--- break ---")


"""
for文と同様、breakを使用することができます。
ループを強制終了することができます。
以下のサンプルではループ中でendを入力した場合、
breakが呼び出され即ループ処理を終了します。
なお、whileの後ろの条件式は常にTrueであるため、
breakしない限りループし続けます。
"""

while True:
	print('キーを入力して下さい')
	c = input()

	if c == 'end':
		break

	print(c + 'が入力されました')


print("--- while-else ---")


"""
for文と同様にwhile文に対してelseを使用することができます。
for文と同様に、breakしない場合はループ内の処理回数によらず
elseブロック内部の処理は必ず実行されます。
以下のサンプルでは、endもしくはbreakと入力するまでループ処理が実行されます。
break以外の場合は必ずelse内部が実行されることが確認できます。
"""

loop_flg = True    # ループ処理を続行するかどうかのフラグ

while loop_flg:
	print('キーを入力して下さい')
	c = input()

	if c == 'end':
		# ループ処理のフラグをOFFにする
		loop_flg = False
	elif c == 'break':
		# ループ処理をbreakで抜ける
		break

	print(c + 'が入力されました')

else:
	print('処理を終了します')


print("--- continue ---")


"""
こちらもfor文と同様、continueを使用すると
その回の後続処理をスキップすることができます。
以下のサンプルではキー入力値をprint出力していますが、
入力値がskipの場合、処理をスキップしています。
"""

loop_flg = True    # ループ処理を続行するかどうかのフラグ

while loop_flg:
	print('キーを入力して下さい')
	c = input()

	if c == 'end':
		loop_flg = False
	elif c == 'break':
		print('処理をスキップします')
		continue

	print(c + 'が入力されました')
