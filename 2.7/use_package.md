# 如何正确的使用python package
一般，我们使用python其他的模块的时候，如果简单的在一个包内引用其他模块的函数，使用`import 模块名称`就ok了，
然后使用`模块名称.函数名称`来调用这个函数，或者使用`from 模块名　import 函数名称`来引用
```python
import model

print model.add(1,2)

"""
或者使用该方式，效果相同

from model import add
print add(1,2)
"""
```

当引用其他包的其他模块时，一般使用`from 包名　import 模块名`　或者 直接使用from倒入函数`from 包名．模块名　import 函数名称`来使用这个函数
```python
from test import db2
print db2.delete()

"""
或者使用该方式，效果相同

from test.db2 import delete
print delete()
"""
```
当然以上的方式完全可以帮助我们解决问题，但是我们已经知道了，想要引用其他包的python模块，该模块所在的包必须包含一个名为`__init__.py`的文件，
这个文件是标志该文件夹是个python目录，我们可以使用`from 包名　import 模块名，...`的方式，把该包里的模块引用到这个文件，然后在其他位置
引用该包的模块时，只需要导入这个包名即可,如：`import test`，那如何使用模块中的函数：`包名．模块名．函数名`这样来使用，虽然效果是一样的，
但是这个感觉整个项目的模块结构更加清晰,例如
```
.
├── app.py
└── celerys
    ├── __init__.py
    └── tasks.py

1 directory, 3 files

```
\_\_init\_\_.py
```python
"""
import models
"""

from celerys import tasks
```
tasks.py
```python
#! /bin/python

from celery import Celery

broker = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'

app = Celery('tasks', broker=broker, backend=backend)

@app.task
def add(x, y):
    return x + y
```
app.py
```python
import celerys

if __name__ == '__main__':
    print celerys.tasks.add(1, 2)

```
