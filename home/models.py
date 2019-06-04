from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# 每个模型代表数据库中的一张表
# 每个类的实例代表数据表中的一行数据
# 类中的每个变量代表数据表中的一列字段


class User(AbstractUser):
    """
    网站用户定义
    """
    USER_PRIVILEGE = ((1, 'Guest'),
                      (2, 'Member'),
                      (3, 'Admin'))

    SEX = (('M', 'Male'),
           ('F', 'Female'))

    # username = models.CharField(max_length=100, blank=False, null=False)
    # password = models.CharField(max_length=100, blank=False, null=False)
    # email = models.EmailField(blank=False)
    sex = models.CharField(max_length=1, choices=SEX, default='M', verbose_name='性别')
    birthday = models.DateField(default=timezone.now, verbose_name='生日')
    age = models.PositiveSmallIntegerField(default=0)
    head_portrait = models.ImageField(upload_to='files/media')     # 头像
    # date_joined = models.DateTimeField('用户注册时间', auto_now_add=True)  # register time
    date_modified = models.DateTimeField(auto_now=True, verbose_name='最近一次修改时间')  # the last time of modify
    date_login = models.DateTimeField(auto_now=True, verbose_name='最近一次登录时间')  # the last time of login
    privilege = models.IntegerField(choices=USER_PRIVILEGE, default=1, verbose_name='权限')  # 权限
    level = models.PositiveSmallIntegerField(default=0, verbose_name='等级')     # 等级
    integral = models.PositiveIntegerField(default=0, verbose_name='积分')       # 积分

    # def decade_born_in(self):
    #     return self.birthday.strftime('%Y')[:3] + "0's"
    #
    # decade_born_in.short_description = 'Birth decade'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-integral']
        # unique_together = ('self.user.username', )
