
class MySingleton:

    _obj = None
    _init_flag = True

    #如果类 cls 为 None ， 则新建对象
    def __new__(cls, *args, **kwargs):
        if cls._obj == None:
            cls._obj = object.__new__(cls)

        return cls._obj

    #不再重复初始化
    def __init__(self,name):
        if MySingleton._init_flag:
            print("init ......")
            self.name = name
            MySingleton._init_flag = False

a = MySingleton("aa")
b = MySingleton("bb")

print(a)
print(b)