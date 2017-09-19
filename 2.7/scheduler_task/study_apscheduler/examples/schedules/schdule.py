#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-13 上午11:40
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : asyncio.py
# @Product        : PyCharm
# @Docs           : 

import os
import time
from datetime import datetime


def asyncio_schedule():
    """
    python version >= 3.4.0
    :return:
    """
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    try:
        import asyncio
    except ImportError:
        import trollius as asyncio

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass


def background_schedule():
    from apscheduler.schedulers.background import BackgroundScheduler

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()


def blocking_schedule():
    from apscheduler.schedulers.blocking import BlockingScheduler

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


def gevent_schedule():
    from apscheduler.schedulers.gevent import GeventScheduler

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = GeventScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    g = scheduler.start()  # g is the greenlet that runs the scheduler loop
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass


def qt_schedule():
    import signal
    import sys
    from apscheduler.schedulers.qt import QtScheduler

    try:
        from PyQt5.QtWidgets import QApplication, QLabel
    except ImportError:
        try:
            from PyQt4.QtGui import QApplication, QLabel
        except ImportError:
            from PySide.QtGui import QApplication, QLabel

    def tick():
        label.setText('Tick! The time is: %s' % datetime.now())

    app = QApplication(sys.argv)

    # This enables processing of Ctrl+C keypresses
    signal.signal(signal.SIGINT, lambda *args: QApplication.quit())

    label = QLabel('The timer text will appear here in a moment!')
    label.setWindowTitle('QtScheduler example')
    label.setFixedSize(280, 50)
    label.show()

    scheduler = QtScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()

    # Execution will block here until the user closes the windows or Ctrl+C is pressed.
    app.exec_()


def tornado_schedule():
    from tornado.ioloop import IOLoop
    from apscheduler.schedulers.tornado import TornadoScheduler

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = TornadoScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        IOLoop.instance().start()
    except (KeyboardInterrupt, SystemExit):
        pass


def twisted_schedule():
    from twisted.internet import reactor
    from apscheduler.schedulers.twisted import TwistedScheduler

    def tick():
        print('Tick! The time is: %s' % datetime.now())

    scheduler = TwistedScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        reactor.run()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    # gevent_schedule()
    # twisted_schedule()
    tornado_schedule()
    print 123
    pass
