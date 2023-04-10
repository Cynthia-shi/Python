'''封装'''


# 封装可以帮助我们隐藏对象的内部实现细节，
# 使得对象的使用者只能通过暴露的公共接口来操作对象，
# 从而提高代码的可维护性和安全性。
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age < 0 or age > 120:
            raise ValueError("年龄必须在0到120之间")
        self.age = age

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("分数必须在0到100之间")
        self.grade = grade

# 定义了一个Student类，包含三个属性：name、age和grade。
# 为了封装这些属性，我们提供了三个getter和三个setter方法。
# 其中    get_name、get_age和get_grade方法用于获取属性值，
# 而      set_name、set_age和set_grade方法用于设置属性值。
# 在set_age和set_grade方法中，我们加入了一些参数检查的代码，以确保年龄和分数的取值范围符合常理。

# 通过上述实现，我们实现了对Student对象属性的封装。
# 外部使用者只能通过公共接口（getter和setter方法）来访问或修改对象属性的值，而不能直接访问或修改对象的内部实现细节。
# 这样，即使在对象内部的实现细节发生变化，只要公共接口保持不变，外部使用者就不需要改变自己的代码，这提高了代码的可维护性。
# 同时，通过在setter方法中加入参数检查的代码，我们可以保证对象属性的取值范围符合常理，从而提高了代码的安全性。

class Person:
    def __init__(self, name, age):
        self._name = name   # 将属性标记为私有属性
        self._age = age
    
    def get_name(self):
        return self._name   # 只暴露必要的接口
    
    def set_name(self, name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        self._age = age

# 创建一个Person对象
person = Person("张三", 20)

# 调用对象的方法
print(person.get_name())  # 输出：张三
print(person.get_age())   # 输出：20

# 修改对象的属性
person.set_name("李四")
person.set_age(25)

# 再次调用对象的方法
print(person.get_name())  # 输出：李四
print(person.get_age())   # 输出：25

# 在上面的例子中，我们定义了一个名为Person的类，并封装了类的属性和方法。
# 创建对象时，我们可以通过构造函数来初始化对象的属性值。
# 在对象创建后，我们可以通过对象的方法来访问和修改对象的属性值。
# 这样，我们就能够使用封装后的类来实现更加可靠和安全的编程。

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("宽度必须大于0")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("高度必须大于0")

    def area(self):
        return self._width * self._height

rectangle = Rectangle(10, 20)
print(rectangle.width)  # 输出：10
rectangle.width = 5
print(rectangle.width)  # 输出：5
rectangle.width = -5    # 输出：宽度必须大于0
print(rectangle.width)  # 输出：5
print(rectangle.area()) # 输出：100

