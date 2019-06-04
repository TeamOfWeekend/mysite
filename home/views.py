from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from . import tasks
import json

# from .models import User
from .forms import UserLoginForm, UserRegisterForm, UserModifyForm

# Create your views here.

User = get_user_model()


def add1(request):
    # a = request.GET['a']
    # b = request.GET['b']
    a = request.GET.get('a', 0)     # 当没有a传递时，值为0
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    from_email = settings.DEFAULT_FROM_EMAIL
    # subject主题  content内容  to_addr发送目标，是一个列表
    msg = EmailMultiAlternatives('Test', 'Django send email!', from_email, ['823919142@qq.com'])
    msg.send()
    return HttpResponse(str(c))


def home_view(request):
    return render(request, 'home/home.html')


# 用户注册视图
def register_view(request):
    if 'GET' == request.method:
        register_form = UserRegisterForm()
    elif 'POST' == request.method:
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            # 如果你指定commit=False，那么save方法不会理解将表单数据存储到数据库，
            # 而是给你返回一个当前对象。这时你可以添加表单以外的额外数据，再一起存储
            register_form.save()
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return HttpResponseRedirect(reverse('home:home'))
        else:
            message = register_form.errors
    return render(request, 'home/register.html', locals())


def login_view(request):
    if 'POST' == request.method:
        login_form = UserLoginForm(request.POST)
        message = '用户名或密码输入不正确，请核对'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # 使用认证系统的login()方法登录用户。
                # 它接收一个HttpRequest参数和一个User对象参数。
                # 该方法会把用户的ID保存在Django的session中
                login(request, user)
                return render(request, 'home/home.html', locals())
            else:
                message = '用户名或密码不正确'
                return render(request, 'home/login.html', {'message': message})
        else:
            message = login_form.errors
            return render(request, 'home/login.html', locals())
    login_form = UserLoginForm()
    return render(request, 'home/login.html', locals())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:home'))


def test_view(request, *args, **kwargs):
    tasks.test.delay(1, 2)
    result = {'code': 0, 'msg': '这是一个后台任务'}
    return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')
