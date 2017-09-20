# python 的类初步 

# 基础语法
### 定义
关键字：class
格式： class ClassName(): pass

### 初始化
使用`__init__(self)`来进行初始化操作,`self`是python类中方法中必须存在的参数，表示当前对象，
使用该参数传递对象，类似java的this, 当然`self`只是一个别名，你可用随便指定任意名称，
如`abc`,但是不建议这样做，可读性差

```python
# -*- coding=utf-8 -*-
# 定义
class Person():
    def __init__(self):
        print '初始化 ...'

# 引用
p=Person()

print p

"""结果：
>>初始化 ...
>><__main__.Person instance at 0x7f0ac74f1c68>
"""
```
### 初始化并且传递参数
使用`__init__(self,param)`来进行初始化操作

```python
# -*- coding=utf-8 -*-
# 定义
class Person():
    def __init__(self, params):
        self.params = params
        print '初始化 ...'


# 引用
p = Person("hello python")

print p.params

"""结果：
>>初始化 ...
>>hello python
"""
```

### 传递任意参数
```python
# -*- coding=utf-8 -*-
# 定义
class Person():
    def __init__(self, *args,**kwargs):
        print '传入参数：',kwargs,args
        for k, v in kwargs.iteritems():  # 使用setattr()方法添加属性
            setattr(self, k, v)

        print '初始化 ...'


# 引用

p = Person(**{'k':1,'kk':2})

print p.__dict__  # 打印对象属性字典

```



# 对象操作之动态属性
python 实例对象可用动态的添加或删除属性
### 添加
* `setattr(object,'field_name',value)` : 添加或修改object对象的属性field_name,值为value
* `object.field_name = value` : 直接使用`对象.属性=值` 为对象添加或修改属性
### 获取
* `getattr(object,'field_name',default_value)`：获取object对象的field_name属性，假如该属性不存在，返回default_value默认值
* `object.filed_name` : 直接使用`对象.属性` 获取对象的属性值，如果属性不存在，抛出异常
### 删除
* `delattr(object,'field_name')` : 删除object对象的field_name属性，如果属性不存在，抛出异常
* `del object.filed_name` : 使用`del 对象.属性` 删除object对象的field_name属性，如果属性不存在，抛出异常
### 判读是否存在
* `hasattr(object, field_name)`: 判断object对象是否存在field_name属性


# 属性和方法
在类里＂私有属性＂使用双下划线（\_\_）开头，＂私有方法＂也是使用双下划线（\_\_）开头，＂受保护属性和受保护方法＂使用单下划线（\_）开头，
＂公开属性和方法使用字母开头＂：
```python
class A(object):
    def __init__(self):
        self.__name = "tom"  # private 私有属性,不能被外部调用, (实际是可以用 ._{className}__{filedName}来访问)
        self._id = 10  # protected 受保护的属性,可以被外部调用，但不建议
        self.age = 20  # public 公开的属性,完全被外部访问

    def __say_hi(self):
        """
        私有方法,不能被外部调用,(实际是可以用 ._{className}__{methodName}来访问)
        :return:
        """
        print 'private method : say hi %s' % self.__name

    def _hello(self):
        """
        受保护的方法,可以被外部调用,但不建议
        :return:
        """
        print 'protected method: hello %s' % self._id

    def hello_world(self):
        """
        公开的方法
        :return:
        """
        print "public method : hello world %s" % self.age

```
