#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 13:44
# @Author  : Tom.lee
# @File    : numpy_polynomial_poly1d.py
# @Software: PyCharm

"""
多项式
"""
import numpy as np

# 构造多项式
p1 = np.poly1d([1])  # 1
p2 = np.poly1d([1, 2])  # x + 2
p3 = np.poly1d([1, 2, 3])  # x^2 + 2x + 3
p4 = np.poly1d([1, 2, 3, 4])  # x^3 + 2* x^2 + 3x + 4
print '\np1:', p1
print '\np2:', p2
print '\np3:', p3
print '\np4:', p4
# 评估x = 0.5处的多项式：
print '\n\n求函数0.5处的值：'
print p1(0.5), 1
print p2(0.5), 0.5 + 2
print p3(0.5), 0.5 ** 2 + 2 * 0.5 + 3
print p4(0.5), 0.5 ** 3 + 2 * 0.5 ** 2 + 3 * 0.5 + 4
# 解
print '\n\n解：'
print p1.r
print p2.r
print p3.r
print p4.r


print "*" * 20, 'Y = X + 1', "*" * 20
x = np.linspace(0, 1, 10)  # 构造x
y = np.array(map(lambda x: x + 1, x))  # 计算y
m = np.polyfit(x, y, 2)  # 拟合多项式参数
y1 = np.poly1d(m)  # 构造多项式
print "\nx取值：", x
print "\ny取值：", y
print "\n多项式参数：", m
print "\n一维多项式：", y1
print "\n使用一维多项式计算y值：", y1(x)
print "\n计算一维多项式的解：", y1.r
print "\n比较多项式与函数计算的结果：", "多项式：", y1(120), " 函数：", 120 + 1
