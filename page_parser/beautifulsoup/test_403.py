#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-25 下午3:17
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : test_403.py
# @Product        : PyCharm

import bs4

t403 = """
<html>
 <head>
  <title>403 Forbidden</title>
 </head>
 <body>
  <h1>403 Forbidden</h1>
  资源 bc6d81de-97af-4ebd-b01a-b23a6567bea2 is protected and cannot be deleted.<br /><br />



 </body>
</html>
"""
soup = bs4.BeautifulSoup(t403, "html.parser", from_encoding='utf-8')

title = soup.find('title')
body = soup.find('body')
title_text = title.getText()
body_text = body.getText().replace(title_text, '').replace('\n', '')

print {title_text.split(' ')[-1]: {'message': body_text, 'code': 1}}
