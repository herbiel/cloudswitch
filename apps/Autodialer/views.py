from django.shortcuts import render

# Create your views here.

from Autodialer.tasks import start_running
from django.http import HttpResponse
from django.views.generic import View
from cloudswitch.freeswitch import command
#celery测试
class CeleryTask(View):
 def get(self, request):
     print('>=====开始发送请求=====<')
     start_running.delay(30)
     # start_running.apply_async(('发送短信',), countdown=10)  # 10秒后再执行异步任务
     return HttpResponse('<h2> 请求已发送 </h2>')

class CeleryTest(View):
 def get(self, request):
     print('>=====开始发送请求=====<')
     res = command('status')
     print(res)
     return HttpResponse(res)
