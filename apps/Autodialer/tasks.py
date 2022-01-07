#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cloudswitch 
@File    ：tasks.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/7 3:07 下午 
'''
from cloudswitch.celery import app
@app.task
def start_running(info):
 print(info)
 print('--->>开始执行任务<<---')
 print('比如发送短信或邮件')
 print('>---任务结束---<')