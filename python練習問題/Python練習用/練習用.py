#!/usr/bin/python
# -*- coding: Shift-JIS -*-
# Magic comment


import calendar
import math
import matplotlib.pyplot as plt


print(1 + 1) 
1 + 1

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()


plt.show()

print(100 * 55 + 40 * 8)
print((100 * 5) + (40 * 8))
print(10 * 20)
print(5 % 3)
print(10 % 2)
print(-100)
print(100 + -99)
print(100 + (-99))
print(10 ** 3)


# ����(float�^)
0.1
100.0

# ������float�^
(10 + 20)
(10 + 10.0)
(2 / 3)
(3 / 3)

# �������Z
(3 / 2)
(3 // 2)
(3.0 // 2.0)
print((100 * 5) + (40 * 8) + (80 * 5) + (60 * 10) + (90 * 20) + (110 * 10))

# �ϐ��Ƒ����
variable = 50
print(50 + 1)
variable = 50
print(variable + 1)
momo = 100 * 5
mikan = 40 * 8
nashi = 80 * 5
kiwi = 60 * 10
suika = 90 * 20
kaki = 110 * 10
goukei = momo + mikan + nashi + kiwi + suika + kaki
print(goukei)

# �ϐ���
variable = 1
variable_123 = 1
# 123_variable �� NG (�����Ŏn�܂��Ă���)
# vari��able �� NG (�L���͕ϐ����Ƃ��Ďg���Ȃ�)
# raise �� NG (�uraise�v�Ƃ����P���python�œ��ʂȈӖ������̂Ŏg���Ȃ�)
print(1 + 2) # �����̓R�����g
# ���̍s�͂܂�܂�R�����g�ł�

# ����
abs(-200)

# �߂�l

# �֐��Ɖ��Z�q
a = abs(100 + 200) / 2   # 150.0
print(a)

# �֐��ƕϐ�
minus_value = 100 * -1
abs(minus_value)    # 100

abs(100 * -1)    # 100 * -1 = -100

abs_value = abs(10)    # 20
print(abs_value * 2)    # abs(10) * 2 �Ɠ��� 20

# �֐��̗�
# abs()�֐�
abs(100)    # 100

abs(100 * -1)    # -100

# round()�֐�
# round(���l, �L������)
round(1.12, 1)    # 1.1

# mini()�֐���max()�֐�
min(10, 20, 5, 30)    # 5
min(4, 8, 2, 20, 5, 6, 2, 9)    # 2
max(10, 20, 5, 30)    # 30

# import��
# import ���W���[����
# import math    # math���W���[�����g�p����
# ���W���[����.�֐���()
# import math
math.sqrt(2.0)

# import calendar    # calendar���W���[�����g�p����
calendar.prmonth(2020, 12)    # 2020�N��12���̃J�����_�[��\������


# ������
print(123)
print(456)
print("Python Programming!")
print('Python Programming!')


# �����Ɛ����̈Ⴂ
print(123 * 456)    # 56088
# "123" * "456"    # �G���[


# print�֐�
print(42)    # 42
print(1, 2, 3)    # 1 2 3

# �������print()�֐�
print("����5�ƁA�݂���8��", 100 * 5 + 40 * 8, "�~�ɂȂ�܂��B")
# ����5�ƁA�݂���8��820�~�ɂȂ�܂��B


# input()�֐�
input("�D���ȕ�������͂��Ă�������")
string = input("���������͂��Ă�������:")
print("������", string, "�����͂���܂����B")


# ������̉��Z�q�Ɛ��l
print(123 + 456)
print("123" + "456")
# 123 + "456"    ���l�ƕ�����𑫂��ƃG���[�ɂȂ�A���Z���邱�Ƃ͂ł��Ȃ��B

# ������̐��l��
text = "123"
print(int(text))

text1 = "123"
text2 = "456"
print(text1, "��", text2, "�𑫂���", int(text1) + int(text2), "�ɂȂ�܂��B")

text = "123.4"
float(text)
# int("Hello")    ���l�ȊO�̕����́A���l�ɂ͂ł��Ȃ��B�G���[�ɂȂ�B

# ���l�̕�����
num = 123
str(num)    # "123"
height = 172    # height��172��������
print("���̐g����" + str(height) + "cm�ł��B")


# ���]�b�g
text = "Lower Letters"     # �ϐ�text�ɕ�����"Lower Letters"����
uppered_text = text.upper()    # upper()���]�b�g�ő啶�����쐬
print(uppered_text)    # LOWER LETTERS
# ���]�b�g�̌Ăяo�����@�f�[�^.���]�b�g��(����1, ����2, ����3....)

# �������find���]�b�g
text = "The shells she sells are sea-shells, I'm sure."
text.find("sea")    # 25

# ���]�b�g�Ɗ֐�
# ���]�b�g�ƃf�[�^
# data = 10000
# data.upper()    �G���[ �����ɑ啶�������������Ȃ�

data = 0.5
data.as_integer_ratio()    # (1, 2)

# data = "abracadabra"
# data.as_integer_ratio()    # ���l�f�[�^��p���]�b�g�ŁA������f�[�^���g�����Ƃ���ƃG���[�ɂȂ�

# ���K���
text = input("�������͂��ĉ������B")    # �ϐ�text�ɕ��������
lower_text = text.lower()    # ���͂�����������������ɕϊ�
print(text, "���������ɕϊ������", lower_text, "�ɂȂ�܂��B")


# ��r���Z�q
100 > 10    # True
10 > 100    # False
10 < 100    # True�@10��100��菬����
100 < 100    # False�@100��100�ȏ�
10 <= 100    # True �@10��100
100 <= 100    # True�@100��100�Ɠ�����
100 == 100    # True�@100��100�Ɠ�����
99 == 100    # False  99��100�͓������Ȃ�
99 != 100     # True  99��100�͓������Ȃ�
100 != 100    # False  100��100�Ɠ�����

# ������̔�r
"123" < "456"     # True
"python" < "Python"    # True
"Python-1" < "Pthon-a"    # True


# if���ɂ���������
a = 100    # �ϐ�a��100��ݒ肷��

if a == 100:    # a��100�Ɠ�������΁Aprint()�֐������s����
	print("100�_���_�I")

# if���̏�����
"""if a == 100:
    ����1
    ����2
    ����3
^^^^
�X�y�[�X��4��������
"""

# ��������False�ƂȂ�ꍇ
a = 99    # �ϐ�a��99��ݒ肷��

if a == 100:    # a��100�Ɠ�������΁Aprint�֐������s
	print("100�_���_�I")

# else��
"""
if ������:
	����1
	����2
	�E�E�E
else:
	����3
	����4
	�E�E�E
"""

a = 100    # �ϐ�a��100��ݒ肷��

if a == 100:    # a��100�Ɠ�������΁Aprint()�֐������s
	print("100�_���_�I")
else:
	print("���i�I")


a == 0
if a == 100:
	print("100�_���_�I")
else:
	print("���i�I")


# ��r�ȊO�̏�����
print("123�͐����ł����H", "123".isdecimal())
print("abc�͐����ł����H", "abc".isdecimal())


string = input("���������͂��ĉ������B:")
if string.isdecimal():
	print(string, "�͐����ł��B")
else:
	print(string, "�͐����ł͂���܂���B")


# elif��
print("123�̓A���t�@�x�b�g�ł����H", "123".isalpha())
print("abc�̓A���t�@�x�b�g�ł����H", "abc".isalpha())
# isalpha()���]�b�g�̓A���t�@�x�b�g�����łȂ��A�Ђ炪�Ȃ�J�^�J�i���A���t�@�x�b�g�Ƃ��Ĕ��肷��B


"""
if ������1:
	����1
	�E�E�E
elif ������2:
	����2
	�E�E�E
elif ������3:
	����3
	�E�E�E
else:
	����n
	�E�E�E
"""


string = input("��������͂��ĉ������B:")

if string.isdecimal():
	print(string, "�͐����ł��B")
elif string.isalpha():
	print(string, "�̓A���t�@�x�b�g�ł��B")
# isalpha()���]�b�g�̓A���t�@�x�b�g�����łȂ��A�Ђ炪�Ȃ�J�^�J�i���A���t�@�x�b�g�Ƃ��Ĕ��肷��B
else:
	print(string, "�͐����ł��A���t�@�x�b�g�ł�����܂���B")


# �u�[���^�Ƙ_�����Z�q
print(1 > 2)
print("abc" == "abc")

true_value = True
print("true_value ��", true_value)

false_value = False
print("false_value ��", false_value)


# and���Z�q
age = 11    # ��Ƃ��āA11�� �g��130cm�Ƃ���
height = 130

if (10 <= age) and (120 <= height):
	print("����肢�������܂�")
else:
	print("���������������B")


age = 11    # ��Ƃ��āA11�� �g��110cm�Ƃ���
height = 110    # ���̍s��130����110cm�ɕύX

if (10 <= age) and (120 <= height):
	print("����肢�������܂�")
else:
	print("���������������B")


# �_����
# or���Z�q
age = int(input("�N�����͂��ĉ������B:"))    # �N���90�΂Ƃ���

if (age <= 10) or (80 <= age):
	print("10�Έȉ��̕���80�Έȏ�̕��͂�������������")
else:
	print("����肢�������܂��B")


# �_���a
# C = A or B
# not���Z�q
# not (age < 10)
age = 20    # �N���20

if not (age < 10):
	print("����肢�������܂�")
