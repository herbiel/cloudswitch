# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from account.models import Domain
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Extension(models.Model):
    number = models.CharField(max_length=20,verbose_name=u"分机号码",default="")
    password = models.CharField(max_length=20,verbose_name=u"密码",default="")
    displayname = models.CharField(max_length=20,verbose_name=u"显示名字",default="")
    domain = models.ForeignKey(Domain,verbose_name=u"域名",on_delete=models.CASCADE)
    enable = models.BooleanField(default=False,verbose_name=u"启用")
    class Meta:
        verbose_name = u"分机"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.number


class Gateway(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"名称",default="")
    username = models.CharField(max_length=20, verbose_name=u"用户名",default="")
    password = models.CharField(max_length=20,verbose_name=u"密码",default="")
    realm = models.CharField(max_length=20,verbose_name=u"认证地址",default="")
    proxy = models.CharField(max_length=20,verbose_name=u"认证代理",default="")
    domain = models.CharField(max_length=20, verbose_name=u"域名",default="")
    register = models.BooleanField(default=False,verbose_name=u"是否注册")
    enable = models.BooleanField(default=False, verbose_name=u"启用")

    class Meta:
        verbose_name = u"网关"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name

class Dialplan(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名称",default="")
    gateway = models.CharField(max_length=50, verbose_name=u"网关",default="")
    expression = models.TextField(max_length=20, verbose_name=u"匹配条件",default="")
    domain = models.CharField(max_length=20, verbose_name=u"域名",default="")
    enable = models.BooleanField(default=False, verbose_name=u"启用")

    class Meta:
        verbose_name = u"路由"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.name