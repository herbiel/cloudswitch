#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 上午12:35
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
from xadmin.views import CommAdminView
from .models import Serverstatus
import xadmin

class ServerAdmin(object):
    object_list_template = "status.html"

    def get_context(self):
        context = CommAdminView.get_context(self)
        enter_date = '2021'
        age = 12
        context.update(
            {
                "enter_date": enter_date,
                "age": age
            }
        )
        return context

xadmin.site.register(Serverstatus, ServerAdmin)