#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-21 上午12:36
# @Author  : tom.lee
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from downloader import HtmlDownloader
from parser import HtmlParser
from urlsmanager import URLSManager
from writer import FileWriter
from tools import Decorator
from proxypools import Proxy, ProxiesPool


class SpiderWorker(object):
    def __init__(self, url, size=20):
        self.url = url
        self.pool = ProxiesPool()
        self.parser = HtmlParser(url)
        self.url_manager = URLSManager(url_pattern=url, size=size)
        self.writer = FileWriter()

    @Decorator.time
    def start(self):
        self.url_manager.add_url(self.url)
        while self.url_manager.has_next():
            hd = HtmlDownloader(proxies=self.pool.get_proxy_ip())
            url = self.url_manager.get_url()
            data = hd.download(url)
            urls = self.parser.simple_tags(data, 'a', attributes=['href'])
            self.url_manager.add_urls([url_.get('href') for url_ in urls])
            title = self.parser.element(data, 'title')
            title = title.getText() if title else 'unknown'
            self.writer.load_data('[%s] %s' % (title, url))
        self.writer.writer()

p=Proxy()
p.start()
SpiderWorker('http://www.jikexueyuan.com/').start()
p.join()