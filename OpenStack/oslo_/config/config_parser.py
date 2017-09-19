#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-31 下午1:29
# @Author         : Tom.Lee
# @File           : config_parser.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from oslo_config import cfg
from oslo_config import types


class ConfigManager(object):
    PortType = types.Integer(1, 65535)
    default_opts = [
        cfg.StrOpt(
            'bind_host',
            default='0.0.0.0',
            help='IP address to listen on.'),
        cfg.Opt(
            'bind_port',  # 只有Opt类型才能指定PortType
            type=PortType,
            default=9292,
            help='Port number to listen on.')
    ]
    default_opt = cfg.ListOpt(
        'enabled_api',
        default=['ec2', 'api_compute'],
        help='List of APIs to enable by default.')
    cli_opts = [
        cfg.BoolOpt('verbose',
                    short='v',
                    default=False,
                    help='Print more verbose output'),
        cfg.BoolOpt('debug',
                    short='d',
                    default=False,
                    help='Print debugging output'),
    ]
    rabbit_group = cfg.OptGroup(
        name='RABBIT',
        title='RABBIT options'
    )
    rabbit_opt = cfg.BoolOpt(
        'ssl',
        default=False,
        help='use ssl for connection')
    rabbit_opts = [
        cfg.StrOpt(
            'host',
            default='localhost',
            help='IP/hostname to listen on.'),
        cfg.IntOpt(
            'port',
            default=5672,
            help='Port number to listen on.')
    ]

    def __init__(self):
        self.conf = cfg.CONF
        self._register_opts()

    def _register_opts(self):
        # default
        self.conf.register_opt(self.default_opt)
        self.conf.register_opts(self.default_opts)
        # rabbit
        self.conf.register_group(self.rabbit_group)
        self.conf.register_opts(self.rabbit_opts, self.rabbit_group)
        self.conf.register_opt(self.rabbit_opt, self.rabbit_group)
        # cli
        self.conf.register_cli_opts(self.cli_opts)
        self.conf(default_config_files=['config.conf'])

    @property
    def bind_port(self):
        return getattr(self.conf, 'bind_port', None)

    @property
    def bind_host(self):
        return getattr(self.conf, 'bind_host', None)


config_manager = ConfigManager()
if __name__ == '__main__':
    print config_manager.bind_port
    print config_manager.bind_host
