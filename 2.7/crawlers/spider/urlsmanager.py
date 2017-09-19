#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-19 下午10:18
# @Author  : tom.lee
# @Site    : 
# @File    : urlsmanager.py
# @Software: PyCharm
import urlparse


class URLSManager(object):
    def __init__(self, url_pattern=None, size=None):
        self.url_pattern = url_pattern
        self.size = size
        self.pending_urls = set()
        self.processed_urls = set()

    def has_next(self):
        return len(self.pending_urls) > 0

    def add_url(self, url):
        if not url:
            return
        url = url.rstrip('/')
        if self.url_pattern and urlparse.urlparse(
                self.url_pattern).netloc != urlparse.urlparse(url).netloc:
            return
        if url in self.pending_urls | self.processed_urls:
            return
        if self.size and len(self.processed_urls) >= self.size:
            self.pending_urls = set()
            return
        self.pending_urls.add(url)

    def add_urls(self, urls):
        if not urls:
            return
        [self.add_url(url) for url in urls]

    def get_url(self):
        url = self.pending_urls.pop()
        self.processed_urls.add(url)
        return url
