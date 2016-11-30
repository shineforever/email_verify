#! /usr/bin/env python
# coding: utf-8
from django.db import models

# Create your models here.

class Account(models.Model):
    """
    用户注册，发送邮件确认
    """
    name = models.CharField(max_length=10,unique=True,verbose_name=u"用户名")
    email = models.EmailField(unique=True,verbose_name=u"邮箱地址")
    token = models.CharField(max_length=50,blank=True, null=True,verbose_name=u"token值")
    verification_status = models.BooleanField(default=False,verbose_name=u"注册状态")
    authcode = models.CharField(max_length=50,verbose_name=u"authcode值")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
