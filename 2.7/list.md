# list 列表
列表list为Python的有序集合，列表的下标从0开始，`list[0]`获取第一个元素；列表支持倒序操作；`list[-1]`获取列表倒数第一个元素。
在python终端，使用`dir(list)`获取方法及属性列表，使用`help(list)`获取其使用方法,　可变对象

# 基本操作
### 声明

```python
# 创建一个空列表
list_val = []

# 声明并赋值,可以是不同的类型
list_val = [1,2,2,'abc',[1,2,3],{'k':v}]
```
### 添加
* `list.append(val)`追加到列表尾部；
* `list.insert(index,val)`按下标插入到列表内部任意位置

### 删除
注意删除元素时，要判读该元素是否存在列表中`if 5 in list: list.remove(5)` 或者 `if index < len(list): list.pop(index)`
* `list.remove(val)` 删除列表元素；注意要判读该元素是否存在列表中`if 5 in list: list.remove(5)`
* `list.pop()` 删除尾部元素，并返回该元素的值 
* `list.pop(index)` 删除指定位置的元素，并返回该元素的值 
* `del list[index]` 删除指定位置的元素，没有返回值
* `del list` 删除整个列表，没有返回值

### 修改
* `list[index] = new_val` 使用下标更新列表元素

# 排序
### sort()永久排序
`list.sort()` 使用sort()方法对list列表进行永久排序，没有参数默认根据数字升序，字母顺序排序
`list.sort(reverse=True)` 使用sort()方法的reverse=True参数对list列表进行永久排序，按与默认顺序相反的顺序排序
```python
list=[1,'a',3,2]

list.sort()  # 该方法没有返回值 print list.sort() >> None
print list   # [1,2,3,'a']

```

### sorted()临时排序
`sorted()`方法的排序规则与sort()方法相同
```python
list=[1,3,2]

print sorted(list)  # [1,2,3]
print list 			# [1,3,2]

```

### reverse()列表反转
使用`reverse()`方法使列表元素顺序发生反转，注意该方法对列表的改变是永久的
```python
list=[1,2,3]

print list   			# [1,2,3]

list.reverse()    		# None, 该方法没有返回值
print list              	# [3,2,1] ,使用`reverse()`方法永久的改变了列表的元素位置


```
---
# 确定列表长度
使用`len()`函数获取列表长度，如：`list=[1,2,3] ; print len(list) >> 3`

---
# 遍历
* 带下标遍历:
```python
x = [11, 12, 13, 14, 15]
for index, value in enumerate(x):
    print index, ':', value
```

* 简单遍历:
```python
for val in list:
   print val
```

* 精简操作,使用列表解析式: `[表达式 for v in list]` 返回一个新的列表
```python
num_list = [1, 2, 3] # [1,2,3]

# 简单的列表解析式
num_list = [v+1 for v in num_list] # [2,3,4]

# 嵌套的列表解析式
ww, ll = ['1', '22', '333', '4444'], []
for w in ww:
    for l in w:
        ll.append(l)

print ll
print [l for w in ww for l in w]

"""结构变形
print[l 
      for w in ww 
         for l in w]

"""
```

---
# 切片
注意参数start,end为列表下标：
* `list[start:stop]` # [start,stop)
* `list[:stop]`      # [0,end)
* `list[:-1]`        #[0,len-1) 即返回列表的前len-1个元素
* `list[start:]`     # [start,len)
* `list[-1:]`        # [len-1,len)
* `list[:]`          # [0,len) ,copy
* `list[::2]`   # 先取2个元素组成元组,(0,1),(2,3),(4,5)，然后取下标为1的值 ==>[0,2,4]
* `list[::-1]`  # 先取1个元素组成元组，(5,),(4,)(3,),(2,),(1,),(1,) >> [5,4,3,2,1,0] 列表反转的技巧

