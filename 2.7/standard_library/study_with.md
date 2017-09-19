# with 的使用
<a href="https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/">帮助文档</a>
##自定义with类

with 语句是在 Python 2.5 版本引入的，从 2.6 版本开始成为缺省的功能。
with 语句作为 try/finally 编码范式的一种替代，用于对资源访问进行控制的场合。
自定义支持 with 语句的类，以及使用 contextlib 工具加入对 with 语句的支持

要使用 with 语句，首先要明白上下文管理器这一概念。有了上下文管理器，with 语句才能工作。
下面是一组与上下文管理器和with 语句有关的概念。

上下文管理协议（Context Management Protocol）：包含方法 __enter__() 和 __exit__()，支持
该协议的对象要实现这两个方法。

上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了
__enter__() 和 __exit__() 方法。上下文管理器定义执行 with 语句时要建立的运行时上下文，
负责执行 with 语句块上下文中的进入与退出操作。通常使用 with 语句调用上下文管理器，
也可以通过直接调用其方法来使用。

运行时上下文（runtime context）：由上下文管理器创建，通过上下文管理器的 __enter__() 和
__exit__() 方法实现，__enter__() 方法在语句体执行之前进入运行时上下文，__exit__() 在
语句体执行完后从运行时上下文退出。with 语句支持运行时上下文这一概念。
上下文表达式（Context Expression）：with 语句中跟在关键字 with 之后的表达式，该表达式
要返回一个上下文管理器对象。

语句体（with-body）：with 语句包裹起来的代码块，在执行语句体之前会调用上下文管
理器的 __enter__() 方法，执行完语句体之后会执行 __exit__() 方法。

可以用于 with 语句中，比如可以自动关闭文件、线程锁的自动获取和释放

自定义上下文管理器
开发人员可以自定义支持上下文管理协议的类。
自定义的上下文管理器要实现上下文管理协议所需要的 __enter__() 和 __exit__() 两个方法：
context_manager.__enter__() ：进入上下文管理器的运行时上下文，在语句体执行前调用。
with 语句将该方法的返回值赋值给 as 子句中的 target，如果指定了 as 子句的话
context_manager.__exit__(exc_type, exc_value, exc_traceback) ：退出与上下文管理器相关的运行时上下文，
返回一个布尔值表示是否对发生的异常进行处理。参数表示引起退出操作的异常，如果退出时没有发生异常，则3个参数都为None。
如果发生异常，返回True 表示不处理异常，否则会在退出该方法后重新抛出异常以由 with 语句之外的代码逻辑进行处理。
如果该方法内部产生异常，则会取代由 statement-body 中语句产生的异常。要处理异常时，不要显示重新抛出异常，
即不能重新抛出通过参数传递进来的异常，
只需要将返回值设置为 False 就可以了。之后，上下文管理代码会检测是否 __exit__() 失败来处理异常


``` python
class Resource:
    def __init__(self, tag):
        self.tag = tag
        print 'Resource [%s]' % tag

    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print '[Exit %s]: Free resource.' % self.tag
        print 'exc_tb : %s' % exc_tb
        if exc_tb is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            return False


# excute sort: init-enter-print-exit
with Resource('amlyj'):
    print '[with-body] Run without exceptions.'

print '---------------------------------------'
with Resource('With-Exception'):
    print '[with-body] Run with exception.'
    raise Exception
    print '[with-body] Run with exception. Failed to finish statement-body!'
print '---------------------------------------'
with Resource("amlyj") as f:
    print f
```

## contextlib 模块
contextlib 模块提供了3个对象：装饰器 contextmanager、函数 nested 和上下文管理器 closing。使用这些对象，
可以对已有的生成器函数或者对象进行包装，加入对上下文管理协议的支持，避免了专门编写上下文管理器来支持 with 语句。

### 装饰器 contextmanager 使用示例
```python
from contextlib import contextmanager

    @contextmanager
    def demo():
        print '[Allocate resources]'
        print 'Code before yield-statement executes in __enter__'
        yield '*** contextmanager demo ***'
        print 'Code after yield-statement executes in __exit__'
        print '[Free resources]'

    with demo() as value:
        print 'Assigned Value: %s' % value
```


生成器函数中 yield 之前的语句在 __enter__() 方法中执行，
yield 之后的语句在 __exit__() 中执行，而 yield 产生的值赋给了 as 子句中的 value 变量。

需要注意的是，contextmanager 只是省略了 __enter__() / __exit__() 的编写，
但并不负责实现资源的“获取”和“清理”工作；
“获取”操作需要定义在 yield 语句之前，
“清理”操作需要定义 yield 语句之后，
这样 with 语句在执行 __enter__() / __exit__() 
方法时会执行这些语句以获取/释放资源，即生成器函数中需要实现必要的逻辑控制，包括资源访问出现错误时抛出适当的异常。

### 函数 nested
nested 可以将多个上下文管理器组织在一起，避免使用嵌套 with 语句。
```python
 with nested(A(), B(), C()) as (X, Y, Z):
         # with-body code here
         
 # 等价于
 with A() as X:
       with B() as Y:
            with C() as Z:
                 # with-body code here
```
需要注意的是，发生异常后，如果某个上下文管理器的 __exit__() 方法对异常处理返回 False，则更外层的上下文管理器不会监测到异常。
 
