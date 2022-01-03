#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 上午12:01
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm


import xadmin
from .models import Domain

class DomainAdmin(object):
    pass


xadmin.site.register(Domain,DomainAdmin)
