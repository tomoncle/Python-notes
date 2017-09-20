#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-8 下午1:50
# @Author         : Tom.Lee
# @File           : study_itertools.py
# @Product        : PyCharm
# @Source         :


import itertools

"""
合并多个词为一个列表:　
>>>itertools.chain(*iterable)
"""
lst = itertools.chain('hello', 'world', '!')
print type(lst)  # <type 'itertools.chain'>
print list(lst)  # ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '!']

"""
返回指定长度的序列中的字符"组合"(排列组合):
>>>itertools.combinations(iterable, r)
"""
lst1 = itertools.combinations('abc', 2)
print list(lst1)  # [('a', 'b'), ('a', 'c'), ('b', 'c')]

"""
返回指定长度的“组合”，组合内元素可重复:
>>>itertools.combinations_with_replacement(iterable, r)
"""
ls2 = itertools.combinations_with_replacement('abc', 2)
print list(ls2)
