from django.conf.urls import url

from demo_view import views

urlpatterns =[
    url(r'^demoview/',views.demoview.as_view())
]