#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-4 上午11:21
# @Author         : Tom.Lee
# @Description    : http://blog.csdn.net/gzlaiyonghao/article/details/1483728 
# @File           : test.py
# @Product        : PyCharm

import re

"""
Levenshtein Distance 编辑距离算法,计算字符串相似度

    比如要计算cafe和coffee的编辑距离。cafe→caffe→coffe→coffee 为3
先创建一个6×8的表（cafe长度为4，coffee长度为6，各加2）＊代表空白占位符

*	*	c	o	f	f	e	e

*   0	1	2	3	4	5	6

c	1	0	1	2	3	4	5

a	2	1	1	2	3	4	5

f	3	2	2	1	2	3	4

e	4	3	3	2	2	2	3


从3,3格开始，开始计算。取以下三个值的最小值：
1.如果最上方的字符等于最左方的字符，则为左上方的数字。否则为左上方的数字+1。（对于3,3来说为0）
2.左方数字+1（对于3,3格来说为2）
3.上方数字+1（对于3,3格来说为2）
"""

a = 'cafee'
b = 'cof1ee'


def minimum(a, b):
    m, n = len(a), len(b)
    col_size, matrix = m + 1, []
    for i in range((m + 1) * (n + 1)):
        matrix.append(0)
    for i in range(col_size):
        matrix[i] = i
    for i in range(n + 1):
        matrix[i * col_size] = i
    for i in range(n + 1)[1:n + 1]:
        for j in range(m + 1)[1:m + 1]:
            if a[j - 1] == b[i - 1]:
                cost = 0
            else:
                cost = 1
            min_value = matrix[(i - 1) * col_size + j] + 1
            if min_value > matrix[i * col_size + j - 1] + 1:
                min_value = matrix[i * col_size + j - 1] + 1
            if min_value > matrix[(i - 1) * col_size + j - 1] + cost:
                min_value = matrix[(i - 1) * col_size + j - 1] + cost
            matrix[i * col_size + j] = min_value
    return matrix[n * col_size + m]


s1 = 'Invalid input for operation: Requested subnet with cidr: 172.16.17.0' \
     '/24 for network: c6aa9c38-ccee-467f-a1e7-c718a33ecc06 overlaps with another subnet.'

s2 = 'Invalid input for operation: Requested subnet with cidr: 192.168.11.0/24' \
     ' for network: 028d91af-b461-4d9d-ab76-da4a8845d3cf overlaps with another subnet.'


def pop_cidr_uuid(s):
    s = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])/24', re.S).sub('', s)
    s = re.compile(r'([a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12})', re.S).sub('', s)
    return s


s001 = 'Invalid input for operation: Requested subnet with cidr:  for network:  overlaps with another subnet.'
print minimum(s001, pop_cidr_uuid(s1))
