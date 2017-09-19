#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-5 下午1:10
# @Author         : Tom.Lee
# @Description    : 
# @File           : study_logging.py
# @Product        : PyCharm

"""
注意：basicConfig有一个 很大的缺点。
调用basicConfig其实是给root logger添加了一个handler，
这样当你的程序和别的使用了 logging的第三方模块一起工作时，
会影响第三方模块的logger行为。这是由logger的继承特性决定的。
"""

import logging
import sys

FORMAT_STR = "[%(asctime)s] %(name)s:%(levelname)s: %(message)s"


# logger = logging.getLogger("django")
# logger.debug(logging.DEBUG)  # 使用django热加载


def config1():
    """
    **********************Config 1**********************
    """
    # config 1.
    # 设置默认的level为DEBUG
    # 设置log的格式
    # 注意：basicConfig有一个 很大的缺点。
    # 调用basicConfig其实是给root logger添加了一个handler，
    # 这样当你的程序和别的使用了 logging的第三方模块一起工作时，
    # 会影响第三方模块的logger行为。这是由logger的继承特性决定的。
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )

    # 记录log
    logging.debug('debug')
    logging.info('info')
    logging.warn('warn')
    logging.error('error')
    logging.critical('critical')


def config2():
    """
    ********************Config 2************************
    """
    # # config 2
    # 使用一个名字为fib的logger
    logger = logging.getLogger('app_name')
    # 设置logger的level为DEBUG
    logger.setLevel(logging.DEBUG)
    # 创建一个输出日志到控制台的StreamHandler
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    # 给logger添加上handler
    logger.addHandler(handler)

    logger.debug('debug message')
    logger.info('hello world')


def config3():
    """
    config3 输出到文件
    """
    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger("AppName")
    # 指定logger输出格式
    formatter = logging.Formatter(FORMAT_STR)
    # 文件日志
    file_handler = logging.FileHandler("test.log")
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值
    # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.INFO)

    # 输出不同级别的log
    logger.debug('this is debug info')
    logger.info('this is information')
    logger.warn('this is warning message')
    logger.error('this is error message')
    logger.fatal('this is fatal message, it is same as logger.critical')
    logger.critical('this is critical message')



# if __name__ == '__main__':

