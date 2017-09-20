#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-7 下午3:10
# @Author         : Tom.Lee
# @File           : np_arange.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import numpy as np


# 四维数组
t = np.arange(3 * 4 * 5 * 6).reshape((3, 4, 5, 6))
print len(t), len(t[0]), len(t[0][0]), len(t[0][0][0])

s = np.arange(3 * 4 * 5 * 6)[::-1].reshape((5, 4, 6, 3))
print len(s), len(s[0]), len(s[0][0]), len(s[0][0][0])
