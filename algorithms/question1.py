#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 21:56
# @Author  : tom.lee
# @Site    : 
# @File    : question1.py
# @Software:

"""
输入一个数组a，和一个整数k，计算出这个数组随机组成的数字，大于或等于的值中最小的一个

"这个算法有问题．有时间再改吧."
"""

a = [1, 3, 4, 5]
k = 1222

a.sort()
kps = False
ks = list(str(k))
length = len(ks)


def _min(lis, v):
    for n in lis:
        if n < v:
            continue
        else:
            return n
    return None


def deep(start, length, kps):
    for i in range(start, length):
        if kps:
            ks[i] = str(a[0])
        if int(ks[i]) in a:
            continue
        else:
            m = _min(a, int(ks[i]))
            kps = True
            if not m:
                ks[i - 1] = str(a[a.index(int(ks[i - 1]) + 1)])

                deep(i, length, kps)
            else:
                ks[i] = str(m)


deep(0, length, kps)
print ''.join(ks)
