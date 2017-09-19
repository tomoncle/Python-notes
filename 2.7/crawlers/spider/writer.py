#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-21 上午12:17
# @Author  : tom.lee
# @Site    : 
# @File    : writer.py
# @Software: PyCharm
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class FileWriter(object):
    def __init__(self, file_name=None):
        self.file_name = file_name or 'data.txt'
        self._data = []

    def load_data(self, data):
        if not data:
            return
        self._data.append(data)

    def writer(self):
        f = open(self.file_name, 'wb+')
        [f.write('%s\n\n' % d) for d in self._data]
        f.close()
