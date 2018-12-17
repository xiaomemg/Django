from django.conf.urls import url

from read import views

urlpatterns =[
    url(r'^index/',views.index),
    url(r'^ps/',views.ps),
    url(r'^rep/',views.rep)

]