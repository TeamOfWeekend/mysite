#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :tasks.py
@Site       :
@Time       :2019/5/28 21:05
@Software   :PyCharm
"""
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import CollegeInfo
from .mydata.mydata import MyData


@shared_task
def add_student():
    if CollegeInfo.objects.all().count() is 0:
        MyData.create_colleges()
    MyData.create_random_student()
