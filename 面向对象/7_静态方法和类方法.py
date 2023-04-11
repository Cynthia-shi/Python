'''
静态方法是一种不依赖于类实例的方法，可以通过类名来直接调用。  
类方法是一种作用于整个类的方法，可以通过类名或类实例来调用。
'''


# 实例方法：可以获取类属性、构造函数定义的变量，属于 method 类型。只能通过实例化调用。
# 静态方法：不能获取类属性、构造函数定义的变量，属于 function 类型。两种调用方式：类.方法名 ，实例化调用。
# 类方法 ：可以获取类属性，不能获取构造函数定义的变量，属于 method 类型。两种调用方式：类.方法名 ，实例化调用。


'''classmethod'''
# classmethod能够完成的功能有：
# 修改类中的变量，不论是类变量还是类实例传入的参数变量
# 产生类实例，即装饰有classmethod的函数能够产生类实例
# 修改类变量的例子：
class Worker:

    raise_percent = 1       # 默认没有涨工资，比例为1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod            # 加入此装饰器
    def ch_raise_percent(cls, num):        # 修改涨薪比例的函数
        cls.raise_percent = num * cls.raise_percent   # 传入一个数乘以之前的涨薪比例
    # 这里要多解释一下，传入的是cls，这里cls代表类本身。要传入类本身才能够修改类本身的内容(如类变量)，
    # 由于传的是类本身，使用class的话会与class定义语句有冲突，因此使用classmethod要传入类的信息时，
    # 将类本身以cls形式传入。
    # 后面传入的num是在调用这个函数(即ch_raise_percent)时传入的参数，这个参数和创建类实例需要的
    # 参数是没有关系的，因为调用这个函数仅仅是修改了类本身的信息。

        
Worker.ch_raise_percent(1.3)   
# 这里在类外部调用classmethod装饰的函数，并传入一个num参数用于修改涨薪比例
print(Worker.raise_percent)
# 使用类本身查看其类变量是否变化

# 执行结果为1.3，表示这里我们确实把Worker类的raise_percent类变量给修改了。

# 有人可能会想使用其它方式不能直接修改类变量吗，
# 比如在类函数中传入self，然后调用类变量(即self.raise_percent)来进行修改，
# 但是实际上你在类函数中调用后修改产生的是局部变量，整个类是获取不到你修改得到的局部变量的。


# 产生类实例的方法：
# 产生类实例的方法真的是非常好用啊，
# 比如你的初始数据是一堆有规则的字符串，
# 而这些字符串中包含着每个类实例所需的参数，
# 那么你只需要添加一个classmethod装饰的函数，
# 用这个函数帮你处理一下你的字符串，
# 将这些字符串分成独立的项，
# 再将这些项传递给类就可以产生类实例啦！
class Worker:

    def __init__(self, name, age, height, salary):
        self.name = name
        self.age = age
        self.height = height
        self.salary = salary
    
    @classmethod
    def str_handler(cls, string):
        name, age, height, salary = string.split('/')  
        # 将传入的字符串以/分割产生列表，一一对应
        return cls(name, age, height, salary)
        # 这里return返回的就是cls，也就是一个类实例，将Worker类类实例需要的
        # 所有项都传入了cls，这就是一个完完整整的类实例啦
        # 要注意return返回值可以被变量接收，接收后就成为类实例咯
    
A = 'Jack/20/1.75/1000'   
B = 'Mary/18/1.65/2000'
# 两个需要处理的字符串

a = Worker.str_handler(A)
b = Worker.str_handler(B)
# 两次调用此类中的函数，产生两个类实例即a和b

print(a.name, a.age, a.height, a.salary)
print(b.name, b.age, b.height, b.salary)
# 查看类实例是否创建成功



'''staticmethod'''
# staticmethod也叫静态方法，
# 实际上staticmethod装饰的函数的功能可能和类本身没什么太大的关系，
# 因为staticmethod装饰的函数不能传入类实例或者类变量或者刚刚提到的cls。
# 因此这个函数处理的功能只是额外的，比如帮你记录一下日期之类的功能。
# 这样的功能可能在某些时候会用上，所以就把这样的函数也顺带包装在类中。
class Worker:

    def __init__(self, name, age, height, salary):
        self.name = name
        self.age = age
        self.height = height
        self.salary = salary
    
    @classmethod
    def str_handler(cls, string):
        name, age, height, salary = string.split('/')
        return cls(name, age, height, salary)
        
    @staticmethod           # 静态方法装饰器
    def read_file(worker_file):
        f = open(worker_file,'r')
        lines = f.readlines()
        return lines
    # 这里的功能就是读取工作人员的记录文件，将每一行内容作为一个item
    # 记录到lines列表，最后将列表传出以供后续利用
    # 有没有留意到，这个和类本身的功能是没有关系的，也就是实际上我们在类外部执行这个函数
    # 或者单独执行这些代码也是一样的功能，只不过包装在类中更便于管理和使用而已
    
all_workers = Worker.read_file('/project/Python/data/2020_workers.txt')  
# 使用上面的静态方法读取一个文件
for item in all_workers:
    worker = Worker.str_handler(item)
    print(worker.name, worker.age, worker.height, worker.salary)
# 通过for循环可以将文件中所有行都转为类实例
# 后面对类实例的操作就不写啦


