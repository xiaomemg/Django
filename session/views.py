from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def set_session(request):
    # 设置session
    request.session['itcast1'] = 'python1'
    return HttpResponse('出来了')


def get_session(request):
    #
    return None