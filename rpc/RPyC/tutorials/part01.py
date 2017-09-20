#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 下午3:37
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : part01.py
# @Product        : PyCharm
# @Source         :

"""
rpyc 客户端查询服务端信息

"""

import os

import rpyc

# 打印当前路径
print os.getcwd()

# 启动内置服务
# os.system('python /usr/local/bin/rpyc_classic.py')
"""
CMD:
    tom@aric-ThinkPad-E450:~$ python /usr/local/bin/rpyc_classic.py
    INFO:SLAVE/18812:server started on [0.0.0.0]:18812
"""

# 连接服务器
conn = rpyc.classic.connect('localhost')

mod1 = conn.modules.sys  # 访问服务器上的sys模块
mod2 = conn.modules["xml.dom.minidom"]  # 访问服务器上的xml.dom.minidom模块
print mod1, mod2

# 打印服务器启动路径
print conn.modules.os.getcwd()
