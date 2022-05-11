#!/usr/bin/python
# -*- coding: UTF-8 -*-


import random
import math
import tkinter

def calc_distance(x1,y1,x2,y2):
    #2点間の距離を求める
    diff_x = x1 -x2
    diff_y = y1 -y2
    return math.sqrt(diff_x**2 + diff_y**2)

def start():
    global suika_x
    global suika_y
    global suika_num
    global player_num
    global player_y
    global player_x
    global distance

    suika_x = random.randrange(0,5) #すいかのx座標
    suika_y = random.randrange(0,5) #すいかのy座標
    suika_num = suika_x * 6 + suika_y

    player_x = random.randrange(0,5) #プレイヤーのx座標
    player_y = random.randrange(0,5) #プレイヤーのy座標
    player_num = player_x * 6 + player_y

    distance = calc_distance(player_x,player_y,suika_x,suika_y)
    print(player_x,player_y,player_num)

def changeText_up():
    global player_num
    global player_y
    global player_x
    global distance
    global i_data

    i_data = "No."+str(player_num)

    if player_y > 0 and player_y <= 5 :
        label[player_num]['text'] = str(i_data)
        label[player_num]['relief'] = "ridge"

        player_y = player_y - 1
        player_num = player_x * 6 + player_y

        label[player_num]['text'] = str("T")
        label[player_num]['relief'] = "flat"

        distance = calc_distance(player_x,player_y,suika_x,suika_y)

    print(player_x,player_y,player_num,i_data)
    suika_label[0]['text']= str(format(distance,'.3f'))

    if distance == 0 :
        suika_label[2]['text']= str("すいかを割りました！！！")

def changeText_down():
    global player_num
    global player_y
    global player_x
    global distance
    global i_data

    i_data = "No."+str(player_num)

    if player_y >= 0 and player_y < 5 :
        label[player_num]['text'] = str(i_data)
        label[player_num]['relief'] = "ridge"

        player_y = player_y + 1
        player_num = player_x * 6 + player_y

        label[player_num]['text'] = str("T")
        label[player_num]['relief'] = "flat"

        distance = calc_distance(player_x,player_y,suika_x,suika_y)

    print(player_x,player_y,player_num,i_data)
    suika_label[0]['text']= str(format(distance,'.3f'))

    if distance == 0 :
        suika_label[2]['text']= str("すいかを割りました！！！")

def changeText_left():
    global player_num
    global player_y
    global player_x
    global distance
    global i_data

    i_data = "No."+str(player_num)

    if player_x > 0 and player_x <= 5 :
        label[player_num]['text'] = str(i_data)
        label[player_num]['relief'] = "ridge"

        player_x = player_x - 1
        player_num = player_x * 6 + player_y

        label[player_num]['text'] = str("T")
        label[player_num]['relief'] = "flat"

        distance = calc_distance(player_x,player_y,suika_x,suika_y)

    print(player_x,player_y,player_num,i_data)
    suika_label[0]['text']= str(format(distance,'.3f'))

    if distance == 0 :
        suika_label[2]['text']= str("すいかを割りました！！！")

def changeText_right():
    global player_num
    global player_y
    global player_x
    global distance
    global i_data

    i_data = "No."+str(player_num)

    if player_x >= 0 and player_x < 5 :
        label[player_num]['text'] = str(i_data)
        label[player_num]['relief'] = "ridge"

        player_x = player_x + 1
        player_num = player_x * 6 + player_y

        label[player_num]['text'] = str("T")
        label[player_num]['relief'] = "flat"

        distance = calc_distance(player_x,player_y,suika_x,suika_y)

    print(player_x,player_y,player_num,i_data)
    suika_label[0]['text']= str(format(distance,'.3f'))

    if distance == 0 :
        suika_label[2]['text']= str("すいかを割りました！！！")

start()

frame=[]
label=[]
suika_label=[]

#window
root = tkinter.Tk()
root.title("test_tk")
root.geometry("400x300")

#frame
i = 0
while i <= 5:
    frame.append(tkinter.Frame(root, width=100, height=100, background="white", cursor="mouse"))
    i=i+1

#label
j = 0
while j <= 35:
    if j <= 5:
        label.append(tkinter.Label(frame[0],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))
    elif j <= 11:
        label.append(tkinter.Label(frame[1],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))
    elif j <= 17:
        label.append(tkinter.Label(frame[2],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))
    elif j <= 23:
        label.append(tkinter.Label(frame[3],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))
    elif j <= 29:
        label.append(tkinter.Label(frame[4],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))
    elif j <= 35:
        label.append(tkinter.Label(frame[5],text="No."+str(j+1),width=5, height=2,relief="ridge",bg="white"))

    j=j+1

frame[0].pack(side=tkinter.LEFT,anchor=tkinter.N)
frame[1].pack(side=tkinter.LEFT,anchor=tkinter.N)
frame[2].pack(side=tkinter.LEFT,anchor=tkinter.N)
frame[3].pack(side=tkinter.LEFT,anchor=tkinter.N)
frame[4].pack(side=tkinter.LEFT,anchor=tkinter.N)
frame[5].pack(side=tkinter.LEFT,anchor=tkinter.N)

x = 0
while x <= 35:
    label[x].pack()
    x=x+1

suika_label.append(tkinter.Label(text=str(format(distance,'.3f'))))
suika_label[0].place(x=280,y=70)
suika_label.append(tkinter.Label(text="すいかまでの距離"))
suika_label[1].place(x=280,y=50)
suika_label.append(tkinter.Label(text="--------"))
suika_label[2].place(x=280,y=100)

#button
button1 = tkinter.Button(root,text="up",height=1,width=4,command=changeText_up)
button1.place(x=340,y=200)
button2 = tkinter.Button(root,text="down",height=1,width=4,command=changeText_down)
button2.place(x=340,y=260)
button3 = tkinter.Button(root,text="left",height=1,width=4,command=changeText_left)
button3.place(x=320,y=230)
button4 = tkinter.Button(root,text="right",height=1,width=4,command=changeText_right)
button4.place(x=360,y=230)

#frame[1].propagate(0)

root.mainloop()