### 拓展切片
**注：list[i:j:stride]：**表示拓展切片，i表示起始索引，j表示终止索引，stride表示步长，stride默认为1,只能为非0整数
* stride正数：切片从左往右切，切出[i:j),然后按照stride的值，进行获取，表示相隔(stride-1)个元素取出一个元素，组成新列表
* stride负数：切片从右往左切，因为从右往左切，所以此时，j为起始索引，ｉ为终止索引，切出[j:i],所以"i的值要大于j",
              注意此时起始下标默认为None,假如起始下标j=0，表示从第二个元素开始，包含终止索引然后按照stride的值，进行获取

**举例**：



# 列表的引用
如果你将列表list赋值给变量a,而将a赋值给b,则a,b两个变量指向的位置时一样的，所以你改变b时，a也会发生相同的变化
```python
a = [1,2,3]
b = a

print a     # [1,2,3]
print b     # [1,2,3]

b.append(4) 
print a     # [1,2,3,4]
```
如何避免不更改原来的列表?
* 列表复制:`new_list = old_list[:]`,但这种方法只适用于简单列表，也就是列表中的元素都是基本类型，
如果列表元素还存在列表的话，这种方法就不适用了。原因就是，象a[:]这种处理，只是将列表元素的值生成一个新的列表，如果列表元素也是一个列表，如：a=[1,[2]]，那么这种复制对于元素[2]的处理只是复制[2]的引用，而并未生成 [2]的一个新的列表复制
```
>>> a=[1,[2]]
>>> b=a[:]
>>> b
[1, [2]]
>>> a[1].append(3)
>>> a
[1, [2, 3]]
>>> b
[1, [2, 3]]
```
* 使用copy模块中的deepcopy函数:
```
>>> import copy
>>> a=[1,[2]]
>>> b=copy.deepcopy(a)
>>> b
[1, [2]]
>>> a[1].append(3)
>>> a
[1, [2, 3]]
>>> b
[1, [2]]
```

# 转换
“字符串”原理上其实是一个个字符的列表，所以 `str='ab0'; list=list(str) >> ['a','b',0]`,
所以对字符串进行截取时，可以先转换为列表处理，然后利用`join()`函数再转换为字符串
* str 转 list : `list(str)`
* list 转 str : `''.join(list)`

“字典”是成对存在的，所以要转换时，保证列表的对称
* list 转 dict : 
```
>>> list_k=['a','b','c','d']
>>> list_v=[1,2,3,4]
>>> dict(zip(list_k,list_v))
{'a': 1, 'c': 3, 'b': 2, 'd': 4}
>>> 
```
如果列表中元素为 元素个数为2的列表，可用直接使用dict(list)来转换，如`dict([['a',1],['b',2]])`

* dict 转 list :
```
>>> keys=dict.keys()
>>> keys
['a', 'c', 'b', 'd']
>>> values=dict.values()
>>> values
[1, 3, 2, 4]
>>>
```
元组()与set()可用直接使用同名函数，互相转换，如：`list((1,2))， tuple([1,2,3])`


# 常用函数
### range()函数
`range()`函数可以返回一个数值列表：`range(5)`返回`[0, 1, 2, 3, 4]`注意第一个元素是从0开始，
在python 终端，你可以使用`help(range)`查看`range()`函数的使用方法：
```
range(...)
    返回包含整数的列表。

    range(stop) -> 返回一个数值列表，stop指定终止值,但不包含
    range(4) >> [0, 1, 2, 3]. 
    
    range(start, stop[, step]) -> 返回一个数值列表,可用start指定起始值，setp指定步长，当给定步长时，它指定增量（或递减）
    range(i, j)   >> [i, i+1, i+2, ..., j-1]; start (!) 默认从0开始.
    range(1,10,2) >> [1, 3, 5, 7, 9]

```
### min()函数
`min()`返回一个**可迭代**对象中最小的值或**传入多个参数**的最小参数，`help(min)`查看帮助文档
```
min(...)
    min(iterable[, key=func]) -> value
    min(a, b, c, ...[, key=func]) -> value
    
    With a single iterable argument, return its smallest item.
    With two or more arguments, return the smallest argument.
(END)

```
举例：
```
>>> min([1,2,34])
1
>>> min([1,2,34],0)
0
>>> 
>>> min(['a',2,34])
2

```

# 技巧
### list列表想加
```
list = list1+list2
```




