from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.

# from .models import User
User = get_user_model()

# 方式一
# class UserAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(UserDetail)


# 方式二
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 在admin增加user页面不显示某些属性
    # exclude = ('password_new', 'level', 'integral')
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email', 'privilege'),
        }),
        ('More', {
            # 折叠显示
            'classes': ('collapse',),
            'fields': ('sex', 'birthday', 'head_portrait'),
        })
    )
    # 在admin页面中显示时，显示的属性
    list_display = ('username', 'privilege', 'sex', 'age', 'email', 'date_joined')
    # 指定在list_display中哪些字段可以被编辑
    list_editable = ('privilege', )
    # 激活右边栏，填入过滤项
    list_filter = ('privilege', 'date_joined')
    # 添加搜索框
    search_fields = ['username']
    # 为页面创建一个时间导航栏，可通过日期过滤对象
    date_hierarchy = 'date_joined'
    # 设置一个数值，当列表元素总数小于这个值的时候，将显示一个“show all”链接，
    # 点击后就能看到一个展示了所有元素的页面。该值默认为200.
    list_max_show_all = 10
    # 设置每页显示多少个元素。Django自动帮你分页。默认为100
    list_per_page = 5
    # 设置排序的方式
    ordering = ('username', 'date_joined')
    # 设置预填充字段
    prepopulated_fields = {'username': ('username', 'password')}
    # 设置不可修改的属性
    # readonly_fields = ('sex', )
