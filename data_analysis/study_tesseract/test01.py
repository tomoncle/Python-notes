#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-7 下午1:21
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : test01.py
# @Product        : PyCharm

"""
# BASH

$ tesseract image_path out
$ cat out.txt
"""
import Image

import pytesseract

file_obj = Image.open('./image/20170807142300.png')
print pytesseract.image_to_string(file_obj)
