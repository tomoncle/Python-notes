#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-15 下午2:00
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : client_test.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


import rpyc
from rpyc.utils.registry import UDPRegistryClient


def service01():
    conn = rpyc.connect(host='localhost', port=18861)
    root = conn.root  # MyService object
    # object
    print root

    print root.get_service_name()
    print root.get_service_aliases()

    # custom method
    print root.get_answer()  # 66
    print root.exposed_get_answer()  # 66
    # print root.get_question()  # AttributeError: cannot access 'get_question'

    registrar = UDPRegistryClient()
    list_of_servers = registrar.discover("foo")
    print rpyc.discover(service_name='MY', host='localhost')


if __name__ == '__main__':
    service01()
