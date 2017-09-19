# python 类深入

# 特殊方法
### \_\_new__() 方法：
在python内部，真正的初始化函数时\_\_new__()方法,它在\_\_init__()方法之前被调用，它是一个类方法，在创建对象时调用。
而\_\_init__()方法是在创建完对象后调用，对当前对象的实例做一些一些初始化，无返回值。
如果重写了\_\_new__()而在\_\_new__()里面没有调用\_\_init__()或者没有返回实例,那么\_\_init__()将不起作用。

###### 使用
* 使用\_\_new__()方法设计单例模式
```python
import threading
lock = threading.Lock()


class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args):
        if not Singleton.__instance:
            # set lock keep thread safe
            try:
                lock.acquire()
                if not Singleton.__instance:
                    Singleton.__instance = object.__new__(cls, *args)
            except Exception, e:
                print 'Singleton: init error : %s' % e
            finally:
                lock.release()
        return Singleton.__instance


### TEST
s1 = Singleton()
s2 = Singleton()
s1.dicts = {'name': 'tom'}

print id(s2) == id(s1), s2.dicts
```
### \_\_setattr__() 方法：
python可用动态给对象添加属性，禁止添加属性需要重写该方法
```python
 def __setattr__(self, key, value):
        pass
```

### \_\_dict__() 方法：
使用\_\_dict__()方法用于返回对象的属性字典，python重写\_\_setattr__()方法禁止对象添加属性，
但是可以通过 ` obj.__dict__['index']= 11 `添加属性，重写\_\_dict__()方法可以禁用此方法
```python
  def __dict__(self):
        pass
```
###### 构造全局字典
```python
import threading

lock = threading.Lock()


class ApplicationDICT(object):
    __instance = None
    __maps = {}

    def __new__(cls, *args):
        if not ApplicationDICT.__instance:
            # set lock keep thread safe
            try:
                lock.acquire()
                if not ApplicationDICT.__instance:
                    ApplicationDICT.__instance = object.__new__(cls, *args)
            except Exception, e:
                print 'Singleton: init error : %s' % e
            finally:
                lock.release()
        return ApplicationDICT.__instance

    @property
    def maps(self):
        return self.__maps

    def set_maps(self, k, v):
        assert k and v
        self.__maps[k] = v

    def __setattr__(self, key, value):
        pass

    def __dict__(self):
        pass

```
