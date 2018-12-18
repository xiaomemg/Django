from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


# def demoview(request):
#     return None
# 定义一个装饰器
def my_decorator(func):
    def wrpper(self, request, *args, **kwargs):
        print('起来了')
        print('%s' % request.method)
        return func(self, request, *args, **kwargs)

    return wrpper


# 创建一个类视图
class demoview(View):
    @my_decorator
    def get(self, request):
        return HttpResponse('走，我们走')

    @my_decorator
    def post(self, request):
        return HttpResponse('Bug出现了')
