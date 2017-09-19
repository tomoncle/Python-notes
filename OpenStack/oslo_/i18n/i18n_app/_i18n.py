#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-9-16 下午3:10
# @Author         : Tom.Lee
# @CopyRight      : 2016-2017 OpenBridge by yihecloud
# @File           : _i18n.py.py
# @Product        : PyCharm
# @Docs           : https://docs.openstack.org/oslo.i18n/latest/user/usage.html
# @Source         :

import oslo_i18n

DOMAIN = "i18n_app"

_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

# The primary translation function using the well-known name "_"
_ = _translators.primary

# The contextual translation function using the name "_C"
# requires oslo.i18n >=2.1.0
_C = _translators.contextual_form

# The plural translation function using the name "_P"
# requires oslo.i18n >=2.1.0
_P = _translators.plural_form

# Translators for log levels.
#
# NOTE(dhellmann): This is not needed for new projects as of the
# Pike series.
#
# The abbreviated names are meant to reflect the usual use of a short
# name like '_'. The "L" is for "log" and the other letter comes from
# the level.
_LI = _translators.log_info
_LW = _translators.log_warning
_LE = _translators.log_error
_LC = _translators.log_critical


def get_available_languages():
    """
    返回当前可以提供翻译的语言列表

    #所有的语言包在　/usr/local/lib/python2.7/dist-packages/babel/locale-data/
    :return:
    """
    return oslo_i18n.get_available_languages(DOMAIN)


def translate(msg, user_locale='zh_CN'):
    """
    翻译"msg"为指定的语言,默认"en_US"

    :param msg: the object to translate
    :param user_locale: the locale to translate the message to, if None the
                        default system locale will be used
                        'en_US' 'zh_CN'
    :returns: the translated object in unicode, or the original object if
              it could not be translated
    """
    return oslo_i18n.translate(msg, user_locale)


def enable_lazy(enable=True):
    return oslo_i18n.enable_lazy(enable)
