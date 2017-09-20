#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 上午11:29
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : log.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
import logging

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG
# 设定日志格式
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(fmt)
log.addHandler(handler)
