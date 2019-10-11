from tkinter import messagebox
from tkinter import *

root = Tk()

btn01 = Button(root)
btn01["text"] = "点我"

btn01.pack()


def songhua(e):   #e是时间对象
    messagebox.showinfo("Message", "送你一朵花")
    print("送你一朵花")


btn01.bind("<Button-1>", songhua)

root.mainloop()
