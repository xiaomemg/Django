import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse('哈哈哈')

def qs(request):
    # 里面的GET：获取参数的位置
    # a = request.GET.get('a')
    # b = request.GET.get('b')
    # alist = request.GET.getlist('a')
    # print(a)
    # print(b)
    # print(alist)
    # return HttpResponse('跑起来了')
    # aa = request.POST.get('aa')
    # bb = request.POST.get('bb')
    # alist = request.POST.getlist('aa')
    # print(aa)
    # print(bb)
    # print(alist)
    # return HttpResponse('跑起来了')
    # 请求传输非表单类型  request.body
    json_bytes = request.body
    json_str = json_bytes.decode()
    # 把json字符串转换成字典
    data_dict = json.loads(json_str)
    a = data_dict.get('a')
    b = data_dict.get('b')
    print(a)
    print(b)
    return HttpResponse('起来了')

def weather(request,city,year):
    print(city)
    print(year)
    return HttpResponse("来了，来了")


def headers(request):
    length=request.META['CONTENT_LENGTH']
    type = request.META['CONTENT_TYPE']
    print(length)
    print(type)
    return HttpResponse('跑起来了')


def others(request):
    print(request.method)
    print(request.user)
    print(request.path)
    return HttpResponse('动起来了')


def demo_response(request):
    # 定义一个json字符串
    s = '{"name":"zhangsan"}'
    # 返回的是一个json字符串
    return HttpResponse(s,content_type="application/json",status=400)


def home(request):
    print("我靠")
    return HttpResponseRedirect('/reqresp/others/')


def demo_view(request):
    # return JsonResponse({'city':'beijing'})
    # 重定向
    return redirect('/reqresp/others/')