import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from demo_table.models import BookInfo


class BookInfoListView(View):

    def get(self,request):
        '''
        获取所有的数据
        路由：　/books/

        '''
        # 取数据区获取
        # queryset:查询集（从数据库中获取的集合）
        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'btitle':book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment':book.bcomment
            })
        # JsonResponse(dict,safe=True)
        return JsonResponse(book_list,safe=False)

    # 新增数据
    def post(self,request):
        '''
        新增数据
        路由：　/books/
        :param request:
        :return:
        '''
        # 接收用户传过来的数据
        json_bytes = request.body
        json_str = json_bytes.decode()
        dict_data = json.loads(json_str)
        book = BookInfo.objects.create(
            btitle= dict_data.get('btitle'),
            bpub_date=dict_data.get('bpub_date')
        )
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

class BookInfoDetailView(View):
    def get(self,request,pk):
        '''获取单个数据'''
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

