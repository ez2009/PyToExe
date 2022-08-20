#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import shutil
from tkinter import *
from tkinter import filedialog as fd
from easygui import msgbox
from ChooseFile_function import ChooseFile
from StartTurn_function import StartTurn

root = Tk()
root.minsize(400, 400)
root.title('python文件转exe')
file = "0"

def ChooseFile():
    global file
    file = fd.askopenfilename()
    lb = Label(root, text=file, font=("simhei", 30))
    lb.pack()
    lb.place(x=0, y=100)

def StartTurn():
    msgbox("开始打包，请耐心等待(点击 ok按钮开始)", "提示")
    if file != "0":
        run_file = os.getcwd()
        shutil.copy(file, run_file)
        basename = os.path.basename(file)
        name = "pyinstaller -F -w ", basename
        system = "".join(name)
        os.system(str(system))
        delete_filename = run_file + '\\' + os.path.basename(file)
        delete_file = ''.join(delete_filename)
        os.remove(delete_file)
        show_text = "打包完成！请到路径", run_file, "里的 dist文件夹查看，有导入素材的文件要把exe程序移动回原文件夹才可使用！"
        show_text = "".join(show_text)
        msgbox(show_text, "提示")
    else:
        msgbox("文件路径为空，请重新选择文件！", "警告")

lb1 = Label(root, text="PyExe转换器", font=("simhei", 30))
lb1.pack()

btn = Button(root, width=15, height=2,text ="选择文件", command=ChooseFile)
btn.pack()
btn.place(x = 50, y = 260,anchor='w')

btn1 = Button(root, width=15, height=2,text ="开始转换", command=StartTurn)
btn1.pack()
btn1.place(x = 250, y = 260,anchor='w')

root.mainloop()
