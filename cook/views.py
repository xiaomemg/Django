from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_cook(request):
    response = HttpResponse('跑起来了')
    # 设置cookie
    response.set_cookie('itcast1','python1')
    response.set_cookie('itcast2','python2')
    return response


def get_cook(request):
    cookie = request.COOKIES.get('itcast1')
    print(cookie)
    return HttpResponse('来了，来了')