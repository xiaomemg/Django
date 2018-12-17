from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('哈哈哈')

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('跑起来了')


def weather(request,city,year):
    print(city)
    print(year)
    return HttpResponse("来了，来了")
