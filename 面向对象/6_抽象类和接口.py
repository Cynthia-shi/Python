'''
抽象类
是一种无法实例化的类，  
它只能作为其他类的父类来使用，用于描述一组相关类的共性特征。  
接口
是一种抽象的数据类型，  
它只描述了对象的方法而不提供实现。类可以实现接口，以便实现相同的行为。
'''

# 抽象类是一种特殊的类，在 Python 中可以通过 abc 模块来定义。
# 它不能直接被实例化，只能被用作其他类的基类，用来定义方法的接口和规范。
# 以下是一个简单的抽象类的例子：
import abc

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass
    
    @abc.abstractmethod
    def perimeter(self):
        pass
# 在上面的例子中，定义了一个抽象类 Shape，它有两个抽象方法 area 和 perimeter。
# 这些抽象方法只是定义了方法名和参数，但没有具体的实现。
# 子类必须实现这些抽象方法才能被实例化。

# 以下是一个实现了 Shape 抽象类的具体类的例子：
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
# 在上面的例子中，Rectangle 类继承自 Shape 抽象类，
# 并实现了其抽象方法 area 和 perimeter。
# 这样，Rectangle 类就可以被实例化了。

a = Rectangle(3, 5)
print(a.area())
print(a.perimeter())

# 需要注意的是，
# 如果子类没有实现父类中定义的所有抽象方法，那么子类也会成为抽象类。
# 如果在子类中调用父类的抽象方法，那么 Python 会抛出 NotImplementedError 异常。



# 在 Python 中，接口是一种约定，它规定了一个类应该实现哪些方法。
# Python 并没有像 Java 等语言一样提供接口的显式定义，
# 但是可以通过抽象基类（Abstract Base Class，简称 ABC）来实现接口的功能。
# 以下是一个简单的接口示例：
import abc

class Payment(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount):
        pass
# 在上面的示例中，定义了一个名为 Payment 的接口，它规定了一个方法 pay。
# 这个方法并没有具体的实现，只是定义了方法名和参数。
# 子类必须实现这个方法才能被实例化。

# 以下是一个实现 Payment 接口的具体类的示例：
class Cash(Payment):
    def pay(self, amount):
        print("Paid ${} in cash".format(amount))

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid ${} by credit card".format(amount))

a = Cash()
print(a.pay(300))
b = CreditCard()
print(b.pay(500))

# 在上面的示例中，定义了两个具体类 Cash 和 CreditCard，
# 它们分别实现了 Payment 接口的 pay 方法。
# 这样，Cash 和 CreditCard 就可以被实例化，并调用 pay 方法来实现付款功能。

# 需要注意的是，
# 如果子类没有实现接口中定义的方法，那么子类也会成为抽象类。
# 如果在子类中调用接口的方法，那么 Python 会抛出 NotImplementedError 异常。

