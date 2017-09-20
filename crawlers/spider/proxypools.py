#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-22 下午11:04
# @Author  : tom.lee
# @Site    : 代理池
# @File    : proxyspools.py
# @Software: PyCharm
import logging
import re
import threading
import time
import random

from tools import ReThread
from downloader import HtmlDownloader
from parser import HtmlParser

lock = threading.Lock()


class ProxiesPool(object):
    __instance = None
    __pool = []

    def __new__(cls, *args):
        if not ProxiesPool.__instance:
            try:
                lock.acquire()
                if not ProxiesPool.__instance:
                    ProxiesPool.__instance = object.__new__(cls, *args)
            except Exception, e:
                logging.error('ProxiesPool: init error : %s' % e)
            finally:
                lock.release()
        return ProxiesPool.__instance

    @property
    def pool(self):
        return self.__pool

    def add(self, ip):
        if not ip:
            return
        self.__pool.append(ip)

    def get_proxy_ip(self):
        if self.pool:
            proxies = self.pool[random.randint(0, len(self.pool) - 1)]
        else:
            proxies = None
        print proxies
        return proxies

    def __setattr__(self, key, value):
        pass

    def __dict__(self):
        pass


class Proxy(ReThread):
    proxy_site = 'http://www.xicidaili.com/nn'

    def run(self):
        while self.is_running:
            self.__update_proxy_pool()
            time.sleep(60 * 15)

    @staticmethod
    def __re_number(s):
        if not s:
            return 0
        return float('%0.2f' % float(re.sub('[^\d+.\d+$]', '', s)))

    def __update_proxy_pool(self):
        downloader = HtmlDownloader()
        proxy_pool = ProxiesPool()
        parser = HtmlParser()
        data = downloader.download(self.proxy_site)
        speed_times = parser.multilevel_tags(data, [{'tr': None}, {'div': {'class': 'bar'}}])
        ip_data = parser.elements(data, 'tr')[1:]
        speed = speed_times[::2]
        times = speed_times[1::2]
        for i, ip in enumerate(ip_data):
            d = {}
            for j, value in enumerate(filter(lambda x: x, ip_data[i].text.split('\n'))):
                if j == 0:
                    d['ip'] = value
                elif j == 1:
                    d['port'] = value
                continue
            if len(d.keys()) != 2:
                continue
            if self.__re_number(speed[i].get('title')) > 1 \
                    or self.__re_number(times[i].get('title')) > 1:
                continue

            proxy_pool.add({'http': '%s:%s' % (d.get('ip'), d.get('port'))})

