'''
方法的重载
指的是在同一个类中定义多个同名但参数不同的方法。
这些方法可以根据参数的不同来进行区分，从而实现不同的功能。
Python 不支持方法的重载，因为 Python 中方法的参数类型和数量是可以动态变化的。

方法的重写
指的是在子类中重新定义一个和父类中同名的方法。
子类中的方法会覆盖父类中的方法，从而改变方法的行为。
子类的方法可以调用父类中被重写的方法，以实现部分重用。
'''

# 方法的重载指的是在同一个类中定义多个同名但参数不同的方法。
# 以下是一个简单的例子：
class Math:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z
# 在上面的例子中，Math 类中定义了两个同名但参数不同的 add 方法，
# 一个是 add(x, y)，一个是 add(x, y, z)。
# 这就是方法的重载。
# 但是，这样写在 Python 中是不支持的，因为 Python 中方法的参数类型和数量是可以动态变化的。

# 方法的重写指的是在子类中重新定义一个和父类中同名的方法。
# 以下是一个简单的例子：
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
# 在上面的例子中，Animal 类定义了一个 speak 方法，在 Dog 类中对其进行了重写。
# Dog 类的 speak 方法输出了 "Dog barks"，覆盖了父类 Animal 中的 speak 方法。

# 需要注意的是，子类中的重写方法名和参数应该和父类中的方法名和参数一致。
# 同时，子类的方法可以调用父类中被重写的方法，以实现部分重用。以下是一个例子：
class Animal:
    def speak(self):
        print("Animal speaks")
 
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()

d = Dog()
print(d.speak())

# 在上面的例子中，Dog 类对父类 Animal 中的 speak 方法进行了重写，
# 同时在重写的方法中调用了 super().speak() 来执行 Animal 类中的 speak 方法，
# 从而实现了部分重用。

# 这就是方法的重载和重写的区别。
# 方法的重载是同一个类中定义多个同名但参数不同的方法，
# 而方法的重写是在子类中重新定义一个和父类中同名的方法。
