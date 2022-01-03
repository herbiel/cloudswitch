# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Broadcastivr(models.Model):
    task_name = models.CharField(max_length=20,verbose_name=u"任务名称",default="")
    start_time = models.DateTimeField(max_length=20,verbose_name=u"开始时间",default="")
    end_time = models.DateTimeField(max_length=20, verbose_name=u"结束时间", default="")
    broadcastPlaybackUri = models.CharField(max_length=200, verbose_name=u"语音文件url", default="")
    fail_retry_time = models.CharField(max_length=20, verbose_name=u"失败重试次数", default="")
    enable = models.BooleanField(default=False,verbose_name=u"启用")
    class Meta:
        verbose_name = u"Broadcastivr"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.task_name

class Predictive(models.Model):
    task_name = models.CharField(max_length=20,verbose_name=u"任务名称",default="")
    start_time = models.DateTimeField(max_length=20,verbose_name=u"开始时间",default="")
    end_time = models.DateTimeField(max_length=20, verbose_name=u"结束时间", default="")
    cps = models.FloatField( verbose_name=u"并发", default="")
    predictive_cps = models.FloatField(verbose_name=u"预测并发", default="")
    enable = models.BooleanField(default=False,verbose_name=u"启用")
    class Meta:
        verbose_name = u"Predictive"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.task_name

class Task(models.Model):
    task_name = models.CharField(max_length=20,verbose_name=u"任务名称",default="")
    number = models.CharField(max_length=20,verbose_name=u"号码", default="")
    describe = models.CharField(max_length=20,verbose_name=u"描述", default="",null=True)
    class Meta:
        verbose_name = u"Task"
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.task_name