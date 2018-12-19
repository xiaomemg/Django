def my_middleware(get_response):
    print("我已经在被使用")
    def middleware(request):
        print("我在被请求之前已经被使用了")
        response = get_response(request)
        print("我在被请求之后被使用了")
        return response
    return middleware
