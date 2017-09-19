#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-7-5 下午2:14
# @Author         : Tom.Lee
# @Description    : 
# @File           : study_argparse.py
# @Product        : PyCharm

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test argparse')

    parser.add_argument('--user', dest='USER', type=str,
                        required=True,
                        help='User Name')
    parser.add_argument('-H', '--host', dest='HOST', type=str,
                        default='localhost',
                        help='Server Ip Address')
    parser.add_argument('-P', '--port', dest='PORT', type=int,
                        default=3306,
                        help='Server Connection Port')

    args = parser.parse_args()
    print args
    print getattr(args, 'no', None)
    print getattr(args, 'PORT', None)
