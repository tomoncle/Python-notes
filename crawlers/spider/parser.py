#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-19 下午10:10
# @Author  : tom.lee
# @Site    : 解析器
# @File    : parser.py
# @Software: PyCharm



import urlparse

import bs4


class HtmlParser(object):
    """
    网页解析器，可以继承此类，实现更复杂功能
    """
    url_filed = 'href'
    parser = 'html.parser'
    encoding = 'utf-8'

    def __init__(self, base_url=None):
        self.__base_url = base_url

    def simple_tags(self, data, tag=None, patterns=None, attributes=None):
        """
        单个标签解析
        """
        tags = self.__parser_tags(data, tag, patterns)
        return self.__tags(tags, attributes)

    def multilevel_tags(self, data, multilevel_patterns=None, attributes=None):
        """
        多标签解析
        """
        if not multilevel_patterns:
            return data

        for tag_patterns in multilevel_patterns:
            tag, patterns = tag_patterns.items()[0]
            data = self.__parser_tags(data, tag, patterns)
            multilevel_patterns.remove(tag_patterns)

            if not multilevel_patterns:
                return self.__tags(data, attributes)

            return self.multilevel_tags(data, multilevel_patterns, attributes)

    def element(self, data, tag=None, patterns=None):
        """
        查询符合条件的第一个标签元素
        """
        elements = self.elements(data, tag, patterns)
        return elements[0] if elements else None

    def elements(self, data, tag=None, patterns=None):
        return self.__parser_tags(data, tag, patterns)

    def __tags(self, data, attributes=None):
        tags = [dict(tag_.attrs, text='%s'.encode(self.encoding) % tag_.getText())
                for tag_ in data]

        if not attributes:
            return tags

        for tag_attr in tags:
            for k, v in tag_attr.items():
                if k in attributes:
                    continue
                tag_attr.pop(k)

        if self.__base_url:
            return self.__format_url(tags)

        return tags

    def __parser_tags(self, data, tag=None, patterns=None):
        return self.__data_parser(data).find_all(tag, patterns)

    def __data_parser(self, data):
        return bs4.BeautifulSoup(str(data), self.parser, from_encoding=self.encoding)

    def __format_url(self, maps):
        for m in maps:
            if not m.get(self.url_filed):
                continue
            m[self.url_filed] = urlparse.urljoin(self.__base_url, m.get(self.url_filed))
        return maps
