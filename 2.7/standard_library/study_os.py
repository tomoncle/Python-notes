#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-4-19 上午11:02
# @Author         : Tom.Lee
# @Description    : 
# @File           : helper_os.py
# @Product        : PyCharm
import commands
import os
import sys


def shell():
    command_ls = 'ls -al /opt'
    command_docker = 'docker ps -a'

    # 使用os.system()模块
    ros = os.system(command_ls)
    print '\n\nos.system() : ', ros

    # 使用os.popen()模块
    output = os.popen(command_docker)
    result = output.read()
    print '\n\nos.popen() : ', result

    # 使用commands模块
    (status, output) = commands.getstatusoutput(command_docker)
    print '\n\ncommands : ', status, output


def deep_look_dir(dir_path, deep=1, console_full_path=False):
    """
    deep_look_dir(dir_name, console_full_path=False)

    遍历文件夹下所有文件
    :param dir_path:  os.path.dirname(__file__)
    :param deep:
    :param console_full_path:
    :return:
    """
    if deep == 1:
        print dir_path

    files = os.listdir(dir_path)
    split_symbol = '｜＿' * deep if deep == 1 else '｜' + '　' * (deep - 1) + '｜＿'

    for f in files:
        f_path = os.path.join(dir_path, f)
        console_name = f_path if console_full_path else f

        if not os.path.isfile(f_path):
            print "{sp} {dir_path}/: ".format(
                sp=split_symbol,
                dir_path=console_name)
            num = deep + 1
            deep_look_dir(f_path, num, console_full_path)

        else:
            print split_symbol, console_name


if '__main__' == __name__:
   deep_look_dir('/root/pythonStudy')
