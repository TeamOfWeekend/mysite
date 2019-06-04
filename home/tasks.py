#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :tasks.py
@Site       :
@Time       :2019/5/26 14:20
@Software   :PyCharm
"""
from __future__ import absolute_import, unicode_literals
import time
from celery import task, shared_task


@task
def test(a, b):
    print('这是任务开始')
    print(a+b)
    time.sleep(10)
    print('这是任务结束')


@shared_task
def test_beat(x, y):
    print(x+y)

