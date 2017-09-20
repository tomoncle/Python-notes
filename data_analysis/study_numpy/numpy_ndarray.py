#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-22 上午12:41
# @Author  : tom.lee
# @File    : study_numpy.py
# @Software: PyCharm

"""
numpy
Numpy是Python的一个科学计算的库，提供了矩阵运算的功能
"""

import numpy as np


def split_line():
    print '*' * 6 ** 2


def np_version():
    """
    版本
    :return:
    """
    print np.version.version


def np_list():
    """
    numpy 数组 ：

    只能存储一种数据结构，
    使用 "numpy.array()"来创建，
    使用" dtype = numpy.类型" 来显示指定

    :return:
    """
    # 创建
    l = np.array([1, 2, 3], dtype=np.int8)
    a = np.array([1, 2, 3, 4])
    b = np.array((5, 6, 7, 8))
    c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
    print 'l:', l
    print 'a:', a
    print 'b:', b
    print 'c:', c
    split_line()

    # 类型
    print l.dtype, c.dtype
    split_line()

    # 大小:  数组a的shape只有一个元素，因此它是一维数组。
    #       而数组c的shape有两个元素，因此它是二维数组，其中第0轴的长度为3，第1轴的长度为4
    print l.shape, c.shape
    split_line()

    # 改变数组每个轴的长度 : 只是改变每个轴的大小，数组元素在内存中的位置并没有改变
    c.shape = 4, 3
    print c
    split_line()

    # 当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度，因此下面的程序将数组c的shape改为了(2,6)
    c.shape = 2, -1
    print c
    split_line()

    # 使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
    # 注意此时数组a和d其实共享数据存储内存区域
    d = a.reshape((2, 2))
    print 'a:', a
    print 'd:', d
    split_line()


def np_list_create():
    # 使用xrange创建一维数组 [start,end,步长)包含起始位置,不包含终止位置,
    # 元素个数: (end-start)/步长
    np_lst = np.arange(0, 10, 1)
    print np_lst
    print '大小:%d' % np_lst.shape
    split_line()

    # 等差数列
    # linspace(strat,end,size), [start,end]包含起始位置和终止位置,一共创建size个元素
    # 可以通过endpoint关键字指定是否包括终值
    print np.linspace(0, 1, 12)
    split_line()

    # 等比数列
    # logspace(开始指数，结束指数，数量，底数默认10)
    print np.logspace(0, 2, 20)
    split_line()


def np_list_by_byte():
    """
    使用frombuffer, fromstring, fromfile等函数可以从字节序列创建数组
    使用时一定要传入dtype参数
    
    Python的字符串实际上是字节序列，每个字符占一个字节，
    因此如果从字符串s创建一个8bit的整数数组的话，所得到的数组正好就是字符串中每个字符的ASCII编码
    :return: 
    """
    s = 'abcdefg'
    print np.frombuffer(s, dtype=np.int8)
    split_line()

    print np.fromstring(s, dtype=np.int8)
    split_line()

    # 如果从字符串s创建16bit的整数数组，那么两个相邻的字节就表示一个整数，
    # 把字节98和字节97当作一个16位的整数， 它的值就是98*256+97 = 25185。
    # 可以看出内存中是以little endian(低位字节在前)方式保存数据的。
    # 所以字符串的长度必须是偶数
    print np.fromstring('abcdefgh', dtype=np.int16)
    split_line()


def np_list_by_func():
    """
    通过函数创建数组
    :return: 
    """
    # fromfunction 传入一个函数，和表示一个维度大小的可迭代对象（元组，列表）
    # 即（10，）表示一维数组，一维元素10个，此时函数接收一个参数
    #   (5,6)表示二维数组，一维元素5个，二维元素6个，此时函数接收2个参数
    print np.fromfunction(lambda x: x + 1, (10,))
    print np.fromfunction(lambda x, y: (x + 1) * (y + 1), (5, 6))
    split_line()


def np_list_opt():
    """
    numpy 列表基本操作和python list基本一致
    :return: 
    """
    l = np.arange(10, 1, -1)
    print l
    print '做小值：', l.min()
    print '最大值：', l.max()
    print '下标0的元素：', l[0]
    split_line()

    # 高级用法，不会共享内存空间，以上操作会共享内存空间
    print l[np.array([1, 5, 3])]  # 使用数组获取下标元素
    print l[[1, 5, 3]]  # 使用列表获取下标元素　
    split_line()

    # 列表直接过滤
    print l[l > 3]  # 直接获取列表大于3的值
    print l > 3  # 判断列表元素是否大于3返回一个boolean 列表
    split_line()


if __name__ == '__main__':
    # np_version()
    # np_list()
    # np_list_create()
    # np_list_by_byte()
    # np_list_by_func()
    # np_list_opt()
    print np.fromfunction(lambda x: x, (10,))
