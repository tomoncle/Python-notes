# 文件处理

#读取文件

###read()
 一次性读取，读取大文件时容易内存溢出
```python
def read_file():
    with open(path, "r") as f:
        print f.read()   # 一次性读取，容易内存溢出

```
###readlines()
一次性读到列表，读取大文件时容易内存溢出
```python
def read_line_file():
    with open(path, "r") as f:
        for line in f.readlines(): # 一次性读取，容易内存溢出
            print line
```


###读取大文件
1.使用pythonic方式读取大文件（推荐方法）：
```python
def read_big_file(path):
    """
    使用pythonic方式读取大文件
    :param path:
    :return:
    """
    with open(path) as f:  # 文件对象f当作迭代对象， 系统将自动处理IO缓冲和内存管理
        for line in f:
            print line

```
2.按指定大小读取大文件（建议是二进制文件，如果是字符串处理会，出现截取不准确）：
```python

def get_big_file(path, size):
    with open(path, "r") as f:
        while True:
            block = f.read(size)  # 每次读取固定长度到内存缓冲区
            if block:
                yield block
            else:
                return  # 如果读取到文件末尾，则退出
```

#写入文件

###文件复制
使用　pythonic　方式复制文件（推荐方法）:
```python
def copy_file(src, target):
    start = time.time()
    dest = open(target, 'wb+')
    with open(src) as f:  # 文件对象f当作迭代对象， 系统将自动处理IO缓冲和内存管理
        for line in f:
            dest.write(line)
    dest.close()
    print '时长：', time.time() - start, '秒'
```
按指定大小复制文件（以二进制方式打开源文件）:
```python
def copy_file_block(src, target, size):
    start = time.time()
    dest = open(target, 'wb+')
    with open(src, "r") as f:
        while True:
            block = f.read(size)  # 每次读取固定长度到内存缓冲区
            if block:
                dest.write(block)
            else:
                break  # 如果读取到文件末尾，则退出
    dest.close()
    print '时长：', time.time() - start, '秒'

```

#练习：
计算大文件中单词排序个数
```python
    
    import time
    
    start = time.time()
    dic = {}
    with open(path) as f:
        for line in f:
            lit = line.split(";")
            for i in lit:
                if dic.get(i):
                    dic[i] = dic.get(i) + 1
                else:
                    dic[i] = 1
    
    print '时长：', time.time() - start, '秒'
    sort = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    for v in sort:
        print v
```



