#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 上午10:56
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : process_pool.py
# @Product        : PyCharm

from datetime import datetime
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass