from django.conf.urls import url

from reqresp import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^qs/',views.qs),
    # 未命名参数按定义的顺序传递
    url(r'^weather/([a-z]+)/(\d{4})/$',views.weather)
]