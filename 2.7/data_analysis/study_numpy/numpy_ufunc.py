#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/23 21:51
# @Author  : Tom.lee
# @Site    : 
# @File    : numpy_ufunc.py
# @Software: PyCharm

"""
ufunc是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。
NumPy内置的许多ufunc函数都是在C语言级别实现的，因此它们的计算速度非常快
"""
import numpy as np


def foo(x):
    # 由图可知，函数分3段,周期函数
    # 设：y= kx + b ,且b=0
    c0, hc, c = 0.4, 1.0, 0.6
    if x > 1:
        x = float(x) % 1.0
    if x <= c0:
        k = hc / c0
        return k * x
    elif x < c:
        k = (hc - 0) / (c0 - c)
        return k * (x - c)
    else:
        return 0


X = np.linspace(0, 2, 20)
Y = np.array(map(foo, X))
print X
print Y
