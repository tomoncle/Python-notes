# Python 类注解

```python

class Person(object):
    # 类属性，所有实例只存在一份类属性，共享该属性．
    class_attr = None

    def __init__(self, id, name):
        """
        实例方法，第一个参数必须为 self
        :param id: 实例属性
        :param name: 实例属性
        """
        self.id = id
        self.name = name
        self.__private_filed = 'private filed'  # 使用"__"开头的属性,为私有属性,外部无法访问

    @classmethod
    def class_method(cls):
        """
        类方法, 使用 @classmethod 注解来标注,参数为 cls
        可以通过cls.属性或方法名调用
        """
        return ' this is class method'

    @staticmethod
    def static_method():
        """
        static方法, 使用@staticmethod 注解来标注
        只能通过Person.属性名或方法名，一个全局函数
        """
        return ' this is static method'

    def get_private_filed(self):
        """
        可以定义方法来提供外部访问该属性，而不知道内部结构
        :return:__private_filed
        """
        return self.__private_filed

```

# Python类深入
### 访问限制
        python中访问限制,如果一个属性由双下划线开头(__)，该属性就无法被外部访问.
        但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，
        以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，
        通常我们不要把普通属性用"__xxx__"定义。
        以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
### 属性
        绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，
        则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！
        也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
        当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。但不会影响其他实例对象
        当类属性变为(__)私有时，外部依然无法访问
### 函数方法
        我们在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象：
        举例：p1.get_grade 返回的是一个函数对象但这个函数是一个绑定到实例的函数，
        　　　p1.get_grade() 才是方法调用
        因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType()
        把一个函数变为一个方法：
        代码：
                import types
                def fn_get_grade(self):
                    if self.score >= 80:
                        return 'A'
                    if self.score >= 60:
                        return 'B'
                    return 'C'
                class Person(object):
                    def __init__(self, name, score):
                        self.name = name
                        self.score = score
                p1 = Person('Bob', 90)
                p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
                print p1.get_grade()
        end:
### 类方法
        通过标记一个 @classmethod，该方法将绑定到类上，而非类的实例。
        类方法的第一个参数将传入类本身，通常将参数名命名为 cls
        因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。
### 继承
        class Person(object):
            def __init__(self, name, gender):
                self.name = name
                self.gender = gender
        class Student(Person):
             #定义Student类时，只需要把额外的属性加上，例如score：
             def __init__(self, name, gender, score):
                super(Student, self).__init__(name, gender)
                self.score = score
        一定要用 super(Student, self).__init__(name, gender) 去初始化父类，否则，
        继承自 Person 的 Student 将没有 name 和 gender。
        函数super(Student, self)将返回当前类继承的父类，即 Person ，
        然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，
        不需要写出（也不能写）。
### python中判断类型
        函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型
        如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型。
        >>>p = Person('zhangsan','male')
        >>>isinstance(p, Person)
        True
### python中多态
        类具有继承关系，并且子类类型可以向上转型看做父类类型
        子类重写父类的方法，调用时首先调用子类的方法实现
### python中多重继承
        class A(B,C):
            pass
        多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。
### python中获取对象信息
        type() 函数获取变量的类型
        dir() 函数获取变量的所有属性
        setattr(s, 'name', 'Adam')  # 设置新的name属性
        getattr(s, 'age', 20)  # 获取age属性，如果属性不存在，就返回默认值20
# python的特殊方法
### \_\_str__()和 \_\_repr__()
        如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
        代码：
            def __str__(self):
                　return '(Person: %s)' % self.name
            __repr__ = __str__  #偷懒的定义__repr__函数
    　　 end:
        因为 Python 定义了__str__()和__repr__()两种方法，
        __str__()用于显示给用户，而__repr__()用于显示给开发人员。
### \_\_cmp__()
        对 int、str 等内置数据类型排序时，Python的 sorted() 按照默认的比较函数 cmp 排序，
        但是，如果对一组 Student 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()
        代码：
            def __cmp__(self, s):
                if self.name < s.name:
                    return -1
                elif self.name > s.name:
                    return 1
                else:
                    return 0
        end:
        使用：print sorted(person_list)
        以分数排序：
        　　def __cmp__(self, s):
                if self.score == s.score:
                    return cmp(self.name, s.name)
                return -cmp(self.score, s.score)
### \_\_len__()
        如果一个类表现得像一个list，要获取有多少个元素，就得用 len() 函数。
        要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数。
### \_\_slots__
        如果要限制添加的属性，例如，Student类只允许添加 name、gender和score 这3个属性，
        就可以利用Python的一个特殊的__slots__来实现。
        __slots__的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，
        使用__slots__也能节省内存
        代码：
            class Student(object):
                __slots__ = ('name', 'gender', 'score')
                pass
        end:
### \_\_call__
        所有的函数都是可调用对象。
        一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
        class A(object):
            def __call__(self,s):
                return 'hello %s'%s
        >>>a=A
        >>>print a('jack')
        hello jack
### python中 @property
        @property表示可以将方法当作属性来使用
        第一个score(self)是get方法，用@property装饰，
        第二个score(self, score)是set方法，用@score.setter装饰
        　　　　
        代码：
            @property
            def score(self):
                return self.__score
            @score.setter
            def score(self, score):
                if score < 0 or score > 100:
                    raise ValueError('invalid score')
                self.__score = score
        end:
        使用：
            obj.score = 90 #调用set方法
            print obj.score　#调用get方法

# 练习
```python
def fib(num):
    """
    斐波那契数列
    """
    a, b, L = 0, 1, []
    for n in range(num):
        L.append(a)
        a, b = b, a + b
    return L


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Rational(object):
    """
    分数计算
    """

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)

    __repr__ = __str__


r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2
```
