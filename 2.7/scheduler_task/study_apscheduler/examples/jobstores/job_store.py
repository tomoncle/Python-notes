#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 上午11:14
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017
# @File           : mongodb.py
# @Product        : PyCharm
# @Docs           : 


from datetime import datetime, timedelta
import sys
import os

from apscheduler.schedulers.blocking import BlockingScheduler


def alarm(time):
    print('Alarm! This alarm was scheduled at %s.' % time)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # ################ mongodb
    scheduler.add_jobstore('mongodb', collection='example_jobs')

    if len(sys.argv) > 1 and sys.argv[1] == '--clear':
        scheduler.remove_all_jobs()

    alarm_time = datetime.now() + timedelta(seconds=10)
    scheduler.add_job(alarm, 'date', run_date=alarm_time, args=[datetime.now()])
    print('To clear the alarms, run this example with the --clear argument.')
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
