#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 上午11:33
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : demo.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


import os

from apscheduler.schedulers.blocking import BlockingScheduler

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job('sys:stdout.write', 'interval', seconds=3, args=['tick ...\n'])
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
