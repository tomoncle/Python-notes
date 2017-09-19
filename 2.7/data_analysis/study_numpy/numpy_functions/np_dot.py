#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-7 下午3:07
# @Author         : Tom.Lee
# @File           : np_dot.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
import numpy as np

"""
>>> import numpy as np
Examples
--------

>>> np.random.rand(3,2)
array([[ 0.14022471,  0.96360618],  #random
       [ 0.37601032,  0.25528411],  #random
       [ 0.49313049,  0.94909878]]) #random


>>> np.dot(3, 4)
12

Neither argument is complex-conjugated:

>>> np.dot([2j, 3j], [2j, 3j])
(-13+0j)

For 2-D arrays it is the matrix product:

>>> a = [[1, 0], [0, 1]]
>>> b = [[4, 1], [2, 2]]
>>> np.dot(a, b)
array([[4, 1],
       [2, 2]])

>>> a = np.arange(3*4*5*6).reshape((3,4,5,6))
>>> b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
>>> np.dot(a, b)[2,3,2,1,2,2]
499128
>>> sum(a[2,3,2,:] * b[1,2,:,2])
499128

"""

# ############################### 一维 ###############################
"""
参数个数相同：
"""

print np.dot(3, 4)  # 3*4 -> 12
print np.dot([1, 2, 3], [4, 5, 6])  # 1 * 4 + 2 * 5 + 3 * 6 -> 32

"""
参数列表不同(短的参数元素个数只能为1,且不能为列表[]类型):
如：
>>> np.dot([1, 2, 3], [4, 5])
ValueError: shapes (3,) and (2,) not aligned: 3 (dim 0) != 2 (dim 0)

>>> np.dot([1, 2, 3], [4])　
ValueError: shapes (3,) and (1,) not aligned: 3 (dim 0) != 1 (dim 0)

>>> np.dot([1, 2, 3], 4)
[ 4  8 12]

"""
print np.dot([1, 2, 3], 4)  # [1*4,2*4,3*4] -> [ 4  8 12]


# ############################### 二维 ###############################
"""
参数个数相同：

计算过程:

第一轮:
    1. A中取第一个元素[x1, y1]
       B中取各个元素中的第一个值[m1, m2]
       矩阵相乘-> x1*m1+y1*m2

    2. A中取第一个元素[x1, y1]
       B中取各个元素中的第二个值[n1, n2]
       矩阵相乘-> x1*n1+y1*n2
--> [[ 77 110]]
第二轮:
    1. A中取第二个元素[x2, y2]
       B中取各个元素中的第一个值[m1, m2]
       矩阵相乘-> x2*m1+y2*m2

    2. A中取第二个元素[x2, y2]
       B中取各个元素中的第二个值[n1, n2]
       矩阵相乘-> x2*n1+y2*n2
--> [[ 77 110] [165 242]]


"""

x1, y1 = 1, 2
x2, y2 = 3, 4

m1, n1 = 11, 22
m2, n2 = 33, 44

A = [[x1, y1], [x2, y2]]  # 行
B = [[m1, n1], [m2, n2]]  # 列

print np.dot(A, B)
# [[ 77 110]
#  [165 242]]

print '测试计算过程:'
print x1 * m1 + y1 * m2, x1 * n1 + y1 * n2  # 77 110
print x2 * m1 + y2 * m2, x2 * n1 + y2 * n2  # 165 242


def my_dot_w2(a, b):
    # 判断是否为列表
    if isinstance(a, list) and isinstance(b, list):
        assert len(a) == len(b)
        l1, l2 = a, b
        result = []

        if isinstance(l1[0], list):  # 判断是否为多维数组
            size = len(l1)
            for index, value in enumerate(l1):
                start, cell = 0, []

                while start < size:
                    cell.append(my_dot_w2(value, map(lambda x: x[start], l2)))
                    start += 1

                result.append(cell)
            return result

        else:  # 一维数组
            return sum(map(lambda j: l1[j] * l2[j], xrange(len(l1))))

    # 以下为数字与数组的矩阵算法，找出集合
    elif isinstance(a, list) and isinstance(b, int):
        return map(lambda x: x * b, a)

    elif isinstance(b, list) and isinstance(a, int):
        return map(lambda x: x * a, b)

    # 都为数字的算法
    elif isinstance(a, int) and isinstance(b, int):
        return a * b

    # 其他情况抛出异常
    else:
        raise Exception('params must be "list or int"!')


print '**' * 50
print my_dot_w2([1, 2], 3)  # 1*3,2*3 = [3, 6]
print np.dot([1, 2], 3)

print my_dot_w2(3, [1, 2])  # 3*1,3*2 = [3, 6]
print np.dot(3, [1, 2])

print my_dot_w2([1, 2], [3, 4])  # 1*3+2*4 = 11
print np.dot([1, 2], [3, 4])

print my_dot_w2(A, B)
print np.dot(A, B)





