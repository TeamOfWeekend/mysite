"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# import xadmin

urlpatterns = [
    # 修改admin的url，避免使用admin这么简单的路径
    path('admin/', admin.site.urls),
    # path('admin/', xadmin.site.urls),

    # include语法相当于多级路由，它把接收到的url地址去除与此项匹配的部分，
    # 将剩下的字符串传递给下一级路由urlconf进行判断
    path('', include('home.urls', namespace='home')),   # 主页，不去除任何匹配项进行匹配
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('colleges/', include('colleges.urls', namespace='colleges')),
    # path('polls/', include('polls.urls', namespace='polls')),
    # path('users/', include('users.urls', namespace='users')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
