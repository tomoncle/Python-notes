# python 中一些常用的技巧

##### 转义
* Python中`"%"`的转义是`"%%"`

##### float类型保留小数：
```python
b = float('%0.6f'%0.12345678)
print b   #0.123457
```

##### url检测
```python
url = 'https://www.baidu.com/'

print url.rstrip('/')
print url.rstrip('/')+'/home'
```

##### url 转换函数
```python
import urlparse
urlparse.urljoin('http://www.aa.com:90/aa.html', '/abc.html')
# http://www.aa.com:90/abc.html


from __future__ import print_function

import urlparse

u = urlparse.urlparse('029_t002661t9gt.321002.2.ts?index=29&start=310000&end=320400')
query_params = dict([s.split('=') for s in u.query.split('&')])
print('query_params : {}'.format(query_params))
# query_params : {'index': '29', 'end': '320400', 'start': '310000'}
```

##### 去空格
```python
s = ' 1 2 3 4 5 6 '

print '|%s|' % s.lstrip(' ')  # 去除左边空格 |1 2 3 4 5 6 |
print '|%s|' % s.rstrip(' ')  # 去除右边空格 | 1 2 3 4 5 6|
print '|%s|' % s.strip(' ')  # 去除两边空格  |1 2 3 4 5 6|
print '|%s|' % s.replace(' ', '')  # 去除所有空格 |123456|
```

##### 显示有限的接口到外部
```
当发布python第三方package时, 并不希望代码中所有的函数或者class可以被外部import,
在__init__.py中添加__all__属性,
该list中填写可以import的类或者函数名, 可以起到限制的import的作用, 防止外部import其他函数或者类
```

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import utils

__all__ = ['utils']
```

---
## Python博客
* 关于`raw_input()` 和 `input()` ：http://www.cnblogs.com/way_testlife/archive/2011/03/29/1999283.html


