#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-29 下午2:33
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : html_message.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# #config
FROM_ADDRESS = ''  # sender's address
EMAIL_PWD = ''     # password
TO_ADDRESSES = ''  # recipient's email address
SMTP_HOST = ''
SMTP_PORT = 25

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = FROM_ADDRESS
msg['To'] = TO_ADDRESSES

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP()
s.connect(host=SMTP_HOST, port=SMTP_PORT)
s.login(FROM_ADDRESS, EMAIL_PWD)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(FROM_ADDRESS, [TO_ADDRESSES], msg.as_string())
s.quit()
