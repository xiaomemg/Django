from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^book/$',views.BookInfoListView.as_view()),
    url(r'^book/(?P<pk>\d+)/$',views.BookInfoDetailView.as_view()),
]