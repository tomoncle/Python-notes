#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 13:12
# @Author  : Tom.lee
# @Site    : 
# @File    : numpy_list_multidimensional.py
# @Software: PyCharm

"""
numpy 多维数组
"""
import numpy as np


def split_line():
    print '*' * 6 ** 2


a = np.arange(10, 0, -1)
print a
b = np.arange(100, 200, 10)
print b
split_line()


def multi_2():
    """
    构建 x,y 二维数组
    
    reshape(纵轴高度,横轴高度)
    :return: 
    """
    y = a.reshape(-1, 1)  # 表示y轴
    x = b  # 表示x轴
    xy = y + x  # 表示y轴元素与x序列每个元素想加
    print xy

    print '下标（5,5）：', xy[5, 5]
    print xy.shape
    split_line()


def multi_2_func():
    """
    使用函数创建2维数组
    :return: 
    """
    print np.fromfunction(lambda x, y: (x + 1) * y, (10, 5))
    split_line()


def sin():
    """
    正弦函数
    :return: 
    """
    x = np.linspace(0, 2 * np.pi, 10)

    # 使用np.sin(x)对 每个x中的元素求正弦值,x值不变
    y = np.sin(x)
    print x, '\n', y
    split_line()

    # 使用np.sin(x,x) 对每个x中的元素求正弦值，并赋值给x, 即x,z 共享内存空间
    z = np.sin(x, x)
    print x, '\n', z
    split_line()


if __name__ == '__main__':
    # multi_2()
    # multi_2_func()
    sin()
