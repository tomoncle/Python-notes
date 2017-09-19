#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-4-19 下午10:26
# @Author  : tom.lee
# @Site    : 
# @File    : downloader.py
# @Software: PyCharm
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# from .tools import Dir


class HtmlDownloader(object):
    openSSL_error = "'X509' object has no attribute '_x509'"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Ubuntu Chromium/50.0.2661.102 ' \
                 'Chrome/50.0.2661.102 Safari/537.36'

    def __init__(self, headers=None, cookies=None, timeout=10, proxies=None, verify=False):
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.proxies = proxies
        self.verify = verify

    def _make_headers(self):
        headers = self.headers or {}
        if not headers.get('User-Agent'):
            headers['User-Agent'] = self.user_agent
        if self.cookies:
            headers['Cookie'] = self.cookies
        return headers

    def _request(self, url):
        try:
            resp = requests.get(
                url, headers=self._make_headers(), timeout=self.timeout,
                proxies=self.proxies, verify=self.verify)
            return resp.status_code, resp.content
        except requests.exceptions.Timeout:
            logging.error('requests timeout: %s' % url)
            return 502, None
        except requests.exceptions.RequestException:
            logging.error('requests RequestException: %s' % url)
            return 500, None
        except Exception, e:
            if e.message == self.openSSL_error:
                print """package error, please execute :
                pip install -U pyOpenSSL"""
            else:
                logging.error('requests unKnow error: %s' % url)
            return 500, None

    def download(self, url, retry=-1):
        """
        :param url:
        :param retry: 失败重试
        :return:
        """
        code, content = self._request(url)
        if retry > 0 and code != 200:
            self.download(url, retry - 1)
        return content if code == 200 else ''

