#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author     :Leo
@Connect    :lipf0627@163.com
@File       :forms.py
@Site       :
@Time       :2019/4/19 22:02
@Software   :PyCharm
"""

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=32, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': "Username",
                                                                            'autofocus': ''}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': "Password"}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}),
    #         'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}),
    #     }


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'sex')
        # exclude = ('head_portrait', 'password_new', 'date_joined', 'date_modified', 'privilege', 'level', 'integral', 'age')
        email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空'})
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': "Username",
                                               'autofocus': ''}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': "Password1"}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': "Password2"}),
            'email': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': "Email"}),
            'sex': forms.Select(attrs={'class': 'form-control', }),
            'birthday': forms.SelectDateWidget(attrs={'class': 'form-control',}),
            # 'head_portrait': forms.FileInput(attrs={'class': 'form-control',
            #                                         'type': 'file',
            #                                         'id': 'image_upload',
            #                                         'accept': ''}),
        }
        labels = {
            'birthday': _('Birthday'),
        }
        help_texts = {
            'birthday': _('Please choose your birthday'),
        }
        error_messages = {
            'birthday': {
                'Input': _('Please choose your birthday')
            },
        }


class UserModifyForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('age',)
        exclude = ('date_joined', 'date_modified', 'privilege', 'level', 'integral')
