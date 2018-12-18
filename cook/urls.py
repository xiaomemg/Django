from django.conf.urls import url

from cook import views

urlpatterns = [
    url(r'^set_cook/',views.set_cook),
    url(r'^get_cook/',views.get_cook)
]