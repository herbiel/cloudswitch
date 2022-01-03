# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Domain(models.Model):
    domain = models.CharField(max_length=100, verbose_name="域名")
    enable = models.BooleanField(default=False, verbose_name=u"启用")

    class Meta:
        verbose_name = "域名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.domain


class UserProfile(AbstractUser):
#    domain = models.ForeignKey(Domain,verbose_name='域名',on_delete=models.CASCADE)
    domain = models.CharField(max_length=100, verbose_name="域名")
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
