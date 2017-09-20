#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-22 上午1:18
# @Author  : tom.lee
# @Site    : 
# @File    : study_filter.py
# @Software: PyCharm

"""
按照某种规则过滤掉一些元素

接收一个 boolean返回值的函数，可用时lambda,可以是自定义的函数，
迭代传入的可迭代对象的每个元素进行过滤
"""

lst = [1, 2, 3, 4, 5, 6]
# 所有奇数都会返回True, 偶数会返回False被过滤掉
print filter(lambda x: x % 2 != 0, lst)
# 输出结果 [1, 3, 5]

