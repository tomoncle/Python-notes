#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-25 下午3:08
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : test.py
# @Product        : PyCharm

from restful import TestCase


if __name__ == '__main__':
    t = TestCase()
    base_url = 'http://0.0.0.0:9091'

    # # get job list
    # print t.get(base_url + '/jobList')[1]
    # # get user list
    print t.get(base_url + '/jobs')[1]
    # add user
    # data = {'name': 'node-16', 'status': 'AVAILABLE'}
    # print t.post(base_url + '/nodes', data=data)[1]

    # edit user
    # data = {'job_id': 'node01-tick', 'status': 'pause'}
    # print t.put(base_url + '/jobs', data=data)[1]

    # delete user
    # data = {'user_id': 5}
    # print t.delete(base_url + '/mailUsers', data=data)[1]
