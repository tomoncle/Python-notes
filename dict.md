# python 字典dict
无序，k-v对存在，查找速度快，占用内存高，key是唯一值，不能重复。
在python终端，使用`dir(dict)`获取方法及属性列表，使用`help(dict)`获取其使用方法

# 基本操作
### 声明
* `声明`：`dict={}`
* `声明并赋值`：`dict={'key':'value','num':1,'list':[1,2],'tup':(1,2,3)}`

### 添加或修改
* `dict['key'] = 'value'`：使用dict['key']=value的方式为字典重新赋值，或添加元素

### 删除
* `d.pop('k')` : 删除字典指定的k,并且返回该k的值
* `del d['k']` : 删除字典的指定k
* `del dict`   : 删除整个字典

### 取值
* `dict['k']`     : 当dict不存在k时，抛出异常
* `dict.get('k')` : 当dict不存在k时，返回None

### 遍历
* 获取keys列表：`dict.keys()`
* 获取值列表  ：`dict.values()`
* 获取(k,v)元组列表：`dict.items()`
* 获取以上列表的可迭代对象，需要使用`dict.iterkeys(); dict.itervalues(); dict.iteritems()`
```python
for k,v in dict.items():
    print 'key:',k," -value:",v
```

# 转换
* str 转 dict : 
  * `eval()`函数: 使用`eval()`函数可以使字符串转为字典 `eval(str)`
  * `exec()`函数: 需要声明一个被赋值的变量
```python
>>> s="{'k':1,'w':2}"
>>> d=None
>>> exec('d='+s)
>>> d
{'k': 1, 'w': 2}
>>> d['k']
1
>>> 
```
  * json模块：转换带特殊字符的字典
```shell
>>> s='[{"RepoDigests": null,"Created":1466711701,"Size":5042677,"VirtualSize":5042677,"Labels":null}]'
>>> import json
>>> print json.loads(s) 
[{u'Labels': None, u'Size': 5042677, u'RepoDigests': None, u'VirtualSize': 5042677, u'Created': 1466711701}]
>>> 
```
* dict 转 str : `str(dict)`

# 技巧
### 按顺序获取dict的元素
```python
keys=dict.keys()
for k in keys.sort():
    print dict.get('k')

```

### 字典想加
```python
a={1:1}
b={2:2}

c= dict(a,**b) # 返回值为大字典
a.update(b) # 返回值为None,a为大字典
```

### 从大字典取出小字典
```python
dic = {'a': 1, 'b': 2, 'c': 3}
lis = ['a', 'b']

print dict(zip(lis, map(lambda k: dic.get(k), lis)))
```

### 两个元组或列表转字典
```python
k = ['a', 'b', 'c']
v = [1, 2, 3]

print zip(k, v)
print dict(zip(k, v))

```

### 对象列表构造大字典
```python
class E:
   def __init__(self, k, v):
        self.k = k
        self.v = v

e1 = E('a', 1)
e2 = E('b', 2)
e3 = E('c', 3)
l = [e1, e2, e3]

print reduce(lambda o1, o2: dict(o1, **o2),
             map(lambda e: {e.k: e.v}, l))
```
