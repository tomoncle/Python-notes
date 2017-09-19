#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-4-20 下午1:53
# @Author         : Tom.Lee
# @Description    : 
# @File           : test.py
# @Product        : PyCharm

import re
import urlparse

import bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">标题</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# print html_doc


soup = bs4.BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')
pattern = {'class': 'sister', 'id': re.compile(r'^link\d+$')}
data = soup.find_all('a', pattern)
print data

# 对象属性
print data[0]
print data[2].getText()
print data[0].contents
print data[0].attrs


#
# tags_a = soup.find_all(name='a', attrs={'class': 'sister'})
# for a in tags_a:
#     print type(a), a.get('id'), a.get('href'), a.get('no_found')
#     print dict(a.attrs, tag_name=a.getText())
print isinstance(data,bs4.element.ResultSet)
bs4_str = ' '.join([str(_tag) for _tag in data])
sp = bs4.BeautifulSoup(bs4_str, "html.parser", from_encoding='utf-8')
data = sp.find_all('a', pattern)
print data
print data[2].getText()


# 字符串拼接
# print urlparse.urljoin('https://www.baidu.com', '//www.ji.com')