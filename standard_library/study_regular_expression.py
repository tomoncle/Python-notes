#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-11 上午11:56
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : *regular_expression.py
# @Product        : PyCharm
# @docs           : http://www.cnblogs.com/dreamer-fish/p/5282679.html

import re

"""
正则表达式: r'[...]'　,[]内为要匹配的字符，用"|"来表示多种匹配

1.特殊符号使用"\"转义：　"[" --> "\["
2.替换字符串：将123替换为空 re.compile(r'[123]').sub('', str)
3.查找特殊字符： 使用r'[...]'表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'

"""

# **********************替换字符***********************
#
#   re.compile(r'[...]').sub('', str)
#
# **********************替换字符***********************


# 1.去掉字符串中无用的字符 "[u'","'", "u'" ,"']"
s = "[u'node-2.domain.tld', u'node-1.domain.tld']"
s1 = re.compile(r"[\[u'|'\]| u']").sub('', s).split(',')
print s1, type(s1)  # ['node-2.domain.tld', 'node-1.domain.tld'] <type 'list'>

# 2.替换空格为'--'
print re.compile(r'\s').sub('--', '1234 56 ')  # 1234--56--

# **********************匹配查找字符***********************
#
#   re.findall(r'*', content)　默认匹配每一行字符串为查找对象
#   re.findall(r'[\d+]', s, re.S) 匹配时以整个字符串为查找对象
#
# **********************匹配查找字符***********************

# 1.提取字符中的数字
s = '123abc456@#$%^7890'
print re.findall(r'[\d+]', s)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print re.findall(r'\d+', s, re.S)  # ['123', '456', '7890']

# 2.匹配Cidr  172.16.6.18/24
print re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])/24', s, re.S)
# 3.匹配uuid  c6aa9c38-ccee-467f-9a1e-c718a33ecc06
print re.findall(r'([a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12})', s, re.S)

s = "You are not permitted to modify 'architecture' on this image."
# 4.匹配单引号之内的值　(?<=').*?(?=')
print re.findall(r"(?<=').*?(?=')", s, re.S)  # ['architecture']
