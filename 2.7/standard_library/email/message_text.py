#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-28 下午4:31
# @Author         : Tom.Lee
# @File           : text_message.py
# @Product        : PyCharm
# @Source         :

"""创建并发送简单文本消息"""
import smtplib
from email.mime.text import MIMEText

# # config email
me = ''
you = ''
smtp_host = ''
smtp_port = 25
passwd = ''
textfile = 'textfile'

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read(), 'text', 'utf-8')
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.connect(host=smtp_host, port=smtp_port)
s.set_debuglevel(1)
s.login(me, passwd)
s.sendmail(me, [you], msg.as_string())
s.quit()
