'''
class Emp:
    #装饰器
    @property
    def salary(self):
        print("salary run .. ")
        return 100;


emp1 = Emp()

print(emp1.salary)


'''


class Emp:


    def __init__(self,name,salary):
        self._name = name    #_私有属性
        self._salary = salary

    # 装饰器  代替getter setter 方法
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
    '''
     def get_salary(self):
        return self._salary

    def set_salary(self,salary):
        self._salary =salary
    '''



emp1 = Emp("zjf",2000)

#print(emp1.get_salary())

#emp1.set_salary(200)

#print(emp1.get_salary())

print(emp1.salary)

emp1.salary = 200
print(emp1.salary)

