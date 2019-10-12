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

        self.label01 = Label(self, text = "标签", width=10, height=2,
                             bg="white", fg="red")
        self.label01.pack()

        # 显示图像

        global photo  # 需要把photo声明为全剧变量，否则本方法执行之后photo会销毁，窗口显示图像
        photo = PhotoImage(file="imgs/img.png")
        self.label02 = Label(self, image=photo)
        self.label02.pack()
          

root = Tk()
root.geometry("400x100+200+300")
root.title("zjf")

app = Application(master=root)

root.mainloop()