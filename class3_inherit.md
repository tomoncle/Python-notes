# 类继承
语法：
```python
class ClassName(父类)：
    def __init__(self [,父类属性] [,子类属性]):
        # 重写init方法
        super(ClassName, self).__init__([父类属性] [,子类属性])
        self.子类属性 = 子类属性
```

举例：如下代码，函数`super(Student, self)`将返回当前类继承的父类，即 `Person` ，
然后调用`__init__()`方法，注意`self`参数已在`super()`中传入，在`__init__()`中将隐式传递，不需要写出（也不能写）
```python
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def say_hello(self):
        return 'hello python'

    def show_me(self):
        return 'my name is %s , sex is %s' % (self.name, self.sex)


class Student(Person):
    # 定义Student类时，只需要把额外的属性加上，例如score：
    def __init__(self, name, sex, score):
        super(Student, self).__init__(name, sex)
        self.score = score

    def student(self):
        """子类方法"""
        return 'i am a student, my name is %s' % self.name

    def show_me(self):
        """重写父类方法"""
        return 'my name is %s , sex is %s , my final score is %d' % (self.name, self.sex, self.score)


stu = Student("aric", 'man', 20)
print stu.__dict__  # 查看子类属性字典 >>{'score': 20, 'name': 'aric', 'sex': 'man'}
print stu.say_hello()  # 查看子类继承父类的方法 >>hello python
print stu.student()  # 查看子类独有的方法 >>i am a student, my name is aric
print stu.show_me()  # 查看子类重写的父类方法 >>my name is aric , sex is man , my final score is 20

```





