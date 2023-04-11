'''装饰'''

# 装饰器（decorator）是一种特殊的函数，它可以用来修改其他函数的行为。
# 装饰器本质上是一个闭包，它可以将被装饰的函数作为参数，并返回一个新的函数，
# 新的函数可以包装原始函数，从而实现对原始函数行为的修改或增强。

# 装饰器的作用主要有以下几个方面：
# 实现代码的复用：
# 使用装饰器可以将一些通用的功能封装起来，然后在多个函数中重复使用。
# 例如，可以使用装饰器实现日志记录、性能统计、输入验证等功能，从而减少代码的冗余和复杂度。
# 动态修改函数行为：
# 使用装饰器可以在运行时动态地修改函数的行为，例如增加函数的功能、增加函数的参数等。
# 装饰器的这种特性使得它在框架和库的开发中得到广泛的应用。
# 实现 AOP 编程：
# 装饰器可以实现面向切面编程（AOP）的思想，即将通用的横切关注点（如日志记录、异常处理等）
# 从业务逻辑中分离出来，然后在需要的地方动态地将它们注入到函数中。
# 代码更加简洁：
# 使用装饰器可以使代码更加简洁，从而提高代码的可读性和可维护性。
# 例如，使用装饰器可以避免使用大量的 if/else 语句或 try/except 语句，从而让代码更加清晰和易于理解。
# 总之，装饰器是 Python 中非常强大和灵活的工具，可以用来解决很多常见的编程问题，同时也可以提高代码的复用性、可维护性和可读性。

# Python 中有很多装饰器，它们可以用于不同的场景，比如：
# @property: 用于将一个方法封装为属性，使其可以像访问实例变量一样来访问。
# @staticmethod: 用于将一个方法封装为静态方法，使其不需要访问实例变量。
# @classmethod: 用于将一个方法封装为类方法，使其可以访问类变量。
# @abstractmethod: 用于定义抽象方法，使其必须在子类中被实现。
# @final: 用于将一个方法或属性封装为最终版本，使其不可被重写或修改。
# @asyncio.coroutine: 用于将一个方法封装为协程，使其可以使用 async/await 语法来调用。
# @contextmanager: 用于定义上下文管理器，使其可以使用 with 语句来管理资源。
# @wraps: 用于将一个函数的元信息（如名称、文档字符串、参数列表等）复制到一个装饰器函数中。


'''property'''

# property装饰器的使用可能较复杂一点，property的翻译就是属性，因此其跟属性有关啦。
# 而装饰器又是用来装饰函数的，那其实加property装饰器的功能就是将函数的返回值作为类的属性啦。
# 也就是说我们调用这个被装饰的函数不需要加括号去运行，而是直接像变量或者属性一样获取这个值。
class Worker:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @property
    def name_and_salary(self):
        return self.name+'的工资是'+str(self.salary)
    # 需要有返回值，返回值作为获取到的属性嘛

A = Worker('Jack',1000)
print(A.name_and_salary)
# 注意这里不用加括号哦，像变量或者属性一样去调用就好了

# 当然property不止这点作用，使用property装饰后，被装饰的函数就成为了新的装饰器，
# 新的装饰器常用的有三个，
# 如上例中就是getter(默认的，即赋予类使用者获取某属性的能力)、
#           setter(赋予类使用者在类外部给某类属性重新赋值的能力)和
#           deleter(赋予类使用者在类外部删除某属性的能力)。
class Worker:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property     
    # 先使用property装饰原函数，装饰之后就可以使用setter和deleter方法来进行装饰并有更多的功能了
    # 这里默认已经有了getter的功能，也就是能够获取到这个属性的能力
    def view_salary(self):
        return self.salary

    @view_salary.setter
    # setter装饰器能够使我们在类外部重新设置view_salary这个属性
    # 而没有setter的话就会报错  AttributeError: can't set attribute
    def view_salary(self, new_salary):
        self.salary = new_salary
        return new_salary

    @view_salary.deleter
    # deleter装饰器的设置使我们可以在类外部使用del删除这个属性，但是这里我试了将self.salary
    # 设置为其它值也是可以的哦，这个值设置非空的话还是会有属性继续存在的哦。也就是在类外部使用
    # del的功能取决于你自己在这里设置的操作
    # 我这里是设置为空值了
    def view_salary(self):
        self.salary = None

A = Worker('J',1000)

A.view_salary = 2000
# 这里在外部进行赋值，是使用的设置的setter方法哦，没有setter会报错的！！
print("使用setter后的view_salary 值是：", A.view_salary)

del A.view_salary  # 尝试删除
print("使用del后J 的view_salary 的属性值是：", A.view_salary)


