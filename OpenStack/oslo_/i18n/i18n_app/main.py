#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-16 下午2:53
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : main.py
# @Product        : PyCharm
# @Docs           : https://docs.openstack.org/oslo.i18n/latest/user/usage.html
# @Source         : 

from _i18n import get_available_languages

languages = get_available_languages()

print languages



