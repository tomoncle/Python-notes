#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 20:49
# @Author  : Tom.lee
# @Site    : 
# @File    : graphs_histogram.py
# @Software: PyCharm

"""
直方图
"""
import matplotlib.pyplot as plt
import numpy as np

N = 5
# 男生分数
menMeans = (20, 35, 30, 35, 27)
# 女生分数
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, color='#d62728', yerr=menStd)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))  # 设置x轴刻度
plt.yticks(np.arange(0, 81, 5))  # 设置y轴刻度
plt.legend((p1[0], p2[0]), ('Men', 'Women'))
plt.savefig("../save_file/graphs_histogram.png")
plt.show()
