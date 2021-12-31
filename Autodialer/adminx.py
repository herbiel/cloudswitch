#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cloudswitch 
@File    ：adminx.py.py
@Author  ：herbiel8800@gmail.com
@Date    ：2021/12/31 11:23 上午 
'''
import xadmin
from .models import BroadcastPlayback,Predictive
from xadmin import views

class BroadcastPlaybackAdmin(object):
    pass

class PredictiveAdmin(object):
    pass


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'CLOUDSWITCH'
    # 设置base_site.html的Footer
    site_footer  = '深圳唐牛科技有限公司'


class RegDataAdmin(object):
    list_display = ('year', 'cn')
    list_per_page = 20
    data_charts = {
        "user_count": {'title': u"User Register Raise", "x-field": "year", "y-field": ("cn",),
                       "order": ('year',)},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(BroadcastPlayback,BroadcastPlaybackAdmin)
xadmin.site.register(Predictive,PredictiveAdmin)
xadmin.site.register()