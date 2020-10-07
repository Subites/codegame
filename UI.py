from tkinter import *
def reset():
    global warning
    global str
    root = Tk()
    width = 1366
    height = 768
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
    str=StringVar()
    warning = Label(root, textvariable=str, fg='red', font=('宋体', 12))  # 用于显示警告信息
    warning.pack(anchor='center')
def UIdraw(cameraphoto):
    str.set(cameraphoto)
    warning.update()

