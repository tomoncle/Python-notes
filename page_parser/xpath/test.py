#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-5-6 下午1:10
# @Author  : tom.lee
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from lxml import etree

f = open('file.txt')
content = f.read()
selector = etree.HTML(content)

divs = selector.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]')
for r in divs:
    item_ = None or {}
    item_['title'] = r.xpath('a/div/text()')[0]
    item_['link'] = r.xpath('a/@href')[0]
    item_['desc'] = r.xpath('div/text()')[0].replace('\n', '').strip()
    print item_
