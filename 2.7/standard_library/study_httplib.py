#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-21 下午2:45
# @Author         : Tom.Lee
# @File           : study_httplib.py
# @Product        : PyCharm
import httplib
import urllib


def request_get(host, port, url, params=None, headers=None, timeout=5):
    status, http_clint, data = None, None, None
    try:
        http_clint = httplib.HTTPConnection(host, port, timeout=timeout)
        url = url + urllib.urlencode(params or {})
        http_clint.request('GET', url, headers=headers or {})
        response = http_clint.getresponse()
        status = response.status
        data = response.read()
    except Exception, e:
        print e
    finally:
        if http_clint:
            http_clint.close()
        return status, data


def request_post(host, port, url, body=None, headers=None, timeout=5):
    status, http_clint, data = None, None, None
    try:
        http_clint = httplib.HTTPConnection(host, port, timeout=timeout)
        http_clint.request('POST', url, body, headers)
        response = http_clint.getresponse()
        status = response.status
        data = response.read()

    except Exception, e:
        print 'http post error :{0}'.format(e)
    finally:
        if http_clint:
            http_clint.close()
        return status, data
