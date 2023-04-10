'''类和对象'''


# 类是一种自定义的数据类型，可以用来描述具有相同属性和方法的对象。
# 类的定义可以通过class关键字来实现，
# 代码定义了一个Car类，该类具有make、model和year属性，以及一个get_descriptive_name方法。
# 其中，__init__方法是一个特殊的方法，它会在创建对象时被调用，用于初始化对象的属性。
class Car:
    # 定义构造函数
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # 定义方法
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car('audi', 'a4', 2022)
print(my_car.get_descriptive_name())  # 输出：2022 Audi A4

your_car = Car('bmw', 'x5', 2023)
print(your_car.get_descriptive_name())  # 输出：2023 Bmw X5

# 分别创建了两个Car类的对象my_car和your_car，并分别调用它们的get_descriptive_name方法。
# 这样的类定义和对象创建方式，是面向对象编程的基础。


# 在面向对象编程中，类只是一个模板或蓝图，需要通过实例化来创建对象。
# 实例化是指使用类创建对象的过程，通过实例化可以获得一个具体的对象，该对象具有类定义的属性和方法。
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car('audi', 'a4', 2022)
your_car = Car('bmw', 'x5', 2023)

print(my_car.get_descriptive_name())  # 输出：2022 Audi A4
print(your_car.get_descriptive_name())  # 输出：2023 Bmw X5

my_car.year = 2024  # 修改 my_car 对象的 year 属性
print(my_car.get_descriptive_name())  # 输出：2024 Audi A4
print(your_car.get_descriptive_name())  # 输出：2023 Bmw X5

# 在上述示例中，通过Car类创建了一个名为my_car的对象，这个对象包含了make、model和year等属性，以及get_descriptive_name等方法。
# 通过调用my_car.get_descriptive_name()方法，可以得到对象的具体信息。

# 在实例化时，需要在类名后面加上括号，并传入类的初始化方法中定义的参数，即可创建一个新的对象。
# 在这个过程中，类的初始化方法会被调用，并将参数传递给它。
# 这个方法会创建一个新的对象，并为对象设置属性的初始值。

# 需要注意的是，通过类创建的对象是独立的，即不同的对象之间互相独立，修改其中一个对象不会影响其他对象。
# 例如，示例创建了两个对象my_car和your_car，它们之间互相独立:
#      通过创建两个对象my_car和your_car，分别具有不同的属性值。
#      然后，通过修改my_car对象的year属性，可以看到该对象的属性被修改了，但是your_car对象的属性没有被修改，依然保持不变。
#      这说明不同的对象之间是互相独立的。