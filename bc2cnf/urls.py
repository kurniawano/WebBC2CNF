from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^index.html', views.index, name='index'),
    url(r'^convert/$', views.convert, name='convert'),
]
