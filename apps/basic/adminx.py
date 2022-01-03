#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/3 下午10:34
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import Extension,Gateway,Dialplan

class ExtensionAdmin(object):
    pass

class GatewayAdmin(object):
    pass

class DialplanAdmin(object):
    pass

xadmin.site.register(Extension,ExtensionAdmin)
xadmin.site.register(Gateway,GatewayAdmin)
xadmin.site.register(Dialplan,DialplanAdmin)
