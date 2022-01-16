#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cloudswitch 
@File    ：tasks.py
@Author  ：herbiel8800@gmail.com
@Date    ：2022/1/7 3:07 下午 
'''
from cloudswitch.celery import app
import threading
from time import sleep,ctime
import sys
import ESL
import queue

host = '192.168.50.15'
port = 8021
auth = 'ClueCon'


def command(command):
    con = ESL.ESLconnection(host, port,auth)

    if not con.connected():
        print
        'Not Connected'
        sys.exit(2)

    # Run command
    e = con.api(command)
    result = ''
    if e:
        result = e.getBody()
    else:
        result = "null"
    print(result)





@app.task
def start_running(thread_num):
  print('---开始---:%s' % ctime())




  threads = []

  for i in range(thread_num):
      t = threading.Thread(target=command,args=('originate sofia/internal/sip:50033@192.168.50.16:5080 sleep:5000,hangup inline',))
      threads.append(t)

  for i in range(thread_num):
      threads[i].start()
  for i in range(thread_num):
      threads[i].join()


  print('---结束---:%s' % ctime())