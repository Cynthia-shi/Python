'''继承'''


# 通过继承，一个类可以从另一个类中继承属性和方法。继承是面向对象编程中实现代码复用的一种方式。
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.fuel_capacity = 50

my_car = Car('audi', 'a4', 2022)
print(my_car.get_descriptive_name())  # 输出：2022 Audi A4

# Vehicle类包含一个get_descriptive_name方法，而Car类继承了Vehicle类，并添加了一个名为fuel_capacity的属性。
# 在Car类的初始化方法中，通过super()函数调用父类的初始化方法，从而继承了Vehicle类中的make、model和year等属性。



# Python同时继承多个父类有两种方法
# 1.使用未绑定方法逐个调用
# 2.使用super()函数。
# 
# 注意，
# 当子类继承于多个父类时，
# super() 函数只可用于调用第一个父类的构造函数，
# 其余父类的构造函数只能使用未绑定的方式调用。

class Employee:
    def __init__(self,salary):
        self.salary=salary
    def work(self, *args, **kwargs):
        print('普通员工在写代码，工资为：',self.salary)

class Customer:
    def __init__(self,favourite,address):
        self.favourite=favourite
        self.address=address
    def info (self):
        print('我是一个顾客，我的爱好是：%s,地址是%s'%(self.favourite,self.address))

class Mannager(Employee,Customer):
    def __init__(self,salary,favourite,address):
        print('Manngaer的构造方法')
        # 方法一：用未绑定方法来构造,使用类名直接构造,逐个调用
        # Employee.__init__(self,salary)
        # Customer.__init__(self,favourite,address)
        
        # 方法二：使用super()和未绑定方法
        super().__init__(salary)
        #与上一行代码效果相同
        # super(Mannager,self).__init__(salary)

        Customer.__init__(self,favourite,address)

m=Mannager(25000,'it产品','广州')
m.work()
m.info()
