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

