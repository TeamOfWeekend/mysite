#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :urls.py
@Site       :
@Time       :2019/4/22 21:12
@Software   :PyCharm

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from . import views

# 命名空间
app_name = 'polls'


# 注意path于re_path的用法区别
# path 2.0版本
# re_path 用于兼容1.x版本

urlpatterns = [
    # 主页
    # path('', views.index, name='index'),

    # 参数name相当于给url起个别名，结合app_name唯一定位一个url，可用于render、reverse、html中等
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]


# 增加的条目
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.error
