#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-2 上午11:32
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : restful.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import requests


def json_console_format(s):
    import json
    return json.dumps(s, indent=5)


class TestCase(object):
    @classmethod
    def _response(cls, res):
        try:
            return res.status_code, json_console_format(res.json())
        except (ValueError, Exception):
            return res.status_code, res.content

    def get(self, url, params=None, **kwargs):
        res = requests.get(url=url, params=params, verify=False, **kwargs)
        return self._response(res)

    def post(self, url, data=None, body=None, **kwargs):
        res = requests.post(url, data=data, json=body, verify=False, **kwargs)
        return self._response(res)

    def put(self, url, data=None, body=None, **kwargs):
        res = requests.put(url, data=data, json=body, verify=False, **kwargs)
        return self._response(res)

    def delete(self, url, **kwargs):
        res = requests.delete(url, verify=False, **kwargs)
        return self._response(res)

    def head(self, url, headers=None, **kwargs):
        res = requests.head(url, headers=headers or {}, verify=False, **kwargs)
        return self._response(res)

    def patch(self, url, data=None, body=None, **kwargs):
        res = requests.patch(url, data=data, json=body, verify=False, **kwargs)
        return self._response(res)

