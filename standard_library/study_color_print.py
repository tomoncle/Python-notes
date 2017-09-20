#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-21 下午2:50
# @Author         : Tom.Lee
# @File           : study_color_print.py
# @Product        : PyCharm

"""
\033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
\033[0m          <!--采用终端默认设置，即取消颜色设置-->
"""

print '\033[1;31;40m '
print '*' * 25, 'LOG', '*' * 25
print 'hello world!'
print '\033[0m'
