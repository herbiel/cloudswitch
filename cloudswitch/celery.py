#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cloudswitch 
@File    ：celery.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/7 3:04 下午 
'''

from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量, 改为你项目的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cloudswitch.settings')
# 创建应用
app = Celery('cloudswitch')

# 配置应用
app.conf.update(
 # 本地Redis服务器
 BROKER_URL=settings.BROKER_URL,
)

app.autodiscover_tasks(settings.INSTALLED_APPS)