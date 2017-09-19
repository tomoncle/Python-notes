#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-8-31 上午10:40
# @Author         : Tom.Lee
# @File           : config.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : https://github.com/openstack/oslo.config/blob/master/oslo_config/cfg.py

"""
配置文件中的选项(group, opts)，必须在代码中显示的注册，否则无法解析
"""

from oslo_config import cfg
from oslo_config import types

# 端口规范
PortType = types.Integer(1, 65535)

# 多个配置项组成一个模式
default_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.Opt('bind_port',  # 只有Opt类型才能指定PortType
            type=PortType,
            default=9292,
            help='Port number to listen on.')
]

# 单个配置项模式
default_opt = cfg.ListOpt('enabled_api',
                          default=['ec2', 'api_compute'],
                          help='List of APIs to enable by default.')

# 命令行选项
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

# 配置 rabbit_group 组
rabbit_group = cfg.OptGroup(
    name='RABBIT',
    title='RABBIT options'
)
# 配置组中的模式，通常以配置组的名称为前缀（非必须）
rabbit_opt = cfg.BoolOpt('ssl',
                         default=False,
                         help='use ssl for connection')
# 配置组中的多配置项模式
rabbit_opts = [
    cfg.StrOpt('host',
               default='localhost',
               help='IP/hostname to listen on.'),
    cfg.IntOpt('port',
               default=5672,
               help='Port number to listen on.')
]


def register_default_opts(conf):
    """
    注册默认组的配置项
    """
    conf.register_opt(default_opt)
    conf.register_opts(default_opts)


def register_rabbit_group(conf):
    """
    注册　rabbit 信息
    """
    # 配置组必须在其组件被注册前注册！
    conf.register_group(rabbit_group)
    # 注册配置组中含有多个配置项的模式，必须指明配置组
    conf.register_opts(rabbit_opts, rabbit_group)
    # 注册配置组中的单配置项模式，指明配置组
    conf.register_opt(rabbit_opt, rabbit_group)


def register_cli_opts(conf):
    """
    注册　cli 选项
    :param conf:
    :return:
    """
    conf.register_cli_opts(cli_opts)


def get_bind_host(conf):
    """
    使用选项 bind_host
    """
    return getattr(conf, 'bind_host', None)


def get_bind_port(conf):
    """
    使用选项 bind_port
    """
    return conf.bind_port


def get_rabbit_username(conf):
    """
    配置文件中存在，代码没有注册，不能解析
    """
    return conf.RABBIT.username


if __name__ == '__main__':
    # 创建配置类
    config = cfg.CONF
    # 开始注册default
    register_default_opts(config)
    register_rabbit_group(config)
    register_cli_opts(config)

    # 加载配置文件
    config(default_config_files=['config.conf'])
    print 'host:', get_bind_host(config)
    # list_all_sections
    for section in config.list_all_sections():
        print section

    print config.RABBIT
    print config.RABBIT.host
    print get_rabbit_username(config)
