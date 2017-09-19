# decorator装饰器

装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

#函数装饰器
###简单的装饰器
```python
def decorator(func):
    """
    func 即为调用该函数的方法
    """
    def wrapper(*args, **kwargs):
        print '方法%s调用装饰器' % func.__name__
        return func(*args, **kwargs)

    return wrapper


@decorator
def show():
    """
    @符号是装饰器的语法糖,在定义函数的时候使用，避免再一次赋值操作
    使用＠语法糖，等价于 show=decorator(show)
    """
    print '......show......'



show()

```
###带参数的装饰器
```python
def logging(level):
    """
    对简单装饰器的一次封装，返回一个新的装饰器,传递了level参数
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print ("%s is running" % func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logging(level="warn")
def hell(name='foo'):
    print("i am %s" % name)


hell()
```
#类装饰器
相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器还可以依靠类内部的`__call__`方法，
当使用`@`形式将装饰器附加到函数上时，就会调用此方法。

```python
class Logging(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('Logging starting')
        self._func()
        print ('Logging ending')


@Logging
def tes():
    print ('bar')


tes()
```

#装饰器缺点
###举例
使用装饰器极大地复用了代码，但是他有一个缺点就是"原函数的元信息"不见了
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print func.__name__, func.__doc__, 'call decorator'
        return func(*args, **kwargs)

    return wrapper


@decorator
def show():
    """ show test """
    print '......'


show()
print show.__name__  # wrapper
print show.__doc__  # None
```
###改进装饰器
使用`functools.wraps`装饰器,它能把原函数的元信息拷贝到装饰器函数中，
这使得装饰器函数也有和原函数一样的元信息了。
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print func.__name__, func.__doc__, 'call decorator'
        return func(*args, **kwargs)

    return wrapper


@decorator
def show():
    """ show test """
    print '......'


show()
print show.__name__  # show
print show.__doc__  # show test

```


# 内置装饰器
@staticmathod、@classmethod、@property


# 装饰器的顺序
```python
@a
@b
@c
def f ():
    pass
# 等效于
f = a(b(c(f)))
```


