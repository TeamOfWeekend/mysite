#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :urls.py
@Site       :定义learning_logs的URL模式
@Time       :2019/4/15 21:55
@Software   :PyCharm
"""

from django.urls import path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView
from . import views

# 命名空间
app_name = 'home'


# 注意path于re_path的用法区别
# path 用于不含参数方法的URL映射
# re_path 用于含参数方法的URL映射

urlpatterns = [
    # 主页
    # path('', views.index, name='index'),
    path('add1/', views.add1, name='add1'),
    path('add2/<int:a>/<int:b>', views.add2, name='add2'),

    # 参数name相当于给url起个别名，结合app_name唯一定位一个url，可用于render、reverse、html中等
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    # path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('test/', views.test_view, name='test_view'),

] + staticfiles_urlpatterns()
