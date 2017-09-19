#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-7 下午3:15
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : np_mgrid_ogrid.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


# #创建网格索引
"""
>>> import numpy as np


# 密集网格np.mgrid
>>> mgrid = np.lib.index_tricks.nd_grid()
>>> mgrid[0:5,0:5]
array([[[0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]],
       [[0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 2, 3, 4]]])
>>> mgrid[-1:1:5j]
array([-1. , -0.5,  0. ,  0.5,  1. ])


# 稀疏网格np.ogrid
>>> ogrid = np.lib.index_tricks.nd_grid(sparse=True)
>>> ogrid[0:5,0:5]
[array([[0],
        [1],
        [2],
        [3],
        [4]]), array([[0, 1, 2, 3, 4]])]


"""
