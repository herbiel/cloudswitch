from django.db import models

# Create your models here.
class Serverstatus(models.Model):
    class Meta:
        verbose_name = u"服务器状态"
        verbose_name_plural = verbose_name