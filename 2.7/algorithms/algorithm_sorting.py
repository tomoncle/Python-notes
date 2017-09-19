#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-4-19 上午11:14
# @Author         : Tom.Lee
# @Description    : 
# @File           : algorithm_sorting.py
# @Product        : PyCharm


def bubble_sort():
    """
    冒泡排序：
    n个元素，循环n-1轮，
    每一轮，比较n-i次，选出最大值
    """
    L = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    n = len(L)
    for i in range(1, n):  # 比较n-1轮
        # print n - i
        for j in range(n - i):  # 每i轮比较n-i次，选出最大值
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

    print L


def insertion_sort():
    """
    插入排序算法：
    原序列：[2,3,1,34,5,6,11,7,8]

    下标从0开始：
    第一次：取下标1 和下标[:1]比较
    第二次：取下标2 和下标[:2]比较
    。。。
    第n-1次：取下标n-1(注意此时的元素已经是最后一个元素了)和[:n-1]比较
    共比较n-1次
    """

    L = [9, 8, 7, 5, 6, 4, 3, 2, 1]
    n = len(L)
    for i in range(n - 1):
        for j in range(i + 1):  # 因为下标从0开始，所以第i次，对应的数据位置要 i+1表示当前下标位置
            # print i+1,'-',j
            if L[i + 1] < L[j]: L[i + 1], L[j] = L[j], L[i + 1]

    print L


def selection_sort():
    """
    选择排序算法：

    每次找出最小元素，放置到序列头部，循环序列

    第一次：找出最小放到下标0
    第二次：在剩余找出最小放到下标1
    。。。
    第n-1次
    """
    L = [5, 4, 3, 2, 1, 0, -77]
    n = len(L)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # print i,'-',j
            if L[i] > L[j]: L[i], L[j] = L[j], L[i]

    print L
