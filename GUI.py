#!/usr/bin/python3
from tkinter import filedialog
from tkinter.dialog import  *
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import *
from DB import *
import requests
#from gxy_db import all_songs

#root窗口

root=Tk()
root.geometry('600x300')
root.minsize(200,100)

def Upload():
    return""
    # print('upload')
    # selectFileName = filedialog.askopenfilename(title='选择文件')#选择文件
    #
    # r = requests.post('http://0.0.0.0:8080/upload', files={'file':open(selectFileName,'rb')})
    # print(r.content.decode('utf-8'))
    # setText = r.content.decode('utf-8')
    # print(setText.__class__)
    # E1.delete(0,END)
    # E1.insert(0,setText)
# def upload():
#     win=Tk()
#     win.wm_title("Upload Music")
#     label1=Label(win,text="Please select a music")
#     label1.grid(column=0,row=0)
#     entry1=Entry(win)
#     entry1.grid(column=0,row=1)
#     button1=Button(win,text="Select",command=askopenfilename)
#     button1.grid(column=1,row=1)
#     button2=Button(win,text="Okay")
#     button2.grid(column=0,row=4,sticky=W)
#     button3=Button(win,text="Cencel")
#     button3.grid(column=1,row=4,sticky=W)
#     win.mainloop()

def popupmenu(event):
    menu_right.post(event.x_root, event.y_root)

def Delete_Song():
    Song_Name=listbox_songs.get(listbox_songs.curselection())
    listbox_songs.delete(listbox_songs.curselection(),listbox_songs.curselection())
    Delete_Song_In_Db(Song_Name[0])

#定义窗口的title
root.wm_title("Music Collection Management System ")

#定义菜单
menu_bar=Menu(root)
menu_bar.add_command(label="All Songs")
menu_bar.add_command(label="My Song Lists")

# 定义按钮
E1 = Entry(root, width=50)
E1.grid(row=0, column=0,sticky=W)
button_upload=Button(root,text="Upload Music",command=Upload)
button_upload.grid(column=1,row=0,sticky=W)
# menu_musiclist=Menu(menu_bar)

#menu_musiclist.add_command(label="Upload Music",command=upload)
#menu_musiclist.add_command(label="Delete Music")
#menu_musiclist.add_command(label="Download Music")

#menu_bar.add_cascade(label="All Music",menu=menu_musiclist)
# menu_bar.add_cascade(label="My Music List")
# label_defaultlist=Label(root,text="Default List")
# label_defaultlist.pack()
listbox_songs=Listbox(root,width=60,height=25)
#listbox_songs.width(200)
Result=All_Songs()
for item in Result:
    listbox_songs.insert(END, item)


menu_right = Menu(root, tearoff=0)
menu_right.add_command(label="删除",command=Delete_Song)

listbox_songs.bind("<Button-3>", popupmenu)
listbox_songs.grid()

root['menu']=menu_bar


#button1=Button(root,text="My music",)
#button1.grid(column=0,row=0)
#button2=Button(root,text="Download")
#button2.grid(column=1,row=0)
#button1.pack()
#button2.pack()
#label1.pack()
root.mainloop()


