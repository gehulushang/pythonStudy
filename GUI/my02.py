from tkinter import messagebox
from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)       # super 代表的是父类的定义 调用父类构造器
        self.master = master
        self.pack()

        self.createWidget()

    # 创建组件
    def createWidget(self):

        self.btn01 = Button(self)
        self.btn01["text"] = "点击"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        # 创建退出按钮
        self.btnQ = Button(self, text = "退出", command = root.destroy)
        self.btnQ.pack()

    def songhua(self):
        messagebox.showinfo("Message", "送你一朵花")
        print("送你一朵花")


root = Tk()
root.geometry("400x100+200+300")
root.title("zjf")

app = Application(master=root)

root.mainloop()
