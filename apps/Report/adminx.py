#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 上午12:35
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : adminx.py
# @Software: PyCharm
from xadmin.views import CommAdminView
import re
from .models import Serverstatus
from cloudswitch.freeswitch import command
import xadmin

class ServerAdmin(object):

    object_list_template = "status.html"

    def get_context(self):
        context = CommAdminView.get_context(self)
        enter_date = '2021'
        res = command('status')
        cpu = 100 - int(res.split('/')[1].split()[0].split('.')[0])

        startup = re.findall(r'\d+', res)[20]
        peak = re.findall(r'\d+', res)[24]
        sec = re.findall(r'\d+', res)[25]
        context.update(
            {
                "enter_date": enter_date,
                "cpu": cpu,
                "startup": startup,
                "peak": peak,
                "sec": sec
            }
        )
        return context

xadmin.site.register(Serverstatus, ServerAdmin)