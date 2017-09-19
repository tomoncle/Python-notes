#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-31 下午2:43
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : graphs_trigonometric.py
# @Product        : PyCharm

import matplotlib.pyplot as plt
import numpy as np


# 三角函数图
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# 计算函数值
y_cos, y_sin = np.cos(x), np.sin(x)

# 设置横轴和纵轴的界面高度与宽度
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(y_sin.min() * 1.1, y_sin.max() * 1.1)
# 横轴和纵轴描述

# 设置刻度值
plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True))
plt.yticks(np.linspace(-1, 1, 11, endpoint=True))

# 设置坐标轴的位置 Spines
ax = plt.subplot(1, 1, 1)
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 画图
# 对线条的颜色，宽度进行设置
plt.plot(x, y_sin, color='red', linewidth=2.5, label='sin(x)')
plt.plot(x, y_cos, color='blue', linewidth=2.5, label='cos(x)')
plt.legend(loc='upper left', frameon=False)
plt.title('trigonometric function')
plt.savefig("../save_file/graphs_trigonometric.png")
plt.show()
