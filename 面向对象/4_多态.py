'''多态'''


# 多态指的是不同对象对同一消息做出不同的响应。
# 具体来说，如果一个类继承了另一个类的方法，并对该方法进行了重新定义，那么在调用该方法时，会根据对象的类型决定调用哪个方法。
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现该方法")
        # 在面向对象编程中，抛出NotImplementedError异常通常用于表示一个方法是抽象的，需要在子类中实现。
        # 也就是说，如果一个父类定义了一个方法，但该方法在父类中没有具体的实现，
        # 而只是抛出了NotImplementedError异常，那么子类必须覆盖该方法并提供自己的实现。
        # 抛出NotImplementedError异常的主要用意是提示子类实现该方法。
        # 如果子类没有覆盖该方法或忘记实现该方法，调用该方法时就会抛出NotImplementedError异常，
        # 从而提醒开发者需要在子类中实现该方法。
        # 这有助于提高代码的可读性和可维护性，让代码更加健壮和可靠。

class Dog(Animal):
    def speak(self):
        return "汪汪汪"

class Cat(Animal):
    def speak(self):
        return "喵喵喵"

animals = [Dog("旺财"), Cat("咪咪"), Dog("小黑")]

for animal in animals:
    print(f"{animal.name} 说 {animal.speak()}")

# 定义了一个Animal类，该类包含一个speak方法，并抛出了一个NotImplementedError异常。
# 然后，定义了一个Dog类和一个Cat类，它们分别继承了Animal类，并重新定义了speak方法。
# 最后，创建了一个包含多个Dog和Cat对象的列表，并遍历该列表，输出每个对象的名称和它们的speak方法的返回值。
# 在输出结果中，可以看到不同类型的对象对同一个speak消息做出了不同的响应。

