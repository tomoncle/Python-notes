#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 1:38
# @Author  : Tom.lee
# @File    : graphs_quadratic.py
# @Software: PyCharm


"""
numpy 多项式 与 matplotlib 二次函数折线图
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np

# 如果最小二乘拟合中的矩阵是秩不足，则引发警告。只有在满 == False时，才会发出警告。
# 警告可以通过以下方式关闭：
warnings.simplefilter('ignore', RuntimeWarning)
warnings.simplefilter('ignore', np.RankWarning)


def foo(x0):
    # 由图可知，函数分3段,周期函数
    # 设：y= kx + b ,且b=0
    c0, hc, c = 0.4, 1.0, 0.6
    if x0 > 1:
        x0 = float(x0) % 1.0
    if x <= c0:
        k = hc / c0
        return k * x0
    elif x < c:
        k = (hc - 0) / (c0 - c)
        return k * (x0 - c)
    else:
        return 0


# x 的取值 0到2 范围取50个点
x = np.linspace(0, 2, 50, dtype=np.float64)

# 计算对应的y值，并转换为nparray 对象
y = np.array(map(foo, x)).astype(np.float64)

print "x值：", x
print "y值：", y

m = np.polyfit(x, y, 20)  # 调整拟合多项式的度为20，生成多项式参数
print "多项式参数：", m


# 一维多项式
p1 = np.poly1d(m)  # 根据多项式参数构造一维多项式
print "一维多项式：", p1

# 根据x使用多项式求解y值，
# yp=np.polyval(np.polyfit(x, y, 20),x)，x可以是单个值也可以是列表
y1 = p1(x)
print "一维多项式根据x的计算值：", y1

# 以点（“．”）绘制实际值折线
plot1 = plt.plot(x, y, '.', label='original values')
# 以线（“r”）绘制最小二乘拟合折线
plot2 = plt.plot(x, y1, 'r', label='polyfit values')

# x轴描述
plt.xlabel('X')
# Y轴描述
plt.ylabel('Y')
# plt.legend(loc=1)  # 指定legend的位
# 标题
plt.title('y = kx (0<x<0.6) | y = 0 (0.6<x<=1)')

# 保存文件　eps, pdf, pgf, png, ps, raw, rgba, svg, svgz.
plt.savefig("../save_file/graphs_quadratic.png")
plt.show()
