#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cloudswitch 
@File    ：adminx.py.py
@Author  ：herbiel8800@gmail.com
@Date    ：2021/12/31 11:23 上午 
'''
from __future__ import absolute_import,unicode_literals
import xadmin
from django.template.base import logger

import apps
from .models import Broadcastivr, Predictive, Task
from xadmin import views
from django.http import HttpResponseRedirect
import xlrd
from django.db import transaction


#from djcelery.models import (
#  TaskState, WorkerState,
#  PeriodicTask, IntervalSchedule, CrontabSchedule,
#)



class BroadcastPlaybackAdmin(object):
    pass


class PredictiveAdmin(object):
    pass


class TaskAdmin(object):
    import_excel = True
    def post(self,request,*args,**kwargs):
        if 'excel' in request.FILES:
            file = request.FILES.get('excel')
            files = xlrd.open_workbook(filename=None, file_contents=file.read())
            table = files.sheets()[0]
            rows = table.nrows  # 总行数
            # print(rows)
            with transaction.atomic():  # 控制数据库事务交易
                for i in range(1, rows):
                    rowVlaues = table.row_values(i)
                    print(rowVlaues)
                    Task.objects.create(task_name=rowVlaues[0], number=rowVlaues[2], describe=rowVlaues[3])
            return HttpResponseRedirect('/xadmin/Autodialer/task')
        return super(TaskAdmin, self).post(request, *args, **kwargs)


class GlobalSetting(object):
    # 设置base_site.html的Title
    site_title = 'CLOUDSWITCH'
    # 设置base_site.html的Footer
    site_footer = '深圳唐牛科技有限公司'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Broadcastivr, BroadcastPlaybackAdmin)
xadmin.site.register(Predictive, PredictiveAdmin)
xadmin.site.register(Task, TaskAdmin)

#celery

#xadmin.site.register(IntervalSchedule) # 存储循环任务设置的时间
#xadmin.site.register(CrontabSchedule) # 存储定时任务设置的时间
#xadmin.site.register(PeriodicTask) # 存储任务
#xadmin.site.register(TaskState) # 存储任务执行状态
#xadmin.site.register(WorkerState) # 存储执行任务的worker