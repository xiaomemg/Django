def my_middleware(get_response):
    print("初始化时被使用")
    def middleware(request):
        print("视图函数调用之前被使用了")
        response = get_response(request)
        print("视图函数调用之后被使用了")
        return response
    return middleware
