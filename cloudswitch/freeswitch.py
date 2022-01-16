#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/16 下午7:02
# @Author  : herbiel8800@gmail.com
# @Site    : 
# @File    : freeswitch.py
# @Software: PyCharm

'''
single_command.py - execute a single command over ESL
'''
import sys
import ESL

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
    return