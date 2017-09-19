#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-11 上午11:29
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : utils.py
# @Product        : PyCharm


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
openSSL_error = "'X509' object has no attribute '_x509'"


def http_inspect(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.Timeout:
            raise ConnectionError('连接超时')
        except requests.exceptions.RequestException:
            raise ConnectionError('请求失败')
        except Exception, e:
            if e.message == openSSL_error:
                print """package error, please execute :
                pip install -U pyOpenSSL"""
            raise ConnectionError('连接失败')

    return wrapper


class ConnectionError(Exception):
    """
    服务连接失败
    """
    pass


class RequestsUtils(object):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Ubuntu Chromium/50.0.2661.102 ' \
                 'Chrome/50.0.2661.102 Safari/537.36'

    def __init__(self, headers=None, cookies=None, timeout=3, proxies=None, verify=False):
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

    @http_inspect
    def get(self, url, params=None):
        return requests.get(url,
                            params=params,
                            headers=self._make_headers(),
                            timeout=self.timeout,
                            proxies=self.proxies,
                            verify=self.verify)


if __name__ == '__main__':
    req = RequestsUtils()
    print req.get('http://192.168.1.111:8088/web')
